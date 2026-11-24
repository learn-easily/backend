# შენი სფერო: „ჩარიცხვა“ „ჯგუფის“ გავლით

საშინაო · HW-11 · შენი სფერო · R3

## მოთხოვნები

- შენი „ჩარიცხვის“ entity [სფეროს ცხრილიდან](../07-lms-discovery/materials/domains.html) — შენი „ჯგუფის“ **შიგნით**: `private List`, `IReadOnlyCollection`, `internal` constructor · `DbSet` **არ არის**
- „ჯგუფის“ მეთოდი (`Enroll`-ის ანალოგი) — შენი სფეროს R3-ის **ყველა** ნაწილი, თითოს თავისი `Error`
- slice: `POST /api/<ჯგუფები>/{id}/<ჩარიცხვები>` · არ არსებობს → **404** · R3 დაირღვა → **409**
- `RowVersion` + `IsRowVersion()` · root-ის ველი, რომელიც ყოველ ჩარიცხვაზე იცვლება · `DbUpdateConcurrencyException` → **409**
- unique index `(<ჯგუფის>Id, <ადამიანის>Id)` · მიგრაცია
- „ჯგუფი“ → კატალოგი და ლექტორი: **Restrict** · კატალოგის Delete, თუ „ჯგუფები“ აქვს → **409**

## ✓ მზადაა, როცა

`Task.Delay(5000)`-ით და ორი ერთდროული მოთხოვნით ბოლო ადგილზე ერთი იღებს 200-ს, მეორე **409**-ს · ცხრილში ჩანაწერების რაოდენობა ლიმიტს არ აჭარბებს · ცდის მერე `Task.Delay` წაშლილია

## ⭐ ბონუსი

- „გარიცხვა“: `Unenroll` „ჯგუფის“ მეთოდად (არ არის ჩარიცხული → 409) · `DELETE /api/<ჯგუფები>/{id}/<ჩარიცხვები>/{personId}`
- „ჯგუფის“ წევრების სია projection-ით: სახელი, გვარი, ჩარიცხვის თარიღი

## ამოხსნა

ლექტორის LMS-ში (ნიმუში): გარიცხვა და ჯგუფის სტუდენტები. შენს სფეროში იგივე ფორმა იქნება, შენი სახელებით.

```csharp Entities/Group.cs · Unenroll !
public Result Unenroll(Guid studentId)
{
    var enrollment = _enrollments.FirstOrDefault(e => e.StudentId == studentId);
    if (enrollment is null)
        return Result.Failure(GroupErrors.NotEnrolled);

    _enrollments.Remove(enrollment);
    EnrolledCount--;
    return Result.Success();
}
```

```csharp Features/Groups/UnenrollStudent/UnenrollStudentHandler.cs
public async Task<IResult> HandleAsync(Guid groupId, Guid studentId)
{
    var group = await _db.Groups
        .Include(g => g.Enrollments)
        .FirstOrDefaultAsync(g => g.Id == groupId);
    if (group is null)
        return Results.NotFound(GroupErrors.NotFound);

    var result = group.Unenroll(studentId);
    if (result.IsFailure)
        return Results.Conflict(result.Error);

    try
    {
        await _db.SaveChangesAsync();
    }
    catch (DbUpdateConcurrencyException)
    {
        return Results.Conflict(GroupErrors.ConcurrentChange);
    }

    return Results.NoContent();
}
```

```csharp Features/Groups/GetGroupStudents/GetGroupStudentsHandler.cs
public async Task<IResult> HandleAsync(Guid groupId)
{
    if (!await _db.Groups.AnyAsync(g => g.Id == groupId))
        return Results.NotFound(GroupErrors.NotFound);

    var students = await _db.Groups
        .Where(g => g.Id == groupId)
        .SelectMany(g => g.Enrollments)
        .Join(_db.Students, e => e.StudentId, s => s.Id,
            (e, s) => new GroupStudentItem(s.Id, s.FirstName, s.LastName, e.EnrolledAt))
        .OrderBy(x => x.LastName)
        .ToListAsync();

    return Results.Ok(students);
}
```

```check
? `Unenroll`-ში `_enrollments.Remove(...)` ბაზიდან ჩანაწერს შლის?
= კი. EF ხედავს, რომ Enrollment root-ის სიიდან ამოვარდა, და რადგან ის აუცილებელი ურთიერთობაა (GroupId), შენახვისას DELETE-ს წერს. `EnrolledCount--` კი root-ის რიგს ცვლის, ამიტომ ვერსიაც იცვლება
? GetGroupStudents-ში რატომ ვიყენებთ `Join`-ს და არა `e.Student.FirstName`-ს?
= Enrollment-ს Student-ზე navigation არ აქვს: სტუდენტი სხვა aggregate-ია და ჯგუფი მას მხოლოდ Id-ით იცნობს. წაკითხვისას კი შეგვიძლია ორი ცხრილი SQL-ში დავაკავშიროთ — ეს წაკითხვაა და aggregate-ის წესებს არ არღვევს
```

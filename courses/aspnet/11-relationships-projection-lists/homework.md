# შენი სფერო: ურთიერთობები, projection და სიები

საშინაო · HW-11 · შენი სფერო

## მოთხოვნები

- შენი „ჯგუფი“ → კატალოგი და → ლექტორის როლი: navigation property-ები, `HasOne / WithMany`, **Restrict** · მიგრაცია
- კატალოგს — „ჯგუფების“ სია მხოლოდ წასაკითხად (`IReadOnlyCollection` + `private List`)
- **GetById** „ჯგუფზე“: projection, პასუხში კატალოგის სახელი და ლექტორის სრული სახელი
- **GetAll** „ჯგუფებზე“: `[AsParameters]`, ფილტრი კატალოგით, დალაგება (`startDate` / `-startDate`, default — სახელი), pagination (`pageSize` ≤ 50), `PagedResponse<T>`
- კატალოგის **Delete**: თუ „ჯგუფები“ აქვს → **409**

## ✓ მზადაა, როცა

Scalar-ში `GET …?page=2&pageSize=2` სწორ ორ ჩანაწერს და `totalCount`-ს აბრუნებს · ლოგში ჩანს ერთი SQL JOIN-ით (GetById) · ჯგუფიანი კატალოგის წაშლა 409-ს აბრუნებს, არა 500-ს

## ⭐ ბონუსი

- კატალოგის GetAll-ში თითო ჩანაწერს დაუმატე „ჯგუფების“ რაოდენობა: `c.Groups.Count` projection-ში. ნახე ლოგში, რა SQL შეიქმნა
- დაამატე ფილტრი ლექტორით (`lecturerId`)

## ამოხსნა

ლექტორის LMS-ში (ნიმუში). შენს სფეროში იგივე ფორმა იქნება, შენი სახელებით.

```csharp Features/Courses/DeleteCourse/DeleteCourseHandler.cs !
public async Task<IResult> HandleAsync(Guid id)
{
    var course = await _db.Courses.FindAsync(id);
    if (course is null)
        return Results.NotFound();

    if (await _db.Groups.AnyAsync(g => g.CourseId == id))
        return Results.Conflict(CourseErrors.HasGroups);

    _db.Courses.Remove(course);
    await _db.SaveChangesAsync();
    return Results.NoContent();
}

// CourseErrors.cs
public static readonly Error HasGroups = new(
    "Course.HasGroups", "კურსს ჯგუფები აქვს და ვერ წაიშლება");
```

```csharp Features/Courses/GetCourses/GetCoursesHandler.cs · ბონუსი
public async Task<IResult> HandleAsync()
{
    var courses = await _db.Courses
        .OrderBy(c => c.Title)
        .Select(c => new CourseListItem(c.Id, c.Title, c.DurationWeeks, c.Groups.Count))
        .ToListAsync();

    return Results.Ok(courses);
}
```

```sql SQL (ლოგიდან) · ბონუსი
SELECT c.Id, c.Title, c.DurationWeeks, (
    SELECT COUNT(*) FROM Groups AS g WHERE c.Id = g.CourseId)
FROM Courses AS c
ORDER BY c.Title
```

```check
? `c.Groups.Count` projection-ში ჯგუფებს მეხსიერებაში ტვირთავს?
= არა. EF მას SQL-ის ქვემოთხოვნად (`SELECT COUNT(*)`) თარგმნის და მხოლოდ რიცხვი მოდის. `Include(c => c.Groups)` + მეხსიერებაში `Count` კი ყველა ჯგუფს ჩატვირთავდა
? რატომ არ ვამოწმებთ Delete-ში ჯგუფებს `course.Groups.Any()`-ით?
= `FindAsync` ჯგუფებს არ ტვირთავს: `Groups` ცარიელი იქნება და შემოწმება ყოველთვის `false` იქნება. `_db.Groups.AnyAsync(...)` პირდაპირ ბაზას ეკითხება
```

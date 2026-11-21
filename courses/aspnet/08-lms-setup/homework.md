# შენი სფერო: პროექტი, კატალოგი და ადამიანები

საშინაო · HW-08 · შენი სფერო · backlog №1–2

## მოთხოვნები

- პროექტი **`<სფერო>.Api`** (მაგ. `FitHub.Api`): Controllers, DataContext, SQL Server, მიგრაციები. სახელები [სფეროს ცხრილიდან](../07-lms-discovery/materials/domains.html)
- **კატალოგი** (შენი „კურსი“): სრული CRUD · **R1** სახელი უნიკალურია → **409** · ცარიელი ან არასწორი → **400**
- **ორი როლის ადამიანები** (შენი „სტუდენტი“ და „ლექტორი“): FirstName, LastName, Email · **R2** → **409** · სრული CRUD
- ყველგან async, DTO + Mapper, `Guid` Id

## ✓ მზადაა, როცა

Swagger-ში იგივე სახელით მეორე კატალოგის ჩანაწერი და იგივე Email-ით მეორე ადამიანი **409**-ს აბრუნებს, Update-ისას საკუთარი სახელის ან Email-ის შენარჩუნება კი 409-ს **არ** აბრუნებს

## ⭐ ბონუსი

- Email შენახვამდე გაასუფთავე: `Trim()` + `ToLowerInvariant()`
- R2 ზუსტად წაიკითხე: „ერთ email-ზე **ერთი ადამიანი**“. შეიძლება თუ არა ორი სხვადასხვა როლის ადამიანს ერთი email ჰქონდეს? რა უნდა შეამოწმო?

## ამოხსნა

ლექტორის LMS-ში (ნიმუში): სტუდენტის შექმნა. შენს სფეროში იგივე ფორმა იქნება, შენი სახელებით.

```csharp Controllers/StudentsController.cs · Create !
[HttpPost]
public async Task<IActionResult> Create(CreateStudentRequest request)
{
    if (string.IsNullOrWhiteSpace(request.FirstName) ||
        string.IsNullOrWhiteSpace(request.LastName) ||
        string.IsNullOrWhiteSpace(request.Email))
        return BadRequest("სახელი, გვარი და Email სავალდებულოა");

    var email = request.Email.Trim().ToLowerInvariant();
    if (await _db.Students.AnyAsync(s => s.Email == email))
        return Conflict("ამ Email-ით სტუდენტი უკვე არსებობს");

    var student = request.ToEntity(email);
    _db.Students.Add(student);
    await _db.SaveChangesAsync();
    return CreatedAtAction(nameof(GetById),
        new { id = student.Id }, student.ToResponse());
}
```

```csharp Data/DataContext.cs · OnModelCreating
modelBuilder.Entity<Student>(student =>
{
    student.Property(s => s.Email).HasMaxLength(200);
    student.HasIndex(s => s.Email).IsUnique();
});
modelBuilder.Entity<Lecturer>(lecturer =>
{
    lecturer.Property(l => l.Email).HasMaxLength(200);
    lecturer.HasIndex(l => l.Email).IsUnique();
});
```

```check
? Update-ში Email-ის შემოწმება როგორ გამოიყურება?
= `await _db.Students.AnyAsync(s => s.Email == email && s.Id != id)`: ვეძებთ **სხვა** სტუდენტს ამავე Email-ით, საკუთარ თავს გარდა
? ბონუსი: სტუდენტს და ლექტორს ერთი email შეიძლება ჰქონდეთ?
= R2-ით არა: „ერთ email-ზე ერთი ადამიანი“. ამიტომ სტუდენტის შექმნისას `Lecturers`-შიც უნდა შეამოწმო. unique index ამას ვერ დაიცავს: ის ერთ ცხრილს ხედავს. ამ წესს შემდეგ ლექციებში დავუბრუნდებით
```

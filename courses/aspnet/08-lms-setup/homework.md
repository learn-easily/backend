# შენი LMS: სტუდენტები და ლექტორები

საშინაო · შენი LMS · backlog №2

## მოთხოვნები

- `Student` და `Lecturer`: **FirstName**, **LastName**, **Email**, **CreatedAt** (Id: Guid)
- **R2**: Email უნიკალურია: unique index ბაზაში + `AnyAsync` → **409**
- ცარიელი სახელი, გვარი ან Email → **400**
- `StudentsController` და `LecturersController`: სრული CRUD, async, DTO + Mapper. ახალი მიგრაცია

## ✓ მზადაა, როცა

Swagger-ში ერთი Email-ით მეორე სტუდენტი (ან ლექტორი) აბრუნებს 409-ს, Update-ისას საკუთარი Email-ის შენარჩუნება კი 409-ს **არ** აბრუნებს

## ⭐ ბონუსი

- Email შენახვამდე გაასუფთავე: `Trim()` + `ToLowerInvariant()`, რომ „Ana@Mail.com“ და „ana@mail.com“ ერთი და იგივე იყოს
- R2 ზუსტად წაიკითხე: „ერთ email-ზე **ერთი ადამიანი**“. შეიძლება თუ არა სტუდენტს და ლექტორს ერთი email ჰქონდეთ? რა უნდა შეამოწმო?

## ამოხსნა

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

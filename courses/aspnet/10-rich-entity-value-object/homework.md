# შენი სფერო: rich entity-ები, Email და „ჯგუფი“

საშინაო · HW-10 · შენი სფერო

## მოთხოვნები

- `Common/Result.cs`: `Error`, `Result`, `Result<T>` — როგორც ლექციაზე
- **კატალოგი** (შენი „კურსი“) — rich entity: `private set`, `private` constructor, `Create` და `Update` აბრუნებს Result-ს · ყველა შეცდომა `…Errors` კლასში
- **`Email`** Value Object (`sealed record`) · ორივე როლის ადამიანი მას იყენებს · `HasConversion` DataContext-ში
- ორივე როლის ადამიანები — rich entity (`Create` იღებს `Email`-ს, არა `string`-ს)
- **შენი „ჯგუფი“** [სფეროს ცხრილიდან](../07-lms-discovery/materials/domains.html): rich entity, ადგილების ლიმიტი შენი სფეროს წესით, წარსულში ვერ დაიწყება · slice-ები: **Create** და **GetById** · მიგრაცია
- handler-ებში შეცდომა: entity → **400**, „არ არსებობს“ → **404**, უნიკალურობა → **409**

## ✓ მზადაა, როცა

handler-ებში აღარც `IsNullOrWhiteSpace`-ია და აღარც `Trim().ToLowerInvariant()` · Scalar-ში არასწორი Email, ლიმიტზე მეტი ადგილი და გუშინდელი თარიღი **400**-ს აბრუნებს თავისი `code`-ით

## ⭐ ბონუსი

- ძებნა: სადმე ისევ ხომ არ წერია `new <შენი entity> {` entity-ის გარეთ? (`Ctrl+Shift+F`)
- R2 ორ ცხრილზე: შეიძლება თუ არა ორ სხვადასხვა როლის ადამიანს ერთი Email ჰქონდეს? თუ არა, დაამატე შემოწმება ორივე Create handler-ში

## ამოხსნა

ლექტორის LMS-ში (ნიმუში): ლექტორი Email-ით და ჯგუფის წაკითხვა. შენს სფეროში იგივე ფორმა იქნება, შენი სახელებით.

```csharp Features/Lecturers/CreateLecturer/CreateLecturerHandler.cs !
public async Task<IResult> HandleAsync(CreateLecturerRequest request)
{
    var email = Email.Create(request.Email);
    if (email.IsFailure)
        return Results.BadRequest(email.Error);

    var result = Lecturer.Create(request.FirstName, request.LastName, email.Value);
    if (result.IsFailure)
        return Results.BadRequest(result.Error);

    var lecturer = result.Value;
    if (await _db.Lecturers.AnyAsync(l => l.Email == lecturer.Email))
        return Results.Conflict(LecturerErrors.EmailTaken);

    _db.Lecturers.Add(lecturer);
    await _db.SaveChangesAsync();
    return Results.Created($"/api/lecturers/{lecturer.Id}", lecturer.ToResponse());
}
```

```csharp Features/Lecturers/UpdateLecturer/UpdateLecturerHandler.cs
public async Task<IResult> HandleAsync(Guid id, UpdateLecturerRequest request)
{
    var lecturer = await _db.Lecturers.FindAsync(id);
    if (lecturer is null)
        return Results.NotFound();

    var email = Email.Create(request.Email);
    if (email.IsFailure)
        return Results.BadRequest(email.Error);

    var result = lecturer.Update(request.FirstName, request.LastName, email.Value);
    if (result.IsFailure)
        return Results.BadRequest(result.Error);

    if (await _db.Lecturers.AnyAsync(l => l.Email == lecturer.Email && l.Id != id))
        return Results.Conflict(LecturerErrors.EmailTaken);

    await _db.SaveChangesAsync();
    return Results.NoContent();
}
```

```csharp Data/DataContext.cs · OnModelCreating
modelBuilder.Entity<Lecturer>(lecturer =>
{
    lecturer.Property(l => l.Email)
        .HasConversion(
            email => email.Value,
            value => Email.FromDatabase(value))
        .HasMaxLength(Email.MaxLength);
    lecturer.HasIndex(l => l.Email).IsUnique();
});
```

```csharp Features/Groups/GetGroupById/GetGroupByIdHandler.cs
public async Task<IResult> HandleAsync(Guid id)
{
    var group = await _db.Groups.FindAsync(id);
    if (group is null)
        return Results.NotFound();

    return Results.Ok(group.ToResponse());
}
```

```check
? Update-ში `Email.Create` რატომ არის `FindAsync`-ის შემდეგ და არა წინ?
= ორივე სწორია: ჯერ არსებობის შემოწმება ჩვეულებრივ უფრო ლოგიკურია (არარსებულ ლექტორზე 404 უფრო ზუსტი პასუხია, ვიდრე 400 Email-ზე), მაგრამ ბაზასთან ერთი ზედმეტი მიმართვა ჯდება. მთავარია, ყველა handler-ში ერთნაირად წერდე
? ჯგუფს ახლა `Capacity` აქვს, მაგრამ ჩარიცხვა ჯერ არ არის. „ჯგუფი სავსეა“ — ვინ უნდა შეამოწმოს: handler-მა თუ Group-მა? და რატომ?
= Group-მა: წესი ჯგუფის ყველა ჩარიცხვას ერთად ეხება, ამიტომ ჩარიცხვები ჯგუფის ნაწილი უნდა იყოს და მხოლოდ ჯგუფის მეთოდით უნდა იცვლებოდეს. ეს შემდეგი ლექციის თემაა: Aggregate
```

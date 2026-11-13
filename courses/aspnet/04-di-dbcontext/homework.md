# LibraryApi — წევრები და გატანა ბაზაში

ერთი DataContext — სამი ცხრილი

## მოთხოვნები

- `MemberService` — MembersController-ის ლოგიკა ბაზით (Email-ის შემოწმება, Argon2) · Controller მხოლოდ მას ითხოვს
- `Loan`: `Id`, `BookId`, `MemberId` (Guid), `LoanedAt` · `DbSet<Loan> Loans` · ახალი მიგრაცია
- `LoanService(DataContext)`: `GetAll` · `IsLoaned(bookId)` · `Create` → `null`, თუ წიგნი ან წევრი არ არის
- `POST /api/loans` → 201 · 404 · 409 · `GET /api/loans` · ყველა სერვისი — `AddScoped`

## ✓ მზადაა, როცა

გადატვირთვის შემდეგ ყველაფერი ადგილზეა, და ერთი წიგნის მეორედ გატანა 409-ს აბრუნებს

## ⭐ ბონუსი

- `GET /api/members/{id}/loans` — წევრის გატანები (404, თუ წევრი არ არის)
- მთვლელი LoanService-ში და DataContext-ში: Scoped → Transient → Singleton — რას ხედავ და რატომ?

## 💡 მინიშნება

`Member`-ისთვის — `DbSet<Member> Members`; მიგრაციის სახელი, მაგ. `AddMembersAndLoans`. DTO-ები — `record CreateLoanRequest(Guid BookId, Guid MemberId)` და `record LoanResponse(Guid Id, Guid BookId, Guid MemberId, DateTime LoanedAt)`. LoanService წიგნსაც, წევრსაც და გატანასაც ერთი DataContext-ით ამოწმებს: `_db.Books.Find(...)`, `_db.Members.Find(...)`, `_db.Loans.Any(...)`. ბაზაში ყველა ცხრილი ერთ DataContext-შია. ბონუსის მთვლელები ბოლოს წაშალე.

## ამოხსნა

```csharp Services/LoanService.cs
public class LoanService
{
    private readonly DataContext _db;

    public LoanService(DataContext db)
    {
        _db = db;
    }

    public List<Loan> GetAll() => _db.Loans.ToList();

    public bool IsLoaned(Guid bookId) =>
        _db.Loans.Any(l => l.BookId == bookId);

    public Loan? Create(Guid bookId, Guid memberId)
    {
        if (_db.Books.Find(bookId) is null) return null;
        if (_db.Members.Find(memberId) is null) return null;

        var loan = new Loan
        {
            BookId = bookId,
            MemberId = memberId,
            LoanedAt = DateTime.UtcNow
        };
        _db.Loans.Add(loan);
        _db.SaveChanges();
        return loan;
    }
}
```

```csharp Controllers/LoansController.cs · Create !
[HttpPost]
public IActionResult Create(CreateLoanRequest request)
{
    if (_loans.IsLoaned(request.BookId)) return Conflict();

    var loan = _loans.Create(request.BookId, request.MemberId);
    if (loan is null) return NotFound();

    return Created($"/api/loans/{loan.Id}", ToResponse(loan));
}

private static LoanResponse ToResponse(Loan l) =>
    new(l.Id, l.BookId, l.MemberId, l.LoanedAt);
```

```csharp Program.cs
builder.Services.AddDbContext<DataContext>(options =>
    options.UseSqlServer(
        builder.Configuration.GetConnectionString("Default")));

builder.Services.AddScoped<BookService>();
builder.Services.AddScoped<MemberService>();
builder.Services.AddScoped<LoanService>();
```

```csharp Data/DataContext.cs
public DbSet<Book> Books { get; set; }
public DbSet<Member> Members { get; set; }
public DbSet<Loan> Loans { get; set; }
```

ექსპერიმენტის პასუხი:

```check
? AddTransient<LoanService>() — რა შეიცვალა console-ში?
= არაფერი: ერთ მოთხოვნაზე LoanService-ს მხოლოდ LoansController ითხოვს, ამიტომ ერთხელ იქმნება — ისევე, როგორც Scoped-ით
? AddSingleton<LoanService>() — რა მოხდა?
= აპლიკაცია არ ჩაირთო: „Cannot consume scoped service 'DataContext' from singleton 'LoanService'“ — Singleton ერთ DataContext-ს სამუდამოდ დაიჭერდა
```

```note
LoansController-ში არცერთი DataContext ან `new` არ წერია: მან მხოლოდ თქვა, რა სჭირდება — `LoanService`. LoanService-მა თქვა — `DataContext`. დანარჩენს Container აწყობს და მოთხოვნის ბოლოს ხურავს. `Loan`-ის `Id`-ს, ისევე როგორც სხვა Guid-ებს, EF Core `Add`-ის დროს თვითონ ავსებს.
```

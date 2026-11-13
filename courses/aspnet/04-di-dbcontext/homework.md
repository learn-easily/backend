# LibraryApi — წევრები და გატანა ბაზაში

ერთი DataContext — სამი ცხრილი

## მოთხოვნები

- MembersController — `static` სიის ნაცვლად `DbSet<Member> Members` (Email-ის შემოწმება და Argon2 რჩება)
- `Loan`: `Id`, `BookId`, `MemberId` (Guid), `LoanedAt` · `DbSet<Loan> Loans` · ახალი მიგრაცია
- `LoansController(DataContext)` · `POST /api/loans` `{ bookId, memberId }` → 201 · 404 · 409 (უკვე გატანილია)
- `GET /api/loans` — ყველა გატანა · ყველგან DataContext constructor-ით, `new`-ის გარეშე

## ✓ მზადაა, როცა

გადატვირთვის შემდეგ ყველაფერი ადგილზეა, და ერთი წიგნის მეორედ გატანა 409-ს აბრუნებს

## ⭐ ბონუსი

- `GET /api/members/{id}/loans` — წევრის გატანები (404, თუ წევრი არ არის)
- მთვლელი DataContext-ში: Scoped → Transient → Singleton — რას ხედავ console-ში და რატომ?

## 💡 მინიშნება

მიგრაციის სახელი, მაგ. `AddMembersAndLoans`. DTO-ები — `record CreateLoanRequest(Guid BookId, Guid MemberId)` და `record LoanResponse(Guid Id, Guid BookId, Guid MemberId, DateTime LoanedAt)`. LoansController წიგნსაც, წევრსაც და გატანასაც ერთი DataContext-ით ამოწმებს: `_db.Books.Find(...)`, `_db.Members.Find(...)`, `_db.Loans.Any(...)` — ბაზაში ყველა ცხრილი ერთ DataContext-შია. ბონუსის მთვლელი ბოლოს წაშალე.

## ამოხსნა

```csharp Controllers/LoansController.cs · Create !
[HttpPost]
public IActionResult Create(CreateLoanRequest request)
{
    if (_db.Books.Find(request.BookId) is null) return NotFound();
    if (_db.Members.Find(request.MemberId) is null) return NotFound();
    if (_db.Loans.Any(l => l.BookId == request.BookId)) return Conflict();

    var loan = new Loan
    {
        BookId = request.BookId,
        MemberId = request.MemberId,
        LoanedAt = DateTime.UtcNow
    };
    _db.Loans.Add(loan);
    _db.SaveChanges();
    return Created($"/api/loans/{loan.Id}", ToResponse(loan));
}
```

```csharp Controllers/LoansController.cs
[ApiController]
[Route("api/[controller]")]
public class LoansController : ControllerBase
{
    private readonly DataContext _db;

    public LoansController(DataContext db)
    {
        _db = db;
    }

    [HttpGet]
    public IActionResult GetAll() =>
        Ok(_db.Loans.ToList().Select(ToResponse));

    private static LoanResponse ToResponse(Loan l) =>
        new(l.Id, l.BookId, l.MemberId, l.LoanedAt);

    // Create — ზემოთ
}
```

```csharp Data/DataContext.cs
public DbSet<Book> Books { get; set; }
public DbSet<Member> Members { get; set; }
public DbSet<Loan> Loans { get; set; }
```

ბონუსის პასუხი:

```check
? Transient — რა შეიცვალა console-ში?
= არაფერი: ერთ მოთხოვნაზე DataContext-ს მხოლოდ ერთი Controller ითხოვს, ამიტომ ერთხელ იქმნება — ისევე, როგორც Scoped-ით
? Singleton — რა ჩანს?
= `new DataContext #1` მხოლოდ ერთხელ — ერთი DataContext ყველა მოთხოვნას ემსახურება. ლოკალურად მუშაობს, მაგრამ Change Tracker იზრდება და ერთდროულ მოთხოვნებზე „A second operation was started…“ შეცდომა ჩნდება
```

```note
LoansController-ს სამი შემოწმებისთვის მხოლოდ ერთი dependency სჭირდება — DataContext.
```

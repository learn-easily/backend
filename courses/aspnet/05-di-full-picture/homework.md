# LibraryApi — დაბრუნება და ჯარიმა

FineService ჯარიმის ოდენობას appsettings-იდან იღებს

## მოთხოვნები

- `Loan` + `DueAt`, `ReturnedAt` · `LoanStore` + `GetById` · `LoanResponse` + `ReturnedAt`, `Fine`
- `appsettings.json`: `LoanDays`, `FinePerDay` — რიცხვები კოდში არ წერია
- `FineService(IConfiguration)` — ჯარიმა = დაგვიანებული დღეები × FinePerDay
- `POST /api/loans/{id}/return` → `LoanService.Return` → 200 და ჯარიმა, ან 404 · ჯარიმაზე `LogWarning`

## ✓ მზადაა, როცა

FinePerDay-ის შეცვლა appsettings-ში ჯარიმას ცვლის — კოდის შეხების გარეშე

## ⭐ ბონუსი

- `GET /api/members/{id}/fines` — წევრის ჯამური ჯარიმა: MembersController-ის action, `LoanService` — `[FromServices]` პარამეტრით
- ყველა ახალი კლასი — primary constructor-ით

## 💡 მინიშნება

```json appsettings.json
"Library": { "LoanDays": 14, "FinePerDay": 0.5 }
```

ტესტისთვის 14 დღე ვერ დაელოდებით: `LoanDays`-ს დროებით 0 მიეცით, ან `ReturnedAt`-ის ნაცვლად ფუნქციაში „ახლა“ პარამეტრად გადაეცით. ჯაჭვი ასეთია: LoansController → LoanService → (LoanStore, FineService → IConfiguration, ILogger).

## ამოხსნა

```csharp Services/FineService.cs !
public class FineService(IConfiguration configuration)
{
    public decimal Calculate(Loan loan, DateTime now)
    {
        var lateDays = (now.Date - loan.DueAt.Date).Days;
        if (lateDays <= 0) return 0;

        var perDay = configuration.GetValue<decimal>("Library:FinePerDay");
        return lateDays * perDay;
    }
}
```

```csharp Services/LoanService.cs
public LoanResponse? Return(Guid loanId)
{
    var loan = loans.GetById(loanId);
    if (loan is null) return null;

    loan.ReturnedAt = DateTime.UtcNow;
    var fine = fines.Calculate(loan, loan.ReturnedAt.Value);
    if (fine > 0)
        logger.LogWarning("სესხი {LoanId}: ჯარიმა {Fine}", loanId, fine);

    return new LoanResponse(loan.Id, loan.BookId, loan.MemberId,
        loan.LoanedAt, loan.ReturnedAt, fine);
}
```

```csharp Program.cs
builder.Services.AddSingleton<FineService>();
```

ბონუსი — ჯამი LoanService-ში, endpoint MembersController-ში:

```csharp Services/LoanService.cs · TotalFines
public decimal TotalFines(Guid memberId) =>
    loans.GetAll()
        .Where(l => l.MemberId == memberId && l.ReturnedAt is not null)
        .Sum(l => fines.Calculate(l, l.ReturnedAt!.Value));
```

```csharp Controllers/MembersController.cs · GetFines
[HttpGet("{id:guid}/fines")]
public IActionResult GetFines(Guid id, [FromServices] LoanService loanService)
{
    if (members.GetById(id) is null) return NotFound();
    return Ok(loanService.TotalFines(id));
}
```

```note
`FineService`-მა არ იცის, საიდან მოდის 0.5 — ის `IConfiguration`-ს ითხოვს, და Container აწვდის. `DueAt`-ს LoanStore-ის `Add` ანიჭებს: `loan.DueAt = loan.LoanedAt.AddDays(loanDays)`, სადაც `loanDays` ისევ კონფიგურაციიდან მოდის. `GetFines`-ში ორი პარამეტრია: `id` მისამართიდან, `LoanService` — Container-იდან (`[FromServices]`). LoanService მხოლოდ ამ ერთ action-ს სჭირდება, ამიტომ MembersController-ის constructor-ში არ ვამატებთ.
```

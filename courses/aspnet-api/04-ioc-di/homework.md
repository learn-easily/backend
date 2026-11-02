# LibraryApi — წიგნის გატანა

LoansController სამ dependency-ს ითხოვს

## მოთხოვნები

- `MemberStore` — წევრები MembersController-იდან ცალკე კლასში, `AddSingleton`
- `Models/Loan`: `Id`, `BookId`, `MemberId`, `LoanedAt` · `LoanStore` — სია და `Add`, `GetAll`
- `LoansController` — constructor-ში **სამი** dependency: `BookStore`, `MemberStore`, `LoanStore`
- `POST /api/loans` `{ bookId, memberId }` → 201, ან 404, თუ წიგნი ან წევრი არ არსებობს
- `GET /api/loans` — ყველა გატანა

## ✓ მზადაა, როცა

Ctrl+Shift+F → `new …Store` — 0 შედეგი, და არარსებული წიგნის გატანა 404-ს აბრუნებს

## ⭐ ბონუსი

- ერთი წიგნი ერთდროულად ორჯერ ვერ გავა → `Conflict()` (409)

## 💡 მინიშნება

DTO-ები — `record CreateLoanRequest(int BookId, int MemberId)` და `record LoanResponse(int Id, int BookId, int MemberId, DateTime LoanedAt)`. Entity გარეთ ისევ არ გადის. Controller-ს რამდენიც სჭირდება, იმდენ პარამეტრს წერს constructor-ში — Container ყველას მოუტანს, თუ სამივე დარეგისტრირებულია.

## ამოხსნა

```csharp Controllers/LoansController.cs
[ApiController]
[Route("api/[controller]")]
public class LoansController : ControllerBase
{
    private readonly BookStore _books;
    private readonly MemberStore _members;
    private readonly LoanStore _loans;

    public LoansController(
        BookStore books, MemberStore members, LoanStore loans)
    {
        _books = books;
        _members = members;
        _loans = loans;
    }

    // Create, GetAll — ქვემოთ
}
```

```csharp Controllers/LoansController.cs · Create !
    [HttpPost]
    public IActionResult Create(CreateLoanRequest request)
    {
        if (_books.GetById(request.BookId) is null) return NotFound();
        if (_members.GetById(request.MemberId) is null) return NotFound();
        if (_loans.GetAll().Any(l => l.BookId == request.BookId))
            return Conflict();

        var loan = _loans.Add(new Loan
            { BookId = request.BookId, MemberId = request.MemberId });
        return Created($"/api/loans/{loan.Id}", ToResponse(loan));
    }

    [HttpGet]
    public IActionResult GetAll() =>
        Ok(_loans.GetAll().Select(ToResponse).ToList());

    private static LoanResponse ToResponse(Loan l) =>
        new(l.Id, l.BookId, l.MemberId, l.LoanedAt);
```

```csharp Program.cs
builder.Services.AddSingleton<BookStore>();
builder.Services.AddSingleton<MemberStore>();
builder.Services.AddSingleton<LoanStore>();
```

```csharp Services/LoanStore.cs
public class LoanStore
{
    private readonly List<Loan> _loans = new();
    private int _nextId = 1;

    public List<Loan> GetAll() => _loans;

    public Loan Add(Loan loan)
    {
        loan.Id = _nextId++;
        loan.LoanedAt = DateTime.UtcNow;
        _loans.Add(loan);
        return loan;
    }
}
```

```note
LoansController-ში არცერთი `new …Store()` არ წერია: მან მხოლოდ თქვა, რა სჭირდება. მაგრამ შეამჩნიე — ახლა Controller-ი თვითონ წყვეტს წესებს („წიგნი უკვე გატანილია?“). როცა ასეთი ლოგიკა იზრდება, მას ცალკე კლასში (Service) იტანენ — ზუსტად ამაზეა შემდეგი ლექცია.
```

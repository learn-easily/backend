# LibraryApi — წევრები და გატანები async-ზე

მთელი LibraryApi — async

## მოთხოვნები

- MembersController — ყველა endpoint async (Email-ის შემოწმება — `AnyAsync`; Argon2 ჰეში რჩება სინქრონული)
- LoansController — `POST /api/loans`: სამი შემოწმება async-ით → 201 · 404 · 409
- `GET /api/loans` — `ToListAsync` · მთელ პროექტში არც ერთი `ToList()`, `Find()`, `Any()`, `SaveChanges()`
- არც ერთი `.Result`, `.Wait()` ან `async void`

## ✓ მზადაა, როცა

ყველა endpoint Swagger-ში ისე მუშაობს, როგორც წინა ლექციაზე, და Error List-ში async-ის warning არ არის

## ⭐ ბონუსი

- `GET /api/members/{id}/loans` async-ით (404, თუ წევრი არ არის)
- `GET /api/loans` — `CancellationToken`-ით

## 💡 მინიშნება

LoansController-ის სამ შემოწმებას თითოს თავისი `await` სჭირდება — რიგრიგობით: ერთ DataContext-ზე ერთდროულად ორი ოპერაცია არ შეიძლება. რატომ რჩება Argon2-ის ჰეშირება სინქრონული? ის ლოდინი კი არა, გამოთვლაა (CPU-bound) — async მას არაფერს მისცემს.

## ამოხსნა

```csharp Controllers/LoansController.cs · Create !
[HttpPost]
public async Task<IActionResult> Create(CreateLoanRequest request)
{
    if (await _db.Books.FindAsync(request.BookId) is null) return NotFound();
    if (await _db.Members.FindAsync(request.MemberId) is null) return NotFound();
    if (await _db.Loans.AnyAsync(l => l.BookId == request.BookId)) return Conflict();

    var loan = new Loan
    {
        BookId = request.BookId,
        MemberId = request.MemberId,
        LoanedAt = DateTime.UtcNow
    };
    _db.Loans.Add(loan);
    await _db.SaveChangesAsync();
    return Created($"/api/loans/{loan.Id}", ToResponse(loan));
}
```

```csharp Controllers/LoansController.cs · GetAll
[HttpGet]
public async Task<IActionResult> GetAll(CancellationToken cancellationToken)
{
    var loans = await _db.Loans.ToListAsync(cancellationToken);
    return Ok(loans.Select(ToResponse));
}
```

```csharp Controllers/MembersController.cs · Create
[HttpPost]
public async Task<IActionResult> Create(CreateMemberRequest request)
{
    if (await _db.Members.AnyAsync(m => m.Email == request.Email)) return Conflict();

    var member = request.ToEntity();   // Argon2 ჰეში — სინქრონულად, გამოთვლაა
    _db.Members.Add(member);
    await _db.SaveChangesAsync();
    return CreatedAtAction(nameof(GetById), new { id = member.Id }, member.ToResponse());
}
```

```check
? რატომ არ ვწერთ Argon2-ის ჰეშირებისთვის await-ს?
= ჰეშირება გამოთვლაა (CPU-bound) — სალოდინო არაფერია, ნაკადი ნამდვილად მუშაობს. async-ს მისთვის არაფერი აქვს მოსაცემი
? `loans.Select(ToResponse)` — აქ რატომ არ არის await?
= `ToListAsync`-ის შემდეგ სია უკვე მეხსიერებაშია — Select ჩვეულებრივი LINQ-ია, ბაზაში აღარ მიდის
```

```note
MembersController-ის Create-ში შენი mapping და ჰეშირება შეიძლება სხვაგვარად იყოს დაწერილი (მაგ. ჰეში Controller-ში). მთავარი: ბაზასთან ყველა მიმართვა — `await` + Async, ჰეში — ჩვეულებრივად.
```

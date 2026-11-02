# LibraryApi → LoanService

საშინაოს LoansController — ლოგიკა Service-ში

## ნაბიჯები

- `Services/LoanService` — წესები LoansController-იდან: წიგნი და წევრი არსებობს? წიგნი უკვე გატანილია?
- LoanService ითხოვს: `BookStore`, `MemberStore`, `LoanStore`, `ILogger<LoanService>` — HTTP-ის გარეშე, ვერ შეიქმნა → `null`
- ლოგი: გატანა → `LogInformation`, უარი → `LogWarning`
- LoansController — მხოლოდ **LoanService** სჭირდება: `null` → 400, წარმატება → 201
- `Program.cs`: `AddSingleton<LoanService>()` · Minimal API: `GET /api/loans/count`

## ✓ მზადაა, როცა

LoansController-ში არცერთი Store არ ჩანს, `/api/loans/count` მუშაობს და console-ში გატანის ლოგი ჩნდება

## ⭐ ბონუსი

- `appsettings.json`: `"Library": { "MaxLoansPerMember": 3 }` — LoanService-ში `IConfiguration`-ით შეამოწმე
- LoanService და LoansController — primary constructor-ით

## 💡 მინიშნება

`_configuration.GetValue<int>("Library:MaxLoansPerMember")` — მნიშვნელობას რიცხვად კითხულობს. ShopApi-ის OrderService თქვენი ნიმუშია: Controller → Service → Store.

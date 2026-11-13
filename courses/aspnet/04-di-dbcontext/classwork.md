# LibraryApi → ბაზა + DI

დავალება · LibraryApi

## ნაბიჯები

- 4 პაკეტი · `DataContext` — `DbSet<Book> Books`, constructor `DbContextOptions<DataContext>`-ით
- `appsettings.json` → `ConnectionStrings:Default` (`LibraryDb`) · `AddDbContext`
- BooksController — DataContext-ს **constructor-ში** ითხოვს · `static` სია წაშალე
- 5 endpoint EF Core-ით · მიგრაცია → `Update-Database`

## ✓ მზადაა, როცა

Ctrl+Shift+F → `new DataContext` — 0 შედეგი, და წიგნი გადატვირთვის შემდეგაც ჩანს

## ⭐ ბონუსი

- `GET /api/stats` — წიგნების რაოდენობა და საშუალო ფასი (StatsController, იგივე DataContext)
- მთვლელი DataContext-ის constructor-ში — Scoped → Singleton: რას ხედავ console-ში?

## 💡 რჩევა

ShopApi-ს გზა გაიარე, ოღონდ პირდაპირ საბოლოო ვარიანტით — `new`-ის გარეშე: ჯერ DataContext და connection string (`appsettings.json`-ში `(localdb)\\MSSQLLocalDB` — ორი `\`), მერე `AddDbContext`, მერე BooksController-ის constructor, ბოლოს მიგრაცია (`Add-Migration InitialCreate`). DTO-ები და BookMapper წინა ლექციიდან უცვლელი რჩება: ბაზაში `Book` ინახება, Controller კი შემოსვლისას `ToEntity()`-ს, გასვლისას `ToResponse()`-ს იძახებს.

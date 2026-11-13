# LibraryApi → ბაზა + DI

დავალება · LibraryApi

## ნაბიჯები

- 4 პაკეტი · `DataContext` — `DbSet<Book> Books`, constructor `DbContextOptions<DataContext>`-ით
- `appsettings.json` → `ConnectionStrings:Default` (`LibraryDb`) · `AddDbContext`
- `BookService` — DataContext-ს constructor-ში ითხოვს · `AddScoped<BookService>()`
- BooksController — `BookService`-ს ითხოვს · მიგრაცია → `Update-Database`

## ✓ მზადაა, როცა

`new DataContext` და `new BookService` — 0 შედეგი, და წიგნი გადატვირთვის შემდეგაც ჩანს

## ⭐ ბონუსი

- `GET /api/stats` — წიგნების რაოდენობა და საშუალო ფასი, იმავე `BookService`-ით
- `AddSingleton<BookService>()` — წაიკითხე შეცდომა, მერე `AddScoped` დააბრუნე

## 💡 რჩევა

ShopApi-ს გზა გაიარე, ოღონდ პირდაპირ საბოლოო ვარიანტით — `new`-ის გარეშე: ჯერ DataContext და connection string (`appsettings.json`-ში `(localdb)\\MSSQLLocalDB` — ორი `\`), მერე `AddDbContext`, მერე BookService და `AddScoped`, ბოლოს Controller და მიგრაცია (`Add-Migration InitialCreate`). DTO-ები და BookMapper წინა ლექციიდან უცვლელი რჩება: BookService `Book`-ებს ინახავს, Controller კი შემოსვლისას `ToEntity()`-ს, გასვლისას `ToResponse()`-ს იძახებს.

# LibraryApi → BookStore + DI

დავალება · LibraryApi

## ნაბიჯები

- `Services/BookStore.cs` — სია და 5 მეთოდი (`static`-ის გარეშე)
- BooksController — `BookStore`-ს **constructor-ში** ითხოვს
- `Program.cs`: `AddSingleton<BookStore>()`
- Swagger: POST → GET — ახალი წიგნი ჩანს

## ✓ მზადაა, როცა

Ctrl+Shift+F → `new BookStore` — 0 შედეგი, და POST-ით დამატებული წიგნი GET-ში ჩანს

## ⭐ ბონუსი

- `StatsController`: `GET /api/stats` → წიგნების რაოდენობა, საშუალო ფასი, ყველაზე ძველი წიგნი
- ექსპერიმენტი: `AddSingleton` წაშალეთ და შეცდომა თვითონ წაიკითხეთ

## 💡 რჩევა

ზუსტად ის გზა გაიარეთ, რაც ShopApi-ში: ჯერ BookStore, მერე Controller constructor-ით, ბოლოს რეგისტრაცია. თუ BooksController DTO-ებს და BookMapper-ს იყენებს (წინა ლექციიდან) — ისინი უცვლელი რჩება: BookStore `Book`-ებს ინახავს, Controller კი ისევ შემოსვლისას `ToEntity()`-ს, გასვლისას `ToResponse()`-ს იძახებს.

# LibraryApi — DTO და Mapping

დავალება · LibraryApi

## ნაბიჯები

- `Book`-ს დაამატეთ `PurchasePrice` და `CreatedAt`
- `Dtos/`: **CreateBookRequest**, **UpdateBookRequest**, **BookResponse** (PurchasePrice-ის გარეშე)
- ჯერ **ხელით**: `Mappers/BookMapper` — ToResponse, ToEntity, UpdateFrom
- BooksController — მხოლოდ DTO-ები შემოდის და გადის
- მერე **Riok.Mapperly**: BookMapper გადაწერეთ partial-ად. Controller **არ** უნდა შეიცვალოს

## ✓ მზადაა, როცა

Swagger-ში POST-ს id არ აქვს, GET-ში purchasePrice არ ჩანს და Build-ზე Mapperly-ს გაფრთხილება არ არის

## ⭐ ბონუსი

- `BookResponse`-ს დაამატეთ `Author` — ნახეთ, სად შეიცვალა კოდი
- გახსენით `BookMapper.g.cs` და შეადარეთ თქვენს ხელით დაწერილს
- `GET /api/books/cheap` — **BookResponse**-ების სიით

## 💡 რჩევა

რიგი მნიშვნელოვანია: ჯერ ხელით დაწერილი Mapper, გატესტეთ Swagger-ში, მერე Mapperly. ორივე ვერსია უნდა გესმოდეთ. ShopApi ნიმუშია — გადაწერა კი არა, ყოველი ხაზის გაგებაა მიზანი. თუ ვერ მორჩით, სახლში დაასრულეთ.

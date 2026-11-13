# LibraryApi → async

დავალება · LibraryApi

## ნაბიჯები

- BooksController — `using Microsoft.EntityFrameworkCore;`
- 5 endpoint → `async Task<IActionResult>` · action-ების სახელები **Async-ის გარეშე**
- `ToListAsync` · `FindAsync` · `SaveChangesAsync` — ყველას `await` · `Add` / `Remove` უცვლელია
- თუ StatsController გაქვს — `CountAsync` და `AverageAsync`

## ✓ მზადაა, როცა

Ctrl+Shift+F → `.ToList()` და `.SaveChanges()` — 0 შედეგი, warning-ები არ არის, და Swagger-ში 5-ივე endpoint ისევ მუშაობს

## ⭐ ბონუსი

- `GetAll`-ში დაბეჭდე ნაკადის ნომერი `await`-მდე და შემდეგ — 5-ჯერ გაუშვი: რამდენჯერ შეიცვალა?
- `GetAll`-ს დაამატე `CancellationToken` და გადაეცი `ToListAsync`-ს

## 💡 რჩევა

ShopApi-ის გზა გაიარე: ჯერ `GetAll` (ერთი `await`), გაუშვი და შეამოწმე, მერე დანარჩენი. ყოველ მეთოდში სამი რამ იცვლება: `async`, `Task<IActionResult>` და `await` + Async მეთოდი. DTO-ები და BookMapper არ იცვლება — mapping გამოთვლაა, ლოდინი არ არის. ნაკადის ნომერი: `Environment.CurrentManagedThreadId`.

# LibraryDemo — ბიბლიოთეკა

კლასში · ~30 წთ · იგივე 5 ნაბიჯი

## ნაბიჯები

- ① SSMS: გაუშვი `LibraryDb.sql` (მასალებში)
- ② Console App **LibraryDemo** + 4 პაკეტი
- ③ `Scaffold-DbContext … Database=LibraryDb … -OutputDir Models`
- ④ Program.cs: წიგნები ავტორებით (`Include`) + 1 ახალი წიგნი · `Partials/Book.cs`: `Info => $"{Title} ({Year})"`
- ⑤ `LibraryDb-change.sql` (Books + Pages) → Scaffold `-Force`

## ✓ მზადაა, როცა

`Book.cs`-ში ჩანს `Pages`, და `Info` ისევ მუშაობს

## 💡 რჩევა

გაჭედე? ჯერ StoreDemo-ს სლაიდები (ნაბიჯები 1–5), მერე გვერდით მჯდომი, მერე ლექტორი. ყველაზე ხშირი შეცდომები Scaffold-ზეა: connection string, `Database=LibraryDb`, პაკეტები — „ხშირი შეცდომების“ სლაიდი.

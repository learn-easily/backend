# CinemaDemo — კინოთეატრი

იგივე 5 ნაბიჯი + ორი ახალი რამ

## მოთხოვნები

- SSMS: `CinemaDb.sql` — Movies, Sessions (მასალებში)
- CinemaDemo → Scaffold, კონტექსტის სახელი: `-Context CinemaContext`
- დაბეჭდე სეანსები დროის მიხედვით: „19:30 · ოპენჰაიმერი · 15.00 ₾“
- `Partials/Session.cs`: `Time => StartsAt.ToString("HH:mm")`
- `CinemaDb-change.sql` (Halls + HallId) → `-Force` → დაბეჭდე დარბაზიც

## ✓ მზადაა, როცა

კონსოლი ბეჭდავს: დრო · ფილმი · ფასი · დარბაზი — და `Time` ისევ მუშაობს

## ⭐ ბონუსი

- `-Tables Movies -OutputDir OnlyMovies` — რა დაგენერირდა?
- `-DataAnnotations` — Session.cs-ში რა ატრიბუტები გაჩნდა და რა დარჩა `OnModelCreating`-ში?
- დაამატე დარბაზი უკვე არსებული სახელით — რას იტყვის ბაზა?

## 💡 მინიშნება

```csharp
db.Sessions
    .Include(s => s.Movie)
    .Include(s => s.Hall)
    .OrderBy(s => s.StartsAt)
```

დარბაზი შეიძლება `null` იყოს (`HallId INT NULL`) → `s.Hall?.Name`. ბონუსის მესამე პუნქტზე გაიხსენე: `Halls.Name` — `UNIQUE`.

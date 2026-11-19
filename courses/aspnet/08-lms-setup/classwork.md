# შენი LMS: პროექტი და Courses

დავალება · შენი LMS

## ნაბიჯები

- ახალი პროექტი **Lms.Api** (ASP.NET Core Web API, .NET 10, Controllers) + 4 EF Core პაკეტი + Swashbuckle
- `Entities/Course` · `Data/DataContext` (unique index **Title**-ზე) · connection string `appsettings.json`-ში → `Add-Migration InitialCreate` → `Update-Database`
- `Dtos/` სამი record · `Mappers/CourseMapper`
- `CoursesController`: **GetAll**, **GetById**, **Create** (400 · 409 · 201), ყველა async

## ✓ მზადაა, როცა

Swagger-ში ერთი და იგივე სახელით მეორე POST აბრუნებს **409**-ს, ცარიელი სახელი ან 0 კვირა **400**-ს, ხოლო GET-ში ახალი კურსი ჩანს

## ⭐ ბონუსი

- **Update** და **Delete** (204 · 404 · 409)
- სცადე `AnyAsync` შემოწმების გარეშე: ორჯერ ერთი სახელი → რა სტატუსი მოვიდა და რატომ?

## 💡 რჩევა

ShopApi-ის ნაცნობ გზას გაჰყევი, ოღონდ სახელები ლექსიკონიდან აიღე. რიგი: entity → DataContext → მიგრაცია → DTO → Mapper → Controller. ყოველი endpoint-ის შემდეგ Swagger-ში შეამოწმე და მხოლოდ მერე გადადი შემდეგზე.

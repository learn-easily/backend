# SchoolDemo — დამოუკიდებლად

დავალება · ~13 წთ

## ნაბიჯები

- ახალი **SchoolDemo**, ბაზა **SchoolDb**
- `Student`: `Id`, `FirstName`, `LastName` → `InitialCreate` + 3 სტუდენტი
- ახალი Entity `Group`: `Id`, `Name` — ერთ ჯგუფში ბევრი სტუდენტი → მიგრაცია
- `Program.cs`: 2 ჯგუფი, სტუდენტები გაანაწილე და დაბეჭდე „ჯგუფი → სტუდენტები“

## ✓ მზადაა, როცა

SSMS-ში ჩანს Groups + FK, და კონსოლი ჯგუფებს სტუდენტებით ბეჭდავს

## 💡 მინიშნება

სად იქნება FK — Students-ში თუ Groups-ში? („ბევრის“ მხარეს.) ძველ სტუდენტებს ჯგუფი არ აქვთ — გაიხსენე AddCategories. ჯგუფიდან სტუდენტები: `db.Groups.Include(g => g.Students)`.

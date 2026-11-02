# SchoolDemo — ისტორიაში მოგზაურობა

მიგრაციები წინ, უკან და SQL-ად

## მოთხოვნები

- SchoolDemo ბოლომდე: Group + 1-N კავშირი + დაბეჭდვა (თუ კლასში ვერ მორჩით)
- `Student`-ს `Email` → `Add-Migration AddStudentEmail` → წაიკითხე → `Update-Database`
- `Update-Database <Groups-ის მიგრაცია>` — უკან; SSMS: Email გაქრა? მერე ისევ წინ
- `Script-Migration` — შეინახე SQL, რომელიც EF-მა დაწერა

## ✓ მზადაა, როცა

`__EFMigrationsHistory`-ში 3 მიგრაციაა, და შეგიძლია ახსნა, რა მოხდა Email-ის მონაცემებს უკან დაბრუნებისას

## ⭐ ბონუსი

- Email-ს `int?`-ის მსგავსად ისე დაამატე, რომ ძველ სტუდენტებს ცარიელი კი არა, `NULL` ჰქონდეთ (`string?`)

## ამოხსნა

```csharp Group.cs
public class Group
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;
    public List<Student> Students { get; set; } = new List<Student>();
}
```

```csharp Student.cs
public class Student
{
    public int Id { get; set; }
    public string FirstName { get; set; } = string.Empty;
    public string LastName { get; set; } = string.Empty;
    public string? Email { get; set; }        // NULL ძველებისთვის

    public int? GroupId { get; set; }         // ძველ სტუდენტებს ჯგუფი არ აქვთ
    public Group? Group { get; set; }
}
```

```plain Package Manager Console !
Add-Migration AddGroups
Update-Database
Add-Migration AddStudentEmail
Update-Database

Update-Database AddGroups   # უკან: Email სვეტი იშლება
Update-Database             # წინ: Email ბრუნდება — ცარიელი
Script-Migration            # ყველა მიგრაცია — SQL-ად
```

```warn
უკან დაბრუნებისას `Down()` სვეტს **შლის** — მასში ჩაწერილი Email-ები სამუდამოდ იკარგება. წინ რომ წახვალ, სვეტი ცარიელი დაბრუნდება. ამიტომაა წესი: გაშვებულ მიგრაციას რეალურ ბაზაზე ასე არ „ვატრიალებთ“ — ახალ მიგრაციას ვწერთ.
```

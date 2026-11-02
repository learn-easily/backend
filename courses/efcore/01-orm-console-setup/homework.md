# SchoolDemo — კურსები და ახალი სვეტი

ორი ახალი მიგრაცია

## მოთხოვნები

- `Course`: `Id`, `Title`, `Credits` · `Add-Migration AddCourses` (თუ კლასში ვერ მოასწარით)
- `Student`-ს დაამატეთ `Email` → `Add-Migration AddStudentEmail` → `Update-Database`
- `Program.cs`: 2 კურსი და Email-ები სტუდენტებისთვის · `SaveChanges`
- დაბეჭდეთ მხოლოდ 18+ სტუდენტები, ასაკით დალაგებული (`Where` + `OrderBy`)

## ✓ მზადაა, როცა

`__EFMigrationsHistory`-ში 3 ჩანაწერია და SSMS-ში Students ცხრილს Email სვეტი აქვს

## ⭐ ბონუსი

- `Remove-Migration` — შექმენით ზედმეტი მიგრაცია და `Update-Database`-მდე წაშალეთ

## ამოხსნა

```csharp Student.cs
public class Student
{
    public int Id { get; set; }
    public string FirstName { get; set; } = string.Empty;
    public string LastName { get; set; } = string.Empty;
    public int Age { get; set; }
    public string Email { get; set; } = string.Empty;   // ახალი
}
```

```plain Package Manager Console
Add-Migration AddStudentEmail
Update-Database
```

```csharp Program.cs !
using var db = new DataContext();

db.Courses.Add(new Course { Title = "C#", Credits = 6 });
db.Courses.Add(new Course { Title = "SQL", Credits = 4 });
db.SaveChanges();

var adults = db.Students
    .Where(s => s.Age >= 18)
    .OrderBy(s => s.Age)
    .ToList();

foreach (var s in adults)
    Console.WriteLine($"{s.FirstName} {s.LastName}, {s.Age} — {s.Email}");
```

```note
`Email`-ის დამატებისას არსებულ სტუდენტებს Email არ აქვთ. `string`-ს `= string.Empty` აქვს, ამიტომ მიგრაცია სვეტს `NOT NULL`-ად და ნაგულისხმევი `''`-ით ქმნის — ძველი ჩანაწერები ცარიელ Email-ს მიიღებენ. `Where` და `OrderBy` C#-ში წერია, მაგრამ ბაზაში SQL-ად მიდის: `WHERE Age >= 18 ORDER BY Age`.
```

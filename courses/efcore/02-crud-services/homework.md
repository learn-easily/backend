# SchoolDemo — StudentService და მენიუ

საშინაოს SchoolDemo მენიუთი იმართება

## მოთხოვნები

- `Services/StudentService`: `GetAll`, `GetById`, `Add`, `UpdateEmail`, `Delete`
- `GetAdults()` — 18+ სტუდენტები ასაკით: წინა საშინაოს query სერვისში გადადის
- `Program.cs`: მენიუ — სია, 18+, დამატება, Email-ის შეცვლა, წაშლა, `0` — გასვლა
- Id და ასაკი — `int.TryParse`-ით: ასოებზე პროგრამა არ უნდა გაჩერდეს

## ✓ მზადაა, როცა

Program.cs-ში არცერთი `db.` არ წერია, და მენიუდან შეცვლილი Email SSMS-შიც ჩანს

## ⭐ ბონუსი

- ძებნა გვარით: `Where(s => s.LastName.Contains(text))`
- `CourseService` იმავე ნიმუშით და მენიუში პუნქტი „კურსები“

## 💡 მინიშნება

`int.TryParse(Console.ReadLine(), out var id)` აბრუნებს `true`-ს, თუ რიცხვი შეიყვანეს, და `id`-ში წერს მას. `false`-ზე — დაწერე „არასწორი Id“ და მენიუს დაუბრუნდი.

## ამოხსნა

```csharp Services/StudentService.cs
namespace SchoolDemo.Services;

public class StudentService
{
    private readonly DataContext _db = new DataContext();

    public List<Student> GetAll() => _db.Students.ToList();

    public List<Student> GetAdults() =>
        _db.Students.Where(s => s.Age >= 18).OrderBy(s => s.Age).ToList();

    public Student? GetById(int id) => _db.Students.Find(id);

    public Student Add(Student student)
    {
        _db.Students.Add(student);
        _db.SaveChanges();
        return student;
    }

    // UpdateEmail, Delete — ქვემოთ
}
```

```csharp Services/StudentService.cs · UpdateEmail, Delete !
public bool UpdateEmail(int id, string email)
{
    var student = GetById(id);
    if (student is null) return false;

    student.Email = email;
    _db.SaveChanges();
    return true;
}

public bool Delete(int id)
{
    var student = GetById(id);
    if (student is null) return false;

    _db.Students.Remove(student);
    _db.SaveChanges();
    return true;
}
```

```csharp Program.cs · მენიუ
using SchoolDemo.Services;

Console.OutputEncoding = System.Text.Encoding.UTF8;
Console.InputEncoding = System.Text.Encoding.Unicode;

var service = new StudentService();

while (true)
{
    Console.WriteLine("\n1. სია  2. 18+  3. დამატება  4. Email  5. წაშლა  0. გასვლა");
    Console.Write("არჩევანი: ");

    switch (Console.ReadLine())
    {
        case "1": Print(service.GetAll()); break;
        case "2": Print(service.GetAdults()); break;
        case "3": AddStudent(); break;
        case "4": ChangeEmail(); break;
        case "5": DeleteStudent(); break;
        case "0": return;
        default: Console.WriteLine("არასწორი არჩევანი"); break;
    }
}

void ChangeEmail()
{
    if (!TryReadInt("Id: ", out var id)) return;
    Console.Write("ახალი Email: ");
    var email = Console.ReadLine() ?? "";
    Console.WriteLine(service.UpdateEmail(id, email) ? "✓ შეიცვალა" : "✗ ვერ მოიძებნა");
}

bool TryReadInt(string label, out int value)
{
    Console.Write(label);
    if (int.TryParse(Console.ReadLine(), out value)) return true;
    Console.WriteLine("✗ რიცხვი შეიყვანე");
    return false;
}

// Print, AddStudent, DeleteStudent — იმავე ნიმუშით
```

```note
Program.cs-ში `db.` აღარსად წერია: მენიუმ მხოლოდ ის იცის, **რა** უნდა გაკეთდეს (`service.UpdateEmail`), და არა — **როგორ** (Find, SaveChanges). `UpdateEmail` და `Delete` `bool`-ს აბრუნებს, ამიტომ მენიუ თვითონ წყვეტს, რა დაწეროს: „შეიცვალა“ თუ „ვერ მოიძებნა“.
```

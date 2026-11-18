# სკოლა 🏫

მოსწავლე და მასწავლებელი — ორივე ადამიანია

## მოთხოვნები

- Console App **School**, კლასები ცალკე ფაილებში. `Person`: `Name` (ცარიელი → „უცნობი“), `Age { get; private set; }` (მინიმუმ 5), `Introduce()`
- `Student : Person`: `Grade` (1–12, `private set`), `Study()`
- `Teacher : Person`: `Subject`, `Teach(Student student)` — ბეჭდავს, ვინ ვის ასწავლის. კონსტრუქტორები — `: base(name, age)`-ით
- Main-ში: 2 მოსწავლე და 1 მასწავლებელი; `Person[] people` → ყველა წარდგება `foreach`-ით; მერე `Study()` და `Teach()`

## ✓ მზადაა, როცა

`Name`-ისა და `Age`-ის კოდი მხოლოდ `Person`-შია; `new Student("ანა", 15, 99)` → კლასი 12; `Person[]`-ში ორივე ტიპი ეტევა

## ⭐ ბონუსი

- `Director : Teacher` — დირექტორიც მასწავლებელია! დაამატე `void Announce(string text)`. შვილის შვილს — `Person`-ის ყველაფერიც აქვს

## ამოხსნა

```csharp Program.cs · Main !
Student ana = new Student("ანა", 15, 9);
Student gio = new Student("გიო", 16, 10);
Teacher nino = new Teacher("ნინო", 34, "მათემატიკა");

Person[] people = { ana, gio, nino };
foreach (Person p in people)
{
    p.Introduce();
}

ana.Study();
nino.Teach(gio);
```

```csharp Person.cs
internal class Person
{
    private string name = "";

    public string Name
    {
        get { return name; }
        set
        {
            if (value == "") name = "უცნობი";
            else name = value;
        }
    }

    public int Age { get; private set; }

    public Person(string name, int age)
    {
        Name = name;
        if (age < 5) age = 5;
        Age = age;
    }

    public void Introduce()
    {
        Console.WriteLine($"👋 მე ვარ {Name}, {Age} წლის");
    }
}
```

```csharp Student.cs · Teacher.cs
internal class Student : Person
{
    public int Grade { get; private set; }

    public Student(string name, int age, int grade) : base(name, age)
    {
        if (grade < 1) grade = 1;
        if (grade > 12) grade = 12;
        Grade = grade;
    }

    public void Study()
    {
        Console.WriteLine($"📚 {Name} სწავლობს {Grade} კლასში");
    }
}

internal class Teacher : Person
{
    public string Subject { get; private set; }

    public Teacher(string name, int age, string subject) : base(name, age)
    {
        Subject = subject;
    }

    public void Teach(Student student)
    {
        Console.WriteLine($"🧑‍🏫 {Name} → {student.Name} · გაკვეთილი: {Subject}");
    }
}
```

```note
`Name`-ისა და `Age`-ის წესები მხოლოდ `Person`-შია — `Student` და `Teacher` მათ მემკვიდრეობით იღებენ. `Person[]`-ში ორივე ეტევა, რადგან მოსწავლეც და მასწავლებელიც **არის** ადამიანი. ოღონდ `p.Study()` ციკლში ვერ გამოიძახება — `Person`-მა არ იცის, რომ შიგნით მოსწავლეა.
```

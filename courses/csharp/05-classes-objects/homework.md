# სკოლის ჟურნალი

მოსწავლეები, ქულები და შეფასებები — კლასებით

## მოთხოვნები

- ახალი Console App: **SchoolJournal**, კლასი `Student` — **Student.cs**-ში
- `Student`: `Name` და `int[] Scores` (property-ები)
- ორი კონსტრუქტორი: `Student(string name, int[] scores)` და `Student(string name)` — მეორე სამ ნულოვან ქულას აძლევს (`new int[3]`)
- მეთოდები: `double Average()`, `string Grade()` (switch expression: 9+ ფრიადი, 7+ კარგი, 5+ საშუალო, სხვა — არადამაკმაყოფილებელი), `void PrintReport()`
- Main-ში: `Student[]` მინიმუმ 4 მოსწავლით (ორივე კონსტრუქტორით), ყველას რეპორტი, საუკეთესო მოსწავლე და ფრიადოსნების რაოდენობა
- `PrintReport` ბეჭდავს: `ანა — ქულები: 9 10 8 · საშუალო 9.0 · ფრიადი`

## ✓ მზადაა, როცა

ყველა მოსწავლის რეპორტი იბეჭდება, საშუალო ერთი ციფრით მძიმის შემდეგ, საუკეთესო და ფრიადოსნების რაოდენობა სწორია

## ⭐ ბონუსი

- მოსწავლეები კონსოლიდან შეიყვანე: ჯერ რამდენი მოსწავლეა, მერე თითოეულის სახელი და 3 ქულა (ცალკე `static` მეთოდი `Student ReadStudent()`)

## ამოხსნა

```csharp Program.cs · Main !
Student[] students =
{
    new Student("ნიკა", new int[] { 8, 9, 7 }),
    new Student("ანა", new int[] { 9, 10, 8 }),
    new Student("ლუკა", new int[] { 6, 7, 5 }),
    new Student("მარიამი")
};

Student best = students[0];
int excellent = 0;

foreach (Student s in students)
{
    s.PrintReport();
    if (s.Average() > best.Average()) best = s;
    if (s.Grade() == "ფრიადი") excellent++;
}

Console.WriteLine($"🏆 საუკეთესო: {best.Name} · ფრიადოსნები: {excellent}");
```

```csharp Student.cs · namespace-ის შიგნით
internal class Student
{
    public string Name { get; set; }
    public int[] Scores { get; set; }

    public Student(string name, int[] scores)
    {
        Name = name;
        Scores = scores;
    }

    public Student(string name)
    {
        Name = name;
        Scores = new int[3];
    }

    public double Average()
    {
        int sum = 0;
        foreach (int s in Scores)
        {
            sum += s;
        }
        return sum * 1.0 / Scores.Length;
    }

    public string Grade()
    {
        return Average() switch
        {
            >= 9 => "ფრიადი",
            >= 7 => "კარგი",
            >= 5 => "საშუალო",
            _ => "არადამაკმაყოფილებელი"
        };
    }

    public void PrintReport()
    {
        Console.Write($"{Name} — ქულები: ");
        foreach (int s in Scores)
        {
            Console.Write(s + " ");
        }
        Console.WriteLine($"· საშუალო {Average():F1} · {Grade()}");
    }
}
```

```note
`Grade()` საკუთარ `Average()`-ს იძახებს — კლასის მეთოდებს ერთმანეთის გამოძახება შეუძლიათ. `new int[] { 8, 9, 7 }` — მასივი პირდაპირ კონსტრუქტორის პარამეტრად. `new Student("მარიამი")` მეორე კონსტრუქტორს იძახებს — მარიამს სამი ნული აქვს.
```

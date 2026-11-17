# სკოლის ჟურნალი

მოსწავლეები, ქულები და შეფასებები — კლასებით

## მოთხოვნები

- ახალი Console App: **SchoolJournal**, კლასი `Student` — **Student.cs**-ში
- `Student`: `Name { get; }`, `int[] Scores { get; }`, კონსტრუქტორი `Student(string name, int[] scores)`
- მეთოდები: `double Average()`, `string Grade()` (switch expression: 9+ ფრიადი, 7+ კარგი, 5+ საშუალო, სხვა — არადამაკმაყოფილებელი), `void PrintReport()`
- Program.cs-ში: `Student[]` მინიმუმ 4 მოსწავლით, ყველას რეპორტი, საუკეთესო მოსწავლე და ფრიადოსნების რაოდენობა
- `PrintReport` ბეჭდავს: `ანა — ქულები: 9 10 8 · საშუალო 9.0 · ფრიადი`

## ✓ მზადაა, როცა

ყველა მოსწავლის რეპორტი იბეჭდება, საშუალო ერთი ციფრით მძიმის შემდეგ, საუკეთესო და ფრიადოსნების რაოდენობა სწორია

## ⭐ ბონუსი

- მოსწავლეები კონსოლიდან შეიყვანე: ჯერ რამდენი მოსწავლეა, მერე თითოეულის სახელი და 3 ქულა (ცალკე მეთოდი `Student ReadStudent()`)

## ამოხსნა

```csharp Student.cs !
public class Student
{
    public string Name { get; }
    public int[] Scores { get; }

    public Student(string name, int[] scores)
    {
        Name = name;
        Scores = scores;
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

```csharp Program.cs
Student[] students =
{
    new Student("ნიკა", new int[] { 8, 9, 7 }),
    new Student("ანა", new int[] { 9, 10, 8 }),
    new Student("ლუკა", new int[] { 6, 7, 5 }),
    new Student("მარიამი", new int[] { 10, 9, 10 })
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

```note
`Grade()` საკუთარ `Average()`-ს იძახებს — კლასის მეთოდებს ერთმანეთის გამოძახება შეუძლიათ. `new int[] { 8, 9, 7 }` — მასივი პირდაპირ კონსტრუქტორის პარამეტრად; `{ 8, 9, 7 }` მარტო აქ არ კმარა, რადგან ცვლადის გამოცხადება არ ხდება.
```

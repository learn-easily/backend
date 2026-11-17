# კალკულატორი 2.0 — მეთოდებით

ლექცია 2-ის კალკულატორი — მენიუთი და მეთოდებით

## მოთხოვნები

- ახალი Console App: **Calculator**
- სამი მეთოდი: `double ReadDouble(string question)`, `double Calculate(double a, double b, string op)` (switch expression) და `void PrintResult(double a, double b, string op, double result)` — ფერით: `7 / 2 = 3.5`
- `do-while` მენიუ: გამოთვლის შემდეგ „კიდევ? (კი/არა)“
- 0-ზე გაყოფა: `Calculate`-მდე შეამოწმე და დაბეჭდე გაფრთხილება
- ძირითადი კოდი (მეთოდების ზემოთ) — **15 ხაზზე ნაკლები**

## ✓ მზადაა, როცა

`7 / 2` → `3.5`, `5 * 4` → `20`, `1 / 0` → გაფრთხილება (პროგრამა არ ჩავარდა), „კი“-ზე ახალი გამოთვლა იწყება

## ⭐ ბონუსი

- დაამატე `^` (ხარისხი) — ციკლით, საკუთარი მეთოდით `double Power(double x, int n)`
- გამოთვლების ისტორია: ბოლო 5 პასუხი მასივში, „ისტორია“ ბრძანებაზე დაიბეჭდოს

## ამოხსნა

```csharp Program.cs · ძირითადი კოდი !
string again;

do
{
    double a = ReadDouble("პირველი რიცხვი");
    Console.Write("ოპერაცია (+ - * /): ");
    string op = Console.ReadLine();
    double b = ReadDouble("მეორე რიცხვი");

    if (op == "/" && b == 0)
    {
        Console.WriteLine("⚠ 0-ზე გაყოფა არ შეიძლება");
    }
    else
    {
        PrintResult(a, b, op, Calculate(a, b, op));
    }

    Console.Write("კიდევ? (კი/არა) ");
    again = Console.ReadLine();
} while (again == "კი");
```

```csharp Program.cs · მეთოდები (ძირითადი კოდის ქვემოთ)
double ReadDouble(string question)
{
    Console.Write($"{question}: ");
    return double.Parse(Console.ReadLine());
}

double Calculate(double a, double b, string op)
{
    return op switch
    {
        "+" => a + b,
        "-" => a - b,
        "*" => a * b,
        "/" => a / b,
        _ => 0
    };
}

void PrintResult(double a, double b, string op, double result)
{
    Console.ForegroundColor = ConsoleColor.Green;
    Console.WriteLine($"{a} {op} {b} = {result}");
    Console.ResetColor();
}
```

```note
`return op switch { … };` — switch expression მნიშვნელობას აბრუნებს, ამიტომ მისი შედეგი პირდაპირ `return`-ით შეგვიძლია დავაბრუნოთ, ცალკე ცვლადის გარეშე. `PrintResult(a, b, op, Calculate(a, b, op))` — ჯერ `Calculate` სრულდება, მისი პასუხი კი `PrintResult`-ის მეოთხე პარამეტრი ხდება.
```

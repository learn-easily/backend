# ჯიბის კალკულატორი

ინსტალაცია + კალკულატორი + ასაკი დღეებში

## მოთხოვნები

- **Visual Studio 2026** Community დააინსტალირე: ☑ .NET desktop development, ☑ ASP.NET and web development
- ახალი Console App: **PocketCalculator**
- ჰკითხე ორი მთელი რიცხვი და დაბეჭდე: ჯამი, სხვაობა, ნამრავლი, განაყოფი **ათწილადით** (`7 / 2` → `3.5`) და ნაშთი
- ყოველი პასუხი სხვა ფერით (`Console.ForegroundColor`)
- მეორე ნაწილი: ჰკითხე ასაკი წლებში → დაბეჭდე, დაახლოებით რამდენი დღის, საათის და წუთის ხარ
- კლასის დავალებები, რაც ვერ მოასწარი — ⭐ → ⭐⭐⭐

## ✓ მზადაა, როცა

`7` და `2`-ზე პროგრამა ბეჭდავს: `9`, `5`, `14`, `3.5`, `1` — ხოლო ასაკ `15`-ზე ≈ `5475` დღეს

## ⭐ ბონუსი

- კალკულატორმა ათწილადებიც მიიღოს (`double.Parse`) — `2.5` და `4`

## ამოხსნა

```csharp Program.cs !
Console.OutputEncoding = System.Text.Encoding.UTF8;

Console.Write("პირველი რიცხვი: ");
int a = int.Parse(Console.ReadLine());
Console.Write("მეორე რიცხვი: ");
int b = int.Parse(Console.ReadLine());

Console.ForegroundColor = ConsoleColor.Green;
Console.WriteLine($"{a} + {b} = {a + b}");
Console.ForegroundColor = ConsoleColor.Cyan;
Console.WriteLine($"{a} - {b} = {a - b}");
Console.ForegroundColor = ConsoleColor.Yellow;
Console.WriteLine($"{a} * {b} = {a * b}");
Console.ForegroundColor = ConsoleColor.Magenta;
Console.WriteLine($"{a} / {b} = {a * 1.0 / b}");
Console.ForegroundColor = ConsoleColor.Red;
Console.WriteLine($"{a} % {b} = {a % b}");
Console.ResetColor();
```

```csharp ასაკი დღეებში
Console.Write("რამდენი წლის ხარ? ");
int years = int.Parse(Console.ReadLine());

int days = years * 365;
int hours = days * 24;
int minutes = hours * 60;

Console.WriteLine($"≈ {days} დღე, {hours} საათი, {minutes} წუთი");
```

```note
`a * 1.0 / b` — `1.0`-ზე გამრავლება `a`-ს ათწილადად აქცევს **გაყოფამდე**, ამიტომ `int / int` აღარაა და `3.5` გამოდის. ზუსტად ის ხრიკია, რაც ლექციაზე ნახე: `7.0 / 2`. თუ `a / b * 1.0` დაწერ, ჯერ გაიყოფა (`3`) და მერე გამრავლდება — `3`.
```

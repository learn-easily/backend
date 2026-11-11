# ბოტების ტურნირი

სამი ტვინი, ერთი ჩემპიონი

## მოთხოვნები

- `CreateBrain(type, me, random)` აბრუნებს `Func<int>`-ს — ტვინს, რომელიც **საკუთარ** სიცოცხლეს ამოწმებს
- სამი ტვინი: **აგრესიული**, **ფრთხილი**, **შემთხვევითი**
- `Fight(typeA, typeB, random)` — ორი ბოტის ბრძოლა, აბრუნებს გამარჯვებულს
- ყოველი წყვილი 10-ჯერ ებრძვის. ვინ მოიგო ყველაზე მეტჯერ?

## ✓ მზადაა, როცა

პროგრამა თავისით ატარებს 30 ბრძოლას და ბეჭდავს: `აგრესიული: 14 · ფრთხილი: 11 · შემთხვევითი: 5`

## ⭐ ბონუსი

- მოიფიქრე **მეოთხე** ტვინი, რომელიც სამივეს აჯობებს — მაგ. მოწინააღმდეგის სიცოცხლესაც უყურებს

## 💡 მინიშნება

- **აგრესიული** — სულ ძლიერი დარტყმა, იკურნება მხოლოდ 15 HP-ზე ქვემოთ
- **ფრთხილი** — ჩვეულებრივი დარტყმა, იკურნება 50 HP-ზე ქვემოთ
- **შემთხვევითი** — `random.Next(1, 4)`
- 100 რაუნდზე მეტი → ფრე, რომ ორი ფრთხილი ბოტი უსასრულოდ არ იკურნებოდეს

მეთოდების სრული სიგნატურები: `static Func<int> CreateBrain(string type, Fighter me, Random random)` და `static string Fight(string typeA, string typeB, Random random)`.

ტურნირში `DoMove` ბევრს ბეჭდავს — ბრძოლის დროს შეტყობინებები არ გჭირდება, ამიტომ `OnDamaged`-ს ტურნირში ნუ გამოიწერ. გამარჯვებულების დასათვლელად საკმარისია `int[] wins = new int[3];`

## ამოხსნა

```csharp Program.cs · ტვინები !
static Func<int> CreateBrain(string type, Fighter me, Random random)
{
    if (type == "აგრესიული")
        return () => me.Health < 15 ? 3 : 2;

    if (type == "ფრთხილი")
        return () => me.Health < 50 ? 3 : 1;

    return () => random.Next(1, 4);
}
```

```csharp Program.cs · ბრძოლა
static string Fight(string typeA, string typeB, Random random)
{
    Fighter a = new Fighter { Name = typeA };
    Fighter b = new Fighter { Name = typeB };

    a.ChooseMove = CreateBrain(typeA, a, random);
    b.ChooseMove = CreateBrain(typeB, b, random);

    for (int round = 1; round <= 100; round++)
    {
        DoMove(a, b, random);
        if (b.Health == 0) return a.Name;

        DoMove(b, a, random);
        if (a.Health == 0) return b.Name;
    }

    return "ფრე";
}
```

```csharp Program.cs · ტურნირი
Random random = new Random();
string[] types = { "აგრესიული", "ფრთხილი", "შემთხვევითი" };
int[] wins = new int[types.Length];

for (int i = 0; i < types.Length; i++)
{
    for (int j = i + 1; j < types.Length; j++)
    {
        for (int k = 0; k < 10; k++)
        {
            string winner = Fight(types[i], types[j], random);

            for (int t = 0; t < types.Length; t++)
                if (types[t] == winner) wins[t]++;
        }
    }
}

for (int t = 0; t < types.Length; t++)
    Console.WriteLine($"{types[t]}: {wins[t]}");
```

```note
`CreateBrain` ლამბდას აბრუნებს, რომელიც `me`-ს „იმახსოვრებს“. ამიტომ ორი ფრთხილი ბოტიც კი სწორად მუშაობს — თითოეული **თავის** სიცოცხლეს ამოწმებს. ლექციაზე `player.ChooseMove = bot.ChooseMove;` ზუსტად ამიტომ იყო უსამართლო: ორივე ტვინი `bot.Health`-ს უყურებდა.
```

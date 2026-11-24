# ⚽ ფეხბურთის კლუბი · ნაწილი 1 — პენალტები

ვიწყებთ ჩვენს კლუბს: მოთამაშეები, მეკარე და პენალტების სერია. ამ პროექტს ყოველ ლექციაზე გავაგრძელებთ — ბოლოს მთელი სეზონი გაითამაშება

## მოთხოვნები

- Console App **FootballClub**, კლასი `Player` (**Player.cs**): `Name`, `Shot` (დარტყმა 0–100), `Reflex` (მეკარის რეაქცია 0–100), `Stamina` (თავიდან 100) — კონსტრუქტორით `Player(string name, int shot, int reflex)`
- Program-ში `static void Train(Player p)` — `Shot` +5 (მაქს. 100), `Stamina` −20 (მინ. 0)
- Program-ში `static bool Penalty(Player shooter, Player keeper)` — გოლის შანსი: `shooter.Shot - keeper.Reflex / 2`; შემსრულებელს `Stamina` −5
- Main-ში: `Player[] shooters` — 3 მოთამაშე, ერთი მეკარე. ერთ-ერთი ივარჯიშოს, მერე 5 პენალტი — შემსრულებლები რიგრიგობით; ყოველი დარტყმა იბეჭდება, ბოლოს — „შედეგი: 3/5“

## ✓ მზადაა, როცა

`Train(shooters[2])`-ის შემდეგ `shooters[2].Shot` ნამდვილად გაიზარდა; პენალტის შემდეგ შემსრულებელს `Stamina` დააკლდა; შეგიძლია ახსნა, რატომ ცვლის მეთოდი ნამდვილ მოთამაშეს

## ⭐ ბონუსი

- ორი გუნდის სერია: ორივე გუნდი 5-5 პენალტს ურტყამს (თითოეულს თავისი მეკარე ჰყავს). ფრე? — „ოქროს პენალტი“: სანამ ერთი არ გაიტანს და მეორე არ ააცილებს

## ამოხსნა

```csharp Program.cs · Main !
Player[] shooters =
{
    new Player("ნიკა", 70, 10),
    new Player("ლუკა", 60, 10),
    new Player("გიო", 50, 10)
};
Player keeper = new Player("საბა", 20, 60);

Train(shooters[2]);
Console.WriteLine($"💪 {shooters[2].Name}: დარტყმა {shooters[2].Shot}, ენერგია {shooters[2].Stamina}");

int goals = 0;
for (int i = 0; i < 5; i++)
{
    Player shooter = shooters[i % shooters.Length];

    if (Penalty(shooter, keeper))
    {
        goals++;
        Console.WriteLine($"⚽ {shooter.Name} — გოოოლი!");
    }
    else
    {
        Console.WriteLine($"🧤 {keeper.Name} იგერიებს {shooter.Name}-ის დარტყმას");
    }
}
Console.WriteLine($"შედეგი: {goals}/5");
```

```csharp Program.cs · დამხმარე მეთოდები
static void Train(Player p)
{
    p.Shot += 5;
    if (p.Shot > 100) p.Shot = 100;

    p.Stamina -= 20;
    if (p.Stamina < 0) p.Stamina = 0;
}

static bool Penalty(Player shooter, Player keeper)
{
    int chance = shooter.Shot - keeper.Reflex / 2;
    shooter.Stamina -= 5;
    return Random.Shared.Next(100) < chance;
}
```

```csharp Player.cs · namespace-ის შიგნით
internal class Player
{
    public string Name { get; set; }
    public int Shot { get; set; }
    public int Reflex { get; set; }
    public int Stamina { get; set; } = 100;

    public Player(string name, int shot, int reflex)
    {
        Name = name;
        Shot = shot;
        Reflex = reflex;
    }
}
```

```note
`Train` და `Penalty` მოთამაშის **მისამართს** იღებენ — ამიტომ ცვლიან ნამდვილ ობიექტს მასივში და არა ასლს. `Player shooter = shooters[...]` ახალ მოთამაშეს არ ქმნის — იგივე ობიექტზე მეორე „ისარია“. `i % shooters.Length` → 0, 1, 2, 0, 1 — რიგრიგობით. ყურადღება: ახლა Main-ს შეუძლია `keeper.Reflex = 1000;` — ამას შემდეგ ლექციაზე გავასწორებთ.
```

# ⚽ ფეხბურთის კლუბი · ნაწილი 3 — პოზიციები

მეკარე, მცველი და თავდამსხმელი — ყველა მოთამაშეა, მაგრამ თითოეულს თავისი უნარი აქვს

## მოთხოვნები

- `Player` — საერთო მშობელი: `Name`, `Stamina`, `Price`, `Rest()` და `protected` მეთოდები `Roll(int min, int max)` და `Tire(int amount)`. `Shot` და `Reflex` აქედან გადის — ისინი პოზიციებს ეკუთვნის
- `Goalkeeper : Player` — `Reflex`, `bool Save(int power)` · `Defender : Player` — `Defense`, `bool Tackle()` · `Striker : Player` — `Shot`, `int Shoot()`. ყოველი მოქმედება ენერგიას ხარჯავს `Tire`-ით
- ფასი უნარიდან: `: base(name, reflex * 300)`
- `Club`-ში `Buy(Player p)` არ იცვლება — ყველა პოზიციას იღებს; `PrintSquad`-დან `Shot`/`Reflex` ამოდის (ბეჭდავს სახელს, ენერგიას, ფასს). Main-ში კლუბი 120 000 ₾-ით: 1 მეკარე, 2 მცველი, 2 თავდამსხმელი
- `Penalty` გადააკეთე: `static bool Penalty(Striker s, Goalkeeper g)` → `!g.Save(s.Shoot())`

## ✓ მზადაა, როცა

`Name`-ის წესი და ენერგიის კოდი მხოლოდ `Player`-შია; `club.Buy(new Striker(...))` მუშაობს; `striker.Roll(1, 2)` Main-ში წითელ ხაზს აჩენს; `PrintSquad`-ს უნარების დაბეჭდვა აღარ შეუძლია — რატომ? (ამას შემდეგ ლექციაზე გადავწყვეტთ)

## ⭐ ბონუსი

- `Winger : Striker` — ფლანგელი: `Cross()` (ჩაწოდება, 40–70). შვილიშვილს `Shoot()`-იც აქვს და `Rest()`-იც

## ამოხსნა

```csharp Program.cs · Main !
Club club = new Club("დინამო", 120000);

Goalkeeper saba = new Goalkeeper("საბა", 75);
Striker nika = new Striker("ნიკა", 80);
club.Buy(saba);
club.Buy(new Defender("ლუკა", 70));
club.Buy(new Defender("დათო", 60));
club.Buy(nika);
club.Buy(new Striker("გიო", 55));
club.PrintSquad();   // Club.cs-ში: Console.WriteLine($"   {p.Name} ⚡ {p.Stamina} · {p.Price} ₾");

for (int i = 0; i < 3; i++)
{
    Console.WriteLine(Penalty(nika, saba) ? "⚽ გოლი!" : "🧤 მოიგერია!");
}
```

```csharp Program.cs · დამხმარე მეთოდები
static bool Penalty(Striker s, Goalkeeper g)
{
    return !g.Save(s.Shoot());
}
```

```csharp Player.cs
internal class Player
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

    public int Stamina { get; private set; } = 100;
    public int Price { get; private set; }

    public Player(string name, int price)
    {
        Name = name;
        if (price < 0) price = 0;
        Price = price;
    }

    public void Rest()
    {
        Stamina += 30;
        if (Stamina > 100) Stamina = 100;
    }

    protected void Tire(int amount)
    {
        Stamina -= amount;
        if (Stamina < 0) Stamina = 0;
    }

    protected int Roll(int min, int max)
    {
        return Random.Shared.Next(min, max + 1);
    }
}
```

```csharp Goalkeeper.cs · Defender.cs · Striker.cs
internal class Goalkeeper : Player
{
    public int Reflex { get; private set; }

    public Goalkeeper(string name, int reflex) : base(name, reflex * 300)
    {
        Reflex = reflex;
    }

    public bool Save(int power)
    {
        Tire(5);
        return Roll(0, 100) < Reflex - power / 2;
    }
}

internal class Defender : Player
{
    public int Defense { get; private set; }

    public Defender(string name, int defense) : base(name, defense * 300)
    {
        Defense = defense;
    }

    public bool Tackle()
    {
        Tire(10);
        return Roll(0, 100) < Defense;
    }
}

internal class Striker : Player
{
    public int Shot { get; private set; }

    public Striker(string name, int shot) : base(name, shot * 300)
    {
        Shot = shot;
    }

    public int Shoot()
    {
        Tire(5);
        return Roll(Shot / 2, Shot);
    }
}
```

```note
`Club`-ში არაფერი შეგვიცვლია: `Player[] squad`-ში ყველა პოზიცია ეტევა, რადგან მეკარეც **არის** მოთამაშე. `PrintSquad`-ში დარჩა მხოლოდ `Name`, `Stamina` და `Price` — `Player`-მა არ იცის, რომ შიგნით თავდამსხმელია და `Shot` აქვს. `Tire` და `Roll` — `protected`: შვილები იყენებენ, Main ვერა.
```

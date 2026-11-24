# ⚽ ფეხბურთის კლუბი · ნაწილი 2 — ტრანსფერები

კლუბს აქვს ბიუჯეტი და შემადგენლობა — და ვერავინ „მოიპარავს“ ფულს ან მოთამაშის მონაცემებს

## მოთხოვნები

- `Player` დაიცავი: `Name` — წესით (ცარიელი → „უცნობი“); `Shot`, `Reflex`, `Stamina` — `{ get; private set; }` და ყოველთვის 0–100; ახალი `Price { get; private set; }` (კონსტრუქტორში)
- `Train()` და `Rest()` — `Player`-ის მეთოდები: `Train` — `Shot` +5, `Stamina` −20 (`Stamina` 20-ზე ნაკლები → „დაღლილია“ და არაფერი იცვლება); `Rest` — `Stamina` +30
- ახალი კლასი `Club` (**Club.cs**): `Name`, `Budget { get; private set; }`, `private Player[] squad = new Player[5]` (მინი-ფეხბურთი — 5 მოთამაშე), `Count { get; private set; }`
- `bool Buy(Player p)` — გუნდი სავსეა ან ფული არ ჰყოფნის → `false` და არაფერი იცვლება; `void PrintSquad()`
- Main-ში: კლუბი 100 000 ₾-ით; სცადე 6 მოთამაშის ყიდვა — ერთი ძვირია, მეექვსეს ადგილი აღარ აქვს

## ✓ მზადაა, როცა

`club.Budget = 999999`, `club.squad[0] = null` და `player.Shot = 100` წითელ ხაზს აჩენს; ბიუჯეტი არასდროს ჩადის მინუსში; მე-6 მოთამაშე არ ემატება

## ⭐ ბონუსი

- `Club.TrainAll()` — მთელი გუნდი ვარჯიშობს; `bool Sell(int index)` — მოთამაშე იყიდება ნახევარ ფასად, დანარჩენები მასივში ერთით წინ ინაცვლებენ

## ამოხსნა

```csharp Program.cs · Main !
Club club = new Club("დინამო", 100000);

club.Buy(new Player("ნიკა", 80, 10, 30000));
club.Buy(new Player("ლუკა", 65, 15, 20000));
club.Buy(new Player("მესი", 99, 20, 900000));   // ❌ ძვირია
club.Buy(new Player("საბა", 20, 75, 25000));
club.Buy(new Player("გიო", 55, 10, 10000));
club.Buy(new Player("დათო", 60, 10, 10000));
club.Buy(new Player("ბექა", 50, 10, 5000));      // ❌ ადგილი აღარ არის

club.PrintSquad();
```

```csharp Player.cs · namespace-ის შიგნით
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

    public int Shot { get; private set; }
    public int Reflex { get; private set; }
    public int Stamina { get; private set; } = 100;
    public int Price { get; private set; }

    public Player(string name, int shot, int reflex, int price)
    {
        Name = name;
        Shot = Limit(shot);
        Reflex = Limit(reflex);
        if (price < 0) price = 0;
        Price = price;
    }

    private int Limit(int value)
    {
        if (value < 0) return 0;
        if (value > 100) return 100;
        return value;
    }

    public void Train()
    {
        if (Stamina < 20)
        {
            Console.WriteLine($"😮‍💨 {Name} დაღლილია");
            return;
        }
        Shot = Limit(Shot + 5);
        Stamina -= 20;
    }

    public void Rest()
    {
        Stamina = Limit(Stamina + 30);
    }
}
```

```csharp Club.cs · namespace-ის შიგნით
internal class Club
{
    private Player[] squad = new Player[5];

    public string Name { get; private set; }
    public int Budget { get; private set; }
    public int Count { get; private set; }

    public Club(string name, int budget)
    {
        Name = name;
        if (budget < 0) budget = 0;
        Budget = budget;
    }

    public bool Buy(Player p)
    {
        if (Count == squad.Length)
        {
            Console.WriteLine($"❌ {Name}: შემადგენლობა სავსეა");
            return false;
        }
        if (p.Price > Budget)
        {
            Console.WriteLine($"❌ {p.Name}-ისთვის ფული არ ჰყოფნის");
            return false;
        }

        Budget -= p.Price;
        squad[Count] = p;
        Count++;
        Console.WriteLine($"✍️ {p.Name} → {Name} ({p.Price} ₾)");
        return true;
    }

    public void PrintSquad()
    {
        Console.WriteLine($"🏟️ {Name} · ბიუჯეტი {Budget} ₾");
        for (int i = 0; i < Count; i++)
        {
            Player p = squad[i];
            Console.WriteLine($"   {p.Name} ⚽ {p.Shot} 🧤 {p.Reflex} ⚡ {p.Stamina}");
        }
    }
}
```

```note
`squad` — `private` ველი: გარედან მასივს ვერავინ შეეხება, მოთამაშე მხოლოდ `Buy`-ით ემატება. `Limit` — `private` დამხმარე მეთოდი: შიგნით სამჯერ გვჭირდება, გარედან — არავის. `Count` გვეუბნება, მასივის რამდენი ადგილია დაკავებული. წინა ნაწილის `static Train(Player p)` ახლა მოთამაშის საკუთარი მეთოდია — ცვლილების უფლება მხოლოდ მას აქვს.
```

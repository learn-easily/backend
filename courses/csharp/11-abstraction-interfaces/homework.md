# ⚽ ფეხბურთის კლუბი · ნაწილი 5 — მწვრთნელი და ხელფასები

კლუბს მწვრთნელი ჰყავს და თვის ბოლოს ყველას ხელფასი უნდა გადაუხადოს — ფული თუ არ ეყო, კრიზისია

## მოთხოვნები

- `Player` → `abstract`; `Rating()` → `abstract int Rating()` (პოზიციები თავად ითვლიან: უნარი + `Stamina / 5`)
- `interface IPayable` — `int Salary()`. `Player : IPayable` — ხელფასი `Price / 20`
- ახალი კლასი `Coach : IPayable` — **მოთამაშე არ არის**: `Name`, `Level` (1–5), `Salary()` → `Level * 2000`, `Bonus()` → `Level * 10`
- `Club` მწვრთნელს კონსტრუქტორში იღებს; `Strength()` მწვრთნელის `Bonus()`-საც ითვლის
- `Club.PaySalaries()` — `IPayable[] payroll`: ყველა მოთამაშე + მწვრთნელი → ჯამი; ფული არ ჰყოფნის → „💸 კრიზისი“ და `false`, თორემ ბიუჯეტს აკლდება
- Main-ში: ორი კლუბი, მატჩი, ორივე იხდის ხელფასს

## ✓ მზადაა, როცა

`new Player(...)` წითელ ხაზს აჩენს; მოთამაშეები და მწვრთნელი ერთ `IPayable[]`-ში ეტევიან, თუმცა საერთო მშობელი არ ჰყავთ; ხელფასის გადახდა ბიუჯეტს ამცირებს, მინუსში კი არ ჩადის

## ⭐ ბონუსი

- `Stadium : IPayable` — სტადიონის მოვლა (`Seats / 10` ₾). კლუბს სტადიონიც აქვს და ის `payroll`-შიც შედის — სამი სრულიად სხვადასხვა რამ, ერთი გადახდა

## ამოხსნა

```csharp Program.cs · Main !
Club dinamo = new Club("დინამო", 120000, new Coach("ქართლი", 4));
dinamo.Buy(new Goalkeeper("საბა", 75));
dinamo.Buy(new Defender("ლუკა", 70));
dinamo.Buy(new Defender("დათო", 60));
dinamo.Buy(new Striker("ნიკა", 80));
dinamo.Buy(new Striker("გიო", 55));

Club torpedo = new Club("ტორპედო", 120000, new Coach("ბერია", 2));
torpedo.Buy(new Goalkeeper("ზურა", 65));
torpedo.Buy(new Defender("ოთო", 75));
torpedo.Buy(new Defender("ბექა", 65));
torpedo.Buy(new Striker("ლევანი", 70));
torpedo.Buy(new Striker("ტოკო", 70));

PlayMatch(dinamo, torpedo);
dinamo.PaySalaries();
torpedo.PaySalaries();
```

```csharp IPayable.cs · Coach.cs
internal interface IPayable
{
    int Salary();
}

internal class Coach : IPayable
{
    public string Name { get; private set; }
    public int Level { get; private set; }

    public Coach(string name, int level)
    {
        Name = name;
        if (level < 1) level = 1;
        if (level > 5) level = 5;
        Level = level;
    }

    public int Salary()
    {
        return Level * 2000;
    }

    public int Bonus()
    {
        return Level * 10;
    }
}
```

```csharp Player.cs · ცვლილებები
internal abstract class Player : IPayable
{
    // … Name, Stamina, Price, Rest, Tire, Roll, Train, ToString — როგორც იყო

    public abstract int Rating();

    public int Salary()
    {
        return Price / 20;
    }
}

// Striker.cs — base.Rating() აღარ არსებობს
public override int Rating()
{
    return Shot + Stamina / 5;
}
```

```csharp Club.cs · ცვლილებები
public Coach Coach { get; private set; }

public Club(string name, int budget, Coach coach)
{
    Name = name;
    if (budget < 0) budget = 0;
    Budget = budget;
    Coach = coach;
}

public int Strength()
{
    int total = Coach.Bonus();
    for (int i = 0; i < Count; i++)
    {
        total += squad[i].Rating();
    }
    return total;
}

public bool PaySalaries()
{
    IPayable[] payroll = new IPayable[Count + 1];
    for (int i = 0; i < Count; i++)
    {
        payroll[i] = squad[i];
    }
    payroll[Count] = Coach;

    int total = 0;
    foreach (IPayable p in payroll)
    {
        total += p.Salary();
    }

    if (total > Budget)
    {
        Console.WriteLine($"💸 {Name}: ხელფასისთვის {total} ₾ არ ჰყოფნის — კრიზისი!");
        return false;
    }

    Budget -= total;
    Console.WriteLine($"💰 {Name}: ხელფასები {total} ₾ · დარჩა {Budget} ₾");
    return true;
}
```

```note
`Player` — `abstract`: „უბრალოდ მოთამაშე“ არ არსებობს, ყოველთვის რომელიმე პოზიციაა. მწვრთნელი მოთამაშე **არ არის** — `Coach : Player` არასწორი იქნებოდა. მაგრამ ხელფასი ორივეს აქვს, ამიტომ საერთოს ინტერფეისი ქმნის: `IPayable`. `payroll[i] = squad[i];` — მოთამაშე `IPayable[]`-ში ეტევა, რადგან `Player` მას ახორციელებს.
```

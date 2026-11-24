# ⚽ ფეხბურთის კლუბი · ნაწილი 4 — პირველი მატჩი

ყოველი პოზიცია თავისებურად ფასდება და ვარჯიშობს — კლუბს კი არ აინტერესებს, ვინ ვინ არის

## მოთხოვნები

- `Player`-ში `virtual int Rating()` (`Stamina / 5`) — ყოველი პოზიცია `override`-ით: უნარი + `base.Rating()`
- `Player`-ში `virtual void Train()` (`Tire(20)`) — მეკარე ავარჯიშებს `Reflex`-ს, მცველი `Defense`-ს, თავდამსხმელი `Shot`-ს (+3, მაქს. 100) და მერე `base.Train()`
- `override ToString()` — `Player`: „ნიკა ⭐ 96 ⚡ 100“; პოზიციები წინ ამატებენ 🧤 / 🛡️ / ⚽ + `base.ToString()`
- `Club`-ში: `int Strength()` — ყველა `Rating()`-ის ჯამი; `void TrainAll()` — ვარჯიშობს, ვისაც `Stamina` 20+ აქვს; `PrintSquad` — `Console.WriteLine(squad[i])`
- Program-ში `static void PlayMatch(Club home, Club away)` — გოლები: `Random.Shared.Next(0, club.Strength() / 100 + 1)`. Main-ში ორი კლუბი: მატჩი → ერთი კლუბი ვარჯიშობს → განმეორებითი მატჩი

## ✓ მზადაა, როცა

`Club`-ში არცერთი `if` პოზიციაზე არ არის; `TrainAll`-ის შემდეგ კლუბის `Strength()` გაიზარდა; ახალი პოზიცია (მაგ. `Winger`) მხოლოდ ახალ კლასს მოითხოვს

## ⭐ ბონუსი

- შინ მოთამაშე გუნდს +50 ძალა; `Winger`-ს `override Rating()` — `Shot`-ის ნაცვლად ჩაწოდება ითვლება

## ამოხსნა

```csharp Program.cs · Main !
Club dinamo = new Club("დინამო", 120000);
dinamo.Buy(new Goalkeeper("საბა", 75));
dinamo.Buy(new Defender("ლუკა", 70));
dinamo.Buy(new Defender("დათო", 60));
dinamo.Buy(new Striker("ნიკა", 80));
dinamo.Buy(new Striker("გიო", 55));

Club torpedo = new Club("ტორპედო", 120000);
torpedo.Buy(new Goalkeeper("ზურა", 65));
torpedo.Buy(new Defender("ოთო", 75));
torpedo.Buy(new Defender("ბექა", 65));
torpedo.Buy(new Striker("ლევანი", 70));
torpedo.Buy(new Striker("ტოკო", 70));

dinamo.PrintSquad();
torpedo.PrintSquad();
PlayMatch(dinamo, torpedo);

dinamo.TrainAll();
dinamo.PrintSquad();
PlayMatch(torpedo, dinamo);
```

```csharp Program.cs · დამხმარე მეთოდები
static void PlayMatch(Club home, Club away)
{
    int homeGoals = Random.Shared.Next(0, home.Strength() / 100 + 1);
    int awayGoals = Random.Shared.Next(0, away.Strength() / 100 + 1);
    Console.WriteLine($"🏟️ {home.Name} {homeGoals} : {awayGoals} {away.Name}");
}
```

```csharp Player.cs · ახალი ნაწილი
public virtual int Rating()
{
    return Stamina / 5;
}

public virtual void Train()
{
    Tire(20);
}

public override string ToString()
{
    return $"{Name} ⭐ {Rating()} ⚡ {Stamina}";
}
```

```csharp Striker.cs · ახალი ნაწილი
public override int Rating()
{
    return Shot + base.Rating();
}

public override void Train()
{
    Shot += 3;
    if (Shot > 100) Shot = 100;
    base.Train();
}

public override string ToString()
{
    return "⚽ " + base.ToString();
}
```

```csharp Club.cs · ახალი ნაწილი
public int Strength()
{
    int total = 0;
    for (int i = 0; i < Count; i++)
    {
        total += squad[i].Rating();
    }
    return total;
}

public void TrainAll()
{
    for (int i = 0; i < Count; i++)
    {
        if (squad[i].Stamina >= 20) squad[i].Train();
    }
}

public void PrintSquad()
{
    Console.WriteLine($"🏟️ {Name} · 💪 {Strength()} · {Budget} ₾");
    for (int i = 0; i < Count; i++)
    {
        Console.WriteLine($"   {squad[i]}");
    }
}
```

```note
`Goalkeeper` და `Defender` — ზუსტად `Striker`-ის სქემით (`Reflex`, `Defense`, 🧤, 🛡️). `squad[i].Rating()` ყოველთვის სწორ ფორმულას იძახებს, თუმცა `Club`-მა არ იცის, რომელი პოზიციაა — ეს პოლიმორფიზმია. წინა ნაწილში `PrintSquad` უნარებს ვერ ბეჭდავდა — ახლა `ToString()`-ის `override` ამას თავისით აკეთებს.
```

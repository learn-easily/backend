# ⚽ ფეხბურთის კლუბი · ფინალი — სეზონი + მზადება ტესტისთვის

4 კლუბი, ყველა ყველას ეთამაშება, მოგება ფულს მოაქვს, ხელფასები კი ყოველ მატჩზე — ვინ გახდება ჩემპიონი?

## მოთხოვნები

- `Club`-ში: `Points`, `GoalsFor`, `GoalsAgainst` — `{ get; private set; }` და `void AddResult(int scored, int conceded)`: მოგება 3 ქულა და +15 000 ₾, ფრე 1 ქულა და +5 000 ₾, წაგება 0
- `PlayMatch` ორივე კლუბს შედეგს უწერს `AddResult`-ით; მატჩის შემდეგ ორივე კლუბი იხდის ხელფასს
- Program-ში `static Club MakeClub(string name, int coachLevel)` — 150 000 ₾-იანი კლუბი, რომელიც თავად ყიდულობს 1 მეკარეს, 2 მცველს და 2 თავდამსხმელს შემთხვევითი უნარით (50–90)
- Main-ში: `Club[] league` — 4 კლუბი; ორი ჩადგმული `for` — ყველა წყვილი ერთხელ; ბოლოს ცხრილი (ქულები, გოლები, ბიუჯეტი) და ჩემპიონი
- ტესტისთვის: გადახედეთ ყოველი ლექციის „შევამოწმოთ“-ის კითხვებს და იპოვეთ პროექტში ოთხივე პრინციპი

## ✓ მზადაა, როცა

6 მატჩი თამაშდება და არცერთი კლუბი თავის თავს არ ეთამაშება; ქულები და ბიუჯეტი მხოლოდ `Club`-ის მეთოდებით იცვლება; ოთხივე პრინციპზე შეგიძლიათ თითით აჩვენოთ: „აი, აქ“

## ⭐ ბონუსი

- ორწრიანი სეზონი (შინ და გასვლაზე); ცხრილი ქულებით დალაგებული (bubble sort); ფრე ქულებში → გოლების სხვაობა წყვეტს

## ამოხსნა

```csharp Program.cs · Main !
Club[] league =
{
    MakeClub("დინამო", 4),
    MakeClub("ტორპედო", 3),
    MakeClub("საბურთალო", 5),
    MakeClub("დილა", 2)
};

for (int i = 0; i < league.Length; i++)
{
    for (int j = i + 1; j < league.Length; j++)
    {
        PlayMatch(league[i], league[j]);
    }
}

Console.WriteLine("\n📊 ცხრილი");
Club champion = league[0];
foreach (Club c in league)
{
    Console.WriteLine($"{c.Name} · {c.Points} ქ. · {c.GoalsFor}:{c.GoalsAgainst} · {c.Budget} ₾");
    if (c.Points > champion.Points) champion = c;
}
Console.WriteLine($"🏆 ჩემპიონი: {champion.Name}!");
```

```csharp Program.cs · დამხმარე მეთოდები
static Club MakeClub(string name, int coachLevel)
{
    Club club = new Club(name, 150000, new Coach($"{name}-ის მწვრთნელი", coachLevel));

    club.Buy(new Goalkeeper($"{name} · მეკარე", Random.Shared.Next(50, 91)));
    for (int i = 1; i <= 2; i++)
    {
        club.Buy(new Defender($"{name} · მცველი {i}", Random.Shared.Next(50, 91)));
        club.Buy(new Striker($"{name} · თავდამსხმელი {i}", Random.Shared.Next(50, 91)));
    }
    return club;
}

static void PlayMatch(Club home, Club away)
{
    int homeGoals = Random.Shared.Next(0, home.Strength() / 100 + 1);
    int awayGoals = Random.Shared.Next(0, away.Strength() / 100 + 1);
    Console.WriteLine($"🏟️ {home.Name} {homeGoals} : {awayGoals} {away.Name}");

    home.AddResult(homeGoals, awayGoals);
    away.AddResult(awayGoals, homeGoals);

    home.PaySalaries();
    away.PaySalaries();
}
```

```csharp Club.cs · ახალი ნაწილი
public int Points { get; private set; }
public int GoalsFor { get; private set; }
public int GoalsAgainst { get; private set; }

public void AddResult(int scored, int conceded)
{
    GoalsFor += scored;
    GoalsAgainst += conceded;

    if (scored > conceded)
    {
        Points += 3;
        Budget += 15000;
    }
    else if (scored == conceded)
    {
        Points += 1;
        Budget += 5000;
    }
}
```

```note
`j = i + 1` — ყოველი წყვილი ერთხელ და კლუბი თავის თავს არ ხვდება: 4 კლუბი → 6 მატჩი. ოთხივე პრინციპი: **ინკაფსულაცია** — `Budget`, `Points`, `squad` მხოლოდ `Club`-ის მეთოდებით იცვლება · **მემკვიდრეობა** — პოზიციები `Player`-ის შვილებია · **პოლიმორფიზმი** — `Strength()`-ში `Rating()` ყოველ პოზიციაზე თავისებურად მუშაობს · **აბსტრაქცია** — `abstract Player` და `IPayable`, რომელიც მოთამაშესა და მწვრთნელს აერთიანებს.
```

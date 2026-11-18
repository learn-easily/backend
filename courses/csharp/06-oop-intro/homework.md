# გუნდი vs დრაკონი

სამი გმირი ერთ დრაკონს ებრძვის

## მოთხოვნები

- `Hero[] team` — 3 გმირი (ზუსტად როგორც `Student[]`); დრაკონი — 200 სიცოცხლით
- რაუნდი: **ყოველი ცოცხალი** გმირი უტევს დრაკონს → დრაკონი (თუ ცოცხალია) **პირველ ცოცხალ** გმირს ურტყამს: `dragon.Attack() + 10`
- ბრძოლა გრძელდება, სანამ დრაკონი ცოცხალია **და** გუნდში ერთი ცოცხალი მაინც არის; ბოლოს — გამარჯვებული
- Program-ში ორი `static` მეთოდი: `bool AnyAlive(Hero[] team)` და `Hero FirstAlive(Hero[] team)`

## ✓ მზადაა, როცა

მკვდარი გმირი აღარ უტევს და დრაკონი მას აღარ ურტყამს; ბრძოლა სწორად მთავრდება ორივე შემთხვევაში

## ⭐ ბონუსი

- დრაკონმა **შემთხვევით** ცოცხალ გმირს დაარტყას: `team[Random.Shared.Next(team.Length)]` — სანამ მკვდარი ამოდის, თავიდან აირჩიე

## ამოხსნა

```csharp Program.cs · Main !
Hero[] team =
{
    new Hero("რაინდი", 100),
    new Hero("მშვილდოსანი", 80),
    new Hero("ჯადოქარი", 70)
};
Hero dragon = new Hero("დრაკონი", 200);
while (dragon.IsAlive() && AnyAlive(team))
{
    foreach (Hero h in team)
    {
        if (h.IsAlive()) dragon.TakeDamage(h.Attack());
    }
    if (dragon.IsAlive())
    {
        Hero target = FirstAlive(team);
        target.TakeDamage(dragon.Attack() + 10);
    }
}
Console.WriteLine(dragon.IsAlive() ? "💀 დრაკონმა გაიმარჯვა" : "🏆 გუნდმა გაიმარჯვა!");
```

```csharp Program.cs · დამხმარე მეთოდები
static bool AnyAlive(Hero[] team)
{
    foreach (Hero h in team)
    {
        if (h.IsAlive()) return true;
    }
    return false;
}

static Hero FirstAlive(Hero[] team)
{
    foreach (Hero h in team)
    {
        if (h.IsAlive()) return h;
    }
    return team[0];
}
```

```note
`AnyAlive` და `FirstAlive` გუნდის **მასივს** იღებს — ერთი მეთოდი ნებისმიერი ზომის გუნდისთვის მუშაობს. `FirstAlive`-ის ბოლო `return team[0]` მხოლოდ იმიტომ გვჭირდება, რომ მეთოდმა ყოველთვის რამე დააბრუნოს — ციკლი მას მხოლოდ მაშინ იძახებს, როცა ცოცხალი ნამდვილად არის.
```

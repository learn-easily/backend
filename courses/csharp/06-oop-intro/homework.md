# რაინდი და ჯადოქარი vs დრაკონი

ორი გმირი ერთ დრაკონს ებრძვის

## მოთხოვნები

- ორი გმირი: `knight` (100) და `mage` (70); დრაკონი — 200 სიცოცხლით
- რაუნდი: **ყოველი ცოცხალი** გმირი უტევს დრაკონს → დრაკონი (თუ ცოცხალია) **პირველ ცოცხალ** გმირს ურტყამს (ჯერ რაინდს, ის თუ მოკვდა — ჯადოქარს): `dragon.Attack() + 10`
- ბრძოლა გრძელდება, სანამ დრაკონი ცოცხალია **და** ერთი გმირი მაინც ცოცხალია; ბოლოს — გამარჯვებული
- Program-ში ორი `static` მეთოდი: `bool AnyAlive(Hero a, Hero b)` და `Hero FirstAlive(Hero a, Hero b)`

## ✓ მზადაა, როცა

მკვდარი გმირი აღარ უტევს და დრაკონი მას აღარ ურტყამს; ბრძოლა სწორად მთავრდება ორივე შემთხვევაში

## ⭐ ბონუსი

- დრაკონმა **შემთხვევით** ცოცხალ გმირს დაარტყას: თუ ორივე ცოცხალია, `Random.Shared.Next(2)` აირჩევს, ვის; თუ ერთია — მას

## ამოხსნა

```csharp Program.cs · Main !
Hero knight = new Hero("რაინდი", 100);
Hero mage = new Hero("ჯადოქარი", 70);
Hero dragon = new Hero("დრაკონი", 200);

while (dragon.IsAlive() && AnyAlive(knight, mage))
{
    if (knight.IsAlive()) dragon.TakeDamage(knight.Attack());
    if (mage.IsAlive()) dragon.TakeDamage(mage.Attack());

    if (dragon.IsAlive())
    {
        Hero target = FirstAlive(knight, mage);
        target.TakeDamage(dragon.Attack() + 10);
    }
}
Console.WriteLine(dragon.IsAlive() ? "💀 დრაკონმა გაიმარჯვა" : "🏆 გმირებმა გაიმარჯვეს!");
```

```csharp Program.cs · დამხმარე მეთოდები
static bool AnyAlive(Hero a, Hero b)
{
    return a.IsAlive() || b.IsAlive();
}

static Hero FirstAlive(Hero a, Hero b)
{
    if (a.IsAlive()) return a;
    return b;
}
```

```note
`FirstAlive` გმირის **მისამართს** აბრუნებს — ამიტომ `target.TakeDamage(...)` ნამდვილ რაინდს ან ჯადოქარს აზიანებს და არა ასლს. ციკლი `FirstAlive`-ს მხოლოდ მაშინ იძახებს, როცა ცოცხალი გმირი ნამდვილად არის.
```

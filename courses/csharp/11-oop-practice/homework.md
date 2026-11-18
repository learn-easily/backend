# ზოოპარკის დასრულება + მზადება ტესტისთვის

რაც კლასში ვერ მოასწარით — და ერთი ახალი ცხოველი

## მოთხოვნები

- კლასში დაწყებული ზოოპარკი **ბოლომდე** — ⭐⭐⭐ დონის ჩათვლით
- ახალი ცხოველი თქვენი არჩევით (მაგ. პინგვინი 🐧 — ცურავს, მაგრამ ვერ დაფრინავს) — **ერთი ახალი კლასი**, Main-ის ციკლები არ იცვლება
- Main-ის ბოლოს: ყველა ცხოველი `Console.WriteLine(a)`-ით — `ToString()`
- ტესტისთვის: გადახედეთ ყოველი ლექციის „შევამოწმოთ“-ის კითხვებს და სცადეთ არენა ნულიდან დაწეროთ

## ✓ მზადაა, როცა

ახალი ცხოველი მხოლოდ ახალ კლასს მოითხოვდა; ოთხივე პრინციპზე შეგიძლიათ თითით აჩვენოთ: „აი, აქ“

## ⭐ ბონუსი

- 🏆 მომვლელი: `static void FeedAll(Animal[] animals, int food)` — ყველას აჭმევს და ყველაზე დაღლილს ბეჭდავს

## ამოხსნა

```csharp Program.cs · Main !
Lion leo = new Lion("ლეო");
Parrot kiki = new Parrot("კიკი");
Duck doni = new Duck("დონი");
Fish nemo = new Fish("ნემო");

Animal[] zoo = { leo, kiki, doni, nemo };
foreach (Animal a in zoo)
{
    Console.WriteLine($"{a.Name}: {a.MakeSound()}");
    a.Move();
}

IFlyer[] flyers = { kiki, doni };
foreach (IFlyer f in flyers) f.Fly();

ISwimmer[] swimmers = { doni, nemo };
foreach (ISwimmer s in swimmers) s.Swim();
```

```csharp Animal.cs · IFlyer.cs · ISwimmer.cs
internal abstract class Animal
{
    private string name = "";

    public string Name
    {
        get { return name; }
        set
        {
            if (value == "") name = "უსახელო";
            else name = value;
        }
    }

    public int Energy { get; private set; } = 50;

    public Animal(string name)
    {
        Name = name;
    }

    public void Eat(int food)
    {
        if (food < 0) return;
        Energy += food;
        if (Energy > 100) Energy = 100;
    }

    protected void Spend(int amount)
    {
        Energy -= amount;
        if (Energy < 0) Energy = 0;
    }

    public abstract string MakeSound();

    public virtual void Move()
    {
        Spend(10);
        Console.WriteLine($"{Name} დადის");
    }

    public override string ToString()
    {
        return $"{Name} ⚡ {Energy}";
    }
}

internal interface IFlyer
{
    void Fly();
}

internal interface ISwimmer
{
    void Swim();
}
```

```csharp Lion.cs · Parrot.cs · Duck.cs · Fish.cs
internal class Lion : Animal
{
    public Lion(string name) : base(name) { }

    public override string MakeSound()
    {
        return "ღრრრ! 🦁";
    }
}

internal class Parrot : Animal, IFlyer
{
    public Parrot(string name) : base(name) { }

    public override string MakeSound()
    {
        return "გამარჯობა! 🦜";
    }

    public void Fly()
    {
        Spend(20);
        Console.WriteLine($"{Name} დაფრინავს");
    }
}

internal class Duck : Animal, IFlyer, ISwimmer
{
    public Duck(string name) : base(name) { }

    public override string MakeSound()
    {
        return "კვაჰ! 🦆";
    }

    public void Fly()
    {
        Spend(15);
        Console.WriteLine($"{Name} დაფრინავს");
    }

    public void Swim()
    {
        Spend(5);
        Console.WriteLine($"{Name} ცურავს");
    }
}

internal class Fish : Animal, ISwimmer
{
    public Fish(string name) : base(name) { }

    public override string MakeSound()
    {
        return "... 🐟";
    }

    public override void Move()
    {
        Swim();
    }

    public void Swim()
    {
        Spend(5);
        Console.WriteLine($"{Name} ცურავს");
    }
}
```

```note
`Spend` — `protected`: შვილები იყენებენ, გარედან ენერგიის დაკლება შეუძლებელია. თევზი `Move()`-ს `override`-ით ცვლის — ის არ „დადის“, ცურავს. იხვი ორივე ინტერფეისს ახორციელებს და ორივე მასივში ეტევა.
```

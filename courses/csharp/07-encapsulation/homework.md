# ტამაგოჩი 🐱

შინაური ცხოველი, რომელსაც ვერავინ „გატეხავს“

## მოთხოვნები

- ახალი Console App: **Tamagotchi**, კლასი `Pet` — **Pet.cs**-ში
- `Name` — property წესით: ცარიელი სახელი → „უსახელო“
- `Hunger` და `Happiness` — 0-დან 10-მდე, `{ get; private set; }`, ორივე თავიდან 5
- `Feed()` — შიმშილი −3 · `Play()` — ბედნიერება +2, შიმშილი +2; თუ შიმშილი 8+ — თამაშზე უარს ამბობს
- არცერთი მნიშვნელობა 0-ზე ქვემოთ ან 10-ზე ზემოთ **არასდროს** ადის
- Main-ში `do-while` მენიუ: 1 — აჭამე, 2 — ეთამაშე, 0 — გასვლა; ყოველ ჯერზე `PrintStatus()`

## ✓ მზადაა, როცა

`pet.Hunger = 0` Main-ში წითელ ხაზს აჩენს; რამდენჯერაც არ უნდა აჭამო ან ეთამაშო, მნიშვნელობები 0–10-ში რჩება

## ⭐ ბონუსი

- `Sleep()` — ბედნიერება +1, შიმშილი +1; და `bool IsHappy()` — ბედნიერება 7+ და შიმშილი 3-ზე ნაკლები

## ამოხსნა

```csharp Program.cs · Main !
Pet pet = new Pet("მურკა");
int choice;

do
{
    pet.PrintStatus();
    Console.Write("1 — აჭამე · 2 — ეთამაშე · 0 — გასვლა: ");
    choice = int.Parse(Console.ReadLine());

    if (choice == 1) pet.Feed();
    else if (choice == 2) pet.Play();
}
while (choice != 0);
```

```csharp Pet.cs · namespace-ის შიგნით
internal class Pet
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

    public int Hunger { get; private set; } = 5;
    public int Happiness { get; private set; } = 5;

    public Pet(string name)
    {
        Name = name;
    }

    public void Feed()
    {
        Hunger -= 3;
        if (Hunger < 0) Hunger = 0;
    }

    public void Play()
    {
        if (Hunger >= 8)
        {
            Console.WriteLine($"{Name} ძალიან მშიერია — თამაში არ უნდა 😿");
            return;
        }

        Happiness += 2;
        if (Happiness > 10) Happiness = 10;
        Hunger += 2;
        if (Hunger > 10) Hunger = 10;
    }

    public void PrintStatus()
    {
        Console.WriteLine($"🐱 {Name} · შიმშილი {Hunger}/10 · ბედნიერება {Happiness}/10");
    }
}
```

```note
ყველა წესი `Pet`-შია: Main-ს მხოლოდ მეთოდების გამოძახება შეუძლია. `Play`-ში ადრეული `return` თამაშს წყვეტს, თუ ცხოველი მშიერია — დანარჩენი კოდი აღარ სრულდება.
```

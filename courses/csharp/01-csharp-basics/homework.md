# საკუთარი „გამოიცანი რიცხვი“

ინსტალაცია + თამაში + ბიპ-ბუპ

## მოთხოვნები

- **Visual Studio 2026** Community დააინსტალირე: ☑ .NET desktop development, ☑ ASP.NET and web development
- „გამოიცანი რიცხვი“ **შენ თვითონ** დაწერე — სლაიდში ჩაუხედავად
- თამაშს დაამატე: მაქსიმუმ **7 ცდა**, მერე „Game Over“ და სწორი პასუხი
- კლასის დავალებები, რაც ვერ მოასწარი — ⭐ → ⭐⭐⭐ (ბიპ-ბუპის ჩათვლით)

## ✓ მზადაა, როცა

თამაში სწორ რიცხვზე „🎉 გამოიცანი“-ს წერს, 7 არასწორ ცდაზე კი — „Game Over“-ს და ჩაფიქრებულ რიცხვს

## ⭐ ბონუსი

- თამაშის ბოლოს: „კიდევ ითამაშებ? (კი/არა)“ — და „კი“-ზე თავიდან დაიწყოს

## ამოხსნა

```csharp Program.cs · 7 ცდა !
int secret = Random.Shared.Next(1, 101);
int guess = 0;
int tries = 0;

while (guess != secret && tries < 7)
{
    Console.Write($"ცდა {tries + 1}/7: ");
    guess = int.Parse(Console.ReadLine());
    tries++;

    if (guess < secret) Console.WriteLine("მეტია ⬆");
    else if (guess > secret) Console.WriteLine("ნაკლებია ⬇");
}

if (guess == secret)
    Console.WriteLine($"🎉 გამოიცანი {tries} ცდაში!");
else
    Console.WriteLine($"Game Over! ჩაფიქრებული იყო {secret}");
```

```csharp ბიპ-ბუპ
for (int i = 1; i <= 50; i++)
{
    if (i % 3 == 0 && i % 5 == 0) Console.WriteLine("ბიპბუპ");
    else if (i % 3 == 0) Console.WriteLine("ბიპ");
    else if (i % 5 == 0) Console.WriteLine("ბუპ");
    else Console.WriteLine(i);
}
```

```note
ბიპ-ბუპში რიგს აქვს მნიშვნელობა: „ორივეზე იყოფა“ **პირველი** უნდა შემოწმდეს. თუ ჯერ `i % 3 == 0`-ს შეამოწმებ, 15-ზე „ბიპ“ დაიბეჭდება და `else if`-ები აღარ შემოწმდება — გახსოვს, `if` პირველ სწორ პირობაზე ჩერდება.
```

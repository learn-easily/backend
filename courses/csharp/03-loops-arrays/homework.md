# „გამოიცანი რიცხვი“ 2.0

ლიმიტი, ისტორია და თავიდან თამაში

## მოთხოვნები

- „გამოიცანი რიცხვი“ **შენ თვითონ** დაწერე — სლაიდში ჩაუხედავად
- მაქსიმუმ **7 ცდა**, მერე „Game Over“ და ჩაფიქრებული რიცხვი
- ყოველი ვარაუდი ჩაწერე მასივში `int[] history = new int[7];` და თამაშის ბოლოს დაბეჭდე: `შენი ცდები: 50 75 63`
- თამაშის ბოლოს: „კიდევ ითამაშებ? (კი/არა)“ — `do-while`-ით, „კი“-ზე თავიდან იწყება

## ✓ მზადაა, როცა

სწორ რიცხვზე „🎉 გამოიცანი“ და ცდების ისტორია იბეჭდება; 7 არასწორ ცდაზე — „Game Over“, ჩაფიქრებული რიცხვი და ისტორია; „კი“-ზე ახალი თამაში იწყება

## ⭐ ბონუსი

- ჩაინიშნე **საუკეთესო შედეგი** (ყველაზე ცოტა ცდა) ყველა თამაშიდან და ყოველი თამაშის ბოლოს დაბეჭდე

## ამოხსნა

```csharp Program.cs !
string again;
do
{
    int secret = Random.Shared.Next(1, 101);
    int[] history = new int[7];
    int guess = 0;
    int tries = 0;
    while (guess != secret && tries < 7)
    {
        Console.Write($"ცდა {tries + 1}/7: ");
        guess = int.Parse(Console.ReadLine());
        history[tries] = guess;
        tries++;
        if (guess < secret) Console.WriteLine("მეტია ⬆");
        else if (guess > secret) Console.WriteLine("ნაკლებია ⬇");
    }
    Console.WriteLine(guess == secret ? $"🎉 გამოიცანი {tries} ცდაში!" : $"Game Over! ჩაფიქრებული იყო {secret}");
    Console.Write("შენი ცდები: ");
    for (int i = 0; i < tries; i++)
    {
        Console.Write(history[i] + " ");
    }
    Console.WriteLine();
    Console.Write("კიდევ ითამაშებ? (კი/არა) ");
    again = Console.ReadLine();
} while (again == "კი");
```

```note
ისტორიას `foreach`-ით არ ვბეჭდავთ: 3 ცდაში თუ გამოიცანი, მასივის დანარჩენი 4 ადგილი ნულებია. ამიტომ `for` მხოლოდ `tries`-მდე მიდის. `history[tries] = guess;` — `tries++`-მდე, რომ პირველი ვარაუდი ინდექს 0-ზე ჩაიწეროს.
```

# დავალებები — აირჩიე დონე

ჯერ Program.cs-ში, მერე — ცალკე ფაილში

## ნაბიჯები

- ⭐ **წიგნი** — `Book` კლასი: `Title`, `Author`, `Pages`, კონსტრუქტორი და `void PrintInfo()`. შექმენი 3 წიგნი და დაბეჭდე
- ⭐⭐ **სამი კონსტრუქტორი** — `Book`-ს დაუმატე: `Book()` → სათაური „უსათაურო“, `Book(string title)` და `Book(string title, string author, int pages)`. სამივე გზით შექმენი წიგნი
- ⭐⭐ **ბიბლიოთეკა** — `Book`-ი ცალკე ფაილში (**Book.cs**). `Book[]` 4 წიგნით → იპოვე და დაბეჭდე ყველაზე გრძელი წიგნი და ჯამური გვერდები

## ✓ მზადაა, როცა

სამივე კონსტრუქტორი მუშაობს; `new Book(300)` წითელ ხაზს აჩენს; Book.cs ცალკე ფაილშია და Main-ში უცვლელად მუშაობს

## ⭐ ბონუსი

- ⭐⭐⭐ **საბანკო ანგარიში** — `BankAccount`: `Owner`, `Balance`, ორი კონსტრუქტორი (`BankAccount(string owner)` → ბალანსი 0, და `BankAccount(string owner, decimal balance)`), `void Deposit(decimal amount)`, `bool Withdraw(decimal amount)` — თანხა არ ჰყოფნის → `false`, ბალანსი არ იცვლება
- 🏆 **ტამაგოჩი** — `Pet`: `Name`, `Hunger`, `Happiness` (0–10), `Feed()`, `Play()`, `PrintStatus()` და `do-while` მენიუ

## 💡 მინიშნება

ყველაზე გრძელი წიგნი — ზუსტად როგორც `best` მოსწავლე სლაიდზე: `Book longest = books[0];` და `foreach`. `Withdraw`-ში ჯერ შეამოწმე, მერე შეცვალე: `if (amount > Balance) return false;`. ცარიელ კონსტრუქტორში `Title = "უსათაურო";`.

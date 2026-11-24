# ზოოპარკი 🦁

ყოველი დონე — ერთი პრინციპი

## ნაბიჯები

- ⭐ **🛡️** `Animal`: `Name` წესით, `Energy { get; private set; }` (0–100), `Eat(int food)`, `protected Spend(int amount)`
- ⭐ **🧬** `Lion`, `Parrot`, `Duck`, `Fish` — `Animal`-ის შვილები, `: base(name)`-ით
- ⭐⭐ **🎭** `virtual void Move()` (−10, „დადის“) — თევზი `override`-ით ცურავს; `override ToString()` → „ლეო ⚡ 70“
- ⭐⭐ **🎨** `Animal` → `abstract`; `abstract string MakeSound()` — ყველას თავისი ხმა
- ⭐⭐⭐ **🎨** `IFlyer` (`Fly()`, −20) და `ISwimmer` (`Swim()`, −5): თუთიყუში დაფრინავს, თევზი ცურავს, იხვი — ორივეს

## ✓ მზადაა, როცა

`Animal[]` — ერთი ციკლი

## ⭐ ბონუსი

- 🏆 **მომვლელი** — `static void FeedAll(Animal[] animals, int food)` Program-ში: ყველას აჭმევს და ბოლოს ყველაზე დაღლილს ბეჭდავს

## 💡 მინიშნება

ცარიელი სახელი → „უსახელო“, ენერგია თავიდან 50. ზუსტად სალაროსავით: `Animal` ↔ `Payment`, `MakeSound()` ↔ `Pay()`, `IFlyer` ↔ `IRefundable`. იხვი: `class Duck : Animal, IFlyer, ISwimmer`. `Spend` — `protected`: შვილებმა უნდა გამოიძახონ, გარედან კი — არავინ.

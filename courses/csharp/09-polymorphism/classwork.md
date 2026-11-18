# დავალებები — აირჩიე დონე

ახალი გმირები გუნდში — ბრძოლის კოდი არ იცვლება

## ნაბიჯები

- ⭐ **ქურდი** — `Rogue : Character` (85 სიცოცხლე): `override Attack()` — `RollDamage(6, 12)`, და 50%-ით მეორე დარტყმაც ემატება
- ⭐⭐ **ორკი** — `Orc : Character` (80, პარამეტრების გარეშე): `override Attack()` 8–15 და `override ToString()` — წინ 👹 + `base.ToString()`
- ⭐⭐ **გუნდში** — `Rogue` დაამატე `party` მასივში და გაუშვი ბრძოლა. ბრძოლის ციკლი **არ შეცვალო**

## ✓ მზადაა, როცა

ქურდი ზოგჯერ ორმაგად ურტყამს; `Console.WriteLine(orc)` → „👹 ორკი ❤️ 80/80“; ბრძოლის კოდში არაფერი შეცვლილა

## ⭐ ბონუსი

- ⭐⭐⭐ **ცეცხლგამძლე დრაკონი** — `Dragon`-ში `override TakeDamage`: 30-ზე მეტი დაზიანება 30-მდე მცირდება, მერე — `base.TakeDamage`

## 💡 მინიშნება

50% — `Random.Shared.Next(2) == 0`. ToString-ში: `return "👹 " + base.ToString();`. დრაკონი: `if (damage > 30) damage = 30;` და მერე `base.TakeDamage(damage);`.

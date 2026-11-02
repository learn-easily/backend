# ლექციები

ყველა ლექციის პრეზენტაცია ერთ ადგილას, ერთ ძრავზე.

**საიტი:** https://learn-easily.github.io/lectures/

## სტრუქტურა

```
engine/                      ერთი ძრავი ყველა ლექციისთვის
  engine.js · engine.css · theme-light.css
  index.html                 მთავარი გვერდის შაბლონი (კურსები, ძებნა)
courses/
  <კურსი>/course.json        {"title", "audience", "order"}
  <კურსი>/<NN-slug>/
    deck.html                სლაიდები + სცენარი (<aside class="notes">)
    lecture.json             {"title"}
    materials/               არასავალდებულო — ფაილები ჩამოსატვირთად (მაგ. SQL)
build.py                     აწყობს ყველაფერს → site/
```

| კურსი | საქაღალდე |
|---|---|
| ASP.NET Core Web API | `courses/aspnet-api/` |
| Entity Framework Core | `courses/efcore/` |
| Backend — სკოლის ჯგუფი | `courses/school-backend/` |

## ლექციაზე

1. გახსენი საიტი, აირჩიე ლექცია → **▶ პრეზენტაცია**. Chrome ან Edge.
2. გადაიტანე პროექტორზე, დააჭირე `F`.
3. `Ctrl+Shift+P` — **ლექტორის ფანჯარა** სცენარით. დატოვე ლეპტოპის ეკრანზე.
4. ნავიგაცია მხოლოდ ისრებით: `→` შემდეგი, `←` წინა.

სხვა კლავიშები: `N` შენიშვნები · `O` ყველა სლაიდი · `A` სლაიდის ყველა ნაბიჯი · `Shift+→` შემდეგი სლაიდი.
ზედა მარცხენა კუთხეში (მაუსის მიტანისას) — `← ლექციები`.

## ახალი ლექცია

1. `courses/<კურსი>/<NN-slug>/` — `deck.html` და `lecture.json`.
2. ახალი კურსისთვის — `courses/<კურსი>/course.json`.
3. push `main`-ზე → GitHub Action ააწყობს და გამოაქვეყნებს. მთავარ გვერდზე ავტომატურად გამოჩნდება.

## სცენარის ფორმატი

`<aside class="notes">`-ში, თითო სტრიქონი:

| პრეფიქსი | მნიშვნელობა |
|---|---|
| `→ ` | ნაბიჯი (ერთი დაჭერა) — რაოდენობა უნდა ემთხვეოდეს სლაიდის `step`/`codestep`/`trigger`-ებს |
| `? ` | კითხვა აუდიტორიას |
| `⏱ ` | დრო |
| `! ` | ხაზგასასმელი |
| `~ ` | მხოლოდ ლექტორისთვის |
| (არაფერი) | სათქმელი |

ბილდი შეჩერდება, თუ რომელიმე სლაიდზე ნაბიჯები და `→` არ ემთხვევა.

## ლოკალურად

```bash
python3 -m venv .venv && .venv/bin/pip install pygments   # ერთხელ
.venv/bin/python build.py                                  # ყველაფერი → site/
.venv/bin/python build.py efcore/03                        # მხოლოდ ერთი ლექცია
python3 -m http.server -d site 8000                        # http://localhost:8000
```

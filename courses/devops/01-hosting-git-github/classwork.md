# პირველი რეპოზიტორია — my-portfolio

დავალება · თქვენი პორტფოლიო Git-ში

## ნაბიჯები

- `git config --global user.name` და `user.email` — თქვენი სახელით
- საქაღალდე `my-portfolio`: `index.html` (სახელი + 2-3 წინადადება თქვენზე) და `style.css`
- `git init` და პირველი commit: `"Add home page"`
- `index.html`-ში ახალი წინადადება → `git status` (`modified`) → commit `"Update about text"`
- `style.css`-ში ფერი შეცვალეთ → კიდევ ერთი commit გასაგები მესიჯით

## ✓ მზადაა, როცა

`git log --oneline` აჩვენებს მინიმუმ 3 commit-ს, თქვენი მესიჯებით

## ⭐ ბონუსი

- იგივე ციკლი VS Code-ის **Source Control** პანელით (Ctrl+Shift+G): `+` = add, ✓ = commit
- `git log` (`--oneline`-ის გარეშე) — იპოვეთ ავტორი და თარიღი. გამოსვლა — **q**

## 💡 მინიშნება

```bash
git status            # რა მდგომარეობაა?
git add .             # ყველა ცვლილება staging-ში
git commit -m "..."   # შენახვა ისტორიაში
git log --oneline     # ისტორია მოკლედ
```

`git status` — ყველაზე ხშირი ბრძანება. როცა არ იცით, რა ხდება — ჯერ ის გაუშვით.

# პირველი რეპოზიტორია — my-portfolio

დავალება · თქვენი პორტფოლიო GitHub-ზე

## ნაბიჯები

- საქაღალდე `my-portfolio`: `index.html` (სახელი + 2-3 წინადადება თქვენზე) და `style.css`
- `git init` და პირველი commit: `"Add home page"`
- `.env` ფაილი + `.gitignore` (`.env`, `node_modules/`, `.vscode/`) — `git status` `.env`-ს **აღარ** უნდა აჩვენებდეს
- branch `feature/contacts` → კონტაქტების ბლოკი → commit → merge `main`-ში
- GitHub-ზე **ცარიელი** რეპო `my-portfolio` → `git remote add origin …` → `git push -u origin main`

## ✓ მზადაა, როცა

GitHub-ზე ჩანს `index.html`, `style.css`, `.gitignore` და მინიმუმ 3 commit — `.env` კი **არ** ჩანს

## ⭐ ბონუსი

- GitHub-ის საიტზე შეცვალეთ ერთი ხაზი (✏️) → ლოკალურად `git pull`
- `git log --oneline --graph` — აუხსენით გვერდით მჯდომს, რას ხედავთ

## 💡 მინიშნება

```bash
git switch -c feature/contacts   # ახალი branch + გადასვლა
git switch main                  # main-ზე დაბრუნება
git merge feature/contacts       # branch-ის შერწყმა
```

`git status` — ყველაზე ხშირი ბრძანება. როცა არ იცით, რა ხდება — ჯერ ის გაუშვით.

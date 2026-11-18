# my-portfolio → GitHub

დავალება · თქვენი პორტფოლიო GitHub-ზე

## ნაბიჯები

- `.env` ფაილი + `.gitignore` (`.env`, `node_modules/`, `.vscode/`) — `git status` `.env`-ს **აღარ** უნდა აჩვენებდეს → commit
- GitHub-ზე **ცარიელი** რეპო `my-portfolio` → `git remote add origin …` → `git push -u origin main`
- branch `feature/contacts` → კონტაქტების ბლოკი → commit → merge `main`-ში → `git push`

## ✓ მზადაა, როცა

GitHub-ზე ჩანს `index.html`, `style.css`, `.gitignore` და კონტაქტების ბლოკი — `.env` კი **არ** ჩანს

## ⭐ ბონუსი

- GitHub-ის საიტზე შეცვალეთ ერთი ხაზი (✏️) → ლოკალურად `git pull`
- `git log --oneline --graph` — აუხსენით გვერდით მჯდომს, რას ხედავთ

## 💡 მინიშნება

```bash
git switch -c feature/contacts   # ახალი branch + გადასვლა
git switch main                  # main-ზე დაბრუნება
git merge feature/contacts       # branch-ის შერწყმა
git push                         # ახალი commit-ები → GitHub
```

`git status` — ყველაზე ხშირი ბრძანება. როცა არ იცით, რა ხდება — ჯერ ის გაუშვით.

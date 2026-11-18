# .gitignore და პირველი branch

დავალება · my-portfolio-ს გაგრძელება

## ნაბიჯები

- `.env` ფაილი + `.gitignore` (`.env`, `node_modules/`, `.vscode/`) — `git status` `.env`-ს **აღარ** უნდა აჩვენებდეს → commit
- `git push` — `.gitignore` GitHub-ზეც
- branch `feature/contacts` → კონტაქტების ბლოკი → commit → merge `main`-ში → `git push`

## ✓ მზადაა, როცა

GitHub-ზე ჩანს `index.html`, `style.css`, `.gitignore` და კონტაქტების ბლოკი — `.env` კი **არ** ჩანს

## ⭐ ბონუსი

- `git log --oneline --graph` — აუხსენით გვერდით მჯდომს, რას ხედავთ

## 💡 მინიშნება

```bash
git switch -c feature/contacts   # ახალი branch + გადასვლა
git switch main                  # main-ზე დაბრუნება
git merge feature/contacts       # branch-ის შერწყმა
git push                         # ახალი commit-ები → GitHub
```

`git status` — ყველაზე ხშირი ბრძანება. როცა არ იცით, რა ხდება — ჯერ ის გაუშვით.

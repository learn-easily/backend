# my-portfolio → ინტერნეტში

დავალება · პირველი deploy

## ნაბიჯები

- my-portfolio GitHub-ზეა (Public), რეპოს root-ში — `index.html`, `style.css` და `.gitignore` (`.env`, `node_modules/`, `.vscode/`)
- GitHub-ზე my-portfolio → **Settings → Pages** → Source: **Deploy from a branch** → `main` / `(root)` → **Save**
- **Actions** ჩანართში დაელოდეთ მწვანე ✓-ს → გახსენით `https://<username>.github.io/my-portfolio/`
- ლინკი გაუგზავნეთ გვერდით მჯდომს — მან ტელეფონიდან უნდა გახსნას
- branch `feature/footer` → `index.html`-ის ბოლოს footer (სახელი + წელი) → commit → merge `main`-ში → `git push`
- Actions-ში ახალი deploy → საიტზე footer გამოჩნდა

## ✓ მზადაა, როცა

საიტი იხსნება სხვის ტელეფონზე, footer ჩანს, Actions-ში ორივე deploy მწვანეა, `.env` კი GitHub-ზე არ ჩანს

## ⭐ ბონუსი

- განზრახ გააფუჭეთ: `href="style.css"` → `href="/style.css"` → push → ნახეთ, რა მოხდა → გაასწორეთ და ახსენით, რატომ გაფუჭდა

## 💡 მინიშნება

```bash
git switch -c feature/footer
# index.html-ში footer დავამატეთ
git add index.html
git commit -m "Add footer"
git switch main
git merge feature/footer
git push
```

ძველი ვერსია ჩანს? ჯერ Actions — მწვანეა? მერე `Ctrl + F5` (ბრაუზერის cache).

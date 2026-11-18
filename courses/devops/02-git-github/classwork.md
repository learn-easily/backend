# my-portfolio — Git-იდან GitHub-მდე

დავალება · თქვენი პორტფოლიო Git-ში და GitHub-ზე

## ნაბიჯები

- `git config --global user.name` და `user.email` — იგივე email, რაც GitHub-ზე
- საქაღალდე `my-portfolio`: `index.html` (სახელი + 2-3 წინადადება თქვენზე) და `style.css`
- `git init` → პირველი commit `"Add home page"`
- `index.html`-ში ახალი წინადადება → `git status` (`modified`) → commit `"Update about text"`
- GitHub-ზე **ცარიელი** რეპო `my-portfolio` → `git remote add origin …` → `git push -u origin main`

## ✓ მზადაა, როცა

GitHub-ზე ჩანს `index.html`, `style.css` და 2 commit — თქვენი სახელით

## ⭐ ბონუსი

- GitHub-ის საიტზე **Add a README** → Commit → ლოკალურად `git pull`
- იგივე ციკლი VS Code-ის **Source Control** პანელით (Ctrl+Shift+G)

## 💡 მინიშნება

```bash
git status            # რა მდგომარეობაა?
git add .             # ყველა ცვლილება staging-ში
git commit -m "..."   # შენახვა ისტორიაში
git push              # ჩემი commit-ები → GitHub
```

`git status` — ყველაზე ხშირი ბრძანება. როცა არ იცით, რა ხდება — ჯერ ის გაუშვით.

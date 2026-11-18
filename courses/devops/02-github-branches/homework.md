# პროექტების გვერდი და README

my-portfolio — შემდეგ ლექციაზე ინტერნეტში გამოვაქვეყნებთ

## მოთხოვნები

- branch `feature/projects`: `projects.html` — 2-3 პროექტი (სახელი + მოკლე აღწერა) და ბმული მასზე `index.html`-დან
- მინიმუმ 2 commit გასაგები მესიჯებით → merge `main`-ში → `git push`
- `README.md`: რა პროექტია, ვინ ხართ, რა ტექნოლოგიებით არის აწყობილი

## ✓ მზადაა, როცა

GitHub-ზე `main`-ში ჩანს `projects.html` და `README.md`, ხოლო `git log --oneline --graph`-ში ჩანს branch-ი და merge

## ⭐ ბონუსი

- ერთი და იგივე ხაზი შეცვალეთ სხვადასხვანაირად ორ branch-ზე → merge → თვითონ გადაჭერით კონფლიქტი

## ამოხსნა

```bash ტერმინალი !
git switch -c feature/projects
# projects.html შევქმენით
git add projects.html
git commit -m "Add projects page"
# index.html-ში ბმული დავამატეთ
git add index.html
git commit -m "Link projects page from home"

git switch main
git merge feature/projects
git branch -d feature/projects

# README.md შევქმენით
git add README.md
git commit -m "Add README"
git push
```

```html index.html
<nav>
  <a href="index.html">მთავარი</a>
  <a href="projects.html">პროექტები</a>
</nav>
```

```markdown README.md
# my-portfolio

ჩემი პირადი საიტი — ვინ ვარ და რაზე ვმუშაობ.

**ტექნოლოგიები:** HTML, CSS
```

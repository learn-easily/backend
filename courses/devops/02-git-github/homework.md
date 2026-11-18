# უნარების ბლოკი — ლეპტოპიდან GitHub-მდე

my-portfolio — შემდეგ ლექციაზე `.gitignore`-ს და branch-ებს დავამატებთ

## მოთხოვნები

- `index.html`-ში ბლოკი „ჩემი უნარები“ — სია 4-5 უნარით (`<ul>`), და მისი სტილი `style.css`-ში
- ყოველი ცვლილება — **ცალკე commit**, გასაგები მესიჯით (მინიმუმ 3 ახალი commit)
- `git push` — ყველაფერი GitHub-ზე

## ✓ მზადაა, როცა

GitHub-ის **Commits** გვერდზე ჩანს კლასის commit-ები და მათ ზემოთ — მინიმუმ 3 ახალი, ხოლო `git status` წერს `nothing to commit, working tree clean`

## ⭐ ბონუსი

- `git clone`-ით ჩამოტვირთეთ საკუთარი რეპო **სხვა საქაღალდეში**, იქ შეცვალეთ ერთი ხაზი → commit → push. პირველ საქაღალდეში → `git pull`

## ამოხსნა

```bash ტერმინალი !
# index.html-ში "ჩემი უნარები" დავამატეთ
git add index.html
git commit -m "Add skills section"

# style.css-ში უნარების სტილი
git add style.css
git commit -m "Style skills list"

# index.html-ში ერთი უნარი დავამატეთ
git add index.html
git commit -m "Add Git to skills"

git push
git status
```

```html index.html
<h2>ჩემი უნარები</h2>
<ul class="skills">
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
  <li>Git</li>
</ul>
```

```css style.css
.skills { display: flex; gap: 10px; list-style: none; padding: 0; }
.skills li { background: #ede9fe; padding: 6px 14px; border-radius: 20px; }
```

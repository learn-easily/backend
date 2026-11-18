# უნარები და hosting.md

my-portfolio — შემდეგ ლექციაზე GitHub-ზე ავტვირთავთ

## მოთხოვნები

- `index.html`-ში ბლოკი „ჩემი უნარები“ — სია 4-5 უნარით (`<ul>`), და მისი სტილი `style.css`-ში
- ფაილი `hosting.md`: 3 საიტი, რომლითაც ხშირად სარგებლობთ — თქვენი აზრით, სტატიკურია თუ დინამიური, და რატომ
- ყოველი ცვლილება — **ცალკე commit**, გასაგები მესიჯით (მინიმუმ 3 ახალი commit)

## ✓ მზადაა, როცა

`git log --oneline` აჩვენებს კლასში გაკეთებულ commit-ებს და მათ ზემოთ — მინიმუმ 3 ახალს, ხოლო `git status` წერს `nothing to commit`

## ⭐ ბონუსი

- `hosting.md`-ში დაამატეთ: თქვენი პორტფოლიოსთვის რომელი ჰოსტინგი აირჩიეთ (სახლი, საერთო ბინა, ნაქირავები ბინა, სასტუმრო) და რატომ

## ამოხსნა

```bash ტერმინალი !
# index.html-ში "ჩემი უნარები" დავამატეთ
git add index.html
git commit -m "Add skills section"

# style.css-ში უნარების სტილი
git add style.css
git commit -m "Style skills list"

# hosting.md შევქმენით
git add hosting.md
git commit -m "Add hosting notes"

git log --oneline
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

```markdown hosting.md
# საიტები, რომლებითაც ვსარგებლობ

- **Wikipedia** — დინამიური: ყოველ გვერდს ბაზიდან აწყობს, მომხმარებლები არედაქტირებენ
- **ჩემი ბანკის აპი** — დინამიური: ყველას თავისი ანგარიში და ბალანსი აქვს
- **ლენდინგი / პორტფოლიო** — სტატიკური: ყველა ერთსა და იმავე ფაილებს ხედავს
```

```note
მთავარი კრიტერიუმი: **ყველა ერთსა და იმავეს ხედავს?** → სტატიკური. **პასუხი მომხმარებელზე ან მონაცემზეა დამოკიდებული?** → დინამიური, მას სერვერი და, ჩვეულებრივ, ბაზა სჭირდება.
```

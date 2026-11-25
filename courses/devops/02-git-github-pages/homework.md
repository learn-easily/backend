# პროექტების გვერდი, ლინკი README-ში და მზადება სერვერისთვის

my-portfolio ცოცხალია — შემდეგ ლექციაზე საკუთარ სერვერს ვქმნით

## მოთხოვნები

- branch `feature/projects`: `projects.html` — 2-3 პროექტი (სახელი + მოკლე აღწერა) და ბმული მასზე `index.html`-დან → merge `main`-ში → `git push` → ცოცხალ საიტზე იხსნება
- `README.md`-ში და რეპოს **About → Website**-ში — ცოცხალი საიტის ლინკი
- დარეგისტრირდით **DigitalOcean**-ზე (ბარათი/PayPal; შეამოწმეთ GitHub Student Pack) და დააყენეთ **Termius**
- **Windows:** `wsl --install -d Ubuntu-24.04` (PowerShell, Administrator) → გადატვირთვა → user და პაროლი — შენს კომპიუტერზე SSH გასაღებისთვის, `git`-ისთვის და `rsync`-ისთვის
- **macOS:** საკმარისია ჩაშენებული Terminal

## ✓ მზადაა, როცა

რეპოს გვერდზე ჩანს საიტის ლინკი, `projects.html` ცოცხალ საიტზე იხსნება, DigitalOcean-ში და Termius-ში შედიხართ, Ubuntu-ში `lsb_release -a` აჩვენებს `24.04`

## ⭐ ბონუსი

- `404.html` — საკუთარი „გვერდი ვერ მოიძებნა“: push → გახსენით არარსებული მისამართი, მაგ. `/my-portfolio/abc`

## 💡 თუ WSL არ დაყენდა

`Virtualization` BIOS-ში გამორთულია — ჩართეთ (Intel VT-x / AMD-V). ეს მე-7 ლექციაზე Docker-ისთვისაც დაგჭირდებათ, ამიტომ ახლავე მოაგვარეთ.

## ამოხსნა

```markdown README.md !
# my-portfolio

ჩემი პირადი საიტი — ვინ ვარ და რაზე ვმუშაობ.

🌐 **საიტი:** https://giorgi-beridze.github.io/my-portfolio/

**ტექნოლოგიები:** HTML, CSS · **ჰოსტინგი:** GitHub Pages
```

```console PowerShell (Administrator)
PS> wsl --install -d Ubuntu-24.04
# გადატვირთვის შემდეგ Ubuntu თვითონ გაიხსნება:
Enter new UNIX username: giorgi
New password: ********
```

```console Ubuntu
$ lsb_release -a
Distributor ID: Ubuntu
Description:    Ubuntu 24.04.3 LTS
Release:        24.04
```

```html 404.html
<!DOCTYPE html>
<html lang="ka">
<head><meta charset="UTF-8"><title>ვერ მოიძებნა</title></head>
<body>
  <h1>404 — ეს გვერდი არ არსებობს 🤷</h1>
  <a href="/my-portfolio/">მთავარზე დაბრუნება</a>
</body>
</html>
```

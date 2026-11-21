# Linux-ის ქვესტი და DigitalOcean ანგარიში

შემდეგ ლექციაზე საკუთარ სერვერს ვქმნით

## მოთხოვნები

- `~/linux-quest` საქაღალდეში შექმენით სტრუქტურა: `logs/`, `scripts/`, `notes/`
- `notes/commands.md` — `nano`-ით ჩაწერეთ დღევანდელი 10 ბრძანება და თითოეულის ახსნა თქვენი სიტყვებით
- `scripts/hello.sh` — შიგნით ერთი ხაზი `echo "გამარჯობა, $USER"` → გახადეთ გასაშვები (`chmod`) → გაუშვით `./scripts/hello.sh`
- `logs/app.log` — `echo`-თი ჩაწერეთ 3 ხაზი, ერთ-ერთში სიტყვა `ERROR` → `grep`-ით იპოვეთ მხოლოდ ის ხაზი
- დარეგისტრირდით **DigitalOcean**-ზე (საჭიროა ბარათი ან PayPal; სტუდენტებს შეუძლიათ შეამოწმონ GitHub Student Developer Pack-ის კრედიტი)

## ✓ მზადაა, როცა

`ls -l ~/linux-quest/scripts` აჩვენებს `-rwxr-xr-x hello.sh`, `./scripts/hello.sh` წერს მისალმებას, `grep ERROR logs/app.log` აბრუნებს ერთ ხაზს, DigitalOcean-ის panel-ში შეხვედით

## ⭐ ბონუსი

- `tail -f ~/linux-quest/logs/app.log` ერთ ტერმინალში, მეორედან `echo "new line" >> logs/app.log` — ნახეთ, როგორ ჩნდება ხაზი „ცოცხლად“

## ამოხსნა

```console Ubuntu !
$ mkdir -p ~/linux-quest/{logs,scripts,notes}
$ cd ~/linux-quest
$ nano notes/commands.md

$ echo 'echo "გამარჯობა, $USER"' > scripts/hello.sh
$ chmod +x scripts/hello.sh        # ან: chmod 755
$ ./scripts/hello.sh
გამარჯობა, giorgi

$ echo "INFO app started"   >  logs/app.log
$ echo "ERROR db not found" >> logs/app.log
$ echo "INFO request done"  >> logs/app.log
$ grep ERROR logs/app.log
ERROR db not found
```

`>` ფაილს თავიდან წერს, `>>` — ბოლოში ამატებს. `{logs,scripts,notes}` — სამი საქაღალდე ერთი ბრძანებით.

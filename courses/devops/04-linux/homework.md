# Linux-ის ქვესტი

შემდეგ ლექციაზე სერვერზე Nginx-ს ვაყენებთ

## მოთხოვნები

- სერვერზე, `~/linux-quest`-ში: `logs/`, `scripts/`, `notes/`; `notes/commands.md` — 10 ბრძანება თქვენი ახსნით
- `scripts/hello.sh` (`echo "გამარჯობა, $USER"`) → გასაშვები → `./scripts/hello.sh`
- `logs/app.log` — 3 ხაზი, ერთში `ERROR` → `grep`-ით მხოლოდ ის

## ✓ მზადაა, როცა

`hello.sh` ეშვება, `grep` ერთ ხაზს აბრუნებს

## ⭐ ბონუსი

- `tail -f ~/linux-quest/logs/app.log` ერთ ტერმინალში, მეორედან `echo "new line" >> logs/app.log` — ნახეთ, როგორ ჩნდება ხაზი „ცოცხლად“

## ამოხსნა

```console Termius · giorgi@lms-server !
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

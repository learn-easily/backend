# Linux-ის ქვესტი და სერვერის მომზადება

შემდეგ ლექციაზე სერვერზე Nginx-ს ვაყენებთ

## მოთხოვნები

- სერვერზე, `~/linux-quest`-ში: `logs/`, `scripts/`, `notes/`; `notes/commands.md` — 10 ბრძანება თქვენი ახსნით
- `scripts/hello.sh` (`echo "გამარჯობა, $USER"`) → გასაშვები → `./scripts/hello.sh`
- `logs/app.log` — 3 ხაზი, ერთში `ERROR` → `grep`-ით მხოლოდ ის
- თუ კლასში ვერ მოასწარით: `00-hardening.conf` (root და პაროლი აკრძალულია → `restart ssh`, ჯერ ახალ tab-ში შეამოწმეთ!) · swap 2 GB (`/etc/fstab`-ითაც) · WSL-ში `~/.ssh/config` → `ssh lms`

## ✓ მზადაა, როცა

`hello.sh` ეშვება, `grep` ერთ ხაზს აბრუნებს, `sshd -T` — `no`/`no`, `free -h` — Swap 2.0Gi, `ssh lms` შედის

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

```console Termius · giorgi@lms-server
$ sudo nano /etc/ssh/sshd_config.d/00-hardening.conf
PermitRootLogin no
PasswordAuthentication no
$ sudo sshd -t && sudo systemctl restart ssh

$ sudo fallocate -l 2G /swapfile && sudo chmod 600 /swapfile
$ sudo mkswap /swapfile && sudo swapon /swapfile
$ echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

```plain ~/.ssh/config (WSL-ში)
Host lms
    HostName 164.90.12.34
    User giorgi
    IdentityFile ~/.ssh/id_ed25519
```

`>` ფაილს თავიდან წერს, `>>` — ბოლოში ამატებს. `{logs,scripts,notes}` — სამი საქაღალდე ერთი ბრძანებით.

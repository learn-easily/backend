# Linux-ის ქვესტი სერვერზე

შემდეგ ლექციაზე სერვერს ვიცავთ — დღეს კი მასზე ბრძანებებს ვიწაფავთ

## მოთხოვნები

- Termius-ით სერვერზე, `~/linux-quest`-ში: `logs/`, `notes/`, `backup/`; `notes/commands.md` — 10 ბრძანება თქვენი ახსნით (`nano`)
- `logs/app.log` (`nano`) — 3 ხაზი, ერთში `ERROR` → `grep`-ით მხოლოდ ის
- `notes/commands.md` დააკოპირეთ `backup/`-ში, მერე `notes/`-ში გადაარქვით `linux.md` → `ls -la`-ით შეამოწმეთ ორივე საქაღალდე
- `/etc`-ში იპოვეთ SSH-ის საქაღალდე და ნახეთ, რა ფაილებია შიგნით; `/var/log`-ში — რომელი ლოგია ყველაზე დიდი (`ls -l`)

## ✓ მზადაა, როცა

`grep ERROR ~/linux-quest/logs/app.log` ერთ ხაზს აბრუნებს, `backup/commands.md` და `notes/linux.md` არსებობს, შეგიძლიათ თქვათ, რა ფაილებია `/etc/ssh`-ში

## ⭐ ბონუსი

- Termius-ში ორი tab: პირველში `tail -f ~/linux-quest/logs/app.log`, მეორეში `echo "new line" >> ~/linux-quest/logs/app.log` — ნახეთ, როგორ ჩნდება ხაზი „ცოცხლად“

## ამოხსნა

```console Termius · root@lms-server !
# mkdir -p ~/linux-quest/logs ~/linux-quest/notes ~/linux-quest/backup
# cd ~/linux-quest
# nano notes/commands.md
# nano logs/app.log
INFO app started
ERROR db not found
INFO request done
# grep ERROR logs/app.log
ERROR db not found

# cp notes/commands.md backup/
# mv notes/commands.md notes/linux.md
# ls -la notes backup

# ls /etc/ssh
ssh_config  ssh_config.d  sshd_config  sshd_config.d  ...
# ls -l /var/log
```

`mkdir -p` რამდენიმე საქაღალდეს ერთად ქმნის. `/etc/ssh/sshd_config` — SSH სერვერის კონფიგურაცია: შემდეგ ლექციაზე სწორედ მის გვერდით შევქმნით საკუთარ ფაილს, რომ სერვერი დავიცვათ. ბონუსში `>>` ფაილის ბოლოს ამატებს ხაზს (`>` — თავიდან გადაწერდა).

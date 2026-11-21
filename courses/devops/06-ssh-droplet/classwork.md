# ჩემი პირველი სერვერი

დავალება · Droplet + SSH

## ნაბიჯები

- WSL-ში `ssh-keygen -t ed25519` → `cat ~/.ssh/id_ed25519.pub` — დააკოპირეთ
- DigitalOcean → **Create → Droplets**: Frankfurt · Ubuntu 24.04 · Basic · **SSH Key** · `lms-server`
- `ssh root@<IP>` → `adduser <სახელი>` → `usermod -aG sudo <სახელი>` → `rsync` `~/.ssh`
- **ახალ** ფანჯარაში `ssh <სახელი>@<IP>` → `sudo whoami`

## ✓ მზადაა, როცა

ახალი user-ით შედიხართ სერვერზე პაროლის გარეშე, და `sudo whoami` აბრუნებს `root`

## ⭐ ბონუსი

- `~/.ssh/config`-ში ჩაწერეთ `Host lms` → შედით უბრალოდ `ssh lms`-ით

## 💡 მინიშნება

```bash
ssh root@164.90.12.34          # IP — Droplet-ის გვერდიდან
exit                           # სერვერიდან გამოსვლა
```

`Permission denied (publickey)` — სერვერზე `.pub` არ არის ან სხვა გასაღებით შედიხართ. შეამოწმეთ, რომ DigitalOcean-ში ზუსტად ის `.pub` ჩასვით.

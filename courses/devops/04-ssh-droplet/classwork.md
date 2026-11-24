# ჩემი პირველი სერვერი

დავალება · Droplet + SSH

## ნაბიჯები

- WSL-ში `ssh-keygen -t ed25519` → `.pub` → DigitalOcean: Frankfurt · Ubuntu 24.04 · Basic · **SSH Key** · `lms-server`
- **Termius**: Keychain → Import (პირადი გასაღები) → New Host (IP, `root`) → Connect
- `adduser <სახელი>` → `usermod -aG sudo <სახელი>` → `rsync` `~/.ssh` → `/home/<სახელი>`
- Termius-ში მეორე Host — Username `<სახელი>` → Connect → `sudo whoami`

## ✓ მზადაა, როცა

Termius-ით ახალი user-ით შედიხართ სერვერზე პაროლის გარეშე, და `sudo whoami` აბრუნებს `root`

## ⭐ ბონუსი

- `~/.ssh/config`-ში ჩაწერეთ `Host lms` → შედით უბრალოდ `ssh lms`-ით

## 💡 მინიშნება

`Permission denied (publickey)` — Termius-ში სხვა გასაღებია არჩეული, ან DigitalOcean-ში სხვა `.pub` ჩასვით. Termius-ში ჩასვით **პირადი** (`id_ed25519`), DigitalOcean-ში — **საჯარო** (`id_ed25519.pub`).

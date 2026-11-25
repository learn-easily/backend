# ჩემი პირველი სერვერი

დავალება · ყიდვა + დაკავშირება

## ნაბიჯები

- WSL-ში `ssh-keygen -t ed25519` → `cat ~/.ssh/id_ed25519.pub`
- DigitalOcean: Frankfurt · Ubuntu 24.04 · Basic 1 GB · **SSH Key** (`.pub`) · `lms-server` → Create → დაიმახსოვრეთ IP
- WSL-ში `ssh root@<IP>` → `yes` → `hostname` → `exit`
- **Termius**: Keychain → Import (პირადი გასაღები) → New Host (IP, `root`) → Connect
- Termius-ში: `whoami`, `pwd`, `cat /etc/os-release`, `nproc`, `free -h`, `df -h /` — ემთხვევა იმას, რაც ფორმაში აირჩიეთ?

## ✓ მზადაა, როცა

ტერმინალითაც და Termius-ითაც პაროლის გარეშე შედიხართ, ხოლო `free -h` და `df -h /` აჩვენებს ~1 GB RAM-ს და ~25 GB დისკს

## ⭐ ბონუსი

- Termius-ში იმავე Host-ზე მეორე tab გახსენით → ორივეში `uptime` — ორივე ერთი და იგივე სერვერია

## 💡 მინიშნება

`Permission denied (publickey)` — DigitalOcean-ში სხვა `.pub` ჩასვით, ან Termius-ში სხვა გასაღებია არჩეული. DigitalOcean-ში — **საჯარო** (`id_ed25519.pub`), Termius-ში — **პირადი** (`id_ed25519`).

# ჩემი პირველი სერვერი

დავალება · Droplet + Termius + პირველი ბრძანებები

## ნაბიჯები

- WSL-ში `ssh-keygen -t ed25519` → `.pub` → DigitalOcean: Frankfurt · Ubuntu 24.04 · Basic · **SSH Key** · `lms-server`
- **Termius**: Keychain → Import (პირადი გასაღები) → New Host (IP, `root`) → Connect
- `hostname`, `df -h /`, `free -h`, `cat /etc/os-release` — ჩაიწერეთ, რამდენი დისკი და RAM გაქვთ
- `mkdir -p ~/server-notes` → `nano ~/server-notes/server.md`: IP, region, დისკი, RAM → `Ctrl+O`, `Ctrl+X` → `cat`-ით შეამოწმეთ
- `ls -la ~` → იპოვეთ ფარული `.ssh` → `cat ~/.ssh/authorized_keys` — ეს თქვენი `.pub`-ია?

## ✓ მზადაა, როცა

Termius-ით პაროლის გარეშე შედიხართ სერვერზე, `cat ~/server-notes/server.md` სერვერის მონაცემებს აჩვენებს, `authorized_keys`-ში თქვენი საჯარო გასაღებია

## ⭐ ბონუსი

- `tail -f /var/log/auth.log` — დაელოდეთ ბოტების ცდებს (`Invalid user ...`); `Ctrl+C` → `grep Invalid /var/log/auth.log` — რამდენი სცადა უკვე?

## 💡 მინიშნება

`Permission denied (publickey)` — Termius-ში სხვა გასაღებია არჩეული, ან DigitalOcean-ში სხვა `.pub` ჩასვით. Termius-ში ჩასვით **პირადი** (`id_ed25519`), DigitalOcean-ში — **საჯარო** (`id_ed25519.pub`).

`Tab` — სახელის ავტოშევსება. `↑` — წინა ბრძანება. დაიკარგეთ? `pwd`.

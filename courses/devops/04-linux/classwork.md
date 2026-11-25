# საკუთარი user და უფლებები

დავალება · lms-server root-ის გარეშე

## ნაბიჯები

- root-ით: `adduser <სახელი>` → `usermod -aG sudo <სახელი>` → `rsync --archive --chown=<სახელი>:<სახელი> ~/.ssh /home/<სახელი>`
- Termius-ში მეორე Host — Username `<სახელი>` → Connect → `whoami`, `sudo whoami`
- `sudo apt update && sudo apt upgrade -y` → `sudo apt install -y tree htop` → `tree ~ -a`
- `ls -la ~/.ssh` — რა უფლებები აქვს `authorized_keys`-ს და რატომ? → `touch secret.txt` → `chmod 600 secret.txt` → `ls -l`
- `sudo ss -tlnp` — რომელი port-ია ღია და ვინ უსმენს?

## ✓ მზადაა, როცა

Termius-ით ახალი user-ით შედიხართ პაროლის გარეშე, `sudo whoami` აბრუნებს `root`, `secret.txt` — `-rw-------`, `ss -tlnp`-ში ჩანს `sshd` port 22-ზე

## ⭐ ბონუსი

- `sleep 1000 &` → `ps aux | grep sleep`-ით იპოვეთ PID → `kill`-ით გააჩერეთ → `htop`-ში შეამოწმეთ, რომ აღარ არის

## 💡 მინიშნება

`Permission denied (publickey)` ახალი user-ით — `rsync`-ის ბრძანებაში სახელი შეგეშალათ, ან `/home/<სახელი>/.ssh` სხვას ეკუთვნის: root-ით `ls -la /home/<სახელი>/.ssh`.

# LMS სერვერზე — კონტეინერებით

მე-8 ლექციის ხელით deploy → Compose

## მოთხოვნები

- სერვერზე Docker: `curl -fsSL https://get.docker.com | sudo sh` → `sudo usermod -aG docker $USER` → ხელახლა შესვლა
- ძველი, ხელით გაშვებული სერვისები: `sudo systemctl disable --now lms-api postgresql`
- `git clone` → `~/lms`; სერვერზე **ახალი** `.env` (სხვა, ძლიერი პაროლით, `ASPNETCORE_ENVIRONMENT=Production`) → `chmod 600 .env`
- `docker compose up -d --build` — Nginx-ის `lms-api` კონფიგი არ იცვლება (`127.0.0.1:5000`)
- backup: `pg_dump` → `~/backups/lms-<თარიღი>.sql`

## ✓ მზადაა, როცა

`http://<IP>:8081/api/courses` პასუხობს კონტეინერიდან, `sudo reboot`-ის შემდეგ ყველაფერი თავისით ირთვება, `~/backups`-ში SQL ფაილია

## ⭐ ბონუსი

- LMS-ში პატარა ცვლილება → push → სერვერზე `git pull && docker compose up -d --build` → ცვლილება ჩანს. დაითვალეთ, რამდენი ბრძანება დაგჭირდათ

## ამოხსნა

```console lms-server !
$ curl -fsSL https://get.docker.com | sudo sh
$ sudo usermod -aG docker $USER && exit
$ ssh lms
$ sudo systemctl disable --now lms-api postgresql

$ git clone https://github.com/giorgi/lms.git ~/lms && cd ~/lms
$ nano .env
DB_PASSWORD=h7Kq2-xR9v-Lm4Z
ASPNETCORE_ENVIRONMENT=Production
$ chmod 600 .env

$ docker compose up -d --build
$ docker compose ps
$ curl http://127.0.0.1:5000/api/courses
```

```console lms-server
$ mkdir -p ~/backups
$ docker compose exec db pg_dump -U lms lms > ~/backups/lms-$(date +%F).sql
$ ls -lh ~/backups
```

`$(date +%F)` — დღევანდელი თარიღი (`2026-12-05`) ფაილის სახელში. `restart: unless-stopped`-ის წყალობით reboot-ის შემდეგ კონტეინერები თავისით ირთვება.

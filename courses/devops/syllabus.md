# DevOps Crash Course: GitHub to DigitalOcean

**ტექნოლოგიები:** Git და GitHub, GitHub Pages, Linux (Ubuntu 24.04), SSH და Termius, DigitalOcean Droplet, Nginx, .NET 10 runtime და systemd, PostgreSQL, Docker და Docker Compose, DNS და Let's Encrypt, GitHub Actions, GHCR, cloud-init

**პროექტი:** 02–05 — my-portfolio და Angular აპი (სტატიკური საიტები: ჯერ GitHub Pages, მერე საკუთარ სერვერზე). 06-დან — **LMS**, რომელიც ASP.NET-ის კურსზე იწერება: ჯერ API ხელით, მერე Docker-ით, დომენით და HTTPS-ით, CI/CD-ით; ბოლო ლექციაზე LMS-ს Angular-ის frontend ემატება და მთელი სისტემა ახალ სერვერზე გადადის. ლექტორი LMS-ს კლასში აჩვენებს; სტუდენტი იმავე ნაბიჯებს თავის პროექტზე იმეორებს.

| დანიშნულება | ინსტრუმენტი |
| --- | --- |
| კოდი და ისტორია | Git, GitHub |
| სერვერი | DigitalOcean Droplet (Ubuntu 24.04), SSH, Termius |
| ვებ-სერვერი და reverse proxy | Nginx |
| აპის გაშვება | systemd → Docker, Docker Compose |
| ბაზა | PostgreSQL |
| დომენი და HTTPS | DNS, Let's Encrypt (`certbot`) |
| ავტომატიზაცია | GitHub Actions, GHCR, cloud-init |

---

## საფუძვლები (2 ლექცია)

### 01. რა არის DevOps

რა არის DevOps და რატომ გაჩნდა; DevOps ციკლი და DevOps ინჟინრის ყოველდღიური საქმეები; ხელსაწყოების ჯგუფები — რა არის ამ კურსში და რა შემდეგი ნაბიჯი; სად ცხოვრობს საიტი: სერვერი, DNS, ჰოსტინგის სახეები.

### 02. Git → GitHub Pages — საიტი ინტერნეტში

Git-ის მოკლე გამეორება DevOps-ის კუთხით (`git push` → GitHub → pipeline → საიტი); `.gitignore` და საიდუმლოებები public რეპოში; my-portfolio GitHub Pages-ზე, განახლება `git push`-ით და ტიპური შეცდომები; რატომ ვერ გაეშვება API GitHub Pages-ზე.

## საკუთარი სერვერი (4 ლექცია)

### 03. საკუთარი სერვერი — არჩევა, ყიდვა და SSH

რატომ VPS; როგორ ავარჩიოთ სერვერი (რა იმუშავებს → RAM, CPU, დისკი, region); Droplet-ის შექმნა; SSH: საჯარო ნაწილი სერვერზე, პირადი შენთან, `ssh-keygen`; დაკავშირება ტერმინალით (`ssh root@IP`) და Termius-ით; პირველი ბრძანებები (`whoami`, `pwd`, `ls`, `cd`, `cat`, `free -h`, `df -h`).

### 04. Linux — სერვერის ენა

საკუთარი sudo user root-ის ნაცვლად; `apt`; ფაილური სისტემა (`/`, `~`, `/etc`, `/var/log`, `/var/www`); ფაილებთან მუშაობა; უფლებები (`chmod`, `chown`); პროცესები და port-ები (`ps`, `htop`, `kill`, `ss -tlnp`); სერვერის მომზადება: root-ით და პაროლით შესვლის აკრძალვა, swap, `~/.ssh/config` — ყველაფერი სერვერზე, Termius-ში.

### 05. Nginx — საიტი შენს სერვერზე

Nginx-ის დაყენება და `systemctl`; `ufw` firewall (22 და 80); ფაილების ატვირთვა `rsync`-ით; server block (`listen`, `root`, `index`, `try_files`); Angular SPA და „refresh → 404“; ლოგები და 403 / 404 / connection refused-ის მიზეზები.

### 06. LMS API სერვერზე — ხელით

ASP.NET Core runtime და PostgreSQL სერვერზე; `dotnet publish` და მიგრაციები; systemd სერვისი; Nginx, როგორც reverse proxy; 502 Bad Gateway და `journalctl`. ლექციის ბოლოს — რამდენი ხელით ნაბიჯი დაგვჭირდა და რატომ გვჭირდება Docker.

## კონტეინერები (2 ლექცია)

### 07. Docker — აპი გარემოსთან ერთად

image და container, კონტეინერი vs ვირტუალური მანქანა; `docker run` (port-ები, გარემოს ცვლადები, volume); კონტეინერების მართვა; LMS-ის multi-stage Dockerfile და `.dockerignore`.

### 08. Docker Compose — LMS + ბაზა სერვერზე

`compose.yaml`: services, ports, environment, volumes; სერვისებს შორის კავშირი სახელით, `healthcheck`, `restart`; საიდუმლოებები `.env`-ში; სერვერზე გაშვება, Nginx → კონტეინერი, ბაზის backup.

## Production და ავტომატიზაცია (4 ლექცია)

### 09. დომენი, HTTPS და საიდუმლოებები

DNS ჩანაწერები (A, CNAME) და `dig`; საიტები `server_name`-ით; HTTPS Let's Encrypt-ით და ავტომატური განახლება; ASP.NET Core-ის კონფიგურაციის რიგი; საიდუმლოებები: `user-secrets` შენთან, `.env` სერვერზე; HTTPS proxy-ს უკან.

### 10. CI/CD — თეორია და CI პრაქტიკაში

CI/CD pipeline: build → test → artifact → deploy; Continuous Integration vs Continuous Delivery vs Continuous Deployment და მათი პრინციპები; GitHub Actions: workflow, trigger, job, runner, step; CI ყოველ Pull Request-ზე (build + test), ჩავარდნილი CI-ის ლოგი; branch protection.

### 11. CD — merge → LMS სერვერზე

build GitHub-ზე, სერვერი მხოლოდ იღებს; image GHCR-ში `latest` და `sha` tag-ებით; GitHub Secrets და ცალკე deploy გასაღები; `deploy.yml`: merge → build → GHCR → SSH → `compose pull` + `up -d`; rollback წინა ვერსიაზე.

### 12. ფინალი — მთელი სისტემა ახალ სერვერზე

LMS-ის Angular frontend სისტემაში: multi-stage Dockerfile (node → nginx), `/api` proxy CORS-ის გარეშე, Compose და CD ორი image-ით; სერვერის გამოცვლა: cloud-init, კოდი vs მდგომარეობა (`.env`, მონაცემები, DNS, სერტიფიკატი), ბაზის გადატანა `pg_dump`-ით, DNS და HTTPS, შემოწმება; გავლილი გზა და DevOps-ის რუკა Junior → Middle → Senior.

# ფინალური პროექტი — შენი სისტემა ახალ სერვერზე

კურსის ყველა ლექცია ერთ გზაზე

## მოთხოვნები

- შენი პროექტის ფრონტი სისტემაშია: `web/Dockerfile`, Compose-ში `web`, `deploy.yml`-ში ორი image და `workflow_dispatch`
- Nginx-ის კონფიგი რეპოში: `deploy/nginx/lms.conf`
- ახალი Droplet cloud-init-ით → clone, `.env` (`scp -3`), GHCR login, Nginx → მონაცემები (`pg_dump | psql`) → `SSH_HOST` → Run workflow → DNS → certbot
- შემოწმების სია (ლექციის ნაბიჯი 6) — ყველა ✓ → ძველი Droplet: Power Off → რამდენიმე დღეში **Destroy**
- README: ცოცხალი ლინკი `https://app.<domain>`, CI badge, სისტემის სქემა (web → api → db) და deploy-ის აღწერა

## ✓ მზადაა, როცა

`https://app.<domain>` ახალ სერვერზე მუშაობს ძველი მონაცემებით, PR → CI ✅ → merge → Deploy ✅ ცვლილებას ახალ სერვერზე აჩენს, ხელით არაფერი

## ⭐ ბონუსი

- DevOps-ის რუკა: Junior ტაბზე მონიშნე, რაც უკვე შეგიძლია, და აირჩიე შემდეგი ერთი თემა

## ამოხსნა

```yaml cloud-init.yaml !
#cloud-config
users:
  - name: giorgi
    groups: sudo
    shell: /bin/bash
    sudo: "ALL=(ALL) NOPASSWD:ALL"
    ssh_authorized_keys:
      - ssh-ed25519 AAAA... giorgi@laptop
      - ssh-ed25519 AAAA... github-actions-deploy
package_update: true
packages: [nginx, certbot, python3-certbot-nginx]
runcmd:
  - curl -fsSL https://get.docker.com | sh
  - usermod -aG docker giorgi
  - fallocate -l 2G /swapfile && chmod 600 /swapfile
  - mkswap /swapfile && swapon /swapfile
  - echo '/swapfile none swap sw 0 0' >> /etc/fstab
  - sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
  - systemctl restart ssh
  - ufw allow OpenSSH && ufw allow 'Nginx Full' && ufw --force enable
```

```nginx deploy/nginx/lms.conf
server {
    listen 80;
    server_name app.giorgi.ge;
    location / {
        proxy_pass http://127.0.0.1:4000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

server {
    listen 80;
    server_name api.giorgi.ge;
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```console WSL
$ scp -3 lms:~/lms/.env lms-new:~/lms/.env
$ ssh lms "cd ~/lms && docker compose stop web api"
$ ssh lms-new "cd ~/lms && docker compose up -d db"
$ ssh lms "cd ~/lms && docker compose exec -T db pg_dump -U lms lms" \
  | ssh lms-new "cd ~/lms && docker compose exec -T db psql -U lms lms"
```

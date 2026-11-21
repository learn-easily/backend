# Angular აპი სერვერზე + deploy სკრიპტი

ორი საიტი ერთ სერვერზე: portfolio — port 80, Angular — port 8080

## მოთხოვნები

- თქვენი Angular პროექტი (Frontend კურსიდან): `ng build` → `dist/<app>/browser/` → `rsync` → `/var/www/app`
- server block `/etc/nginx/sites-available/app`: `listen 8080`, SPA fallback `try_files … /index.html`
- `sudo ufw allow 8080/tcp`
- შეამოწმეთ: `http://<IP>:8080/<რომელიმე-როუტი>` → **refresh** → გვერდი იხსნება (არა 404)
- my-portfolio-ში `deploy.sh`: ერთი ბრძანებით ატვირთავს საიტს სერვერზე → `chmod +x` → `./deploy.sh`

## ✓ მზადაა, როცა

ორივე საიტი მუშაობს, Angular-ის შიდა გვერდზე refresh 404-ს არ აბრუნებს, portfolio-ს ცვლილება სერვერზე `./deploy.sh`-ით ჩანს

## ⭐ ბონუსი

- portfolio-ში საკუთარი `404.html` (მე-4 ლექციიდან) + Nginx-ში `error_page 404 /404.html;` — არარსებული გვერდი თქვენს 404-ს აჩვენებს

## ამოხსნა

```nginx /etc/nginx/sites-available/app !
server {
    listen 8080;
    server_name _;

    root /var/www/app;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

```console lms-server
$ sudo mkdir -p /var/www/app && sudo chown -R $USER:$USER /var/www/app
$ sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/
$ sudo nginx -t && sudo systemctl reload nginx
$ sudo ufw allow 8080/tcp
```

```console WSL (Angular-ის პროექტში)
$ ng build
$ rsync -avz --delete dist/my-app/browser/ lms:/var/www/app/
```

```bash deploy.sh
#!/bin/bash
set -e
rsync -avz --delete --exclude .git --exclude deploy.sh ./ lms:/var/www/portfolio/
echo "✅ portfolio განახლდა"
```

`set -e` — თუ რომელიმე ბრძანება ჩავარდა, სკრიპტი ჩერდება. ეს სკრიპტი უკვე პატარა **ავტომატიზაციაა** — კურსის ბოლოს მას GitHub Actions შეცვლის.

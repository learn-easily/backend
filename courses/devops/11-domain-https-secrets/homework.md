# API და Angular — ქვედომენებზე, HTTPS-ით

port-ები 8080/8081 აღარ გვჭირდება

## მოთხოვნები

- `lms-api` server block: `listen 80`, `server_name api.<domain>` (port 8081-ის ნაცვლად); `app` — `app.<domain>` (8080-ის ნაცვლად)
- `sudo certbot --nginx -d api.<domain> -d app.<domain>` → ორივე `https://`-ით
- ufw: წაშალეთ `8080/tcp`, `8081/tcp`, `Nginx HTTP`; დარჩეს `OpenSSH` და `Nginx Full`
- სერვერის `.env`-ში `JWT_KEY` (`openssl rand -base64 64`) → `compose.yaml`-ში `Jwt__Key: ${JWT_KEY}` და `ASPNETCORE_FORWARDEDHEADERS_ENABLED: "true"`
- Angular-ის `environment.prod.ts`-ში `apiUrl: 'https://api.<domain>'` → `ng build` → `rsync`

## ✓ მზადაა, როცა

`https://api.<domain>/api/courses` და `https://app.<domain>` ბოქლომით იხსნება, `sudo ufw status`-ში 8080/8081 აღარ არის, `git grep -i "jwt"`-ით რეპოში ნამდვილი გასაღები არსად ჩანს

## ⭐ ბონუსი

- LMS-ში დროებით endpoint, რომელიც აბრუნებს `Request.Scheme`-ს → `https://api.<domain>/...` → `https` უნდა დაწეროს (forwarded headers მუშაობს) → მერე წაშალეთ

## ამოხსნა

```nginx /etc/nginx/sites-available/lms-api !
server {
    listen 80;
    server_name api.giorgi.ge;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```console lms-server
$ sudo nginx -t && sudo systemctl reload nginx
$ sudo certbot --nginx -d api.giorgi.ge -d app.giorgi.ge
$ sudo ufw delete allow 8080/tcp
$ sudo ufw delete allow 8081/tcp
$ sudo ufw delete allow 'Nginx HTTP'
$ echo "JWT_KEY=$(openssl rand -base64 64 | tr -d '\n')" >> ~/lms/.env
$ cd ~/lms && docker compose up -d
```

```yaml compose.yaml — api
    environment:
      ASPNETCORE_ENVIRONMENT: ${ASPNETCORE_ENVIRONMENT:-Production}
      ASPNETCORE_FORWARDEDHEADERS_ENABLED: "true"
      ConnectionStrings__Default: "Host=db;Database=lms;Username=lms;Password=${DB_PASSWORD}"
      Jwt__Key: ${JWT_KEY}
```

`tr -d '\n'` — `openssl`-ის შედეგიდან ხაზის გადატანებს შლის, რომ გასაღები `.env`-ში ერთ ხაზზე ჩაიწეროს.

# API — სერვისად და Nginx-ის უკან

შენი API მუშაობს 24/7 და ინტერნეტიდანაც ჩანს

## მოთხოვნები

- `lms-api.service` (`Restart=always`, URL, connection string) → `daemon-reload` → `enable --now`
- Nginx: `listen 8081` + `proxy_pass http://127.0.0.1:5000` → `ufw allow 8081/tcp`
- crash-ის ტესტი: `kill -9 <PID>` → 5 წამში ისევ `running`
- README-ში — ყველა ნაბიჯი, რაც პროექტის გასაშვებად გადადგით

## ✓ მზადაა, როცა

`http://<IP>:8081/api/courses` → JSON, `kill -9`-ის და `reboot`-ის შემდეგაც მუშაობს

## ⭐ ბონუსი

- `sudo systemctl stop lms-api` → ბრაუზერში 502 → `sudo tail /var/log/nginx/error.log` — იპოვეთ ხაზი `connect() failed (111: Connection refused)` და ახსენით

## ამოხსნა

```ini /etc/systemd/system/lms-api.service !
[Unit]
Description=LMS API
After=network.target postgresql.service

[Service]
WorkingDirectory=/var/www/lms-api
ExecStart=/usr/bin/dotnet /var/www/lms-api/Lms.Api.dll
Restart=always
RestartSec=5
User=www-data
Environment=ASPNETCORE_ENVIRONMENT=Production
Environment=ASPNETCORE_URLS=http://127.0.0.1:5000
Environment="ConnectionStrings__Default=Host=localhost;Database=lms;Username=lms;Password=Str0ng!Pass"

[Install]
WantedBy=multi-user.target
```

```console Termius · lms-server
$ sudo systemctl daemon-reload
$ sudo systemctl enable --now lms-api
$ systemctl status lms-api
● lms-api.service - LMS API
     Active: active (running)
$ journalctl -u lms-api -n 20
```

```nginx /etc/nginx/sites-available/lms-api
server {
    listen 8081;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```console Termius · lms-server
$ sudo ln -s /etc/nginx/sites-available/lms-api /etc/nginx/sites-enabled/
$ sudo nginx -t && sudo systemctl reload nginx
$ sudo ufw allow 8081/tcp
```

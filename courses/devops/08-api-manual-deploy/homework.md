# API — სერვისად და Nginx-ის უკან

LMS API მუშაობს 24/7 და ინტერნეტიდანაც ჩანს

## მოთხოვნები

- `/etc/systemd/system/lms-api.service` — `Restart=always`, `ASPNETCORE_URLS=http://127.0.0.1:5000`, connection string
- `daemon-reload` → `enable --now` → `systemctl status lms-api` — `active (running)`
- Nginx: `sites-available/lms-api` — `listen 8081`, `proxy_pass http://127.0.0.1:5000` → `ufw allow 8081/tcp`
- ბრაუზერში `http://<IP>:8081/api/courses` → JSON
- crash-ის ტესტი: `sudo kill -9 <PID>` → 5 წამში `systemctl status` ისევ `running`-ს აჩვენებს (ახალი PID-ით)
- README-ში ჩამოწერეთ **ყველა** ნაბიჯი, რომელიც LMS-ის გასაშვებად გადადგით — თავიდან ბოლომდე

## ✓ მზადაა, როცა

API ბრაუზერიდან პასუხობს, `kill -9`-ის შემდეგ თავისით ცოცხლდება, `sudo reboot`-ის შემდეგაც მუშაობს, README-ში ნაბიჯების სიაა

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

```console lms-server
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

```console lms-server
$ sudo ln -s /etc/nginx/sites-available/lms-api /etc/nginx/sites-enabled/
$ sudo nginx -t && sudo systemctl reload nginx
$ sudo ufw allow 8081/tcp
```

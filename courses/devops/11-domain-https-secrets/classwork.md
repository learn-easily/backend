# portfolio — დომენზე და HTTPS-ით

დავალება · DNS + server_name + certbot

## ნაბიჯები

- DNS-ში: `A @ → <IP>`, `CNAME www → @`, `A api → <IP>`, `A app → <IP>` → `dig +short <domain>` აბრუნებს IP-ს
- `sites-available/portfolio`: `server_name <domain> www.<domain>;` → `nginx -t` → `reload` → `http://<domain>`
- `sudo apt install -y certbot python3-certbot-nginx` → `ufw allow 'Nginx Full'`
- `sudo certbot --nginx -d <domain> -d www.<domain>` → `https://<domain>` 🔒

## ✓ მზადაა, როცა

`https://<domain>` და `https://www.<domain>` იხსნება ბოქლომით, `http://`-ზე ავტომატურად გადადის `https://`-ზე

## ⭐ ბონუსი

- `sudo certbot renew --dry-run` → `Congratulations, all simulated renewals succeeded`

## 💡 მინიშნება

```bash
dig +short giorgi.ge        # DNS უკვე მუშაობს?
sudo nginx -T | grep server_name   # რომელი server_name-ები ჩართულია
```

certbot ვერ ამოწმებს დომენს? — DNS ჯერ არ გავრცელდა (`dig`), ან port 80 დახურულია (`ufw status`).

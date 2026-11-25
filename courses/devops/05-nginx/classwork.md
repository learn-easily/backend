# my-portfolio — შენს სერვერზე

დავალება · Nginx + პირველი საიტი

## ნაბიჯები

- სერვერზე: `apt install nginx` → `ufw allow OpenSSH` + `ufw allow 'Nginx HTTP'` → `ufw enable` → `http://<IP>` — „Welcome to nginx!“
- `/var/www/portfolio` (თქვენი user-ის) ← WSL-იდან `rsync -avz --delete --exclude .git ./ lms:/var/www/portfolio/`
- `sites-available/portfolio` — `listen 80`, `root`, `try_files` → `ln -s` → `default`-ის წაშლა
- `nginx -t` → `reload` → `http://<IP>` — თქვენი portfolio

## ✓ მზადაა, როცა

`http://<IP>` აჩვენებს თქვენს portfolio-ს CSS-ით, `projects.html` იხსნება, `sudo tail /var/log/nginx/access.log`-ში ჩანს თქვენი მოთხოვნები

## ⭐ ბონუსი

- გვერდით მჯდომს სთხოვეთ, თქვენი IP გახსნას — `tail -f` access.log-ში იპოვეთ მისი მოთხოვნა

## 💡 მინიშნება

```bash
sudo nginx -t                    # კონფიგი სწორია?
sudo systemctl reload nginx      # ცვლილების ამოქმედება
sudo tail -n 20 /var/log/nginx/error.log   # რა გაფუჭდა?
```

`rsync`-ში ბოლოს `/` მნიშვნელოვანია: `./` — საქაღალდის **შიგთავსი**, და არა თვითონ საქაღალდე.

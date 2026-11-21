# my-portfolio — შენს სერვერზე

დავალება · Nginx + პირველი საიტი

## ნაბიჯები

- `ssh lms` → `sudo apt install -y nginx` → `sudo ufw allow 'Nginx HTTP'` → ბრაუზერში `http://<IP>` — „Welcome to nginx!“
- `sudo mkdir -p /var/www/portfolio` → `sudo chown -R $USER:$USER /var/www/portfolio`
- WSL-ში, my-portfolio-ს საქაღალდიდან: `rsync -avz --delete --exclude .git ./ lms:/var/www/portfolio/`
- `/etc/nginx/sites-available/portfolio` — server block (`listen 80`, `root /var/www/portfolio`, `try_files`)
- ჩართვა: `ln -s` → `default`-ის წაშლა `sites-enabled`-იდან → `nginx -t` → `systemctl reload nginx`
- ბრაუზერში `http://<IP>` — თქვენი portfolio

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

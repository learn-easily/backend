# საიტის საქაღალდე სერვერზე

დავალება · my-portfolio „სერვერის სტილში“

## ნაბიჯები

- `cd ~` → `git clone https://github.com/<username>/my-portfolio.git` → `cd my-portfolio` → `ls -la`
- `sudo mkdir -p /var/www/portfolio` → `sudo cp -r ~/my-portfolio/* /var/www/portfolio/`
- `ls -l /var/www/portfolio` — ვისია ფაილები? → `sudo chown -R $USER:$USER /var/www/portfolio` → ისევ `ls -l`
- `nano /var/www/portfolio/index.html` — სათაურში დაამატეთ „(Linux-იდან)“ → შენახვა `Ctrl+O`, გასვლა `Ctrl+X` → `cat`-ით შეამოწმეთ
- `sudo apt update && sudo apt install -y tree htop` → `tree /var/www`

## ✓ მზადაა, როცა

`tree /var/www` აჩვენებს `portfolio`-ს ფაილებით, `ls -l`-ში მფლობელი თქვენი user-ია, `index.html`-ში ცვლილება ჩანს

## ⭐ ბონუსი

- `htop` გახსენით → იპოვეთ პროცესი `bash` → გამოდით `q`-თი. მეორე ტერმინალში `sleep 1000` → პირველიდან იპოვეთ მისი PID `ps aux | grep sleep`-ით და `kill`-ით გააჩერეთ

## 💡 მინიშნება

```bash
pwd                 # სად ვარ?
ls -la              # რა არის აქ (ფარული ფაილებითაც)
cd ~                # სახლში დაბრუნება
```

`Tab` — სახელის ავტოშევსება. `↑` — წინა ბრძანება. დაიკარგეთ? `pwd`.

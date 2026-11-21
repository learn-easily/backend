# შენი API — პირველად სერვერზე

დავალება · runtime + ბაზა + ხელით გაშვება

## ნაბიჯები

- სერვერზე: `aspnetcore-runtime-10.0` და `postgresql` → `psql`-ში user `lms` და ბაზა `lms`
- შენთან: `dotnet publish -c Release -o ./publish` და `migrations script --idempotent -o migrate.sql`
- `rsync` → `/var/www/lms-api/`, `scp migrate.sql` → სერვერზე `psql … -f migrate.sql`
- ხელით გაშვება `ASPNETCORE_URLS` და `ConnectionStrings__Default`-ით → მეორე ფანჯრიდან `curl http://127.0.0.1:5000/api/courses`

## ✓ მზადაა, როცა

`curl` სერვერზე აბრუნებს JSON-ს (თუნდაც ცარიელ `[]`-ს), ხოლო `psql`-ში `\dt` აჩვენებს თქვენი პროექტის ცხრილებს

## ⭐ ბონუსი

- `curl`-ით POST-ით დაამატეთ კურსი → `psql`-ში `SELECT * FROM "Courses";` — ჩანაწერი ბაზაშია

## 💡 მინიშნება

```bash
cd /var/www/lms-api
ASPNETCORE_URLS=http://127.0.0.1:5000 \
ConnectionStrings__Default="Host=localhost;Database=lms;Username=lms;Password=…" \
dotnet Lms.Api.dll
```

`\` ხაზის ბოლოს — ბრძანება შემდეგ ხაზზე გრძელდება. DLL-ის სახელი = თქვენი პროექტის სახელი (`ls /var/www/lms-api/*.dll`).

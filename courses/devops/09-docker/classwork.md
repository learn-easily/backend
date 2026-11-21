# PostgreSQL — ერთი ბრძანებით

დავალება · პირველი კონტეინერები

## ნაბიჯები

- `docker --version` → `docker run hello-world`
- PostgreSQL კონტეინერი `lms-db`: user/პაროლი/ბაზა `lms`, port `5432`, volume `lms-data`
- თქვენი პროექტის `appsettings.Development.json` → `Host=localhost;...` → `dotnet ef database update` → `dotnet run` → Swagger-ით დაამატეთ ჩანაწერი
- `docker exec -it lms-db psql -U lms` → `SELECT * FROM "Courses";`

## ✓ მზადაა, როცა

`docker ps` აჩვენებს `lms-db`-ს, პროექტი ლოკალურად მუშაობს ამ ბაზასთან, ჩანაწერი ჩანს `psql`-ში

## ⭐ ბონუსი

- `docker rm -f lms-db` → იგივე `docker run` თავიდან → ჩანაწერი ისევ იქაა? ახსენით, რატომ

## 💡 მინიშნება

```bash
docker run -d --name lms-db \
  -e POSTGRES_USER=lms -e POSTGRES_PASSWORD=dev -e POSTGRES_DB=lms \
  -p 5432:5432 -v lms-data:/var/lib/postgresql/data \
  postgres:17
```

`docker logs lms-db` — თუ რამე არ მუშაობს, ჯერ ლოგი.

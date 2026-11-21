# API + ბაზა — ერთი ბრძანებით

დავალება · compose.yaml შენთან

## ნაბიჯები

- წინა ლექციის კონტეინერები: `docker rm -f lms-api lms-db`
- თქვენი პროექტის რეპოში: `compose.yaml` (`db` + `api`) და `.env` (`DB_PASSWORD`, `ASPNETCORE_ENVIRONMENT=Development`); `.env` → `.gitignore`
- `Program.cs`-ში მიგრაციები ჩართვისას (`Database.Migrate()`)
- `docker compose up -d --build` → `docker compose ps` → `http://localhost:5000/swagger`

## ✓ მზადაა, როცა

`docker compose ps` — `db` (healthy) და `api` (running), Swagger-ში ჩანაწერი ემატება, `git status` `.env`-ს არ აჩვენებს

## ⭐ ბონუსი

- `docker compose down` → `up -d` — მონაცემები დარჩა? მერე იფიქრეთ (არ გაუშვათ!): რა მოხდებოდა `down -v`-ზე?

## 💡 მინიშნება

```bash
docker compose logs -f api      # API-ს ლოგი
docker compose ps               # სტატუსები: healthy / running
docker compose down             # გაჩერება (ბაზა რჩება)
```

`api` ვარდება `Connection refused`-ით? შეამოწმეთ connection string-ში `Host=db` და `depends_on` → `service_healthy`.

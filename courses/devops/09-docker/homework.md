# LMS კონტეინერში

Dockerfile — შემდეგ ლექციაზე მას სერვერზე გავუშვებთ

## მოთხოვნები

- LMS-ის რეპოს root-ში: multi-stage `Dockerfile` (`sdk:10.0` → `aspnet:10.0`) და `.dockerignore`
- `docker build -t lms-api .` → `docker images` — რა ზომისაა?
- გაუშვით `-p 8080:8080`-ით, `ConnectionStrings__Default`-ით `lms-db`-ზე (`Host=host.docker.internal`) და `ASPNETCORE_ENVIRONMENT=Development`-ით
- `http://localhost:8080/swagger` — კურსების სია `lms-db`-დან
- commit + push: `Dockerfile` და `.dockerignore` GitHub-ზე

## ✓ მზადაა, როცა

`docker ps` აჩვენებს ორ კონტეინერს — `lms-db` და `lms-api`, Swagger კონტეინერიდან პასუხობს და ბაზის მონაცემებს აჩვენებს, Dockerfile GitHub-ზეა

## ⭐ ბონუსი

- `docker images`-ში შეადარეთ `mcr.microsoft.com/dotnet/sdk:10.0` და `lms-api`-ს ზომები — ახსენით, რატომ არის საბოლოო image ბევრად პატარა

## ამოხსნა

```dockerfile Dockerfile !
FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
WORKDIR /src
COPY Lms.Api/Lms.Api.csproj Lms.Api/
RUN dotnet restore Lms.Api/Lms.Api.csproj
COPY . .
RUN dotnet publish Lms.Api/Lms.Api.csproj -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:10.0
WORKDIR /app
COPY --from=build /app/publish .
USER $APP_UID
EXPOSE 8080
ENTRYPOINT ["dotnet", "Lms.Api.dll"]
```

```plain .dockerignore
**/bin/
**/obj/
.git/
.vs/
.vscode/
*.user
```

```console WSL
$ docker build -t lms-api .
$ docker run -d --name lms-api -p 8080:8080 \
    -e ASPNETCORE_ENVIRONMENT=Development \
    -e ConnectionStrings__Default="Host=host.docker.internal;Database=lms;Username=lms;Password=dev" \
    lms-api
$ docker logs -f lms-api
```

`Lms.Api` — პროექტის საქაღალდე და სახელი; თქვენი თუ სხვაა, შეცვალეთ.

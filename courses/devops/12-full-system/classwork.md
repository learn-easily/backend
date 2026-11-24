# ფრონტი — სისტემის ნაწილი

დავალება · web/Dockerfile + nginx.conf + Compose

## ნაბიჯები

- ფრონტი რეპოს `web/` საქაღალდეში; Angular-ში API-ის მისამართი — ფარდობითი: `/api`
- `web/Dockerfile`: `node:24-alpine` → `npm ci` → `npm run build` → `nginx:alpine` + `dist/<project>/browser`
- `web/nginx.conf`: `location /api/` → `proxy_pass http://api:8080;` და `location /` → `try_files $uri $uri/ /index.html;`
- `compose.yaml`-ში `web` სერვისი (`build: ./web`, `127.0.0.1:4000:80`); root-ის `.dockerignore`-ში `web/`
- შენთან: `docker compose up -d --build` → `http://localhost:4000`

## ✓ მზადაა, როცა

`localhost:4000`-ზე ფრონტი იხსნება, მონაცემებს API-დან იღებს, შიდა გვერდზე refresh → არა 404, ხოლო DevTools → Network-ში მოთხოვნები მიდის `localhost:4000/api/...`-ზე (CORS-ის შეცდომის გარეშე)

## ⭐ ბონუსი

- `deploy.yml`-ში მეორე `build-push-action` (`context: ./web`) და `docker compose pull api web` → PR → merge → `https://app.<domain>`

## 💡 მინიშნება

build-ის საქაღალდის სახელი ნახეთ `angular.json`-ში: `projects.<სახელი>.architect.build.options.outputPath`. თუ `COPY --from=build` ჩავარდა `not found`-ით — გზა არასწორია.

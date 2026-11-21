# ფინალური პროექტი — git push → LMS live

კურსის ყველა ლექცია ერთ გზაზე

## მოთხოვნები

- deploy გასაღები (`ssh-keygen -f ~/.ssh/github-deploy`) → `.pub` სერვერზე; Secrets: `SSH_HOST`, `SSH_USER`, `SSH_KEY`
- `deploy.yml`: push `main`-ზე → GHCR (`latest` + `sha`) → SSH → `compose pull api && up -d`
- სერვერზე: compose-ში `image: ghcr.io/<user>/<repo>:${IMAGE_TAG:-latest}`; ერთხელ `docker login ghcr.io` (PAT `read:packages`)
- README: ცოცხალი ლინკები, CI badge, deploy-ის აღწერა

## ✓ მზადაა, როცა

PR → CI ✅ → merge → Deploy ✅ → ცვლილება `https://api.<domain>`-ზე, ხელით არაფერი

## ⭐ ბონუსი

- rollback: სერვერის `.env`-ში `IMAGE_TAG=<წინა commit-ის sha>` → `docker compose up -d` → ძველი ვერსია → მერე უკან `latest`-ზე

## ამოხსნა

```yaml .github/workflows/deploy.yml !
name: Deploy
on:
  push:
    branches: [main]
permissions:
  contents: read
  packages: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/build-push-action@v6
        with:
          push: true
          tags: |
            ghcr.io/${{ github.repository }}:latest
            ghcr.io/${{ github.repository }}:${{ github.sha }}
      - uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.SSH_HOST }}
          username: ${{ secrets.SSH_USER }}
          key: ${{ secrets.SSH_KEY }}
          script: |
            cd ~/lms
            git pull
            docker compose pull api
            docker compose up -d
```

```yaml compose.yaml — api
  api:
    build: .
    image: ghcr.io/giorgi/lms:${IMAGE_TAG:-latest}
```

```console lms-server
$ echo "<PAT>" | docker login ghcr.io -u giorgi --password-stdin
Login Succeeded
```

GHCR-ის image-ის სახელი **პატარა ასოებით** უნდა იყოს — თუ რეპოს სახელში დიდი ასოებია (`Giorgi/LMS`), გადაარქვით რეპოს სახელი პატარა ასოებით.

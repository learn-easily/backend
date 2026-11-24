# CD — პირველი ავტომატური deploy

დავალება · deploy გასაღები + Secrets + deploy.yml

## ნაბიჯები

- WSL: `ssh-keygen -t ed25519 -f ~/.ssh/github-deploy -N ""` → `ssh-copy-id -i ~/.ssh/github-deploy.pub lms` → შეამოწმეთ `ssh -i ~/.ssh/github-deploy …`
- GitHub → **Settings → Secrets and variables → Actions**: `SSH_HOST`, `SSH_USER`, `SSH_KEY`
- `compose.yaml`-ში `api`-ს: `image: ghcr.io/<user>/<repo>:${IMAGE_TAG:-latest}`; სერვერზე ერთხელ `docker login ghcr.io` (PAT `read:packages`)
- branch `feature/deploy` → `.github/workflows/deploy.yml` → PR → CI ✅ → merge
- Actions-ში **Deploy** ✅ → API-ში პატარა ცვლილება (მაგ. ახალი ველი პასუხში) → PR → merge → ცვლილება `https://api.<domain>`-ზე

## ✓ მზადაა, როცა

merge-ის შემდეგ ცვლილება სერვერზე ჩანს და სერვერზე ხელით არაფერი გაგიშვიათ; GHCR-ში (რეპოს გვერდი → **Packages**) ჩანს image `latest` და `sha` tag-ებით

## ⭐ ბონუსი

- ბოლო ნაბიჯად დაამატეთ შემოწმება: `curl -f https://api.<domain>/api/courses` — თუ API არ პასუხობს, Deploy წითელი გახდება

## 💡 მინიშნება

`SSH_KEY`-ში ჩასვით **პირადი** გასაღების მთელი ფაილი (`cat ~/.ssh/github-deploy`), `-----BEGIN`-იდან `-----END`-ის ჩათვლით. `build-push` ჩავარდა `repository name must be lowercase`-ით? — რეპოს სახელი პატარა ასოებით გადაარქვით.

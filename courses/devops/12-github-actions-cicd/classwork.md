# CI — ყოველ Pull Request-ზე

დავალება · ci.yml + branch protection

## ნაბიჯები

- LMS-ში `.github/workflows/ci.yml`: `on: pull_request` → checkout → setup-dotnet `10.0.x` → `restore` → `build`
- GitHub → **Settings → Rules → Rulesets** (`main`): Require a pull request · Require status checks → `build`
- branch `feature/ci-test` → კოდში განზრახ შეცდომა → PR → ❌ → გაასწორეთ → push → ✅ → merge

## ✓ მზადაა, როცა

Actions-ში ჩანს ერთი წითელი და ერთი მწვანე გაშვება, წითელ PR-ზე Merge ღილაკი დაბლოკილია, `main`-ში პირდაპირ push უარყოფილია

## ⭐ ბონუსი

- README-ში CI-ის badge: Actions → CI → ⋯ → **Create status badge** → ჩასვით README-ში

## 💡 მინიშნება

```yaml
on:
  pull_request:
    branches: [main]
```

ფაილი ზუსტად `.github/workflows/` საქაღალდეში უნდა იყოს. YAML-ში — მხოლოდ space-ები, არა Tab.

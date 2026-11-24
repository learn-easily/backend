# CI — ყოველ Pull Request-ზე

დავალება · ტესტი + ci.yml + branch protection

## ნაბიჯები

- `Lms.Tests` (xUnit) პროექტი solution-ში და ერთი ტესტი თქვენი პროექტის ნებისმიერ მეთოდზე → `dotnet test` შენთან მწვანეა
- `.github/workflows/ci.yml`: `on: pull_request` → checkout → setup-dotnet `10.0.x` → `restore` → `build` → `test`
- branch `feature/ci` → push → PR → CI ✅
- **Settings → Rules → Rulesets** (`main`): Require a pull request · Require status checks → `build`
- branch `feature/ci-break` → ტესტი განზრახ გატეხეთ → PR → ❌ → ლოგში იპოვეთ, რა ჩავარდა → გაასწორეთ → push → ✅ → merge

## ✓ მზადაა, როცა

Actions-ში ჩანს ერთი წითელი და ერთი მწვანე გაშვება, წითელ PR-ზე Merge ღილაკი დაბლოკილი იყო, `main`-ში პირდაპირ push უარყოფილია

## ⭐ ბონუსი

- README-ში CI-ის badge: Actions → CI → ⋯ → **Create status badge** → ჩასვით README-ში

## 💡 მინიშნება

```yaml
on:
  pull_request:
    branches: [main]
```

ფაილი ზუსტად `.github/workflows/` საქაღალდეში უნდა იყოს. YAML-ში — მხოლოდ space-ები, არა Tab. `build` Rulesets-ის სიაში მხოლოდ მაშინ ჩნდება, როცა CI ერთხელ მაინც გაეშვა.

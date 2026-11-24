# ტესტები და CI badge

LMS-ის რეპო მზადაა CD-სთვის — შემდეგ ლექციაზე merge-ის შემდეგ deploy თვითონ მოხდება

## მოთხოვნები

- კიდევ 2 ტესტი თქვენი პროექტის მეთოდებზე — თითოეული **ცალკე PR**-ით, CI ✅-ით
- README-ში CI badge — ის `main`-ის სტატუსს აჩვენებს
- `ci.yml`-ში დაამატეთ `workflow_dispatch` — CI Actions-იდან ხელითაც ეშვებოდეს

## ✓ მზადაა, როცა

`main`-ში ორი ახალი merge-ი PR-ებით, ორივეზე CI მწვანეა, README-ში badge მწვანეა

## ⭐ ბონუსი

- ერთ-ერთი ტესტი `[Theory]` + `[InlineData]`-ით — ერთი ტესტი რამდენიმე მონაცემზე

## ამოხსნა

```yaml .github/workflows/ci.yml !
name: CI

on:
  pull_request:
    branches: [main]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
        with:
          dotnet-version: '10.0.x'
      - run: dotnet restore
      - run: dotnet build --no-restore -c Release
      - run: dotnet test --no-build -c Release
```

```markdown README.md
![CI](https://github.com/giorgi/lms/actions/workflows/ci.yml/badge.svg)
```

```csharp Lms.Tests/CourseTests.cs
[Theory]
[InlineData(1, 1, false)]
[InlineData(2, 1, true)]
public void Enroll_DependsOnCapacity(int capacity, int alreadyEnrolled, bool expected)
{
    var course = new Course { Title = "DevOps", Capacity = capacity };
    for (var i = 0; i < alreadyEnrolled; i++)
        course.Enroll(Guid.NewGuid());

    Assert.Equal(expected, course.Enroll(Guid.NewGuid()));
}
```

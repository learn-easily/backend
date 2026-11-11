# ProductsApi — კიდევ ორი endpoint

დავალება · თქვენი ProductsApi

## ნაბიჯები

- ProductsApi შექმენით და გაუშვით, როგორც ლექციაზე (.NET 10, „Use controllers“ მოხსნილი)
- სიას დაამატეთ კიდევ 2 პროდუქტი
- `GET /api/products/count` — რამდენი პროდუქტია
- `GET /api/products/expensive` — მხოლოდ ის, რომელთა ფასი 100-ზე მეტია (LINQ `Where`)
- ყველა endpoint შეამოწმეთ `.http` ფაილით **და** ბრაუზერით

## ✓ მზადაა, როცა

`.http` ფაილიდან სამივე მოთხოვნა 200-ს აბრუნებს, და ბრაუზერშიც იგივე JSON ჩანს

## ⭐ ბონუსი

- `GET /api/products/cheapest` — ყველაზე იაფი პროდუქტი (`OrderBy` + `First`)
- `GET /api/products/total` — ყველა პროდუქტის ფასების ჯამი

## 💡 მინიშნება

```csharp
app.MapGet("/api/products/count", () => products.Count);
```

ახალი endpoint `app.Run()`-ის **ზემოთ** უნდა დაწეროთ — მის ქვემოთ დაწერილი კოდი აღარ შესრულდება.

# კატეგორიები და REST ცხრილი

ProductsApi + ერთი თეორიული ცხრილი

## მოთხოვნები

- `record Category(int Id, string Name)` და სია 3-4 კატეგორიით
- `GET /api/categories` — კატეგორიების სია
- შეამოწმეთ `.http` ფაილით: 200 და JSON
- ცხრილი (რვეულში ან ფაილში): Category-ს 5 REST endpoint — მეთოდი, მისამართი, წარმატების სტატუს კოდი

## ✓ მზადაა, როცა

`.http` ფაილიდან `GET /api/categories` 200-ს აბრუნებს, და ცხრილში ხუთივე ხაზი წერია

## ⭐ ბონუსი

- `GET /api/categories/count` — კატეგორიების რაოდენობა

## ამოხსნა

```csharp Program.cs !
var categories = new List<Category>
{
    new(1, "ლეპტოპები"),
    new(2, "აქსესუარები"),
    new(3, "მონიტორები"),
};

app.MapGet("/api/categories", () => categories);
app.MapGet("/api/categories/count", () => categories.Count);

app.Run();

record Category(int Id, string Name);
```

```http ProductsApi.http
GET https://localhost:7001/api/categories
```

REST ცხრილი:

| მეთოდი | მისამართი | რას აკეთებს | წარმატებისას |
|---|---|---|---|
| GET | `/api/categories` | სია | 200 |
| GET | `/api/categories/3` | ერთი | 200 (ან 404) |
| POST | `/api/categories` | შექმნა | 201 |
| PUT | `/api/categories/3` | მთლიანად შეცვლა | 204 |
| DELETE | `/api/categories/3` | წაშლა | 204 (ან 404) |

```note
`record Category` ფაილის **ბოლოში** უნდა იყოს, `app.Run()`-ის შემდეგ — Program.cs-ში ტიპების გამოცხადება ზედა დონის კოდის შემდეგ იწერება. პორტი (`7001`) თქვენთან სხვა იქნება.
```

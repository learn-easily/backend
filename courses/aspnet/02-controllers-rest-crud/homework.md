# LibraryApi — BooksController სრულად

ლექციაზე დაწყებული LibraryApi დაასრულეთ: ხუთივე endpoint და ორივე ბონუსი.

## მოთხოვნები

- `Book`: `Id`, `Title`, `Author`, `Year`, `Price`
- `BooksController` — `static` სია 3 წიგნით, 5 endpoint
- სწორი სტატუს კოდები: 200 · 201 · 204 · 404
- POST-ში ცარიელი `Title` → `BadRequest()` (400)
- `GET /api/books/cheap` — წიგნები, რომელთა ფასი 20-ზე ნაკლებია

## ✓ მზადაა, როცა

Swagger-ში Books ჯგუფი ჩანს და ყველა endpoint, ორივე ბონუსის ჩათვლით, გატესტილია.

## ამოხსნა

ორი ბონუსი — ყველაზე საინტერესო ნაწილი. დანარჩენი ზუსტად ProductsController-ის მსგავსია.

```csharp Controllers/BooksController.cs
[HttpGet("cheap")]
public IActionResult GetCheap()
{
    var cheap = _books.Where(b => b.Price < 20).ToList();
    return Ok(cheap);
}

[HttpPost]
public IActionResult Create(Book book)
{
    if (string.IsNullOrWhiteSpace(book.Title))
        return BadRequest();

    book.Id = _nextId++;
    _books.Add(book);
    return CreatedAtAction(nameof(GetById), new { id = book.Id }, book);
}
```

```note
`[HttpGet("cheap")]` მუშაობს `[HttpGet("{id}")]`-თან ერთად, რადგან `cheap` რიცხვი არ არის: ASP.NET Core ჯერ ზუსტ მისამართს ეძებს. `GetCheap` კლასში სადაც გინდა, იქ შეიძლება იდგეს.
```

`string.IsNullOrWhiteSpace` ცარიელ ტექსტსაც იჭერს და მხოლოდ სივრცეებისგან შედგენილსაც (`"   "`). უბრალო `book.Title == ""` მეორე შემთხვევას გამოტოვებდა.

```note
თუ ცარიელი `title` გააგზავნეთ და პასუხად 400 მიიღეთ ტექსტით „The Title field is required“, ჯერ თქვენი `if`-მდეც არ მისულა. `[ApiController]` `string Title`-ს სავალდებულოდ თვლის და ცარიელ მნიშვნელობას თვითონ უარყოფს. ჩვენი `if` ამ წესს კოდში ცხადად აჩვენებს და იმუშავებს მაშინაც, თუ ეს ავტომატური შემოწმება გამორთულია.
```

# Entity Framework Core

**ტექნოლოგიები:** .NET 10, EF Core 10, PostgreSQL (Npgsql), კონსოლის აპი

**პროექტი:** **Shop** — C#-ის კურსის კონსოლის მაღაზია უერთდება SQL-ის კურსზე დაპროექტებულ ბაზას. კოდი ისევ კონსოლშია (Services საქაღალდე + მენიუ `Program.cs`-ში), რომ ყურადღება EF Core-ზე იყოს და არა API-ზე. სტუდენტი იმავეს სახლში **თავის საფინალო პროექტზე** იმეორებს (C#-ის კურსზე არჩეული სფერო). API-ის კურსში ეს ცოდნა ShopApi-ში და LMS-ში გადადის.

| დანიშნულება | Package |
| --- | --- |
| ბაზა | `Npgsql.EntityFrameworkCore.PostgreSQL` |
| მიგრაციები | `Microsoft.EntityFrameworkCore.Design`, `Microsoft.EntityFrameworkCore.Tools` |

---

## საფუძვლები (3 ლექცია)

### 01. EF Core კონსოლში — ORM, DataContext, მიგრაცია

**პრობლემა:** C#-ის ობიექტები და ბაზის ცხრილები ცალ-ცალკე ცხოვრობს — SQL-ის ხელით წერა და შედეგის ობიექტებად გადაკეთება დიდი და შეცდომიანი სამუშაოა. **თემები:** რა არის ORM და EF Core; package-ები; `DataContext` და `DbSet<T>`; connection string; პირველი entity; პირველი მიგრაცია და `update-database`; პირველი ჩაწერა და წაკითხვა.

📚 აუხსნის, რა პრობლემას აგვარებს ORM
📚 დააყენებს EF Core-ს PostgreSQL-ისთვის და შექმნის `DataContext`-ს
📚 შექმნის ბაზას მიგრაციით და ჩაწერს / წაიკითხავს მონაცემს
🛠 Shop | `DataContext` · `Product` entity · პირველი მიგრაცია

### 02. CRUD, სერვისი და კონსოლის მენიუ

**თემები:** `Add`, `Find`, `Where`, `Update`, `Remove`, `SaveChangesAsync`; async მეთოდები (`ToListAsync`, `FirstOrDefaultAsync`); სერვისის კლასი; მენიუ `Program.cs`-ში.

📚 დაწერს სრულ CRUD-ს EF Core-ით
📚 გამოიყენებს async მეთოდებს ბაზასთან
📚 დაყოფს კოდს სერვისებად
🛠 Shop | `ProductService` — დამატება, სია, ძებნა, რედაქტირება, წაშლა · მენიუ

### 03. მიგრაციები სიღრმეში

**პრობლემა:** მოდელი იცვლება — ახალი სვეტი, ახალი ცხრილი — ბაზაში კი უკვე მონაცემია. **თემები:** მიგრაციის ფაილი შიგნიდან; `add-migration`, `update-database`, `remove-migration`; უკან დაბრუნება; seed მონაცემი (`HasData`); მიგრაცია, რომელიც მონაცემს კარგავს.

📚 შეცვლის მოდელს და გადაიტანს ცვლილებას ბაზაში უსაფრთხოდ
📚 დააბრუნებს მიგრაციას უკან
📚 ჩაწერს საწყის მონაცემს seed-ით
🛠 Shop | `Category` ცხრილი · `Product.Stock` სვეტი · კატეგორიების seed

## ურთიერთობები (2 ლექცია)

### 04. ურთიერთობები I: 1–N და 1–1

**თემები:** navigation property და FK property; კონვენციები; 1–N (`Category` → `Products`), 1–1 (`Customer` → `Address`); `Include`; required და optional კავშირი; წაშლის ქცევა.

📚 ააწყობს 1–N და 1–1 კავშირს
📚 ჩატვირთავს დაკავშირებულ მონაცემს `Include`-ით
🛠 Shop | `Category` ↔ `Products` · `Customer` ↔ `User` (1–1 — ავტორიზაცია C#-იდან, ახლა ბაზაში) · `Customer` ↔ `Address` · `Customer` → `Orders`

### 05. ურთიერთობები II: N–N და კონფიგურაცია

**თემები:** N–N — ავტომატური და საკუთარი შუალედური entity (`OrderItem` თავისი ფასით და რაოდენობით); კონფიგურაცია attribute-ებით vs Fluent API (`OnModelCreating`, `IEntityTypeConfiguration`); ინდექსი, unique (`User.Email`), max length, precision; enum ბაზაში — `HasConversion<string>()` (`Role`, `OrderStatus`).

📚 ააწყობს N–N კავშირს შუალედური entity-ით
📚 გაარჩევს attribute-ებს და Fluent API-ს და შეარჩევს სწორს
🛠 Shop | `Order` ↔ `Product` `OrderItem`-ით · `ProductConfiguration` · `Review`

## მოთხოვნები და მონაცემის მართვა (2 ლექცია)

### 06. Querying — LINQ-დან SQL-მდე

**პრობლემა:** კოდი მუშაობს, მაგრამ ბაზას 101 მოთხოვნას უგზავნის. **თემები:** როგორ ითარგმნება LINQ SQL-ად (`ToQueryString`, logging); `Include` / `ThenInclude`; projection `Select`-ით; `AsNoTracking`; eager / explicit / lazy loading; N+1 პრობლემა; `GroupBy` და აგრეგაცია ბაზაში.

📚 დაინახავს, რა SQL იგზავნება ბაზაში
📚 აირიდებს N+1-ს და ზედმეტ მონაცემს projection-ით
🛠 Shop | შეკვეთის დეტალები ერთი მოთხოვნით · ანგარიშები: შემოსავალი კატეგორიით, ტოპ პროდუქტები

### 07. Change Tracking და ტრანზაქციები

**პრობლემა:** შეკვეთა შეინახა, მარაგი კი არ შემცირდა — ან პირიქით. **თემები:** entity-ის მდგომარეობები (`Added`, `Modified`, `Deleted`, `Unchanged`); როგორ პოულობს EF ცვლილებას; ერთი `SaveChanges` = ერთი ტრანზაქცია; ცხადი ტრანზაქცია (`BeginTransactionAsync`).

📚 აუხსნის, როგორ ადევნებს EF თვალს ცვლილებებს
📚 შეასრულებს რამდენიმე ცვლილებას ერთ ტრანზაქციაში
🛠 Shop | `OrderService.PlaceOrder` — შეკვეთა + მარაგი + კალათის გასუფთავება ერთად

## Code First vs Database First (2 ლექცია)

### 08. Code First vs Database First

**პრობლემა:** სამსახურში ბაზა ხშირად უკვე არსებობს და მას სხვა მართავს. **თემები:** ორი მიდგომა და როდის რომელი; `Scaffold-DbContext`; რას ქმნის scaffold და რა არის მისი შეზღუდვები.

📚 გაარჩევს Code First-ს და Database First-ს
📚 შექმნის მოდელს არსებული ბაზიდან scaffold-ით

### 09. Database First პრაქტიკაში

**თემები:** სხვისი ბაზა — სახელები, კავშირები, view-ები; partial კლასები; ბაზის ცვლილების შემდეგ ხელახალი scaffold.

📚 იმუშავებს არსებულ ბაზასთან ისე, რომ ხელით დაწერილი კოდი არ დაიკარგოს

## შეჯამება (1 ლექცია)

### 10. Performance და შეჯამება

**თემები:** pagination (`Skip` / `Take`); raw SQL (`FromSql`, `SqlQuery`); `ExecuteUpdateAsync` / `ExecuteDeleteAsync`; split query; ტიპური შეცდომები; Shop-ისა და სტუდენტების პროექტების განხილვა.

📚 გამოიყენებს pagination-ს და bulk ოპერაციებს
📚 დაწერს raw SQL-ს იქ, სადაც LINQ არ კმარა
🛠 Shop | პროდუქტების გვერდები · ფასდაკლება მთელ კატეგორიაზე `ExecuteUpdateAsync`-ით

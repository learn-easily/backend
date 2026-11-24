# ASP.NET Core Web API

**ტექნოლოგიები:** .NET 10, ASP.NET Core Web API (Controllers → Minimal API), EF Core 10, SQL Server (DevOps-ის Docker-ის ლექციის შემდეგ PostgreSQL), Scalar / OpenAPI, Angular, Claude Code

**პროექტი:** 01–05 — ShopApi (კლასში) და LibraryApi (სტუდენტები). 06-დან — **LMS** (კურსები, ჯგუფები, სტუდენტები, ლექტორები, ლექციები, დასწრება, დავალებები, ქულები), რომელსაც ლექტორი კლასში აწყობს; სტუდენტი იმავე თემებს სახლში თავის არჩეულ სფეროში წერს. ბოლოს LMS-ს Angular-ის frontend ემატება და DevOps-ის კურსში სრული აპლიკაცია სერვერზე იშვება.

| დანიშნულება | Package |
| --- | --- |
| ბაზა | `Microsoft.EntityFrameworkCore.SqlServer`, `Microsoft.EntityFrameworkCore.Tools` |
| Mapping | `Riok.Mapperly` |
| API დოკუმენტაცია | `Microsoft.AspNetCore.OpenApi`, `Scalar.AspNetCore` |
| ვალიდაცია | `FluentValidation` |
| Mediator (pipeline behaviors) | `MediatR` 12.x — ბოლო უფასო (MIT) ვერსია |
| პაროლის hash | `Konscious.Security.Cryptography.Argon2` |
| JWT | `Microsoft.AspNetCore.Authentication.JwtBearer` |

---

## API-ის საფუძვლები (5 ლექცია)

### 01. Backend, API, REST და პირველი Web API

რა არის Backend და რატომ არსებობს; API და REST, HTTP მეთოდები და სტატუს კოდები; როგორ ელაპარაკება frontend სერვერს; .NET-ის პროექტის ტიპები API-სთვის; პირველი ASP.NET Core Web API პროექტი Visual Studio-ში და პირველი endpoint.

### 02. Minimal API vs Controller, REST, CRUD და Swagger

API-ის აწყობის ორი გზა და მათი შედარება; Controller-ები და routing; REST-ის წესები პრაქტიკაში; `IActionResult` და სწორი სტატუს კოდები; Swagger; პროდუქტების სრული CRUD.

### 03. DTO და Mapping

რატომ არ ვაბრუნებთ entity-ს პირდაპირ; Request და Response DTO-ები; ხელით დაწერილი Mapper; mapping-ის package.

### 04. Dependency Injection და DbContext

API-ს ნამდვილ ბაზას ვუერთებთ (EF Core); IoC და DI Container; რეგისტრაცია და lifetime-ები: Singleton, Scoped, Transient; DataContext Controller-ში.

### 05. Async / Await API-ში

რატომ „იჭედება“ სერვერი სინქრონულ კოდზე; Thread pool; async/await EF Core-ის მეთოდებით (`ToListAsync`, `SaveChangesAsync`); async endpoint-ები.

## DDD და LMS-ის დასაწყისი (4 ლექცია)

### 06. DDD: ბიზნესის ენიდან კოდამდე

რა არის Domain-Driven Design; როგორ ვესაუბრებით ბიზნესს; ubiquitous language; როგორ ვგეგმავთ პროექტს და როგორ აისახება ეს კოდში.

### 07. LMS-ის აღმოჩენა: ენა, აქტორები, პროცესები, წესები

DDD LMS-ზე: ლექსიკონი, აქტორები, პროცესები, ბიზნესის წესები (R1–R8) → დომენის რუკა და backlog; სტუდენტი ირჩევს საკუთარ სფეროს საშინაოებისთვის.

### 08. LMS: პროექტის აწყობა და პირველი feature

LMS-ის პროექტი; story №1 „მენეჯერი ქმნის კურსს“ ნაცნობი გზით (Controller, DataContext, DTO, Mapper, async); R1 და R2; რა გვტკივა ამ მიდგომაში.

### 09. არქიტექტურა: Layers vs Vertical Slices

Layers და Vertical Slice Architecture; SRP და DIP; slice: Request · Handler · Endpoint; Controller-ები → Minimal API (`MapGroup`); Swagger → Scalar.

## დომენის მოდელი (2 ლექცია)

### 10. Rich Entity, Value Object და Result

**პრობლემა:** ერთი წესი Create-შიც და Update-შიც მეორდება, Email ოთხ ადგილას სუფთავდება, `course.DurationWeeks = -5` კი კომპილირდება. **თემები:** ანემიური vs rich entity (private set, private constructor, `Create` / `Update`); Result pattern (`Result`, `Result<T>`, `Error`: Code + Message) — მოსალოდნელი შეცდომა exception-ის გარეშე; რომელი წესი entity-ში და რომელი handler-ში (ბაზის საჭიროება: R1, R2); Value Object `Email` (`sealed record`, EF Core `HasConversion`). **LMS:** Course, Student, Lecturer → rich · ახალი entity Group (≤ 20 ადგილი, წარსულში ვერ დაიწყება): Create, GetById.

### 11. Aggregate და Concurrency

**პრობლემა:** R3 მთელ ჯგუფს ეხება; handler-ში დაწერილ შემოწმებას სხვა slice გვერდს აუვლის, ორი ერთდროული მოთხოვნა კი 20-ადგილიან ჯგუფში 21-ე სტუდენტს რიცხავს. **თემები:** Aggregate და Aggregate Root (`Group` → `Enrollment`), ცვლილება მხოლოდ root-ით, `DbSet` შვილზე არ არის; 400 vs 409; Cascade aggregate-ის შიგნით, Restrict გარეთ (ჯგუფიანი კურსის წაშლა → 409); დავიწყებული `Include` და Repository pattern DDD-ში — რას ხსნის, როდის ღირს (კოდში 15-ში); race condition (ცოცხალი ცდა); pessimistic vs optimistic; `rowversion` + `DbUpdateConcurrencyException` → 409; unique index. **LMS:** ჩარიცხვა ჯგუფში (R3).

## პასუხები, შეცდომები და pipeline (3 ლექცია)

### 12. Middleware, Pipeline და Logging

**პრობლემა:** „ხანდახან ნელა მუშაობს“ — რომელი endpoint? `Stopwatch` ყველა handler-ში 20 ასლია: რაც ყველა მოთხოვნას ეხება, handler-ის საქმე არ არის. **თემები:** მოთხოვნის გზა — middleware-ების ჯაჭვი და პასუხი უკან; `Program.cs`-ის `Use…` ხაზები middleware-ებია; `app.Use(…, next)`: წინ / შემდეგ; რიგი მნიშვნელოვანია; short-circuit (ტექნიკური სამუშაოები → 503); საკუთარი middleware class-ად (`RequestDelegate`, `InvokeAsync`, `UseMiddleware`); DI ხაფანგი: Scoped სერვისი `InvokeAsync`-ში, არა constructor-ში; `ILogger<T>`, დონეები, ფილტრი `appsettings`-ში; structured logging (message template vs interpolation, JSON console). **LMS:** მოთხოვნის დროის middleware · ლოგები ჩარიცხვის handler-ში.

### 13. შეცდომები და პასუხები: ერთი ფორმა ყველგან

**პრობლემა:** ყოველი handler თვითონ წყვეტს სტატუსს და შეცდომის ფორმას; exception → stack trace, არარსებული მისამართი → ცარიელი 404 — frontend-ს ხუთი სხვადასხვა ფორმის გარჩევა უწევს. **თემები:** ProblemDetails (RFC 9457) — ერთი ფორმა ყველა შეცდომაზე, წყაროს მიუხედავად; `ErrorType` (Validation, NotFound, Conflict…) → სტატუსი ერთ ადგილას; `ResultExtensions`: `ToOk()`, `ToCreated(uri)`, `ToNoContent()`, შეცდომა → ProblemDetails; `AddProblemDetails`, `IExceptionHandler` + `UseExceptionHandler` (500 დეტალების გარეშე production-ში, ლოგი), `UseStatusCodePages` (404/405); concurrency ერთ ადგილას. **LMS:** ყველა handler ResultExtensions-ზე · try/catch handler-ებში აღარ არის.

### 14. ვალიდაცია და MediatR

**პრობლემა:** ვალიდაცია (ცარიელი ველები, ფორმატი, სიგრძე) entity-მდე უნდა მოხდეს და ყველა ველის შეცდომა ერთად უნდა დაბრუნდეს; validator-ის ხელით გამოძახება ყველა handler-ში მეორდება. **თემები:** FluentValidation (წესები, შეცდომები ველების მიხედვით → ValidationProblem); MediatR 12.x: `IRequest`, `IRequestHandler`, `ISender` — slice-ები MediatR-ზე; pipeline behavior: `ValidationBehavior` და `LoggingBehavior` ერთ ადგილას; middleware vs pipeline behavior: რომელი რისთვის. **LMS:** validator-ები ყველა Create/Update-ზე · ყველა slice MediatR-ზე.

## LMS-ის დასრულება (5 ლექცია)

### 15. განრიგი და დასწრება + Claude Code

**პრობლემა:** ჯგუფის aggregate იზრდება (ლექციები, დასწრება) და მას ბევრი handler ტვირთავს — ყველგან სწორი `Include` სჭირდება; feature-ები მეორდება ნაცნობი pattern-ით. **თემები:** `IGroupRepository` ხელით (`GetAsync`, `Add`), Enroll მასზე; R4 (ლექციები დროში არ ფარავს ერთმანეთს — ჯგუფის წესი; ლექტორი ერთ დროს ერთ ლექციაზე — handler-ის წესი); R6 (15 წთ-ზე მეტი დაგვიანება = გაცდენა); Claude Code: `CLAUDE.md` (VSA, MediatR, Result, aggregate მხოლოდ Repository-ით), პირველი slice ხელით → დანარჩენს AI წერს → review; სია pagination-ით (Skip/Take, `PagedResponse`). **LMS:** განრიგი და დასწრება.

### 16. Authentication და Configuration

**პრობლემა:** API ყველასთვის ღიაა; JWT-ს გასაღები და ვადა კოდში არ უნდა ეწეროს. **თემები:** `appsettings` და environment-ები; Options pattern (`JwtOptions`, `ValidateOnStart`); User Secrets; ანგარიშები და პაროლის hash Argon2id-ით; login → JWT გაცემა; JWT შემოწმება (`AddJwtBearer`), claims, `RequireAuthorization`; 401 ProblemDetails-ით. **LMS:** ანგარიშები სამ როლზე (მენეჯერი, ლექტორი, სტუდენტი), login.

### 17. Authorization

**პრობლემა:** შესული მომხმარებელი ყველაფერს ვერ უნდა აკეთებდეს; ლექტორის როლი საკმარისი არ არის — ჯგუფი მისი უნდა იყოს. **თემები:** როლები და policy-ები; resource-based authorization: R5 („დასწრებას აღრიცხავს და აფასებს მხოლოდ ამ ჯგუფის ლექტორი“); მიმდინარე მომხმარებელი handler-ში (claims); 403 ProblemDetails-ით. **LMS:** policy-ები ყველა endpoint-ზე · R5 დასწრებაზე.

### 18. ფაილები, დრო და შეფასება

**პრობლემა:** სტუდენტი ნამუშევარს ფაილად აბარებს; დედლაინის წესი დროზეა დამოკიდებული და `DateTime.UtcNow`-ით შეუმოწმებელია. **თემები:** დავალებები; ფაილის ატვირთვა (`IFormFile`, ზომა და ტიპი, შენახვა) და ჩამოტვირთვა; `TimeProvider` (`DateTime.UtcNow`-ის ნაცვლად); R7 (დედლაინის შემდეგ არ მიიღება, მენეჯერს გადაწევა შეუძლია; ქულა 1–12 — Value Object). **LMS:** დავალებები, ნამუშევრის ატვირთვა, შეფასება.

### 19. Background Jobs და კურსის დასრულება

**პრობლემა:** ზოგი საქმე მოთხოვნის გარეშე უნდა მოხდეს: დედლაინის შეხსენება, ლექტორის გაფრთხილება მე-4 გაცდენაზე. **თემები:** `BackgroundService` და `PeriodicTimer`; Scoped სერვისი background-ში (`IServiceScopeFactory`); შეტყობინებები აპლიკაციის შიგნით (ბაზაში); R6-ის მეორე ნაწილი; R8 (კურსი ჩაბარებულია: საშუალო ≥ 6 და დასწრება ≥ 75%). **LMS:** შეტყობინებები, კურსის დასრულება — **Backend დასრულებულია**.

## Angular Claude Code-ით (2 ლექცია)

### 20. Angular + Claude Code #1: როგორ ვმუშაობთ AI-სთან

**თემები:** როგორ ვგეგმავთ AI-სთან: `CLAUDE.md`, plan mode, OpenAPI დოკუმენტი როგორც კონტექსტი; CORS; Angular-ის სტრუქტურა; login, layout, JWT interceptor, ProblemDetails-ის ჩვენება; კურსები და ჯგუფები. სტუდენტები კოდს კითხულობენ, ლექტორი გეგმავს და review-ს აკეთებს.

### 21. Angular + Claude Code #2

**თემები:** განრიგი, დასწრება, ნამუშევრის ატვირთვა, ქულები; ბოლო review და შესწორებები. **Frontend დასრულებულია** — სრული აპლიკაცია DevOps-ის კურსში იშვება სერვერზე.

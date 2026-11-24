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

📚 რა არის Backend და რატომ არსებობს · API, REST, HTTP მეთოდები და სტატუს კოდები · როგორ ელაპარაკება საიტი სერვერს
🛠 ShopApi | პირველი Web API პროექტი · პირველი endpoint

### 02. Minimal API vs Controller, REST, CRUD და Swagger

API-ის აწყობის ორი გზა და მათი შედარება; Controller-ები და routing; REST-ის წესები პრაქტიკაში; `IActionResult` და სწორი სტატუს კოდები; Swagger; პროდუქტების სრული CRUD.

📚 Minimal API vs Controller · REST-ის წესები, `IActionResult` · Swagger
🛠 ShopApi | პროდუქტების სრული CRUD

### 03. DTO და Mapping

რატომ არ ვაბრუნებთ entity-ს პირდაპირ; Request და Response DTO-ები; ხელით დაწერილი Mapper; mapping-ის package.

📚 რატომ არ ვაბრუნებთ entity-ს · Request / Response DTO · Mapping: ხელით და Mapperly
🛠 ShopApi | პროდუქტის DTO-ები და Mapper

### 04. Dependency Injection და DbContext

API-ს ნამდვილ ბაზას ვუერთებთ (EF Core); IoC და DI Container; რეგისტრაცია და lifetime-ები: Singleton, Scoped, Transient; DataContext Controller-ში.

📚 Dependency Injection და DI Container · Singleton, Scoped, Transient
🛠 ShopApi | ნამდვილი ბაზა: EF Core, `DataContext`

### 05. Async / Await API-ში

რატომ „იჭედება“ სერვერი სინქრონულ კოდზე; Thread pool; async/await EF Core-ის მეთოდებით (`ToListAsync`, `SaveChangesAsync`); async endpoint-ები.

📚 რატომ „იჭედება“ სინქრონული სერვერი · async / await EF Core-ში
🛠 ShopApi | ყველა endpoint async-ად

## DDD და LMS-ის დასაწყისი (4 ლექცია)

### 06. DDD: ბიზნესის ენიდან კოდამდე

რა არის Domain-Driven Design; როგორ ვესაუბრებით ბიზნესს; ubiquitous language; როგორ ვგეგმავთ პროექტს და როგორ აისახება ეს კოდში.

📚 რა არის DDD · როგორ ვესაუბრებით ბიზნესს · საერთო ენა (ubiquitous language)
🛠 კოდი ჯერ არა — LMS-ის ხედვა და ლექსიკონი

### 07. LMS-ის აღმოჩენა: ენა, აქტორები, პროცესები, წესები

DDD LMS-ზე: ლექსიკონი, აქტორები, პროცესები, ბიზნესის წესები (R1–R8) → დომენის რუკა და backlog; სტუდენტი ირჩევს საკუთარ სფეროს საშინაოებისთვის.

📚 აქტორები, პროცესები, ბიზნესის წესები · დომენის რუკა და backlog
🛠 წესები R1–R8 და backlog · სტუდენტი ირჩევს თავის სფეროს

### 08. LMS: პროექტის აწყობა და პირველი feature

LMS-ის პროექტი; story №1 „მენეჯერი ქმნის კურსს“ ნაცნობი გზით (Controller, DataContext, DTO, Mapper, async); R1 და R2; რა გვტკივა ამ მიდგომაში.

📚 story-დან კოდამდე ნაცნობი გზით · სახელები ლექსიკონიდან, შემოწმებები წესებიდან
🛠 პროექტი · კურსები (R1), სტუდენტები და ლექტორები (R2) — CRUD

### 09. არქიტექტურა: Layers vs Vertical Slices

Layers და Vertical Slice Architecture; SRP და DIP; slice: Request · Handler · Endpoint; Controller-ები → Minimal API (`MapGroup`); Swagger → Scalar.

📚 Layers vs Vertical Slices · SRP და DIP · Minimal API, Scalar
🛠 ყველა feature slice-ებზე: Request · Handler · Endpoint

## დომენის მოდელი (2 ლექცია)

### 10. Rich Entity, Value Object და Result

**პრობლემა:** ერთი წესი Create-შიც და Update-შიც მეორდება, Email ოთხ ადგილას სუფთავდება, `course.DurationWeeks = -5` კი კომპილირდება. **თემები:** ანემიური vs rich entity (private set, private constructor, `Create` / `Update`); Result pattern (`Result`, `Result<T>`, `Error`: Code + Message) — მოსალოდნელი შეცდომა exception-ის გარეშე; რომელი წესი entity-ში და რომელი handler-ში (ბაზის საჭიროება: R1, R2); Value Object `Email` (`sealed record`, EF Core `HasConversion`). **LMS:** Course, Student, Lecturer → rich · ახალი entity Group (≤ 20 ადგილი, წარსულში ვერ დაიწყება): Create, GetById.

📚 Rich entity: წესები entity-ში · Result pattern — შეცდომა exception-ის გარეშე · Value Object (`Email`)
🛠 Course, Student, Lecturer → rich · ახალი: ჯგუფები (≤ 20 ადგილი)

### 11. Aggregate და Concurrency

**პრობლემა:** R3 მთელ ჯგუფს ეხება; handler-ში დაწერილ შემოწმებას სხვა slice გვერდს აუვლის, ორი ერთდროული მოთხოვნა კი 20-ადგილიან ჯგუფში 21-ე სტუდენტს რიცხავს. **თემები:** Aggregate და Aggregate Root (`Group` → `Enrollment`), ცვლილება მხოლოდ root-ით, `DbSet` შვილზე არ არის; 400 vs 409; Cascade aggregate-ის შიგნით, Restrict გარეთ (ჯგუფიანი კურსის წაშლა → 409); დავიწყებული `Include` და Repository pattern DDD-ში — რას ხსნის, როდის ღირს (კოდში 17-ში); race condition (ცოცხალი ცდა); pessimistic vs optimistic; `rowversion` + `DbUpdateConcurrencyException` → 409; unique index. **LMS:** ჩარიცხვა ჯგუფში (R3).

📚 Aggregate და Aggregate Root · Repository: რას ხსნის და როდის ღირს · race condition და optimistic concurrency
🛠 ჩარიცხვა ჯგუფში (R3), ბოლო ადგილი → 409 · ჯგუფიანი კურსის წაშლა → 409

## პასუხები, შეცდომები და pipeline (2 ლექცია)

### 12. Middleware, Pipeline და Logging

**პრობლემა:** „ხანდახან ნელა მუშაობს“ — რომელი endpoint? `Stopwatch` ყველა handler-ში 20 ასლია: რაც ყველა მოთხოვნას ეხება, handler-ის საქმე არ არის. **თემები:** მოთხოვნის გზა — middleware-ების ჯაჭვი და პასუხი უკან; `Program.cs`-ის `Use…` ხაზები middleware-ებია; `app.Use(…, next)`: წინ / შემდეგ; რიგი მნიშვნელოვანია; short-circuit (ტექნიკური სამუშაოები → 503); საკუთარი middleware class-ად (`RequestDelegate`, `InvokeAsync`, `UseMiddleware`); DI ხაფანგი: Scoped სერვისი `InvokeAsync`-ში, არა constructor-ში; `ILogger<T>`, დონეები, ფილტრი `appsettings`-ში; structured logging (message template vs interpolation, JSON console). **LMS:** მოთხოვნის დროის middleware · ლოგები ჩარიცხვის handler-ში.

📚 როგორ გადის მოთხოვნა: middleware-ების ჯაჭვი და რიგი · საკუთარი middleware · `ILogger` და structured logging
🛠 ყოველი მოთხოვნის დროის ლოგი · ლოგები ჩარიცხვაში

### 13. შეცდომები და პასუხები: ერთი ფორმა ყველგან

**პრობლემა:** ყოველი handler თვითონ წყვეტს სტატუსს და შეცდომის ფორმას; exception → stack trace, არარსებული მისამართი → ცარიელი 404 — frontend-ს ხუთი სხვადასხვა ფორმის გარჩევა უწევს. **თემები:** ProblemDetails (RFC 9457) — ერთი ფორმა ყველა შეცდომაზე, წყაროს მიუხედავად; `ErrorType` (Validation, NotFound, Conflict…) → სტატუსი ერთ ადგილას; `ResultExtensions`: `ToOk()`, `ToCreated(uri)`, `ToNoContent()`, შეცდომა → ProblemDetails; `AddProblemDetails`, `IExceptionHandler` + `UseExceptionHandler` (500 დეტალების გარეშე production-ში, ლოგი), `UseStatusCodePages` (404/405); concurrency ერთ ადგილას. **LMS:** ყველა handler ResultExtensions-ზე · try/catch handler-ებში აღარ არის.

📚 ერთი შეცდომის ფორმა ყველგან: ProblemDetails · Result → HTTP ერთ ადგილას (`ToOk`, `ToCreated`) · global exception handler
🛠 ყველა handler ResultExtensions-ზე · try/catch აღარ არის

## უსაფრთხოება (2 ლექცია)

### 14. Authentication და Configuration

**პრობლემა:** API ყველასთვის ღიაა, story-ებს კი აქტორი ჰყავს („მენეჯერი ქმნის კურსს“); JWT-ს გასაღები და ვადა კოდში არ უნდა ეწეროს. **თემები:** `appsettings` და environment-ები; Options pattern (`JwtOptions`, `ValidateOnStart`); User Secrets; ანგარიშები — სტუდენტს და ლექტორს მენეჯერი ქმნის (თვითრეგისტრაცია არ არის), პირველი მენეჯერი seed-ით; პაროლის hash Argon2id-ით; login → JWT; JWT შემოწმება (`AddJwtBearer`), claims; `UseAuthentication` pipeline-ში; 401 ProblemDetails-ით. **LMS:** ანგარიშები სამ როლზე, login.

📚 Configuration, Options, User Secrets · პაროლის hash (Argon2id) · JWT: login და შემოწმება
🛠 ანგარიშები სამ როლზე — მენეჯერი ქმნის · login

### 15. Authorization

**პრობლემა:** შესულ მომხმარებელს ყველაფრის გაკეთება არ უნდა შეეძლოს: კურსს, ჯგუფს და ჩარიცხვას მხოლოდ მენეჯერი აკეთებს. **თემები:** როლები და policy-ები; `RequireAuthorization` ჯგუფებზე და endpoint-ებზე; მიმდინარე მომხმარებელი handler-ში (claims → `CurrentUser`); resource-based authorization — R5 („მხოლოდ ამ ჯგუფის ლექტორი“) მოთხოვნით, რომელიც მომდევნო feature-ებში გამოიყენება; 403 ProblemDetails-ით. **LMS:** policy-ები ყველა არსებულ endpoint-ზე.

📚 როლები და policy-ები · მიმდინარე მომხმარებელი handler-ში · resource-based authorization
🛠 ყველა არსებული endpoint დაცულია · R5-ის მოთხოვნა

## ვალიდაცია და MediatR (1 ლექცია)

### 16. ვალიდაცია და MediatR

**პრობლემა:** ვალიდაცია (ცარიელი ველები, ფორმატი, სიგრძე) entity-მდე უნდა მოხდეს და ყველა ველის შეცდომა ერთად უნდა დაბრუნდეს; validator-ის ხელით გამოძახება ყველა handler-ში მეორდება. **თემები:** FluentValidation (წესები, შეცდომები ველების მიხედვით → ValidationProblem); MediatR 12.x: `IRequest`, `IRequestHandler`, `ISender` — slice-ები MediatR-ზე; pipeline behavior: `ValidationBehavior` და `LoggingBehavior` ერთ ადგილას; middleware vs pipeline behavior: რომელი რისთვის. **LMS:** validator-ები ყველა Create/Update-ზე · ყველა slice MediatR-ზე.

📚 FluentValidation · MediatR: request, handler, sender · pipeline behavior (ვალიდაცია, ლოგი ერთ ადგილას)
🛠 validator-ები ყველა Create/Update-ზე · slice-ები MediatR-ზე

## LMS-ის დასრულება (3 ლექცია)

### 17. განრიგი და დასწრება + Claude Code

**პრობლემა:** ჯგუფის aggregate იზრდება (ლექციები, დასწრება) და მას ბევრი handler ტვირთავს — ყველგან სწორი `Include` სჭირდება; feature-ები მეორდება ნაცნობი pattern-ით. **თემები:** `IGroupRepository` ხელით (`GetAsync`, `Add`), Enroll მასზე; R4 (ლექციები დროში არ ფარავს ერთმანეთს — ჯგუფის წესი; ლექტორი ერთ დროს ერთ ლექციაზე — handler-ის წესი); R6 (15 წთ-ზე მეტი დაგვიანება = გაცდენა); R5 პირველივე slice-იდან — დასწრებას მხოლოდ ჯგუფის ლექტორი აღრიცხავს; Claude Code: `CLAUDE.md` (VSA, MediatR, Result, aggregate მხოლოდ Repository-ით, ყველა endpoint policy-ით), პირველი slice ხელით → დანარჩენს AI წერს → review; სია pagination-ით (Skip/Take, `PagedResponse`). **LMS:** განრიგი და დასწრება.

📚 Repository კოდში (`IGroupRepository`) · Claude Code: `CLAUDE.md`, AI წერს → ჩვენ review · pagination
🛠 განრიგი (R4) · დასწრება (R6, R5)

### 18. ფაილები, დრო და შეფასება

**პრობლემა:** სტუდენტი ნამუშევარს ფაილად აბარებს; დედლაინის წესი დროზეა დამოკიდებული და `DateTime.UtcNow`-ით შეუმოწმებელია. **თემები:** დავალებები; ფაილის ატვირთვა (`IFormFile`, ზომა და ტიპი, შენახვა) და ჩამოტვირთვა; `TimeProvider` (`DateTime.UtcNow`-ის ნაცვლად); R7 (დედლაინის შემდეგ არ მიიღება, მენეჯერს გადაწევა შეუძლია; ქულა 1–12 — Value Object). **LMS:** დავალებები, ნამუშევრის ატვირთვა (მხოლოდ საკუთარი), შეფასება (R5: მხოლოდ ჯგუფის ლექტორი).

📚 ფაილის ატვირთვა და ჩამოტვირთვა · `TimeProvider` · ქულა — Value Object
🛠 დავალებები · ნამუშევრის ატვირთვა · შეფასება (R7)

### 19. Background Jobs და კურსის დასრულება

**პრობლემა:** ზოგი საქმე მოთხოვნის გარეშე უნდა მოხდეს: დედლაინის შეხსენება, ლექტორის გაფრთხილება მე-4 გაცდენაზე. **თემები:** `BackgroundService` და `PeriodicTimer`; Scoped სერვისი background-ში (`IServiceScopeFactory`); შეტყობინებები აპლიკაციის შიგნით (ბაზაში); R6-ის მეორე ნაწილი; R8 (კურსი ჩაბარებულია: საშუალო ≥ 6 და დასწრება ≥ 75%). **LMS:** შეტყობინებები, კურსის დასრულება — **Backend დასრულებულია**.

📚 `BackgroundService`, `PeriodicTimer` · Scoped სერვისი background-ში
🛠 შეხსენებები, მე-4 გაცდენა (R6) · კურსის ჩაბარება (R8) · Backend დასრულებულია

## Angular Claude Code-ით (2 ლექცია)

### 20. Angular + Claude Code #1: როგორ ვმუშაობთ AI-სთან

**თემები:** როგორ ვგეგმავთ AI-სთან: `CLAUDE.md`, plan mode, OpenAPI დოკუმენტი როგორც კონტექსტი; CORS; Angular-ის სტრუქტურა; login, layout, JWT interceptor, ProblemDetails-ის ჩვენება; კურსები და ჯგუფები. სტუდენტები კოდს კითხულობენ, ლექტორი გეგმავს და review-ს აკეთებს.

📚 როგორ ვგეგმავთ AI-სთან: `CLAUDE.md`, plan mode, OpenAPI · CORS · JWT interceptor
🛠 Angular: login, layout, კურსები და ჯგუფები

### 21. Angular + Claude Code #2

**თემები:** განრიგი, დასწრება, ნამუშევრის ატვირთვა, ქულები; ბოლო review და შესწორებები. **Frontend დასრულებულია** — სრული აპლიკაცია DevOps-ის კურსში იშვება სერვერზე.

📚 review AI-ის კოდზე · სრული აპლიკაცია backend + frontend
🛠 Angular: განრიგი, დასწრება, ატვირთვა, ქულები · Frontend დასრულებულია

# ASP.NET Core Web API

**ტექნოლოგიები:** .NET 10, ASP.NET Core Web API (Controllers → Minimal API), EF Core 10, PostgreSQL (Docker-ში — SQL-ის კურსიდან ნაცნობი), Scalar / OpenAPI, Angular, Claude Code

**პროექტი:** 01–05 — ShopApi (კლასში) და LibraryApi (სტუდენტები). 06-დან — **LMS** (კურსები, ჯგუფები, სტუდენტები, ლექტორები, ლექციები, დასწრება, დავალებები, ქულები), რომელსაც ლექტორი კლასში აწყობს; სტუდენტი იმავე თემებს სახლში თავის არჩეულ სფეროში წერს. ბოლოს LMS-ს Angular-ის frontend ემატება და DevOps-ის კურსში სრული აპლიკაცია სერვერზე იშვება.

| დანიშნულება | Package |
| --- | --- |
| ბაზა | `Npgsql.EntityFrameworkCore.PostgreSQL`, `Microsoft.EntityFrameworkCore.Tools` |
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

📚 გაიგებს, რა არის Backend და რა ადგილი უჭირავს მას აპლიკაციაში
📚 გაარჩევს API-ს და REST-ს: რესურსი, HTTP მეთოდები, სტატუს კოდები
📚 აუხსნის, როგორ ელაპარაკება frontend სერვერს (მოთხოვნა → პასუხი, JSON)
📚 შექმნის ASP.NET Core Web API პროექტს Visual Studio-ში და გაუშვებს
🛠 ShopApi | პროექტი `ShopApi` (ASP.NET Core Web API)
🛠 `GET /api/products` — პროდუქტების სია მეხსიერებიდან
🛠 ბრაუზერით შემოწმება და JSON პასუხი


### 02. Minimal API vs Controller, REST, CRUD და Swagger

API-ის აწყობის ორი გზა და მათი შედარება; Controller-ები და routing; REST-ის წესები პრაქტიკაში; `IActionResult` და სწორი სტატუს კოდები; Swagger; პროდუქტების სრული CRUD.

📚 გაარჩევს Minimal API-ს და Controller-ს და იცის, რომელი როდის
📚 დაწერს სრულ CRUD-ს REST-ის წესებით და სწორი სტატუს კოდებით
📚 გამოიყენებს `IActionResult`-ს (Ok, NotFound, CreatedAtAction, NoContent)
📚 შეამოწმებს API-ს Swagger-ში
🛠 ShopApi | `ProductsController`
🛠 `GET /api/products` · `GET /api/products/{id}` · `GET /api/products/cheap`
🛠 `POST` · `PUT /{id}` · `DELETE /{id}` — პროდუქტების სრული CRUD (სია მეხსიერებაში)


### 03. DTO და Mapping

რატომ არ ვაბრუნებთ entity-ს პირდაპირ; Request და Response DTO-ები; ხელით დაწერილი Mapper; mapping-ის package.

📚 აუხსნის, რატომ არ ვაბრუნებთ entity-ს პირდაპირ (შიდა ველები, ზედმეტი მონაცემი)
📚 დაწერს Request და Response DTO-ებს
📚 დაწერს Mapper-ს ხელით და იცის Mapperly-ის გამოყენება
🛠 ShopApi | `CreateProductRequest`, `UpdateProductRequest`, `ProductResponse`
🛠 `ProductMapper` — `ToResponse`, `ToEntity`
🛠 ყველა endpoint DTO-ებზე


### 04. Dependency Injection და DbContext

API-ს ნამდვილ ბაზას ვუერთებთ (EF Core — კურსიდან ნაცნობი, ახლა DI-ით); IoC და DI Container; რეგისტრაცია და lifetime-ები: Singleton, Scoped, Transient; DataContext Controller-ში.

📚 აუხსნის, ვინ ქმნის ობიექტებს და რატომ: IoC და DI Container
📚 გაარჩევს Singleton, Scoped და Transient lifetime-ებს
📚 მიუერთებს API-ს ნამდვილ ბაზას EF Core-ით
🛠 ShopApi | `DataContext` + `DbSet<Product>` · რეგისტრაცია `Program.cs`-ში
🛠 მიგრაცია და PostgreSQL ბაზა (Docker)
🛠 `ProductsController` სტატიკური სიის ნაცვლად `DataContext`-ით


### 05. Async / Await API-ში

async/await-ის საფუძვლები C#-იდან ნაცნობია — აქ: რატომ „იჭედება“ სერვერი სინქრონულ კოდზე, როცა ერთდროულად ბევრი მოთხოვნაა; Thread pool; async/await EF Core-ის მეთოდებით (`ToListAsync`, `SaveChangesAsync`); async endpoint-ები.

📚 აუხსნის, რატომ „იჭედება“ სერვერი სინქრონულ კოდზე (thread pool)
📚 დაწერს async endpoint-ებს EF Core-ის async მეთოდებით
🛠 ShopApi | ყველა action async: `ToListAsync`, `FindAsync`, `SaveChangesAsync`


## DDD და LMS-ის დასაწყისი (4 ლექცია)

### 06. DDD: ბიზნესის ენიდან კოდამდე

რა არის Domain-Driven Design; როგორ ვესაუბრებით ბიზნესს; ubiquitous language; როგორ ვგეგმავთ პროექტს და როგორ აისახება ეს კოდში.

📚 აუხსნის, რა არის DDD და რატომ იწყება პროექტი ბიზნესის გაგებით
📚 ისწავლის ბიზნესთან საუბარს და საერთო ენის (ubiquitous language) შექმნას
📚 დაინახავს, როგორ აისახება ბიზნესის ენა კოდში
🛠 LMS | კოდი ჯერ არა — LMS-ის ხედვა: რას აკეთებს სისტემა და ვისთვის
🛠 ლექსიკონი: კურსი, ჯგუფი, ლექცია, დასწრება, დავალება, ქულა…


### 07. LMS-ის აღმოჩენა: ენა, აქტორები, პროცესები, წესები

DDD LMS-ზე: ლექსიკონი, აქტორები, პროცესები, ბიზნესის წესები (R1–R8) → დომენის რუკა და backlog; სტუდენტი ირჩევს საკუთარ სფეროს საშინაოებისთვის.

📚 ჩამოწერს აქტორებს, პროცესებს და ბიზნესის წესებს
📚 გაარჩევს წესს სურვილისგან
📚 ააწყობს დომენის რუკას და backlog-ს story-ებით
🛠 LMS | აქტორები: მენეჯერი, ლექტორი, სტუდენტი
🛠 წესები R1–R8
🛠 backlog: story-ები პრიორიტეტით
🛠 სტუდენტი ირჩევს თავის სფეროს (ფიტნესი, ავტოსკოლა, კლინიკა…)


### 08. LMS: პროექტის აწყობა და პირველი feature

LMS-ის პროექტი; story №1 „მენეჯერი ქმნის კურსს“ ნაცნობი გზით (Controller, DataContext, DTO, Mapper, async); R1 და R2; რა გვტკივა ამ მიდგომაში.

📚 გადააქცევს story-ს კოდად: სახელები ლექსიკონიდან, შემოწმებები წესებიდან
📚 დაინახავს, რა გვტკივა „ყველაფერი Controller-ში“ მიდგომაში
🛠 LMS | პროექტი `Lms.Api`, `DataContext`, PostgreSQL, მიგრაციები
🛠 `Course` (Title, Description, DurationWeeks 1–52) · `CoursesController` — სრული CRUD
🛠 R1: კურსის სახელი უნიკალურია → 409
🛠 `Student` და `Lecturer` (FirstName, LastName, Email) — CRUD · R2: Email უნიკალურია → 409


### 09. არქიტექტურა: Layers vs Vertical Slices

Layers და Vertical Slice Architecture; SRP და DIP; slice: Request · Handler · Endpoint; Controller-ები → Minimal API (`MapGroup`); Swagger → Scalar.

📚 შეადარებს Layers-ს და Vertical Slices-ს და იცის, რას აჯგუფებს თითოეული
📚 აუხსნის SRP-ს და DIP-ს ჩვენს კოდზე
📚 ააწყობს slice-ს: Request · Handler · Endpoint (Minimal API, `MapGroup`)
📚 გამოიყენებს Scalar-ს Swagger-ის ნაცვლად
🛠 LMS | `Features/Courses/…` — Create, GetAll, GetById, Update, Delete slice-ები
🛠 `CourseEndpoints`: handler-ების რეგისტრაცია + `MapGroup("/api/courses")`
🛠 Students და Lecturers — იგივე slice-ებზე
🛠 Controllers წაშლილია · `/scalar`


## დომენის მოდელი (2 ლექცია)

### 10. Rich Entity, Value Object და Result

**პრობლემა:** ერთი წესი Create-შიც და Update-შიც მეორდება, Email ოთხ ადგილას სუფთავდება, `course.DurationWeeks = -5` კი კომპილირდება. **თემები:** ანემიური vs rich entity (private set, private constructor, `Create` / `Update`); Result pattern (`Result`, `Result<T>`, `Error`: Code + Message) — მოსალოდნელი შეცდომა exception-ის გარეშე; რომელი წესი entity-ში და რომელი handler-ში (ბაზის საჭიროება: R1, R2); Value Object `Email` (`sealed record`, EF Core `HasConversion`). **LMS:** Course, Student, Lecturer → rich · ახალი entity Group (≤ 20 ადგილი, წარსულში ვერ დაიწყება): Create, GetById.

📚 გაარჩევს ანემიურ და rich entity-ს; იცის, რატომ უნდა იცავდეს entity თავის წესებს
📚 გამოიყენებს Result pattern-ს: მოსალოდნელი შეცდომა exception-ის გარეშე
📚 გაარჩევს Entity-ს და Value Object-ს
📚 იცის, რომელი წესი ეკუთვნის entity-ს და რომელი handler-ს
🛠 LMS | `Common/Result.cs` — `Error`, `Result`, `Result<T>`
🛠 `Course.Create` / `Update` + `CourseErrors` — „1–52 კვირა“ ერთ ადგილას
🛠 `Email` Value Object + `HasConversion` · Student, Lecturer → rich
🛠 ახალი `Group` (CourseId, LecturerId, Name, StartDate, Capacity ≤ 20)
🛠 `POST /api/groups` · `GET /api/groups/{id}`


### 11. Aggregate და Concurrency

**პრობლემა:** R3 მთელ ჯგუფს ეხება; handler-ში დაწერილ შემოწმებას სხვა slice გვერდს აუვლის, ორი ერთდროული მოთხოვნა კი 20-ადგილიან ჯგუფში 21-ე სტუდენტს რიცხავს. **თემები:** Aggregate და Aggregate Root (`Group` → `Enrollment`), ცვლილება მხოლოდ root-ით, `DbSet` შვილზე არ არის; 400 vs 409; Cascade aggregate-ის შიგნით, Restrict გარეთ (ჯგუფიანი კურსის წაშლა → 409); დავიწყებული `Include` და Repository pattern DDD-ში — რას ხსნის, როდის ღირს (კოდში 17-ში); race condition (ცოცხალი ცდა); pessimistic vs optimistic; `rowversion` + `DbUpdateConcurrencyException` → 409; unique index. **LMS:** ჩარიცხვა ჯგუფში (R3).

📚 აუხსნის, რა არის Aggregate და Aggregate Root და რატომ იცვლება შვილი მხოლოდ root-ით
📚 გაარჩევს 400-ს და 409-ს
📚 დაინახავს race condition-ს და დაიცავს მისგან optimistic concurrency-ით
📚 იცის, რას ხსნის Repository და როდის ღირს მისი დაწერა
🛠 LMS | `Enrollment` ჯგუფის შიგნით · `group.Enroll(...)` — R3: ადგილი, ერთხელ, პირველი კვირა
🛠 `POST /api/groups/{id}/enrollments` → 409 (Full, AlreadyEnrolled, EnrollmentClosed)
🛠 `EnrolledCount` + `RowVersion` · `DbUpdateConcurrencyException` → 409
🛠 unique index (GroupId, StudentId)
🛠 Restrict კურსზე და ლექტორზე · ჯგუფიანი კურსის წაშლა → 409


## პასუხები, შეცდომები და pipeline (2 ლექცია)

### 12. Middleware, Pipeline და Logging

**პრობლემა:** „ხანდახან ნელა მუშაობს“ — რომელი endpoint? `Stopwatch` ყველა handler-ში 20 ასლია: რაც ყველა მოთხოვნას ეხება, handler-ის საქმე არ არის. **თემები:** მოთხოვნის გზა — middleware-ების ჯაჭვი და პასუხი უკან; `Program.cs`-ის `Use…` ხაზები middleware-ებია; `app.Use(…, next)`: წინ / შემდეგ; რიგი მნიშვნელოვანია; short-circuit (ტექნიკური სამუშაოები → 503); საკუთარი middleware class-ად (`RequestDelegate`, `InvokeAsync`, `UseMiddleware`); DI ხაფანგი: Scoped სერვისი `InvokeAsync`-ში, არა constructor-ში; `ILogger<T>`, დონეები, ფილტრი `appsettings`-ში; structured logging (message template vs interpolation, JSON console). **LMS:** მოთხოვნის დროის middleware · ლოგები ჩარიცხვის handler-ში.

📚 აუხსნის, როგორ გადის მოთხოვნა ASP.NET Core-ში და რატომ არის რიგი მნიშვნელოვანი
📚 დაწერს საკუთარ middleware-ს და დაარეგისტრირებს
📚 გამოიყენებს `ILogger`-ს სწორი დონეებით და structured logging-ით
🛠 LMS | `RequestTimingMiddleware` — ყოველი მოთხოვნის ლოგი: მეთოდი, მისამართი, სტატუსი, დრო (ms)
🛠 „ტექნიკური სამუშაოები“ — middleware, რომელიც 503-ს აბრუნებს (კონფიგურაციით)
🛠 ლოგები `EnrollStudent`-ში: ჩარიცხვა → Information, ჯგუფი სავსეა → Warning
🛠 JSON console logging Development-ში


### 13. შეცდომები და პასუხები: ერთი ფორმა ყველგან

**პრობლემა:** ყოველი handler თვითონ წყვეტს სტატუსს და შეცდომის ფორმას; exception → stack trace, არარსებული მისამართი → ცარიელი 404 — frontend-ს ხუთი სხვადასხვა ფორმის გარჩევა უწევს. **თემები:** ProblemDetails (RFC 9457) — ერთი ფორმა ყველა შეცდომაზე, წყაროს მიუხედავად; `ErrorType` (Validation, NotFound, Conflict…) → სტატუსი ერთ ადგილას; `ResultExtensions`: `ToOk()`, `ToCreated(uri)`, `ToNoContent()`, შეცდომა → ProblemDetails; `AddProblemDetails`, `IExceptionHandler` + `UseExceptionHandler` (500 დეტალების გარეშე production-ში, ლოგი), `UseStatusCodePages` (404/405); concurrency ერთ ადგილას. **LMS:** ყველა handler ResultExtensions-ზე · try/catch handler-ებში აღარ არის.

📚 აუხსნის, რატომ უნდა ბრუნდებოდეს ყველა შეცდომა ერთ ფორმაში (ProblemDetails)
📚 თარგმნის Result-ს HTTP პასუხად ერთ ადგილას
📚 დაამუშავებს მოულოდნელ exception-ს ცენტრალურად
🛠 LMS | `ErrorType` (Validation, NotFound, Conflict…) `Error`-ში
🛠 `ResultExtensions`: `ToOk()`, `ToCreated(uri)`, `ToNoContent()`, შეცდომა → ProblemDetails
🛠 ყველა handler ResultExtensions-ზე — `if (IsFailure) return …` აღარ არის
🛠 `GlobalExceptionHandler` (500 + ლოგი + traceId) · concurrency → 409 ერთ ადგილას
🛠 `AddProblemDetails` + `UseStatusCodePages` — 404/405 იგივე ფორმით


## უსაფრთხოება (2 ლექცია)

### 14. Authentication და Configuration

**პრობლემა:** API ყველასთვის ღიაა, story-ებს კი აქტორი ჰყავს („მენეჯერი ქმნის კურსს“); JWT-ს გასაღები და ვადა კოდში არ უნდა ეწეროს. **თემები:** `appsettings` და environment-ები; Options pattern (`JwtOptions`, `ValidateOnStart`); User Secrets; ანგარიშები — სტუდენტს და ლექტორს მენეჯერი ქმნის (თვითრეგისტრაცია არ არის), პირველი მენეჯერი seed-ით; პაროლის hash Argon2id-ით (C#-ში PBKDF2 გამოვიყენეთ — რატომ არის Argon2id უფრო ძლიერი); login → JWT; JWT შემოწმება (`AddJwtBearer`), claims; `UseAuthentication` pipeline-ში; 401 ProblemDetails-ით. **LMS:** ანგარიშები სამ როლზე, login.

📚 გამოიყენებს Configuration-ს და Options pattern-ს; შეინახავს საიდუმლოს User Secrets-ში
📚 შეინახავს პაროლს უსაფრთხოდ (Argon2id)
📚 აუხსნის JWT-ს: როგორ იცემა, რა წერია შიგნით, როგორ მოწმდება
🛠 LMS | `Account` (Email, PasswordHash, Role) — მიბმული Student-ზე / Lecturer-ზე
🛠 პირველი მენეჯერი — seed სტარტზე (პაროლი User Secrets-იდან)
🛠 `POST /api/auth/login` → JWT · `GET /api/auth/me`
🛠 მენეჯერი ქმნის სტუდენტის / ლექტორის ანგარიშს
🛠 `JwtOptions` + `ValidateOnStart` · `AddJwtBearer` · 401 ProblemDetails-ით


### 15. Authorization

**პრობლემა:** შესულ მომხმარებელს ყველაფრის გაკეთება არ უნდა შეეძლოს: კურსს, ჯგუფს და ჩარიცხვას მხოლოდ მენეჯერი აკეთებს. **თემები:** როლები და policy-ები; `RequireAuthorization` ჯგუფებზე და endpoint-ებზე; მიმდინარე მომხმარებელი handler-ში (claims → `CurrentUser`); resource-based authorization — R5 („მხოლოდ ამ ჯგუფის ლექტორი“) მოთხოვნით, რომელიც მომდევნო feature-ებში გამოიყენება; 403 ProblemDetails-ით. **LMS:** policy-ები ყველა არსებულ endpoint-ზე.

📚 გაარჩევს authentication-ს და authorization-ს
📚 დაწერს როლებს და policy-ებს და დაიცავს endpoint-ებს
📚 გამოიყენებს resource-based authorization-ს (ჯგუფი „ჩემია“ თუ არა)
🛠 LMS | policy-ები: `ManagerOnly`, `LecturerOnly`, `StudentOnly`
🛠 კურსები, ჯგუფები, ჩარიცხვა, ანგარიშები → მხოლოდ მენეჯერი · წაკითხვა → ყველა შესული
🛠 `CurrentUser` — მიმდინარე მომხმარებელი claims-იდან handler-ში
🛠 R5: „მხოლოდ ამ ჯგუფის ლექტორი“ — მზა შემოწმება შემდეგი feature-ებისთვის · 403 ProblemDetails-ით


## ვალიდაცია და MediatR (1 ლექცია)

### 16. ვალიდაცია და MediatR

**პრობლემა:** ვალიდაცია (ცარიელი ველები, ფორმატი, სიგრძე) entity-მდე უნდა მოხდეს და ყველა ველის შეცდომა ერთად უნდა დაბრუნდეს; validator-ის ხელით გამოძახება ყველა handler-ში მეორდება. **თემები:** FluentValidation (წესები, შეცდომები ველების მიხედვით → ValidationProblem); MediatR 12.x: `IRequest`, `IRequestHandler`, `ISender` — slice-ები MediatR-ზე; pipeline behavior: `ValidationBehavior` და `LoggingBehavior` ერთ ადგილას; middleware vs pipeline behavior: რომელი რისთვის. **LMS:** validator-ები ყველა Create/Update-ზე · ყველა slice MediatR-ზე.

📚 დაწერს ვალიდაციას FluentValidation-ით და დააბრუნებს ველების შეცდომებს
📚 აუხსნის, რა არის mediator და რას აძლევს VSA-ს
📚 გამოიყენებს pipeline behavior-ს და გაარჩევს მას middleware-ისგან
🛠 LMS | validator-ები: CreateCourse, UpdateCourse, CreateGroup, Student, Lecturer, Login…
🛠 ყველა slice MediatR-ზე: `IRequest<Result<T>>`, `IRequestHandler`, endpoint → `ISender`
🛠 `ValidationBehavior` — ვალიდაცია ყველა request-ზე ავტომატურად → ValidationProblem
🛠 `LoggingBehavior` — request-ის სახელი და დრო


## LMS-ის feature-ები (3 ლექცია)

### 17. განრიგი და დასწრება + Claude Code

**პრობლემა:** ჯგუფის aggregate იზრდება (ლექციები, დასწრება) და მას ბევრი handler ტვირთავს — ყველგან სწორი `Include` სჭირდება; feature-ები მეორდება ნაცნობი pattern-ით. **თემები:** `IGroupRepository` ხელით (`GetAsync`, `Add`), Enroll მასზე; R4 (ლექციები დროში არ ფარავს ერთმანეთს — ჯგუფის წესი; ლექტორი ერთ დროს ერთ ლექციაზე — handler-ის წესი); R6 (15 წთ-ზე მეტი დაგვიანება = გაცდენა); R5 პირველივე slice-იდან — დასწრებას მხოლოდ ჯგუფის ლექტორი აღრიცხავს; Claude Code: `CLAUDE.md` (VSA, MediatR, Result, aggregate მხოლოდ Repository-ით, ყველა endpoint policy-ით), პირველი slice ხელით → დანარჩენს AI წერს → review; სია pagination-ით (Skip/Take, `PagedResponse`). **LMS:** განრიგი და დასწრება.

📚 დაწერს Repository-ს aggregate-ზე და დაინახავს, რატომ სჭირდება ახლა
📚 იმუშავებს Claude Code-თან: `CLAUDE.md`, დავალების მიცემა, AI-ის კოდის review
📚 დაწერს სიას pagination-ით
🛠 LMS | `IGroupRepository` (GetAsync — ყოველთვის სრული aggregate, Add) · Enroll მასზე
🛠 ლექციები ჯგუფში: `group.ScheduleLecture(...)` — R4: ლექციები არ ფარავს ერთმანეთს · ლექტორი ერთ დროს ერთ ლექციაზე
🛠 `GET /api/groups/{id}/lectures` — pagination-ით
🛠 დასწრება: `MarkAttendance` — R6: 15 წთ-ზე მეტი დაგვიანება = გაცდენა · R5: მხოლოდ ჯგუფის ლექტორი
🛠 `CLAUDE.md` პროექტის წესებით · დანარჩენ slice-ებს Claude Code წერს → review


### 18. ფაილები, დრო და შეფასება

**პრობლემა:** სტუდენტი ნამუშევარს ფაილად აბარებს; დედლაინის წესი დროზეა დამოკიდებული და `DateTime.UtcNow`-ით შეუმოწმებელია. **თემები:** დავალებები; ფაილის ატვირთვა (`IFormFile`, ზომა და ტიპი, შენახვა) და ჩამოტვირთვა; `TimeProvider` (`DateTime.UtcNow`-ის ნაცვლად); R7 (დედლაინის შემდეგ არ მიიღება, მენეჯერს გადაწევა შეუძლია; ქულა 1–12 — Value Object). **LMS:** დავალებები, ნამუშევრის ატვირთვა (მხოლოდ საკუთარი), შეფასება (R5: მხოლოდ ჯგუფის ლექტორი).

📚 ატვირთავს და გასცემს ფაილს უსაფრთხოდ (ზომა, ტიპი, შენახვის ადგილი)
📚 გამოიყენებს `TimeProvider`-ს, რომ დროზე დამოკიდებული წესი შემოწმებადი იყოს
📚 დაწერს მეორე Value Object-ს (ქულა)
🛠 LMS | `Assignment` (Title, Deadline) ჯგუფში · მენეჯერს შეუძლია დედლაინის გადაწევა
🛠 `POST …/submissions` — ფაილის ატვირთვა (მხოლოდ საკუთარი) · ჩამოტვირთვა
🛠 R7: დედლაინის შემდეგ არ მიიღება
🛠 `Score` Value Object (1–12) · შეფასება — R5: მხოლოდ ჯგუფის ლექტორი


### 19. Background Jobs და კურსის დასრულება

**პრობლემა:** ზოგი საქმე მოთხოვნის გარეშე უნდა მოხდეს: დედლაინის შეხსენება, ლექტორის გაფრთხილება მე-4 გაცდენაზე. **თემები:** `BackgroundService` და `PeriodicTimer`; Scoped სერვისი background-ში (`IServiceScopeFactory`); შეტყობინებები ბაზაში და email-ით (MailKit C#-იდან ნაცნობია — აქ `SmtpOptions`-ით და ფონურად); R6-ის მეორე ნაწილი; R8 (კურსი ჩაბარებულია: საშუალო ≥ 6 და დასწრება ≥ 75%). **LMS:** შეტყობინებები (ბაზა + email), კურსის დასრულება.

📚 დაწერს ფონურ სამუშაოს `BackgroundService`-ით
📚 გამოიყენებს Scoped სერვისს (DataContext) background-ში `IServiceScopeFactory`-ით
📚 გააგზავნის email-ს SMTP-ით (MailKit)
🛠 LMS | `Notification` ბაზაში · `GET /api/notifications/me`
🛠 `ReminderService` (`PeriodicTimer`) — დედლაინამდე 24 საათით ადრე შეხსენება
🛠 R6: მე-4 გაცდენაზე ლექტორს შეტყობინება
🛠 R8: კურსის შედეგი — საშუალო ≥ 6 და დასწრება ≥ 75% → ჩაბარებულია


## Production-ისთვის: დაცვა, სისწრაფე, გარე სერვისები (3 ლექცია)

### 20. Rate Limiting

**პრობლემა:** login-ზე წამში ასობით პაროლის ცდა (brute force); ერთ კლიენტს შეუძლია მთელი სერვერი დატვირთოს. **თემები:** rate limiting-ის ოთხი ალგორითმი — fixed window, sliding window, token bucket, concurrency — და ცოცხალი შედარება ბევრი მოთხოვნით; partition მომხმარებლით და IP-ით (მენეჯერს და სტუდენტს სხვადასხვა ლიმიტი); `RequireRateLimiting` / `DisableRateLimiting`; 429 ProblemDetails-ით + `Retry-After`; რატომ არ მუშაობს ჩაშენებული limiter რამდენიმე სერვერზე. **LMS:** login-ის დაცვა, ზოგადი ლიმიტი API-ზე.

📚 გაარჩევს rate limiting-ის ალგორითმებს და იცის, რომელი როდის
📚 დაიცავს endpoint-ებს ლიმიტით მომხმარებლის / IP-ის მიხედვით
📚 დააბრუნებს 429-ს სწორად (ProblemDetails, `Retry-After`)
🛠 LMS | `AddRateLimiter`: policy-ები `login` (IP-ით, მკაცრი) და `api` (მომხმარებლით)
🛠 `POST /api/auth/login` → `RequireRateLimiting("login")`
🛠 ყველა სხვა endpoint → `api` policy · მენეჯერს უფრო მაღალი ლიმიტი
🛠 429 → ProblemDetails + `Retry-After` header

### 21. Caching და Redis

**პრობლემა:** კურსების სია და ჯგუფის დეტალები წამში ბევრჯერ იკითხება, თუმცა იშვიათად იცვლება — ბაზა ზედმეტად იტვირთება; მეხსიერებაში ქეში ორ სერვერზე ერთმანეთს არ ემთხვევა. **თემები:** რა ღირს ქეშად და რა არა; in-memory cache და მისი ზღვარი; Redis (Docker-ში) — distributed cache; `HybridCache`: L1 მეხსიერება + L2 Redis, stampede-ისგან დაცვა; ვადა და გასუფთავება ცვლილებისას (tags); ქეში და მონაცემის „სიძველე“. **LMS:** კურსების სიის და ჯგუფის დეტალების ქეში.

📚 გადაწყვეტს, რა მონაცემი ღირს ქეშად და რამდენ ხანს
📚 გაარჩევს in-memory და distributed cache-ს და იცის, როდის სჭირდება Redis
📚 გამოიყენებს `HybridCache`-ს და გაასუფთავებს ქეშს ცვლილებისას
🛠 LMS | Redis Docker-ში · `AddStackExchangeRedisCache` + `AddHybridCache`
🛠 `GetCourses`, `GetGroupById` → `HybridCache.GetOrCreateAsync` (tag-ებით)
🛠 Create / Update / Delete / Enroll → `RemoveByTagAsync` — ქეში სუფთავდება
🛠 ლოგში ჩანს: პირველი მოთხოვნა ბაზიდან, შემდეგი ქეშიდან

### 22. HttpClient და Resilience

**პრობლემა:** მენეჯერი ლექციას დღესასწაულზე ნიშნავს; დღესასწაულების სიას ხელით ვერ ვწერთ — ის გარე API-დან მოდის, და გარე სერვისი შეიძლება ნელი იყოს ან გაითიშოს. **თემები:** `HttpClient` C#-იდან ნაცნობია — აქ: რატომ არა `new HttpClient()` სერვერზე (socket exhaustion, DNS); `IHttpClientFactory` და typed client; BaseAddress Options-ით; `GetFromJsonAsync`, `CancellationToken`; გარე სერვისის შეცდომა → `Result`, ჩვენი API არ ვარდება; resilience: retry, timeout, circuit breaker (`AddStandardResilienceHandler`); პასუხის ქეში Redis-ში. **LMS:** ლექცია დღესასწაულზე არ ინიშნება.

📚 გამოიძახებს გარე API-ს სწორად: `IHttpClientFactory`, typed client
📚 დაიცავს საკუთარ API-ს გარე სერვისის შეცდომებისგან (Result, timeout)
📚 გამოიყენებს retry-ს და circuit breaker-ს და დაინახავს მათ ლოგში
🛠 LMS | `HolidaysClient` (typed client) + `HolidaysOptions` (BaseAddress)
🛠 `AddStandardResilienceHandler` — retry, timeout, circuit breaker
🛠 დღესასწაულები წლის მიხედვით — `HybridCache`-ში (Redis)
🛠 `group.ScheduleLecture(...)` — ახალი წესი: დღესასწაულზე → 409

## ტესტები (2 ლექცია)

### 23. Unit ტესტები

**პრობლემა:** ყოველი ცვლილების შემდეგ ყველა წესის ხელით შემოწმება Scalar-ში შეუძლებელია; Claude Code-ის კოდის review-ს მტკიცებულება სჭირდება. **თემები:** xUnit და Arrange-Act-Assert C#-იდან ნაცნობია — მოკლე გამეორება; რას ვტესტავთ API-ში; დომენის წესების ტესტი (Result-ის შემოწმება); `FakeTimeProvider` დროზე დამოკიდებული წესებისთვის; fake დამოკიდებულება (HolidaysClient); ტესტის სახელები და სტრუქტურა. **LMS:** ტესტ-პროექტი, დომენის წესების ტესტები.

📚 დაწერს unit ტესტს xUnit-ით (Arrange-Act-Assert, `[Fact]`, `[Theory]`)
📚 შეამოწმებს დომენის წესებს და დროზე დამოკიდებულ წესს `FakeTimeProvider`-ით
📚 ჩაანაცვლებს გარე დამოკიდებულებას fake-ით
🛠 LMS | `Lms.Tests` პროექტი (xUnit)
🛠 `Email`, `Course`, `Group.Enroll` (R3), `ScheduleLecture` (R4), `Score`, დედლაინი (R7) — ტესტები
🛠 R8 (კურსის ჩაბარება) — `[Theory]` რამდენიმე შემთხვევით

### 24. Integration ტესტები

**პრობლემა:** unit ტესტი ამოწმებს წესს, მაგრამ არა იმას, რომ endpoint, auth, ვალიდაცია, ბაზა და ProblemDetails ერთად მუშაობს. **თემები:** `WebApplicationFactory`; სატესტო ბაზა; JWT ტესტში; HTTP სცენარის ტესტი; რა ვტესტავთ integration-ით და რა unit-ით. **LMS:** სრული სცენარების ტესტები — **Backend დასრულებულია**.

📚 დაწერს integration ტესტს `WebApplicationFactory`-ით
📚 შეამოწმებს სრულ სცენარს: auth → ვალიდაცია → ბაზა → პასუხი
📚 გაარჩევს, რა ტესტდება unit-ით და რა integration-ით
🛠 LMS | `LmsApiFactory` — სატესტო ბაზით და JWT-ით
🛠 სცენარი: ჩარიცხვა → 200 · ბოლო ადგილი → 409 · სხვის ჯგუფზე დასწრება → 403
🛠 ვალიდაციის შეცდომა → 400 ProblemDetails `errors`-ით · login-ის ლიმიტი → 429
🛠 Backend დასრულებულია

## Angular Claude Code-ით (2 ლექცია)

### 25. Angular + Claude Code #1: როგორ ვმუშაობთ AI-სთან

**თემები:** როგორ ვგეგმავთ AI-სთან: `CLAUDE.md`, plan mode, OpenAPI დოკუმენტი როგორც კონტექსტი; CORS; Angular-ის სტრუქტურა; login, layout, JWT interceptor, ProblemDetails-ის ჩვენება; კურსები და ჯგუფები. სტუდენტები კოდს კითხულობენ, ლექტორი გეგმავს და review-ს აკეთებს.

📚 დაგეგმავს დავალებას AI-სთვის: `CLAUDE.md`, plan mode, OpenAPI როგორც კონტექსტი
📚 წაიკითხავს და შეაფასებს AI-ის დაწერილ კოდს
🛠 LMS | CORS API-ში
🛠 Angular: სტრუქტურა, login, layout, JWT interceptor, ProblemDetails-ის ჩვენება
🛠 გვერდები: კურსები, ჯგუფები, ჩარიცხვა

### 26. Angular + Claude Code #2

**თემები:** განრიგი, დასწრება, ნამუშევრის ატვირთვა, ქულები, შეტყობინებები; ბოლო review და შესწორებები; სრული აპლიკაციის დემო. **Frontend დასრულებულია** — სრული აპლიკაცია DevOps-ის კურსში იშვება სერვერზე.

📚 გაივლის სრულ review-ს AI-ის კოდზე და შეასწორებს
📚 დაინახავს სრულ აპლიკაციას: frontend + backend
🛠 LMS | Angular: განრიგი, დასწრება, ნამუშევრის ატვირთვა, ქულები, შეტყობინებები
🛠 ბოლო შესწორებები · სრული აპლიკაციის დემო · მზადაა DevOps-ში გასაშვებად

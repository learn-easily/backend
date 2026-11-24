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

ანემიური entity-ის პრობლემა; rich entity: დახურული setter-ები, factory მეთოდი, წესები entity-ში; Result pattern შეცდომისთვის exception-ის ნაცვლად; Value Object `Email` (EF Core-ის value conversion); ახალი feature: ჯგუფები (Group).

### 11. Aggregate და Concurrency

ჩარიცხვა ჯგუფში (R3); Aggregate და Aggregate Root (`Group` → `Enrollment`); ცვლილება მხოლოდ root-ის გავლით; პრობლემა: დავიწყებული `Include` და Repository pattern DDD-ში (რას ხსნის, როდის ღირს — კოდში 15-ში); race condition ბოლო ადგილზე; optimistic concurrency (`rowversion`) და unique index; ჯგუფიანი კურსის წაშლა → 409.

## პასუხები, შეცდომები და pipeline (3 ლექცია)

### 12. Middleware, Pipeline და Logging

როგორ გადის მოთხოვნა ASP.NET Core-ში: middleware-ების ჯაჭვი და მათი რიგი; ჩაშენებული middleware-ები; საკუთარი middleware (მოთხოვნის ლოგი: მეთოდი, მისამართი, სტატუსი, დრო); `ILogger`, ლოგის დონეები, structured logging.

### 13. შეცდომები და პასუხები: ერთი ფორმა ყველგან

API-ის პასუხის ნორმალიზაცია: ნებისმიერი შეცდომა — დომენის, ვალიდაციის, არარსებული მისამართის, 401/403, მოულოდნელი exception — ერთ ფორმაში ბრუნდება (ProblemDetails, RFC 9457); `ErrorType` და სტატუს კოდი ერთ ადგილას; `ResultExtensions` (`ToOk`, `ToCreated`, `ToNoContent`); `AddProblemDetails`, `IExceptionHandler`, `UseStatusCodePages`; production-ში დეტალების გარეშე; concurrency-ის ერთიანი დამუშავება.

### 14. ვალიდაცია და MediatR

FluentValidation; ვალიდაცია handler-ში ხელით → იგივე კოდი ყველა handler-ში; MediatR: `IRequest`, `IRequestHandler`, `ISender`; pipeline behavior-ები: ვალიდაცია და ლოგირება ერთ ადგილას; slice-ები MediatR-ზე.

## LMS-ის დასრულება (5 ლექცია)

### 15. განრიგი და დასწრება + Claude Code

ლექციები (R4) და დასწრება (R6); ჯგუფის aggregate იზრდება → `IGroupRepository` ხელით; პირველი slice ხელით, `CLAUDE.md` პროექტის წესებით (aggregate მხოლოდ Repository-ით); დანარჩენ slice-ებს Claude Code წერს, ჩვენ review-ს ვუკეთებთ; სიები pagination-ით.

### 16. Authentication და Configuration

`appsettings` და environment-ები; Options pattern (`JwtOptions`, `ValidateOnStart`); User Secrets; ანგარიშები; პაროლის hash Argon2id-ით; JWT: გაცემა და შემოწმება; claims.

### 17. Authorization

როლები და policy-ები; resource-based authorization: R5 („მხოლოდ თავისი ჯგუფის ლექტორი“).

### 18. ფაილები, დრო და შეფასება

დავალებები; ნამუშევრის ატვირთვა (`IFormFile`); შეფასება და დედლაინი (R7); `TimeProvider`.

### 19. Background Jobs და კურსის დასრულება

`BackgroundService`; შეხსენებები და მე-4 გაცდენის შეტყობინება (R6); კურსის ჩაბარება (R8). Backend დასრულებულია.

## Angular Claude Code-ით (2 ლექცია)

### 20. Angular + Claude Code #1: როგორ ვმუშაობთ AI-სთან

დაგეგმვა: `CLAUDE.md`, plan mode, OpenAPI როგორც კონტექსტი AI-სთვის; CORS; login, layout, JWT interceptor, კურსები და ჯგუფები.

### 21. Angular + Claude Code #2

განრიგი, დასწრება, ნამუშევრის ატვირთვა, ქულები; ბოლო review და შესწორებები. Frontend დასრულებულია; სრული აპლიკაცია DevOps-ის კურსში იშვება სერვერზე.

# შენი LMS: მთლიანად Vertical Slices-ზე

საშინაო · შენი LMS

## მოთხოვნები

- Courses: ხუთივე slice (Create · GetAll · GetById · Update · Delete)
- **Students** და **Lecturers**: იგივე ხუთ-ხუთი slice, `Features/Students/` და `Features/Lecturers/`. R2 (Email უნიკალურია) handler-ში
- თითო საქაღალდეს თავისი `…Endpoints.cs`: handler-ების რეგისტრაცია + `MapGroup`
- `Controllers` საქაღალდე, `AddControllers()`, `MapControllers()` და Swashbuckle **აღარ არის**; მხოლოდ Scalar

## ✓ მზადაა, როცა

`/scalar`-ში სამი ჯგუფია (Courses · Students · Lecturers), 15 endpoint, და ყოველი პასუხი იგივეა, რაც Controller-ებით იყო

## ⭐ ბონუსი

- `Program.cs` 20 ხაზზე ნაკლებია: რეგისტრაციები მხოლოდ `Add…Handlers()` და `Map…Endpoints()` გამოძახებებია
- ჩამოწერე ერთ წინადადებაში თითო handler-ის „შეცვლის მიზეზი“ (SRP). თუ ორი გამოგივიდა, slice ზედმეტად დიდია

## ამოხსნა

```csharp Features/Students/CreateStudent/CreateStudentEndpoint.cs !
public static class CreateStudentEndpoint
{
    public static void Map(IEndpointRouteBuilder app)
    {
        app.MapPost("/", async (CreateStudentRequest request, CreateStudentHandler handler) =>
            await handler.HandleAsync(request));
    }
}

// StudentEndpoints.cs
var group = app.MapGroup("/api/students").WithTags("Students");
CreateStudentEndpoint.Map(group);
// … დანარჩენი ოთხი slice
```

```csharp Features/Students/CreateStudent/CreateStudentHandler.cs
public class CreateStudentHandler
{
    private readonly DataContext _db;

    public CreateStudentHandler(DataContext db)
    {
        _db = db;
    }

    public async Task<IResult> HandleAsync(CreateStudentRequest request)
    {
        if (string.IsNullOrWhiteSpace(request.FirstName) ||
            string.IsNullOrWhiteSpace(request.LastName) ||
            string.IsNullOrWhiteSpace(request.Email))
            return Results.BadRequest("სახელი, გვარი და Email სავალდებულოა");

        var email = request.Email.Trim().ToLowerInvariant();
        if (await _db.Students.AnyAsync(s => s.Email == email))
            return Results.Conflict("ამ Email-ით სტუდენტი უკვე არსებობს");

        var student = new Student
        {
            FirstName = request.FirstName.Trim(),
            LastName = request.LastName.Trim(),
            Email = email,
            CreatedAt = DateTime.UtcNow
        };
        _db.Students.Add(student);
        await _db.SaveChangesAsync();
        return Results.Created($"/api/students/{student.Id}", student.ToResponse());
    }
}
```

```csharp Features/Students/StudentEndpoints.cs
public static class StudentEndpoints
{
    public static void AddStudentHandlers(this IServiceCollection services)
    {
        services.AddScoped<CreateStudentHandler>();
        services.AddScoped<GetStudentsHandler>();
        services.AddScoped<GetStudentByIdHandler>();
        services.AddScoped<UpdateStudentHandler>();
        services.AddScoped<DeleteStudentHandler>();
    }

    public static void MapStudentEndpoints(this IEndpointRouteBuilder app)
    {
        var group = app.MapGroup("/api/students").WithTags("Students");
        CreateStudentEndpoint.Map(group);
        GetStudentsEndpoint.Map(group);
        GetStudentByIdEndpoint.Map(group);
        UpdateStudentEndpoint.Map(group);
        DeleteStudentEndpoint.Map(group);
    }
}
```

```csharp Program.cs
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddOpenApi();
builder.Services.AddDbContext<DataContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("Default")));
builder.Services.AddCourseHandlers();
builder.Services.AddStudentHandlers();
builder.Services.AddLecturerHandlers();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
    app.MapScalarApiReference();
}

app.UseHttpsRedirection();
app.MapCourseEndpoints();
app.MapStudentEndpoints();
app.MapLecturerEndpoints();
app.Run();
```

```check
? Student-ის `ToEntity` Mapper-ში აღარ არის. რატომ?
= მას მხოლოდ ერთი slice იყენებს (CreateStudent), ამიტომ handler-ში დევს. საერთო რჩება მხოლოდ `ToResponse`: მას ხუთივე slice იყენებს
? Create-ისა და Update-ის შემოწმებები ისევ მეორდება. VSA-მ ეს რატომ ვერ მოაგვარა?
= VSA ფაილებს აწყობს feature-ის მიხედვით, წესების ადგილს კი არ ცვლის. წესები, რომლებიც ბიზნესის ცნებას (სტუდენტს, Email-ს) ეკუთვნის, ცალკე თემაა და შემდეგ ლექციებში მოგვარდება
```

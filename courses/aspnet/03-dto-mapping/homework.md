# MembersController — პაროლი გარეთ არ გადის

LibraryApi-ს ბიბლიოთეკის წევრები ემატება

## მოთხოვნები

- `Models/Member`: `Id` (Guid), `FullName`, `Email`, `PasswordHash`, `JoinedAt`
- `Dtos/`: **CreateMemberRequest** (FullName, Email, Password), **UpdateMemberRequest** (FullName, Email), **MemberResponse** (Id, FullName, Email, JoinedAt)
- `Mappers/MemberMapper` — პირდაპირ **Mapperly**-ით
- **MembersController** — სრული CRUD, სწორი სტატუს კოდები
- Create-ში: `Id`, `JoinedAt` და `PasswordHash` სერვერი ავსებს

## ✓ მზადაა, როცა

`passwordHash` არცერთ პასუხში არ ჩანს, POST არ ითხოვს `id`-ს და `joinedAt`-ს, Build-ზე Mapperly-ს გაფრთხილება არ რჩება

## ⭐ ბონუსი

- Create: ეს Email უკვე არსებობს → `Conflict()` (409)
- `GET /api/members/search?email=...` → `MemberResponse` ან 404

## 💡 მინიშნება

პაროლის hash-ისთვის სტანდარტი **Argon2id**-ია. .NET-ში ჩაშენებული არ არის — ვაყენებთ NuGet-იდან:

```bash
dotnet add package Isopoh.Cryptography.Argon2
```

```csharp
using Isopoh.Cryptography.Argon2;

member.PasswordHash = Argon2.Hash(request.Password);   // Argon2id, salt-ით
bool ok = Argon2.Verify(member.PasswordHash, password); // შემოწმება — შესვლისას
```

`Password` და `PasswordHash` სხვადასხვა სახელია — ნახეთ, რას გეტყვით Mapperly და როგორ უპასუხებთ.

## ამოხსნა

DTO-ები: `Password` მხოლოდ შემოდის, `PasswordHash` საერთოდ არსად გადის.

```csharp Dtos/MemberDtos.cs
public record CreateMemberRequest(
    string FullName, string Email, string Password);

public record UpdateMemberRequest(string FullName, string Email);

public record MemberResponse(
    Guid Id, string FullName, string Email, DateTime JoinedAt);
```

Mapper: ყველა „განზრახ გამოტოვებული“ ველი ცხადად წერია.

```csharp Mappers/MemberMapper.cs !
[Mapper]
public static partial class MemberMapper
{
    [MapperIgnoreSource(nameof(Member.PasswordHash))]
    public static partial MemberResponse ToResponse(this Member member);

    [MapperIgnoreSource(nameof(CreateMemberRequest.Password))]
    [MapperIgnoreTarget(nameof(Member.Id))]
    [MapperIgnoreTarget(nameof(Member.PasswordHash))]
    [MapperIgnoreTarget(nameof(Member.JoinedAt))]
    public static partial Member ToEntity(this CreateMemberRequest request);

    [MapperIgnoreTarget(nameof(Member.Id))]
    [MapperIgnoreTarget(nameof(Member.PasswordHash))]
    [MapperIgnoreTarget(nameof(Member.JoinedAt))]
    public static partial void UpdateFrom(
        [MappingTarget] this Member member, UpdateMemberRequest request);
}
```

Controller — Create, ბონუსით:

```csharp Controllers/MembersController.cs
[HttpPost]
public IActionResult Create(CreateMemberRequest request)
{
    if (_members.Any(m => m.Email == request.Email))
        return Conflict();

    var member = request.ToEntity();
    member.Id = Guid.NewGuid();
    member.JoinedAt = DateTime.UtcNow;
    member.PasswordHash = Argon2.Hash(request.Password);
    _members.Add(member);

    return CreatedAtAction(nameof(GetById),
        new { id = member.Id }, member.ToResponse());
}
```

```note
`Argon2.Hash` აბრუნებს ერთ სტრიქონს, მაგალითად `$argon2id$v=19$m=…,t=…,p=…$…`. მასშივე წერია ალგორითმი, პარამეტრები და „მარილი“ (salt) — ამიტომ ერთი და იგივე პაროლი ორჯერ ერთნაირ hash-ს არ იძლევა, და ცალკე სვეტი salt-ისთვის არ გვჭირდება. პაროლის შემოწმებას (`Argon2.Verify`) ავტორიზაციის თემაში ვნახავთ.
```

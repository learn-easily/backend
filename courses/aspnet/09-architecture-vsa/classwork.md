# შენი LMS: Courses → Vertical Slices

დავალება · შენი LMS

## ნაბიჯები

- `Features/Courses/` · `CourseResponse` + `CourseMapper` (მხოლოდ `ToResponse`)
- slice **CreateCourse**: `CreateCourseRequest` · `CreateCourseHandler` · `CreateCourseEndpoint`
- slice-ები **GetCourses** და **GetCourseById**
- `CourseEndpoints`: `AddCourseHandlers()` + `MapCourseEndpoints()` (`MapGroup("/api/courses")`) → Program.cs
- Swashbuckle → **Scalar**: `MapScalarApiReference()` → `/scalar`

## ✓ მზადაა, როცა

`/scalar`-ში სამივე endpoint მუშაობს და პასუხები იგივეა, რაც Controller-ით იყო (201 · 400 · 409 · 404)

## ⭐ ბონუსი

- slice-ები **UpdateCourse** და **DeleteCourse** და `CoursesController`-ის წაშლა
- შეადარე: რამდენ ფაილს ეხები, თუ „კურსის შექმნას“ ახალი ველი დაემატება, ადრე და ახლა?

## 💡 რჩევა

ჯერ ერთი slice ბოლომდე: CreateCourse. დაარეგისტრირე, გაუშვი და შეამოწმე. მხოლოდ მერე დანარჩენი. სანამ ყველა slice მზად არ არის, Controller და Minimal API ერთად იმუშავებს, ამიტომ `AddControllers` ბოლომდე არ წაშალო. Handler-ის ლოგიკა Controller-ის მეთოდიდან გადმოიტანე; შეიცვლება მხოლოდ `BadRequest()` → `Results.BadRequest()`.

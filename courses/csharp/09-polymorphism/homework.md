# ფიგურები 📐

ერთი `Area()` — სამი ფორმულა

## მოთხოვნები

- ახალი Console App: **Shapes**
- `Shape`: `Name`, `virtual double Area()` (აბრუნებს 0), `override ToString()` → „წრე: ფართობი 12.57“
- `Circle` (რადიუსი), `Rectangle` (სიგანე, სიმაღლე), `Triangle` (ფუძე, სიმაღლე) — სამივე `Shape`-ის შვილი, `override Area()`-ით
- ზომები — `{ get; private set; }`; უარყოფითი ზომა → 0
- Main-ში: `Shape[] shapes` — სამივე ტიპი; **ერთი** `foreach`: დაბეჭდე თითოეული, დაითვალე ჯამური ფართობი და იპოვე ყველაზე დიდი

## ✓ მზადაა, როცა

`Console.WriteLine(s)` ფიგურის სახელს და ფართობს ბეჭდავს; ციკლში არცერთი `if` ტიპზე არ არის; ახალი ფიგურა (მაგ. `Square`) მხოლოდ ახალ კლასს მოითხოვს

## ⭐ ბონუსი

- `Square : Rectangle` — კვადრატიც მართკუთხედია! `public Square(double side) : base(side, side)` — და `Area()`-ს წერა აღარ სჭირდება. სახელი? `override ToString()`

## ამოხსნა

```csharp Program.cs · Main !
Shape[] shapes =
{
    new Circle(2),
    new Rectangle(3, 4),
    new Triangle(6, 5)
};

double total = 0;
Shape largest = shapes[0];

foreach (Shape s in shapes)
{
    Console.WriteLine(s);
    total += s.Area();
    if (s.Area() > largest.Area()) largest = s;
}

Console.WriteLine($"ჯამური ფართობი: {total:F2}");
Console.WriteLine($"ყველაზე დიდი: {largest.Name}");
```

```csharp Shape.cs · Circle.cs · Rectangle.cs
internal class Shape
{
    public string Name { get; private set; }

    public Shape(string name)
    {
        Name = name;
    }

    public virtual double Area()
    {
        return 0;
    }

    public override string ToString()
    {
        return $"{Name}: ფართობი {Area():F2}";
    }
}

internal class Circle : Shape
{
    public double Radius { get; private set; }

    public Circle(double radius) : base("წრე")
    {
        if (radius < 0) radius = 0;
        Radius = radius;
    }

    public override double Area()
    {
        return Math.PI * Radius * Radius;
    }
}

internal class Rectangle : Shape
{
    public double Width { get; private set; }
    public double Height { get; private set; }

    public Rectangle(double width, double height) : base("მართკუთხედი")
    {
        Width = width;
        Height = height;
    }

    public override double Area()
    {
        return Width * Height;
    }
}
```

```note
`Triangle` — იგივე სქემით: `Base * Height / 2`. `Math.PI` — C#-ის მზა `Math` კლასიდან. `{Area():F2}` — ორი ციფრი მძიმის შემდეგ. მთავარი: ციკლმა არ იცის, რომელი ფიგურაა — `s.Area()` ყოველთვის სწორ ფორმულას იძახებს. ეს არის პოლიმორფიზმი.
```

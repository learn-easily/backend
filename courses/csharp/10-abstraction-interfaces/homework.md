# ჭკვიანი სახლი 🏠

მოწყობილობები — abstract კლასით, რეგულირება — ინტერფეისით

## მოთხოვნები

- Console App **SmartHome**. `abstract class Device`: `Name`, `IsOn { get; private set; }`, `TurnOn()`, `TurnOff()`, `abstract string Status()` და `override ToString()` → „🟢 ნათურა: ანთია 💡“
- `interface IAdjustable`: `void Increase()` და `void Decrease()`
- `Lamp : Device` (ანთია / ჩამქრალია) · `Thermostat : Device, IAdjustable` (10–30°C, თავიდან 20) · `Speaker : Device, IAdjustable` (ხმა 0–10, თავიდან 5)
- Main-ში: `Device[]` → ყველა ჩართე და დაბეჭდე; `IAdjustable[]` → ყველას აუწიე

## ✓ მზადაა, როცა

`new Device(...)` წითელ ხაზს აჩენს; ნათურა `IAdjustable[]`-ში არ ეტევა; ტემპერატურა და ხმა საზღვრებს არ სცდება

## ⭐ ბონუსი

- `interface ITimer` (`void SetTimer(int minutes)`) — ნათურასა და დინამიკს. ერთი კლასი — ორი ინტერფეისი: `class Speaker : Device, IAdjustable, ITimer`

## ამოხსნა

```csharp Program.cs · Main !
Lamp lamp = new Lamp("ნათურა");
Thermostat thermo = new Thermostat("თერმოსტატი");
Speaker speaker = new Speaker("დინამიკი");

Device[] devices = { lamp, thermo, speaker };
foreach (Device d in devices)
{
    d.TurnOn();
    Console.WriteLine(d);
}

IAdjustable[] adjustables = { thermo, speaker };
foreach (IAdjustable a in adjustables)
{
    a.Increase();
}
```

```csharp Device.cs · IAdjustable.cs
internal abstract class Device
{
    public string Name { get; private set; }
    public bool IsOn { get; private set; }

    public Device(string name)
    {
        Name = name;
    }

    public void TurnOn() { IsOn = true; }
    public void TurnOff() { IsOn = false; }

    public abstract string Status();

    public override string ToString()
    {
        string power = IsOn ? "🟢" : "⚫";
        return $"{power} {Name}: {Status()}";
    }
}

internal interface IAdjustable
{
    void Increase();
    void Decrease();
}
```

```csharp Lamp.cs · Thermostat.cs
internal class Lamp : Device
{
    public Lamp(string name) : base(name) { }

    public override string Status()
    {
        return IsOn ? "ანთია 💡" : "ჩამქრალია";
    }
}

internal class Thermostat : Device, IAdjustable
{
    public int Temperature { get; private set; } = 20;

    public Thermostat(string name) : base(name) { }

    public void Increase()
    {
        if (Temperature < 30) Temperature++;
    }

    public void Decrease()
    {
        if (Temperature > 10) Temperature--;
    }

    public override string Status()
    {
        return $"{Temperature}°C";
    }
}
```

```note
`Speaker` — როგორც `Thermostat`, ოღონდ `Volume` 0–10. `Device`-ის `ToString()` `Status()`-ს იძახებს — abstract მეთოდს, რომელსაც ყოველი მოწყობილობა თავისებურად წერს. ნათურა `IAdjustable[]`-ში არ ეტევა: მისი „აწევა“ შეუძლებელია — და კომპილატორი ამას თვითონ ამოწმებს.
```

-- CinemaDb — საშინაო დავალება
CREATE DATABASE CinemaDb;
GO
USE CinemaDb;
GO

CREATE TABLE Movies (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Title NVARCHAR(200) NOT NULL,
    DurationMinutes INT NOT NULL,
    ReleaseYear INT NOT NULL
);

CREATE TABLE Sessions (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    MovieId INT NOT NULL FOREIGN KEY REFERENCES Movies(Id),
    StartsAt DATETIME2 NOT NULL,
    Price DECIMAL(6,2) NOT NULL
);

INSERT INTO Movies (Title, DurationMinutes, ReleaseYear)
VALUES (N'ოპენჰაიმერი', 180, 2023), (N'ინტერსტელარი', 169, 2014),
       (N'დიუნა: ნაწილი მეორე', 166, 2024);
INSERT INTO Sessions (MovieId, StartsAt, Price)
VALUES (1, '2026-11-02T19:30:00', 15.00), (2, '2026-11-02T21:00:00', 12.00),
       (3, '2026-11-02T18:00:00', 14.00), (1, '2026-11-03T20:00:00', 15.00);
GO

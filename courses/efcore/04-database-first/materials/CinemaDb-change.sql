-- DBA-ს ცვლილება: დარბაზები
USE CinemaDb;
GO
CREATE TABLE Halls (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(50) NOT NULL UNIQUE,
    Seats INT NOT NULL
);
ALTER TABLE Sessions ADD HallId INT NULL FOREIGN KEY REFERENCES Halls(Id);
GO
INSERT INTO Halls (Name, Seats) VALUES (N'დიდი დარბაზი', 220), (N'VIP', 40);
UPDATE Sessions SET HallId = 1 WHERE Id IN (1, 3);
UPDATE Sessions SET HallId = 2 WHERE Id = 2;
GO

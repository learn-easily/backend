-- StoreDb — „არსებული“ ბაზა, რომელიც DBA-მ შექმნა (მე ვაჩვენებ)
CREATE DATABASE StoreDb;
GO
USE StoreDb;
GO

CREATE TABLE Categories (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(50) NOT NULL
);

CREATE TABLE Products (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100) NOT NULL,
    Description NVARCHAR(500) NULL,
    Price DECIMAL(10,2) NOT NULL,
    CreatedAt DATETIME2 NOT NULL DEFAULT GETDATE(),
    CategoryId INT NOT NULL FOREIGN KEY REFERENCES Categories(Id)
);

CREATE TABLE Customers (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    FullName NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO Categories (Name) VALUES (N'ტექნიკა'), (N'აქსესუარები');
INSERT INTO Products (Name, Price, CategoryId)
VALUES (N'ლეპტოპი', 2400, 1), (N'მაუსი', 45, 2), (N'კლავიატურა', 120, 2);
INSERT INTO Customers (FullName, Email)
VALUES (N'გიორგი მაისურაძე', N'giorgi@mail.ge');
GO

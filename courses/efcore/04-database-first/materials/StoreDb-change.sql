-- DBA-ს ცვლილება: მომხმარებელს ტელეფონი
USE StoreDb;
GO
ALTER TABLE Customers ADD Phone NVARCHAR(20) NULL;
GO

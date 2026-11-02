-- DBA-ს ცვლილება: წიგნს გვერდების რაოდენობა
USE LibraryDb;
GO
ALTER TABLE Books ADD Pages INT NULL;
GO

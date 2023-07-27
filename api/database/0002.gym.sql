-- Base table for gym information
create table dbo.gym(
	gym_id UNIQUEIDENTIFIER DEFAULT NEWID() PRIMARY KEY,
	gym_name NVARCHAR(50) NOT NULL,
	subdomain VARCHAR(20) NOT NULL
)

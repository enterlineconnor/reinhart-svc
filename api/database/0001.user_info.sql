-- Base table for client information
create table dbo.user_info(
	user_id UNIQUEIDENTIFIER DEFAULT NEWID() PRIMARY KEY,
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	phone NVARCHAR(20) NOT NULL,
	email NVARCHAR(50) NOT NULL
)

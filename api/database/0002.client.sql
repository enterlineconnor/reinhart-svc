-- Base table for client information
create table dbo.client(
	client_id UNIQUEIDENTIFIER DEFAULT NEWID() PRIMARY KEY,
	gym_id UNIQUEIDENTIFIER NOT NULL,
	FOREIGN KEY (gym_id) REFERENCES dbo.gym(gym_id),
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	phone NVARCHAR(20) NOT NULL,
	email NVARCHAR(50) NOT NULL
)

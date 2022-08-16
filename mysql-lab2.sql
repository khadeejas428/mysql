CREATE TABLE IF NOT EXISTS users( 
	id int NOT NULL AUTO_INCREMENT, 
	name VARCHAR(100) NOT NULL, 
	email VARCHAR(100) NOT NULL, 
  	password varchar(50) NOT NULL,
	PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS complaints( 
	id INT NOT NULL AUTO_INCREMENT, 
	user_id INT, 
  	complaint text NOT NULL,
  	`date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(id), 
	FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS employee( 
	id INT NOT NULL AUTO_INCREMENT, 
	user_id INT, 
	complaints_details INT,
  	complaintreview ENUM('completed','inprogress','stuck'),
	PRIMARY KEY(id),
	FOREIGN KEY(user_id) REFERENCES users(id)
	FOREIGN KEY(complaints_details) REFERENCES complaints(id)
);
select complaints.user_id,complaints.complaint from complaints left join employee

CREATE TABLE IF NOT EXISTS agent( 
	id INT NOT NULL, 
	user_id INT, 
	complaints_details INT,
	employee_id INT,
	PRIMARY KEY(id), 
	FOREIGN KEY(user_id) REFERENCES users(id)
	FOREIGN KEY(complaints_details) REFERENCES complaints(id)
	FOREIGN KEY(employee_id)REFERENCES employee(id)

);
select * from (select complaints.user_id,complaints.complaint from complaints left join employee)
where complaints. user_id = 'employee-id'or complaints.user_id is null





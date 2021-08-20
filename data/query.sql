
# --------------------------------------------------------------------
DROP TABLE users;

CREATE TABLE users(
	user_id VARCHAR(10),
	pwd VARCHAR(20) NOT NULL,
	name VARCHAR(20) NOT NULL,
	email VARCHAR(40),
	phone VARCHAR(20),
	regdate DATE NOT NULL
);

ALTER TABLE users ADD PRIMARY KEY (user_id);
# --------------------------------------------------------------------
DROP TABLE udata;

CREATE TABLE udata(
	num INT,
	id VARCHAR(10),
	schooltype VARCHAR(10),
	majorcate VARCHAR(10),
	age VARCHAR(10),
	intern VARCHAR(10),
	toeic VARCHAR(10),
	tosp VARCHAR(10),
	train VARCHAR(10),
	jobseek VARCHAR(10),
	cert VARCHAR(10),
	jobsearch VARCHAR(10),
	yrwish VARCHAR(10),
	wishhr VARCHAR(10),
	wishsalary VARCHAR(10),
	jobgradu VARCHAR(10),
	liveexp VARCHAR(10),
	datadate DATE	
);

ALTER TABLE udata ADD PRIMARY KEY (num);
ALTER TABLE udata MODIFY num INT AUTO_INCREMENT;
ALTER TABLE udata AUTO_INCREMENT = 1;
ALTER TABLE udata ADD CONSTRAINT FOREIGN KEY (id) REFERENCES users(user_id);

# --------------------------------------------------------------------
DROP TABLE res;

CREATE TABLE res(
	num INT,
	id VARCHAR(20),
	result VARCHAR(200) NOT NULL,
	resdate DATE
);

ALTER TABLE res ADD PRIMARY KEY (num);
ALTER TABLE res MODIFY num INT AUTO_INCREMENT;
ALTER TABLE res AUTO_INCREMENT = 1;
ALTER TABLE res ADD CONSTRAINT FOREIGN KEY (id) REFERENCES users(user_id);
# --------------------------------------------------------------------



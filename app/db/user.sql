CREATE DATABASE student;
use student;
GRANT ALL on student to root@localhost;

CREATE TABLE vacdetails (
  RegNo int AUTO_INCREMENT,
  Name varchar(50) NULL,
  Vaccination_Status varchar(3) NULL,
  PRIMARY KEY (RegNo)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert into vacdetails(RegNo,Name,Vaccination_Status) values
(1,'Aditi Khule','Yes'),
(2,'Rahul Kumar','No'),(3,'Sunny Singh','No'),(4,'Rani Deo','Yes'),(5,'Mehul Sharma','No'),(6,'Chanda Pathak','Yes'),(7,'Sasha Gupta','Yes')
;

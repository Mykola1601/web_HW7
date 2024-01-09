
DROP TABLE  IF EXISTS "groups";
CREATE TABLE IF NOT EXISTS "groups" (
     id INTEGER PRIMARY KEY AUTOINCREMENT not null,
     group_name string UNIQUE NOT NULL
    );


DROP TABLE  IF EXISTS teachers;
CREATE TABLE IF NOT EXISTS teachers (
     id INTEGER PRIMARY KEY AUTOINCREMENT not null,
     teacher_name STRING NOT NULL
    );


DROP TABLE  IF EXISTS students;
CREATE TABLE IF NOT EXISTS students (
     id INTEGER PRIMARY KEY AUTOINCREMENT not null,
     student_name STRING  NOT NULL,
     group_id REFERENCES "groups" (id)
    );


DROP TABLE  IF EXISTS disciplines;
CREATE TABLE IF NOT EXISTS disciplines (
     id INTEGER PRIMARY KEY AUTOINCREMENT not null,
     discipline_name STRING UNIQUE NOT NULL,
     teacher_id REFERENCES teachers (id)
    );


DROP TABLE  IF EXISTS grades;
CREATE TABLE IF NOT EXISTS grades (
     id INTEGER PRIMARY KEY AUTOINCREMENT not null,
     discipline_id REFERENCES  disciplines (id),
     student_id REFERENCES students  (id),
     grade INTEGER,
     date_off DATE
    );






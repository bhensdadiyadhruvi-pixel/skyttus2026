CREATE TABLE stud(
	stude_id INT,
	name VARCHAR(50),
	department VARCHAR(30),
	year INT,
	marks INT
);

INSERT INTO stude VALUES
(1, 'Dhruvi','It', 1, 82),
(2, 'kittu',  'CSE', 4, 76),
(3, 'yug','ECE', 3, 91),
(4, 'jenny','CSE', 2, 68),
(5, 'jay','ECE', 1, 88);


SELECT * FROM stude;

SELECT name, department FROM stude;

SELECT * FROM stude
WHERE marks > 75;


SELECT * FROM stude
WHERE department = 'CSE';

SELECT * FROM students
ORDER BY marks DESC;

SELECT * FROM students
ORDER BY marks DESC
LIMIT 3;


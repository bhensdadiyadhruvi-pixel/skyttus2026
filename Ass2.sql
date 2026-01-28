CREATE TABLE stude(
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

SELECT COUNT(*) AS total_stude
FROM stude;

SELECT AVG(marks) AS average_marks
FROM stude;

SELECT 
	MAX(marks) AS highest_marks,
	MIN(marks) AS lowest_marks
FROM stude;


SELECT department, AVG(marks) AS avg_marks
FROM stude
GROUP BY department;


SELECT department, AVG(marks) AS avg_marks
FROM stude
GROUP BY department
HAVING AVG(marks) > 70;


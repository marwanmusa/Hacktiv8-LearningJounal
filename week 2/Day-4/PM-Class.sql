SELECT * FROM teachers;

-- Membuat table courses
CREATE TABLE courses (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(20),
    teachers_id INT,
    total_students INT
    );
    
-- Inserting courses data
INSERT INTO courses (name, teachers_id, total_students)
    VALUES  ('Calculus', 2, 20),
            ('Physics', 2, 10),
            ('Calculus', 1, 30),
            ('Computer Science', 1, 20),
            ('Politic', 13, 15),
            ('Algebra', 2, 10),
            ('Algebra', 13, 30),
            ('Computer Science', 10, 35),
            ('Life Science', 11, 20),
            ('Chemistry', 9, 22),
            ('Chemistry', 8, 16),
            ('Calculus', 5, 19),
            ('Politic', 4, 17),
            ('Biology', 6, 22),
            ('Physics', 3, 29),
            ('Biology', 8, 28),
            ('Calculus', 12, 34),
            ('Physics', 13, 34),
            ('Biology', 14, 25),
            ('Calculus', 15, 20);
            
-- Menampilkan table courses
SELECT * from courses;

-- Join table teachers and courses / inner join
SELECT *  from teachers
join courses on teachers.id = courses.teachers_id;

-- Join table teachers and courses / left join
select * from teachers
left join courses on teachers.id = courses.teachers_id;

-- Join table teachers and courses / right join
select * from teachers
RIGHT join courses on teachers.id = courses.teachers_id;

-- Join table teachers and courses / outer join
select * from teachers
left OUTER join courses on teachers.id = courses.teachers_id
UNION
select * from teachers
RIGHT OUTER join courses on teachers.id = courses.teachers_id;

-- Menampilkan nama dosen dan course namenya
SELECT teachers.first_name, teachers.last_name, courses.name
from teachers
join courses on teachers.id = courses.teachers_id;

-- Menampilkan dosen mengajar calculus
select *
FROM teachers
join courses on teachers.id = courses.teachers_id
WHERE courses.name = 'calculus';

-- Melihat jumlah mata kuliah di setiap universitas
select teachers.school, count(courses.name) as total_mk
FROM teachers
join courses on teachers.id = courses.teachers_id
group by teachers.school;

-- Subquery atau inner query
-- Menampilkan nama dosen yang memiliki gaji tertinggi
SELECT first_name, last_name, salary
FROM teachers
WHERE salary = (SELECT MAX(salary) from teachers);

-- Menampilkan rata-rata gaji dosen di cambridge
SELECT school, AVG(salary) as 'Rata-rata Gaji', FLOOR(AVG(salary)), CEIL(AVG(salary))
FROM teachers
WHERE school = 'cambridge university';

-- Dosen dengan gaji tinggi di setiap universitas
SELECT first_name, last_name, school, salary
FROM teachers
where (salary) in (SELECT  max(salary)
                           from teachers
                           GROUP by school);

-- Melihat nama dosen dan jumlah m.k yang diajarkan
select teachers.first_name, COUNT(courses.name) as jum_matkul
from teachers
join courses on teachers.id = courses.teachers_id
GROUP by teachers.first_name
order by jum_matkul DESC;

-- Menampilkan univ yang total m.k lebih dari 5
SELECT teachers.school, COUNT(courses.name) as total_matkul
from teachers
join courses on teachers.id = courses.teachers_id
GROUP BY teachers.school
HAVING total_matkul > 5;

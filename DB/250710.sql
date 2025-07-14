-- 250710 pratice
-- 1
ALTER TABLE tb_employee
ADD COLUMN department_id INT,
ADD CONSTRAINT fk_employee_department
FOREIGN KEY (department_id) REFERENCES tb_department(id);

-- 2
UPDATE tb_employee SET department_id = 1 WHERE id IN (1, 2);
UPDATE tb_employee SET department_id = 2 WHERE id = 3;
UPDATE tb_employee SET department_id = 4 WHERE id = 4;
UPDATE tb_employee SET department_id = 3 WHERE id = 5;

-- 3
SELECT d.name AS department_name, AVG(e.salary) AS avg_salary
FROM tb_employee AS e
JOIN tb_department AS d 
ON e.department_id = d.id
GROUP BY d.name;

SELECT name, salary
FROM tb_employee
ORDER BY salary DESC
LIMIT 3;

SELECT name, start_date
FROM tb_project
ORDER BY start_date ASC
LIMIT 2;

SELECT *
FROM tb_employee
ORDER BY id
LIMIT 2 OFFSET 2;  
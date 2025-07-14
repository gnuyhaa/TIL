-- 실습 테이블 생성
CREATE TABLE Students (
    StudentID INT NOT NULL AUTO_INCREMENT,
    Name VARCHAR(255),
    Age INT,
    Address VARCHAR(255),
    PRIMARY KEY(StudentID)
);

CREATE TABLE Grades (
    StudentID INT,
    Math INT,
    English INT,
    Science INT
);

-- 실습 테이블 데이터 입력
INSERT Students (Name, Age, Address)
VALUES('홍길동',30,'인천'),('이연걸',60,'서울'),('이몽룡',42,'대전'),('성춘향',27,'경기');

INSERT Grades (StudentID, Math, English, Science)
VALUES (1,90,80,50),(2,69,76,65),(3,98,87,97),(4,87,67,79);

CREATE TABLE Students (
    StudentID INT NOT NULL AUTO_INCREMENT,
    Name VARCHAR(16),
    Email VARCHAR(32),
    Phone VARCHAR(16),
    Major VARCHAR(16),
    PRIMARY KEY(StudentID)
);


-- practice 
CREATE TABLE tb_employee (
    id INT AUTO_INCREMENT,
    name VARCHAR(255),
    position VARCHAR(255),
    hire_date DATE,
    is_active BOOLEAN,
    PRIMARY KEY (id)
);

CREATE TABLE tb_department (
    id INT AUTO_INCREMENT,
    name VARCHAR(255),
    created_at DATETIME,
    PRIMARY KEY (id)
);

CREATE TABLE tb_project (
    id INT AUTO_INCREMENT,
    name VARCHAR(255),
    start_date DATE,
    is_finish BOOLEAN,
    PRIMARY KEY (id)
);


INSERT INTO tb_employee (name, position, hire_date, is_active) VALUES
('김아형', '개발자', '2022-03-01', TRUE),
('오수빈', '디자이너', '2023-05-10', FALSE),
('정은지', '기획자', '2021-09-20', TRUE),
('김지우', '마케터', '2020-01-15', FALSE),
('김유선', '개발자', '2023-11-30', TRUE);

INSERT INTO tb_department (name, created_at) VALUES
('개발팀', '2020-01-01 09:00:00'),
('디자인팀', '2020-02-01 10:00:00'),
('기획팀', '2020-03-01 11:00:00'),
('마케팅팀', '2020-04-01 12:00:00'),
('관리팀', '2020-05-01 13:00:00');

INSERT INTO tb_project (name, start_date, is_finish) VALUES
('홈페이지 개편', '2023-01-10', TRUE),
('앱 출시', '2023-02-20', FALSE),
('브랜드 리뉴얼', '2022-10-05', TRUE),
('내부 시스템 개발', '2023-07-15', FALSE),
('고객 설문 조사', '2023-03-01', TRUE);

SELECT name, hire_date
FROM tb_employee
WHERE is_active = TRUE;

------- 250709 adv
ALTER TABLE tb_employee ADD COLUMN salary INT;
UPDATE tb_employee SET salary = 5000 WHERE id = 1;
UPDATE tb_employee SET salary = 6000 WHERE id = 2;
UPDATE tb_employee SET salary = 4500 WHERE id = 3;
UPDATE tb_employee SET salary = 7000 WHERE id = 4;
UPDATE tb_employee SET salary = 5200 WHERE id = 5;


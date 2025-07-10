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
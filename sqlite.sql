

--테이블 생성
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    pw TEXT NOT NULL, 
    usertype TEXT NOT NULL CHECK(usertype IN ('학생', '학부모')),
    grade TEXT NOT NULL CHECK(grade IN ('중3', '중2', '중1', '고3', '고2', '고1', 'N수')),
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

drop table user;

select * from user;

-- 데이터 추가하기
insert into user(id, pw, usertype, grade)
values('test', '123', '학생', 'N수')

insert into user(id, pw, usertype, grade)
values('test', '123', '학생', 'N수')

insert into user(username, password, email, gender)
values('test1', '123', 'test@gmail.com', 'male')

-- 데이터 삭제
delete from user where username ='test1';
-- 데이터 검색
select * from user where username='test';
select * from user;
-- 데이터 수정
update user SET email = 'sample@gmail.com', gender='female' where username='test';
-- drop table user3

CREATE TABLE IF NOT EXISTS test_results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    test_name TEXT NOT NULL,
    score INTEGER NOT NULL,
    test_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(id)
);
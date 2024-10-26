create table user3(
    userid integer primary key autoincrement, 
    username text not null, 
    password text not null,
    email text not null,
    gender text check(gender in ('male', 'female')),
    create_at timestamp default CURRENT_TIMESTAMP
);
-- insert into user3(username, password, email, gender)
-- values('test', '123', 'test@gmail.com', 'male')
-- drop table user3
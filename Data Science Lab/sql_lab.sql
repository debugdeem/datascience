create database lab1;
use lab1;
create table users(
	id INT auto_increment primary key,
    name varchar(20),
    email varchar(30)
    );
insert into users (name, email)
values ('John Doe', 'john.doe@lab1.com');
select * from users;
update users
set email = 'john.doe@lab1.biz');
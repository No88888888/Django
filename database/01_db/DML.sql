CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

SELECT first_namr, age from users;
select * from users;
select rowid from users;
select name,age from users order by age;
select name,age from users order by age desc;
select neme, age, balance from users order by age, balance desc;
select country from users;
select distinct country from users;
select distinct country from users order by country;
select distinct name, county from users; 
select distinct name, country from users order by country;
select name, age, balance from users where age >= 30;
select name, age, balance from users where age >= 30 and balance > 500000;

select name from users where first_name like '%호%';
select name from users where first_name like '%준';
select name, phne from users where phone like '02-%';
select name, age from users where age like '2_';
select name, phone from users where phone like '%-51__-%';

DROP table users;

SELECT first_name, last_name, age from users;

select * from users;

-- 숨어있는 rowid 조회
select rowid, first_name from users;

-- ORDER BY
-- 나이로 오름차순 정렬
select first_name,age from users order by age ASC;

-- 나이로 오름차순, 계좌 수로 내림차순 정렬
select first_name, age, balance from users order by age, balance DESC;


-- FILRTERING
-- 모든 지역 조회
select country from users;

-- 중복없이 지역 조회
select distinct country from users;

-- 중복없이, 내림차순 정렬하여 조회
select distinct country from users order by country;

-- 이름 지역 중복없이 모든 이름, 지역 조회
select distinct first_name, country from users;

-- 이름 지역 중복없이 모든 이름, 지역을 지역 내림차순으로 조회
select distinct first_name, country from users ORDER BY country DESC;

-- 나이 30살 이상인 사람의 이름, 나이, 계좌 조회
select first_name, age, balance from users where age >= 30;


-- 나이 30살 이상이고 계좌 50만원 이상 사람의 이름, 나이, 계좌 조회
select first_name, age, balance from users where age >= 30 and balance > 500000;

-- 이름에 호가 들어가는 사람 조회
select first_name from users where first_name like '%호%';

-- 이름이 준으로 끝나는 사람 조회
select first_name from users where first_name like '%준';

-- 서울 지역사람 조회
select first_name, phone from users where phone like '02-%';

-- 20대 조회
SELECT first_name, age from users where age like '2_';

-- 전화번호 중간 4자리의 시작이 51로 시작하는 사람 조회
select first_name, phone from users where phone like '%-51__-%';

-- 경기도, 강원도 거주자 조회
select first_name, country from users where country in ('경기도', '강원도');
select first_name, country from users where country = '경기도' or country ='강원도';

-- 경기도, 강원도 외 거주자 조회
select first_name, country from users where country not in ('경기도', '강원도');

-- 20~30세 조회
select first_name, age from users where age BETWEEN 20 and 30;

-- 20~30세 외 조회
select first_name, age from users where age not BETWEEN 20 and 30;
select first_name, age from users where age < 20 or age > 30;

-- 계좌 상위 10 조회
select first_name, balance from users order by balance DESC LIMIT 10;

-- 나의 오름차순 기준 상위 5 조회
select first_name, age from users order by age LIMIT 5;

-- 중간 10 이후부터 10개 조회
select rowid, first_name from users LIMIT 10 offset 10;

-- 지역별 그룹 만들고 그룹당 갯수 카운트
select country, COUNT(*) from users group by country;

-- 전체 사람 수 카운트
select count(*) from users;

-- 30세 이상 사람들의 평균 나이
select avg(age) from users where age >=30;

-- 성씨 별 카운트
select last_name, count(*) from users group by last_name;

-- 지역별 평균 나이
select country, avg(age) from users group by country;


-- CREATE
create table classmates (
    name text not null,
    age integer not null,
    address text not NULL
);

insert into classmates (name, age, address) values ('홍길동', 23, '서울');
insert into classmates values ('홍길은', 24, '인천');

update classmates set name='김철수한무두루미', address='제주도' where rowid = 2;

delete from classmates where rowid = 2;

select rowid, * from classmates;

delete from classmates;


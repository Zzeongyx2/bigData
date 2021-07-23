--실습1
--현재 시간 조회
select now();

--현재 시간 - 1일
select now(), now()::date - '1 day' ::interval;

--현재 타임존 조회
show timezone;

--시스템 일자
select current_date, current_time, timeofday();

select now(), current_timestamp, timestamp 'now';

--날짜에서 연도 추출
select date_part('year', timestamp '2020-07-30 20:38:40');
select date_part('year', current_timestamp);

select extract('isoyear' from date '2006-01-01');
select extract('isoyear' from current_timestamp);

select date_trunc('year', timestamp '2020-07-30 20:38:40');
select date_trunc('year', current_timestamp);

--날짜에서 월 추출
select date_part('month', timestamp '2020-07-30 20:38:40');
select date_part('month', current_timestamp);

select extract('month' from timestamp '2020-07-30 20:38:40');
select extract('month' from interval '2 years 3 months');
select extract('month' from interval '2 years 13 months');

select date_trunc('month', timestamp '2020-07-30 20:38:40');

--날짜에서 일 추출
select date_part('day', timestamp '2020-07-30 20:38:40');

select date_trunc('day', timestamp '2020-07-30 20:38:40');

--시간에서 시 추출
select date_part('hour', timestamp '2013-07-30 20:38:40');
select date_part('hour', interval '4 hours 3 minutes');

select date_trunc('hour', timestamp '2020-07-30 20:38:40');

--시간에서 분 추출
select date_part('minute', timestamp '2020-07-30 20:38:40');

select date_trunc('minute', timestamp '2020-07-30 20:38:40');

--시간에서 초 추출
select date_part('second', timestamp '2013-07-30 20:38:40');

select extract('second' from time '17:12:28.5');

select date_trunc('second', timestamp '2013-07-30 20:38:40');


--실습2
--주수 구하기
select EMP_NAME, to_char((current_timestamp - ENT_DATE),'W') WEEKS
from cslee.TB_EMP
where ORG_CD = '10';

--to char
select emp_name, ent_date,
	to_char(ent_date,'yyyy') 입사년,
	to_char(ent_date,'MM') 입사월,
	to_char(ent_date,'DD') 입사일
from cslee.tb_emp;

--extract
select emp_name, ent_date, 
extract('year' from ent_date) 입사년,
extract('month' from ent_date) 입사월,
extract('day' from ent_date) 입사일
from cslee.tb_emp;

--변환함수(to_date, to_number, to_timestamp, cast)
select to_date('05 Dec 2000', 'DD Mon YYYY');

select to_number('12,454.8-', '99G999D9S');

select to_timestamp('05 Dec 2000', 'DD Mon YYYY');

select CAST(123.4 AS VARCHAR(10)), 
	CAST('123.5' AS NUMERIC),
	CAST(1234.5678 AS DEC(6,2)),
	CAST(CURRENT_TIMESTAMP AS DATE),
	TO_CHAR(CURRENT_TIMESTAMP, 'YYYY-MM-DD HH24:MI:SS'), 
	TO_CHAR(1234.56, 'L9,999.99'), 
	TO_NUMBER('$12,345', '$99,999'), 
	TO_DATE('2014/03/01 21:30:18','YYYY/MM/DD HH24:MI:SS'), 
	TO_TIMESTAMP('2014/03/01 21:30:18','YYYY/MM/DD HH24:MI:SS');

--case
select emp_name,
	case when salary > 50000000
	then salary
	else 50000000
	end as revised_salary
from cslee.tb_emp;

select org_name,
	case org_name
		when '영업1팀' then '지사'
		when '영업2팀' then '지사'
		when '영업3팀' then '지사'
		when '경영관리팀' then '본사'
		else '지점'
	end as AREA
from cslee.tb_org;

select EMP_NAME, 
	case when SALARY >= 90000000 then 'HIGH'
		when SALARY >= 60000000 then 'MID'
		else 'LOW'
	end as SALARY_GRADE
from cslee.TB_EMP;

--중첩 case
select EMP_NAME, SALARY, 
	case when SALARY >= 50000000
			then 20000000
		else (case when SALARY >= 20000000
						then 10000000
					else SALARY * 0.5
				end)
	end as BONUS
from cslee.TB_EMP;

--null
--coalesce
select EMP_NAME, position, 
	coalesce(POSITION,'없음')
from cslee.TB_EMP;

--case
select EMP_NAME, POSITION, 
case when POSITION IS NULL
then '없음'
else POSITION
end as 직책
from cslee.TB_EMP

--null과 공집합
select coalesce(salary, 0) SAL 
from cslee.tb_emp
where emp_name='김태진';

select MAX(salary) SAL 
from cslee.tb_emp
where emp_name='김태진';

select coalesce(MAX(salary), 9999) SAL 
from cslee.tb_emp
where emp_name='김태진';


--실습3
--집계함수
select COUNT(*) "전체건수", 
	COUNT(POSITION) "직책건수",
	COUNT(DISTINCT POSITION) "직책종류", 
	MAX(SALARY) "최대", 
	MIN(SALARY) "최소", 
	AVG(SALARY) "평균"
from cslee.TB_EMP;

--group by
select POSITION "직책", 
COUNT(*) "인원수", 
MIN(SALARY) "최소", 
MAX(SALARY) "최대", 
AVG(SALARY) "평균"
from cslee.TB_EMP
group by position;

--having
select ORG_CD "부서", 
COUNT(*) "인원수", 
AVG( SALARY) "평균"
from cslee.TB_EMP
group by ORG_CD
having COUNT(*) >= 4;

select ORG_CD "부서", 
MAX(SALARY) "최대"
from cslee.TB_EMP
group by ORG_CD 
having MIN(SALARY) <= 40000000;

select ORG_CD, POSITION, AVG( SALARY) 
from cslee.TB_EMP
where POSITION IN ('과장','대리','사원')
group by ORG_CD, POSITION;

--고급 집계쿼리
select ORG_CD, 
	AVG(case POSITION when '과장' then SALARY end) "과장", 
	AVG(case POSITION when '대리' then SALARY end) "대리", 
	AVG(case POSITION when '사원' then SALARY end) "사원"
from cslee.TB_EMP
where POSITION IN ('과장','대리','사원')
group by ORG_CD;

select ORG_CD, 
sum(COALESCE((case position when '팀장' then 1 else 0 end),0)) "팀장",
SUM(COALESCE((case position when '과장' then 1 else 0 end),0)) "과장",
SUM(COALESCE((case position when '대리' then 1 else 0 end),0)) "대리",
SUM(COALESCE((case position when '사원' then 1 else 0 end),0)) "사원"
from cslee.tb_emp
group BY ORG_CD;

select ORG_CD, 
COALESCE (SUM(case position when '팀장' then 1 end),0) “팀장”,
COALESCE (SUM(case position when '과장' then 1 end),0) “과장”,
COALESCE (SUM(case position when '대리' then 1 end),0) “대리”,
COALESCE (SUM(case position when '사원' then 1 end),0) “사원”
from cslee.TB_EMP
group by ORG_CD;

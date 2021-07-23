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


--실습4
--equi join
--사원테이블 - 조직 테이블
select TB_EMP.EMP_NAME, TB_EMP.ORG_CD,
	TB_ORG.ORG_CD, TB_ORG.ORG_NAME
from cslee.TB_EMP, cslee.TB_ORG
where cslee.TB_EMP.ORG_CD = cslee.TB_ORG.ORG_CD;

select TB_EMP.EMP_NO, 
	TB_EMP.EMP_NAME, 
	TB_EMP.ORG_CD,
	TB_ORG.ORG_NAME, 
	TB_EMP.POSITION
from cslee.TB_EMP, 
	cslee.TB_ORG
where cslee.TB_EMP.ORG_CD = cslee.TB_ORG.ORG_CD;

--alias 사용
select E.EMP_NO, 
	E.EMP_NAME, 
	E.ORG_CD,
	O.ORG_NAME, 
	E.POSITION
from cslee.TB_EMP AS E, 
	cslee.TB_ORG AS O
where E.ORG_CD = O.ORG_CD
	and E.POSITION = '팀장'
order by O.ORG_NAME; 

--3개 이상 테이블 조인
select A.ACCNO, 
	C.CUST_NAME, 
	P.PROD_NAME, 
	A.CONT_AMT, 
	E.EMP_NAME
from cslee.TB_ACCNT A, cslee.TB_CUST C, cslee.TB_PROD P, cslee.TB_EMP E
where A.CUST_NO = C.CUST_NO
	and A.PROD_CD = P.PROD_CD
	and A.MANAGER = E.EMP_NO;

select E.EMP_NAME 사원명, 
	E.SALARY 연봉, 
	S.GRADE 급여등급
from cslee.TB_EMP E, cslee.TB_GRADE S
where E.SALARY 
between S.LOW_SAL and S.HIGH_SAL;

--inner join
--where
select EMP.EMP_NO, EMP.EMP_NAME, ORG.ORG_NAME
from cslee.TB_EMP EMP, cslee.TB_ORG ORG
where EMP.ORG_CD = ORG.ORG_CD;

--from
select EMP.EMP_NO, EMP.EMP_NAME, ORG.ORG_NAME
from cslee.TB_EMP EMP
inner join cslee.TB_ORG ORG
on EMP.ORG_CD = ORG.ORG_CD;

select ACC.ACCNO, ACC.CUST_NO, CUST.CUST_NAME
from cslee.TB_ACCNT ACC 
inner join cslee.TB_CUST CUST 
on (CUST.CUST_NO = ACC.CUST_NO);

select E.EMP_NAME, E.ORG_CD, O.ORG_CD, O.ORG_NAME
from cslee.TB_EMP E 
join cslee.TB_ORG O
on (E.ORG_CD = O.ORG_CD)
where E.ORG_CD = '10';

--inner 키워드 생략
select EMP.EMP_NO, EMP.EMP_NAME, ORG.ORG_NAME
from cslee.TB_EMP EMP 
join cslee.TB_ORG ORG
on EMP.ORG_CD = ORG.ORG_CD;

--다중조인
--where
select A.ACCNO 계좌번호, C.CUST_NAME 고객명, P.PROD_NAME 상품명, A.CONT_AMT 계약금액, E.EMP_NAME 담당자명
from cslee.TB_ACCNT A, cslee.TB_CUST C, cslee.TB_PROD P, cslee.TB_EMP E
where A.CUST_NO = C.CUST_NO
and A.PROD_CD = P.PROD_CD
and A.MANAGER = E.EMP_NO;

--on
select A.ACCNO 계좌번호, C.CUST_NAME 고객명, P.PROD_NAME 상품명, A.CONT_AMT 계약번호, E.EMP_NAME 담당자명
from cslee.TB_ACCNT A 
inner join cslee.TB_CUST C on A.CUST_NO = C.CUST_NO
inner join cslee.TB_PROD P on A.PROD_CD = P.PROD_CD
inner join cslee.TB_EMP E on A.MANAGER = E.EMP_NO;

--cross
select count(emp_name) from cslee.tb_emp;
select count(org_name) from cslee.tb_org;

select E.EMP_NAME, O.ORG_NAME
from cslee.TB_EMP E cross join cslee.TB_ORG O
order by EMP_NAME;

select count(e.emp_name)
from cslee.TB_EMP E cross join cslee.TB_ORG O;

--left outer join
select E.EMP_NO 사번, E.EMP_NAME 사원명,E.POSITION 직책, O.ORG_NAME 부서명
from cslee.TB_EMP E left outer join cslee.TB_ORG O
on E.ORG_CD = O.ORG_CD
where E.POSITION = '사원';

--right outer join
select E.EMP_NO 사번, E.EMP_NAME 사원명, E.POSITION 직책, O.ORG_NAME 부서명
from cslee.TB_ORG O right outer join cslee.TB_EMP E
on E.ORG_CD = O.ORG_CD
where E.POSITION = '사원';

--full outer join
select A.ORG_CD, A.ORG_NAME, B.ORG_CD, B.ORG_NAME 
from cslee.TB_ORG A full outer join cslee.TB_ORG B
on A.ORG_CD=B.ORG_CD;

select A.ORG_CD, A.ORG_NAME, B.ORG_CD, B.ORG_NAME
from cslee.TB_ORG A left outer join cslee.TB_ORG B
on A.ORG_CD = B.ORG_CD
union
select A.ORG_CD, A.ORG_NAME, B.ORG_CD, B.ORG_NAME
from cslee.TB_ORG A right outer join cslee.TB_ORG B
on A.ORG_CD = B.ORG_CD;

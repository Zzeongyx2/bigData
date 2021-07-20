A_salary <- c(25, 28, 50, 60, 30, 35, 40, 70, 40, 70, 40, 100, 30, 30)
B_salary <- c(20, 40, 25, 25, 35, 25, 20, 10, 55, 65, 100, 100, 150, 300)

# 평균값
mean(A_salary)
mean(B_salary)
mean(A_salary, na.rm = T) # 결측값 제거

# 중앙값
median(A_salary)
median(B_salary)
median(A_salary, na.rm = T) # 결측값 제거

# 절사평균
mean(A_salary, trim = 0.1) # 양끝 10%씩 제외하고 평균 계산
mean(B_salary, trim = 0.1)

# 범위
range(A_salary)
range(B_salary)

# 최소값, 최대값
min(A_salary)
max(A_salary)

min(B_salary)
max(B_salary)

# 분산
var(A_salary)
var(B_salary)

# 표준편차
sd(A_salary)
sd(B_salary)
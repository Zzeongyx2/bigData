# 변수 선언 및 호출
# <- 말고 = 써도 됨
age <- 20
age

age <- 30
age

# 데이터 타입
age <- 20
class(age)

name <- 'JYY'
class(name)

is_effective <- TRUE
is_effective
class(is_effective)

# 팩터타입
sido <- factor('서울', c('서울', '부산', '제주'))
sido
class(sido)
levels(sido)

# NULL과 NA(결측치)
a <- NULL
jumsu <-c(NA, 90, 100)

# Inf(무한대 실수)와 NaN(Not a Number)
10/0
0/0
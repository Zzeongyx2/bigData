A_salary <- c(25, 28, 50, 60, 30, 35, 40, 70, 40, 70, 40, 100, 30, 30)
B_salary <- c(20, 40, 25, 25, 35, 25, 20, 10, 55, 65, 100, 100, 150, 300)

# 사분위수
quantile(A_salary)
quantile(B_salary)

# 상자그림
boxplot(A_salary, B_salary, names = c("A회사 salary", "B회사 salary"))

# 히스토그램
hist(A_salary, xlab = "A사 salary", ylab = "인원수", breaks = 5)
hist(B_salary, xlab = "B사 salary", ylab = "인원수", breaks = 5)

# 도수분포표
cut_value <- cut(A_salary, breaks = 5)
freq <- table(cut_value)
freq

# 범주형 데이터
A_gender <- as.factor(c('남', '남', '남', '남', '남', '남', '남', '남', '남', '여', '여', '여', '여', '여'))
B_gender <- as.factor(c('남', '남', '남', '남', '여', '여', '여', '여', '여', '여', '여', '남', '여', '여'))

A <- data.frame(gender <- A_gender,
                salary <- A_salary)
B <- data.frame(gender <- B_gender,
                salary <- B_salary)

freqA <- table(A$gender)
freqA
freqB <- table(B$gender)
freqB

# 상대적 빈도표
prop.table(freqA)
prop.table(freqB)

# 막대 그래프
barplot(freqA, names = c("남", "여"), col = c("skyblue", "pink"), ylim = c(0, 10))
title(main = "A사")
barplot(freqB, names = c("남", "여"), col = c("skyblue", "pink"), ylim = c(0, 10))
title(main = "B사")

# 파이 그래프
pie(x = freqA, col = c("skyblue", "pink"), main = "A사")
pie(x = freqB, col = c("skyblue", "pink"), main = "B사")

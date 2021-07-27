# 피어슨 상관계수 구하기
cor(Orange$circumference, Orange$age)
# 산점도 그리기
plot(Orange$circumference, Orange$age, col = "red", pch = 19)

cor(iris[, 1:4])

# 상관계수 검정
cor.test(iris$Petal.Length, iris$Petal.Width, method = "pearson")    # 피어슨 상관계수 검정   # 스피어만 상관계수 검정 : method = "spearman"


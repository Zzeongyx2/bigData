# 단순선형회귀

# 모델 생성
data(Orange)
head(Orange)

model <- lm(circumference ~ age, Orange)
model

# 회귀 계수
coef(model)

# 잔차
r <- residuals(model)
r[0:4]

f <- fitted(model)  # 예측한 값 구하기
r <- residuals(model)  # 잔차 구하기
f[0:4] + r[0:4]
Orange[0:4, 'circumference']  # 실제값

# 잔차 제곱합
deviance(model)

# 예측
predict.lm(model, newdata = data.frame(age = 100))

summary(model)

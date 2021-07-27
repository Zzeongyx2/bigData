# 주성분분석
# princomp()
fit <- princomp(iris[, 1:4], cor = TRUE)

# summary()
summary(fit)

# loadings()
loadings(fit)

# 주성분 개수 선택법
# 스크리 그래프
screeplot(fit, type = "lines", main = "scree plot")

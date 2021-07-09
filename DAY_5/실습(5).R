# head()
head(Orange)
head(Orange,3)

# tail()
tail(Orange)
tail(Orange,3)

# str()
str(Orange)

# summary()
summary(Orange)

# csv 파일
# 안열리면 fileEncoding = 'EUC-KR' || 'UTF-8'
nhis <- read.csv("C:/Users/user/Documents/R_basic/NHIS_OPEN_GJ_EUC-KR.csv")
nhis

sample <- read.csv("C:/Users/user/Documents/R_basic/sample.csv",
                   header = F,
                   fileEncoding = 'EUC-KR',
                   stringsAsFactors = TRUE)
sample

#엑셀 파일
install.packages('openxlsx')
library(openxlsx)

nhis_sheet1 = read.xlsx('C:/Users/user/Documents/R_basic/NHIS_OPEN_GJ_EUC-KR.xlsx')
nhis_sheet2 = read.xlsx('C:/Users/user/Documents/R_basic/NHIS_OPEN_GJ_EUC-KR.xlsx', sheet = 2)

nhis_sheet1
nhis_sheet2

# 빅데이터 파일
install.packages('data.table', type="binary")
library(data.table)

nhis_bigdata = fread("C:/Users/user/Documents/R_basic/NHIS_OPEN_GJ_BIGDATA_UTF-8.csv",
                     encoding = 'UTF-8')
str(nhis_bigdata)

# 데이터 추출
Orange[1,]
Orange[1:5,]
Orange[6:10,]
Orange[c(1,5),]
Orange[-c(1:29),]

Orange[Orange$age == 118,]
Orange[Orange$age %in% c(118,484),]
Orange[Orange$age >= 1372,]

Orange[,'circumference']
Orange[1, c('Tree','circumference')]

Orange[,1]
Orange[,c(1,3)]
Orange[,c(1:3)]
Orange[,-c(1,3)]

Orange[1:5,'circumference']
Orange[Orange$Tree %in% c(3,2), c("Tree",'circumference')]

# 정렬
OrangeT1 <- Orange[Orange$circumference < 50,]
OrangeT1[order(OrangeT1$circumference),]

# 내림차순
OrangeT1[order(-OrangeT1$circumference),]

# 그룹별 집계
aggregate(circumference ~ Tree, Orange, mean)

# 데이터 병합
stu1 <- data.frame(no = c(1,2,3), midterm = c(100,90,80))
stu2 <- data.frame(no = c(1,2,3), finalterm = c(100,90,80))
stu3 <- data.frame(no = c(1,4,5), quiz = c(99,88,77))
stu4 <- data.frame(no = c(4,5,6), midterm = c(99,88,77))

merge(stu1,stu2)
merge(stu1,stu3)
merge(stu1,stu3, all = T)

rbind(stu1,stu4)
cbind(stu1,stu2)

library(readxl) #library for reading Excel
#Alumni Giving
giftData <- read_excel("C:/Users/kates/Desktop/MATH365_GIFT.xlsx")
#Actions by Hendrx to Alumni
actionsData <-read_excel("C:/Users/kates/Desktop/MATH365_ACTIONS.xlsx")

#Gifts with outlers
boxplot(giftData$`Gift Amount`)
mean(giftData$`Gift Amount`)

# Gifts with no outliers
giftsNoOutliers <- giftData$`Gift Amount`[!giftData$`Gift Amount` %in% boxplot.stats(giftData$`Gift Amount`)$out]
boxplot(giftData$`Gift Amount`,outline=FALSE)
mean(giftsNoOutliers)


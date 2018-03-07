library(ggplot2)
library(plyr) 
library(readxl) #library for reading Excel
#Alumni Giving
giftData <- read_excel("C:/Users/kates/Desktop/MATH365_GIFT.xlsx")
#Actions by Hendrx to Alumni
actionsData <-read_excel("C:/Users/kates/Desktop/MATH365_ACTIONS.xlsx")
#Bio Data
bioData <- read_excel("C:/Users/kates/Desktop/MATH365_BIO.xlsx")
#Events
eventsData <- read_excel("C:/Users/kates/Desktop/MATH365_EVENTS.xlsx")

#Gifts with outlers
boxplot(giftData$`Gift Amount`)
mean(giftData$`Gift Amount`)

# Gifts with no outliers
giftsNoOutliers <- giftData$`Gift Amount`[!giftData$`Gift Amount` %in% boxplot.stats(giftData$`Gift Amount`)$out]
boxplot(giftData$`Gift Amount`,outline=FALSE)
mean(giftsNoOutliers)

#Alumni Cities
alumniCity <- count(na.omit(bioData$City))
bigAlumCity<-alumniCity[!(alumniCity$freq < 9),] #Outlier in City Size
bigAlumCity100<-alumniCity[!(alumniCity$freq < 100),] #Cities with >100 ppl
bigAlumCity1000<-alumniCity[!(alumniCity$freq < 1000),] #Cities with >1000 ppl from data
bigAlumCity1000BarChart <- ggplot(bigAlumCity1000, aes(x, freq))+geom_bar(stat = "identity")
bigAlumCity1000BarChart
bigAlumCity100BarChart <- ggplot(bigAlumCity100, aes(x, freq))+geom_bar(stat = "identity")
bigAlumCity100BarChart


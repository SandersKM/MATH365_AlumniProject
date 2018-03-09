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

#Alumni Cities Analysis
alumniCity <- count(na.omit(bioData$City))
#You can use this with any number of alumni/friends in cities, but this was the most revealing
#for right now.
bigAlumCity500<-alumniCity[!(alumniCity$freq < 500),] #Cities with >500 ppl from data
bigAlumCity500BarChart <- ggplot(bigAlumCity500, aes(x, freq))+geom_bar(stat = "identity")
bigAlumCity500BarChart


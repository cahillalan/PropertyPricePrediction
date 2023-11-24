mydata <- rep("character", 40)
mydata[11] <- "numeric"
library("ggplot2")
mydata = read.csv("C:/Users/Cahil/Desktop/Database/Dublin15SemiDetatchedHousesComplete.csv")
mydata$label <- as.factor(mydata$label)

areas<-ggplot(mydata, aes(x=Lattitude, y = Longitude, color = label)) + geom_point()
areas + scale_color_brewer(palette="Set1")

mydata$allprices <- NULL

mydata$allprices <- NULL
mydata$details <- NULL
mydata$pricedates <- NULL 
mydata$address <- NULL

mean(mydata$price)
range(mydata$price)
mean(mydata$bedrooms)
mean(mydata$bathrooms)
median(mydata$price)
sd(mydata$price)
library("ggplot2")

fit1 <- lm(price ~ bedrooms , data=mydata)

wilcox.test(mydata$price[mydata$type == "Detached House "] , mydata$price[mydata$type == "Terraced House "])
wilcox.test(mydata$price[mydata$type == "Detached House "] , mydata$price[mydata$type == "Apartment For Sale "])
wilcox.test(mydata$price[mydata$type == "Detached House "] , mydata$price[mydata$type == "Second-Hand Dwelling House/Apartment"])



test <- aov(price~type, data=mydata)
summary(test)
test <- aov(price~bedrooms, data=mydata)
summary(test)
test <- aov(price~bathrooms, data=mydata)
summary(test)
test <- aov(price~area, data=mydata)
summary(test)

kruskal.test(price~type, data=mydata)
kruskal.test(price~area, data=mydata)
kruskal.test(price~bedrooms, data=mydata)
kruskal.test(price~bathrooms, data=mydata)

tapply(mydata$price, mydata$type, mean)

tapply(mydata$price, mydata$bedrooms, mean)
tapply(mydata$price, mydata$bathrooms, mean)
tapply(mydata$price, mydata$area, mean)

ggplot(mydata, aes(price)) +geom_histogram(bins = 20)

ggplot(mydata, aes(x=price, y = bedrooms, color = type)) + geom_point()
ggplot(mydata, aes(x=bedrooms, y = price, color = type)) + geom_point()

ggplot(mydata, aes(x = type, y = price)) + geom_point()

ggplot(mydata, aes(x = type, y = price)) + geom_violin()
ggplot(mydata, aes(x = bedrooms, y = price)) + geom_violin()


ggplot(mydata, aes(x = price, y = type))+geom_point() + facet_wrap(~bedrooms)
ggplot(mydata, aes(x = price, y = bedrooms))+geom_point() + facet_wrap(~type)
ggplot(mydata, aes(x = price, y = bathrooms))+geom_point() + facet_wrap(~type)



mydata = read.csv("C:/Users/Cahil/Desktop/Database/HalfMill.csv")
plot(mydata$price, mydata$bedrooms)

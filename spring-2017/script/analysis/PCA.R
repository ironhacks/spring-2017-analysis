# Read data into R using the read.csv function 

# Set working directory 
setwd("H:/RWorkshop")

# Read in the data file (.csv)
temp = read.csv("/Users/jialincheoh/Desktop/survey-motivation.csv", sep=",")
head(temp)
temp1 <- as.matrix(temp)
head(temp1)
pca <- prcomp((temp1), scale=TRUE)
head(pca)
plot(pca$x[,1], pca$x[,2])
# make a scree plot
pca.var <- pca$sdev^2
pca.var.per <- round(pca.var/sum(pca.var)*100, 1)


barplot(pca.var.per, main="Scree Plot", xlab="Principal Component", ylab="Percent Variation")

## now make a fancy looking plot that shows the PCs and the variation:
library(ggplot2)

pca.data <- data.frame(Sample=rownames(pca$x),
                       X=pca$x[,1],
                       Y=pca$x[,2])
pca.data

ggplot(data=pca.data, aes(x=X, y=Y, label=Sample)) +
  geom_text() +
  xlab(paste("PC1 - ", pca.var.per[1], "%", sep="")) +
  ylab(paste("PC2 - ", pca.var.per[2], "%", sep="")) +
  theme_bw() +
  ggtitle("Q2 PCA Graph")


## get the name of the top 5 survey items that contribute
## most to pc1.

loading_scores <- pca$rotation[,1]
head(loading_scores)
survey_scores <- abs(loading_scores) ## get the magnitudes
survey_score_ranked <- sort(survey_scores, decreasing=TRUE)
head(survey_score_ranked)

## get the name of the top 5 survey items that contribute
## most to pc2. 

loading_scores <- pca$rotation[,2]
head(loading_scores)
survey_scores <- abs(loading_scores) ## get the magnitudes
survey_score_ranked <- sort(survey_scores, decreasing=TRUE)
head(survey_score_ranked)

# Read data into R using the read.csv function 


# Read in the data file (.csv)
temp = read.csv("/Users/jialincheoh/Desktop/survey-motivation-WQ13.csv", sep=",")
head(temp)
temp1 <- as.matrix(temp)
head(temp1)
pca <- prcomp((temp1), scale=TRUE)
head(pca)
plot(pca$x[,1], pca$x[,2])
# make a scree plot
pca.var <- pca$sdev^2
pca.var.per <- round(pca.var/sum(pca.var)*100, 1)


barplot(pca.var.per, main="Scree Plot", xlab="Principal Component", ylab="Percent Variation")

## now make a fancy looking plot that shows the PCs and the variation:
library(ggplot2)

pca.data <- data.frame(Sample=rownames(pca$x),
                       X=pca$x[,1],
                       Y=pca$x[,2])
pca.data

ggplot(data=pca.data, aes(x=X, y=Y, label=Sample)) +
  geom_text() +
  xlab(paste("PC1 - ", pca.var.per[1], "%", sep="")) +
  ylab(paste("PC2 - ", pca.var.per[2], "%", sep="")) +
  theme_bw() +
  ggtitle("Q2 PCA Graph")


## get the name of the top 5 survey items that contribute
## most to pc1.

loading_scores <- pca$rotation[,1]
head(loading_scores)
#survey_scores <- abs(loading_scores) ## get the magnitudes
survey_score_ranked <- sort(loading_scores, decreasing=TRUE)
head(survey_score_ranked)

## get the name of the top 5 survey items that contribute
## most to pc2. 

loading_scores <- pca$rotation[,2]
head(loading_scores)
#survey_scores <- abs(loading_scores) ## get the magnitudes
survey_score_ranked <- sort(loading_scores, decreasing=TRUE)
head(survey_score_ranked)

# Now draw the BiPlot
# From the biplot of PC2, we can see that the intrinsic motivations tend to be negatively correlated with extrinsic. 
# All the survey items are negatively loaded on PC1 
biplot(pca, cex=c(1, 0.7))

# Apply the Varimax Rotation
my.var <- varimax(my.prc$rotation)
my.var


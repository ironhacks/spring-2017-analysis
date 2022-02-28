# Principle Component Analysis in R 
 
# Loading required package: psych
require(psych)

# Loading required package: GPArotation
require(GPArotation)

# Reading raw survey CSV file 
library(lattice)
url <- "/Users/jialincheoh/Desktop/survey_final_read.csv"
survey <- read.csv(url, header=TRUE)
survey

# Rename survey columns 1 to 13
names(survey)[1:13] <- c("monetary_compensation", "excellent_programmer", "internship", 
                         "introduce_ideas", "get_in_touch", "known_creativity", "improve_skills", 
                         "test_capability", "enjoy_problems", "keep_up", "dissatisfaction", "curious", "pass_class")
survey

#Get the correlation of all 13 survey items 
lowerCor(motivation)


# Get the significance of all 13 survey items 
library(correlation)

correlation::correlation(motivation,
                         include_factors = TRUE, method = "auto"
)

# Do the PCA (PRCOMP) with singular value decomposition of the (centered and possibly scaled) data matrix

my.prc = prcomp(motivation, center=TRUE, scale=TRUE)
screeplot(my.prc, main="Scree Plot", xlab="Components")
screeplot(my.prc, main="Scree Plot", type="line" )

# Get the PCA output from PRCOMP 
my.prc 

# Kaiser criterion to determine the number of principle components to keep 
my.prc$sdev ^ 2

# DotPlot PC1
load    <- my.prc$rotation
sorted.loadings <- load[order(load[, 1]), 1]
myTitle <- "Loadings Plot for PC1" 
myXlab  <- "Variable Loadings"
dotplot(sorted.loadings, main=myTitle, xlab=myXlab, cex=1.5, col="red")
summary(my.prc)

# DotPlot PC2
sorted.loadings <- load[order(load[, 2]), 2]
myTitle <- "Loadings Plot for PC2"
myXlab  <- "Variable Loadings"
dotplot(sorted.loadings, main=myTitle, xlab=myXlab, cex=1.5, col="red")

# Now draw the BiPlot
biplot(my.prc, cex=c(1, 0.7))

# Get the first two components loaded 
my.prc$rotation[, 1:2]

# Print all PCA scores generated from PRCOMP 
options(max.print=1000000)
project.b = predict(my.prc, motivation)
project.b

# Apply the Varimax Rotation
## Do varimax rotation on 6 components.
my.var <- varimax(my.prc$rotation[, 1:6])
my.var

# Apply the Varimax Rotation
# Do varimax rotation on 2 components.
my.var <- varimax(my.prc$rotation[, 1:2])
my.var

# Apply the Varimax Rotation
# Do varimax rotation on 3 components.
my.var <- varimax(my.prc$rotation[, 1:3])
my.var


head(my.prc$x)
summary(my.prc)


## Get the PCA scores for 163 participants 
pca <- predict(my.prc, newdata=motivation)
pca

print(my.prc)
summary(motivation)
head(my.prc$x)

# Convert the PCA matrix output to dataframe 
pca_frame <- as.data.frame(pca)
pca_frame

# Combine PC1 and the hack_id
allData <- cbind(pca_frame[1], id = survey$hack_id)
allData

# Get the absolute of the PC1 
allData_abs_PC1 <- abs(allData)
allData_abs_PC1

# Recode for performance and solution transparency for PC1
allData_abs_PC1$performance <- ifelse(allData_abs_PC1$id==1, 1,
                                      ifelse(allData_abs_PC1$id==2, 0,
                                             ifelse(allData_abs_PC1$id==0, 0,
                                                    ifelse(allData_abs_PC1$id==3, 1, NA))))

allData_abs_PC1

allData_abs_PC1$solution <- ifelse(allData_abs_PC1$id==1, 0,
                                   ifelse(allData_abs_PC1$id==2, 1,
                                          ifelse(allData_abs_PC1$id==0, 0,
                                                 ifelse(allData_abs_PC1$id==3, 1, NA))))

allData_abs_PC1

# Unpaired t-test for performance transparency
res <- t.test(PC1 ~ performance, data = allData_abs_PC1, var.equal = TRUE)
res

# Unpaired t-test for solution transparency
res <- t.test(PC1 ~ solution, data = allData_abs_PC1, var.equal = TRUE)
res

# Combine PC2 with hack_id
allData_PC2 <- cbind(pca_frame[2], id = survey$hack_id)
allData_PC2

# Take absolute value of PC2 
allData_abs_PC2 <- abs(allData_PC2)
allData_abs_PC2


# Prepare dataframe for ANOVA analysis 
anova_1 <- as.data.frame(allData_abs_PC1)
anova_1

# Conduct ANOVA for PC1 
ANOVA_RESULTS_1 <- aov(PC1 ~ id, data=anova_1)
summary(ANOVA_RESULTS_1)

# Convert PC2 dataframe to absolute value
anova_2 <- as.data.frame(allData_abs_PC2)
anova_2

# Conduct ANOVA for PC2
ANOVA_RESULTS_2 <- aov(PC2 ~ id, data=anova_2)
summary(ANOVA_RESULTS_2)

# Recode for performance and solution transparency for PC2
allData_abs_PC2$performance <- ifelse(allData_abs_PC2$id==1, 1,
                                      ifelse(allData_abs_PC2$id==2, 0,
                                             ifelse(allData_abs_PC2$id==0, 0,
                                                    ifelse(allData_abs_PC2$id==3, 1, NA))))

allData_abs_PC2

allData_abs_PC2$solution <- ifelse(allData_abs_PC2$id==1, 0,
                                   ifelse(allData_abs_PC2$id==2, 1,
                                          ifelse(allData_abs_PC2$id==0, 0,
                                                 ifelse(allData_abs_PC2$id==3, 1, NA))))

allData_abs_PC2


## We’ll use F-test to test for homogeneity in variances
res.ftest <- var.test(PC2 ~ performance, data = allData_abs_PC2)
res.ftest

## t-test on PC2 for performance 
res <- t.test(PC2 ~ performance, data = allData_abs_PC2, var.equal = TRUE)
res


## We’ll use F-test to test for homogeneity in variances. 
res.ftest <- var.test(PC2 ~ solution, data = allData_abs_PC2)
res.ftest

## t-test on PC2 for solution
res <- t.test(PC2 ~ solution, data = allData_abs_PC2, var.equal = TRUE)
res

## PCA with princomp method in R 

## Perform the Principle Component Analysis 
## cor=TRUE means using correlation matrix instead of the covariance matrix 
## scores=TRUE takes the data and transform into the reduced space/transformed space so that we can work on the data there
princomp_output <- princomp(motivation, scores=TRUE, cor=TRUE)
summary(princomp_output)

## Print the scree plot 

plot(princomp_output)

summary(princomp_output)

plot(princomp_output,type="lines")

# Unrotated components with 6 factors
princomp_output$loadings[, 1:6]

princomp_output$loadings

biplot(princomp_output)

## Print the scores (projections)
## rotated or transformed dataset
fit_unrotated_matrix <- princomp_output$scores[, 1:6]
fit_unrotated_matrix

fit_rotated_matrix <- fit_rotated$scores[, 1:6]
fit_rotated_matrix

### Make unrotated pca matrix as data frame 
fit_unrotated_df <- as.data.frame(fit_unrotated_matrix)
fit_unrotated_df








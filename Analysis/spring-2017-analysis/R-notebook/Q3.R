# Read data into R using the read.csv function 

# Set working directory 
setwd("H:/RWorkshop")

# Read in the data file (.csv)
temp = read.csv("Q3-final.csv", sep=",", row.names=1)
head(temp)
temp1 <- as.matrix(temp)
head(temp1)

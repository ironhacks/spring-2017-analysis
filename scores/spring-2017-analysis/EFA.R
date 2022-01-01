# remove "pass class" survey item 13
motivation <- read.table("/Users/jialincheoh/Desktop/survey-motivation-WQ13.csv", header=TRUE, sep = ",")

# Loading required package: psych
require(psych)

# Loading required package: GPArotation
require(GPArotation)

describe(motivation)

lowerCor(motivation)

library(correlation)

correlation::correlation(motivation,
                         include_factors = TRUE, method = "auto"
)

# display p-values (rounded to 3 decimals)
round(res$P, 3)

fa.parallel(motivation, fm='ml', fa='fa', main="Parallel Analysis Scree Plots", n.iter=100, error.bars=T, sim=F)

fa(r=motivation, nfactors=2, rotate='promax', fm='ml')

fa(r=motivation, nfactors=2, rotate='oblimin', fm='ml')

fa(r=motivation, nfactors=2, rotate='varimax', fm='ml')

# remove "pass class" survey item 13 and "money" survey item 1
motivation <- read.table("/Users/jialincheoh/Desktop/survey-motivation-WQ13-WQ1.csv", header=TRUE, sep = ",")

lowerCor(motivation)

fa.parallel(motivation, fm='ml', fa='fa', main="Parallel Analysis Scree Plots", n.iter=100, error.bars=T, sim=F)

fa(r=motivation, nfactors=2, rotate='promax', fm='ml')

fa(r=motivation, nfactors=2, rotate='oblimin', fm='ml')

fa(r=motivation, nfactors=2, rotate='varimax', fm='ml')




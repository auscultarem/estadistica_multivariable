install.packages("nnet")

library(nnet)
library(caret)

bn <- read.csv("Documentacion de R/r-course-master/data/tema3/banknote-authentication.csv")
bn$class <- factor(bn$class)

t.id <- createDataPartition(bn$class, p= 0.7, list = FALSE)

# se cea un modelo apartir de lo datos de entrenamiento.
mod <- nnet(class ~ ., data = bn[t.id,],
            size = 3, maxit = 10000, decay = .001, rang = 0.05)

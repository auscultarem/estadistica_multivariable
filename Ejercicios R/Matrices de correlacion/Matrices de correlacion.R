#correlation Matrix
library(ggplot2)
install.packages("corrplot")
library(corrplot)

mtcars <- read.csv("Documentacion de R/r-course-master/data/tema7/mtcars.csv")
head(mtcars)
mtcars$X = NULL #Quito la columna que no es numerica para poder realizar
#la matriz de correlacion
mtcars.cor <- cor(mtcars, method = "pearson")

round(mtcars.cor, digits = 2)
#con este comando se grafica una matriz de correlacion y entre mas cerno a 1
#las varibales estan mas realcionadas
corrplot(mtcars.cor)

#matrix de correlacion cuadrada
corrplot(mtcars.cor, method = "shade", shade.col= NA,
     tl.col = "black", tl.srt = 45)

col <- colorRampPalette(c("#BB4444", "#EE9988","#FFFFFF",
                          "#77AADD","#4477AA"))

corrplot(mtcars.cor, method = "shade", shade.col = NA,
         tl.col = "black", tl.srt = 45, col = col(200),
         addCoef.col = "black", addcolorlabel = "no",
         order = "AOE") #type = "lower" lower pinta la matrix inferior

library(reshape2)
mtcars.melted <- melt(mtcars.cor)
head(mtcars.cor)
head(mtcars.melted)

ggplot(data = mtcars.melted, aes(x= Var1, y= Var2, fill= value))+
  geom_tile()

get_lower_triangle <- function(cormat){
  cormat[upper.tri(cormat)] <- NA
  return(cormat)
}

get_upper_triangle <- function(cormat){
  cormat[lower.tri(cormat)] <- NA
  return(cormat)
}

reorder_cormat <- function(cormat){
  dd<- as.dist((1-cormat)/2)
  hc <- hclust(dd)
  cormat <- cormat[hc$order, hc$order]
}

#Me permitira reordenar el clustering
cormat <- reorder_cormat(mtcars.cor)
cormat.ut <- get_upper_triangle(cormat)
cormat.ut.melted <- melt(cormat.ut, na.rm =TRUE)

ggplot(cormat.ut.melted, aes(Var2,Var1, fill = value))+
  geom_tile(color = "white")+
  scale_fill_gradient2(low = "blue", high = "red",
                       mid = "white", midpoint = 0,
                       limit = c(-1,1), space = "Lab",
                       name = "Pearson\nCorrelation")+
  theme_minimal()+
  theme(axis.text.x = element_text(angle = 45, 
                                   vjust = 1, size = 12, hjust = 1))+
  coord_fixed()




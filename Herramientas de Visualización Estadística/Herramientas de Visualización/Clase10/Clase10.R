
datos <- read.table("olympic.txt", header = T, sep = ",")
datos <- as.data.frame(datos)

datos$X100 <- -datos$X100
datos$X400 <- -datos$X400
datos$X110 <- -datos$X110
datos$X1500 <- -datos$X1500

X <- datos[, c(3, 7, 8, 9)]
Y <- datos[, c(-3, -7, -8, -9)]

#Análisis de correlaciones
corrplo
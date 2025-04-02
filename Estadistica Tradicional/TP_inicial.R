"
Tp Inicial
Integrantes: Emi, Agus, Dafne
Fecha de entrega: 02/04
"

library("ggplot2")
library("aplpack")

datos_bebes <- read.table("ENNyS_menorA2.txt", header = TRUE)
names(datos_bebes)
attach(datos_bebes)

#Ejercicio 1

#Ejercicio 6

bagplot(Perim_encef, Talla, approx.limit = 100, 
        xlab = "Perímetro Encefálico", ylab = "Talla", xlim = c(0, 60))
#Los datos atípicos corresponden a aquellos bebés con perímetro encefálico menor a 30 cm y de Talla menor a 40 o mayor a 100
#Se puede observar que el perímetro encefálico suele ser proporcional a la Talla
#Si consideramos talla alta a partir de 80cm, podemos observar dos datos con perímetro 10 (deben estar mal cargados)
##Si consideramos talla baja hasta 60cm, hay más outliers que corresponden a pe grande.

#Ejercicio 7
bagplot(Perim_encef, Talla, approx.limit = 100, 
        xlab = "Perímetro Encefálico", ylab = "Talla", xlim = c(0, 60),
        show.outlier = FALSE)

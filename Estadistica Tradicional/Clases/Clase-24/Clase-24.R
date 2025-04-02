library(glmnet)
# Cargar el dataframe desde un archivo CSV
df <- read.csv("rdpercentGDP.csv")

# Crear el gráfico
plot(df$year, df$argen, type = "l", ylim = c(0, 5), col = "green", 
     xlab = "Año", ylab = "Valores", main = "Comparación de Países a lo Largo de los Años")

# Lista de países y colores
countries <- c("argen", "germany", "france", "china", "japan", "usa", "Reino Unido", "nld", "Finland")
colors <- c("green", "red", "purple", "blue", "orange", "darkgreen", "brown", "pink", "yellow")
names <- c("Argentina", "Alemania", "Francia", "China", "Japón", "USA", "Reino Unido","Países Bajos", "Finland")

# Añadir las líneas de cada país y el texto correspondiente
for (i in seq_along(countries)) {
  lines(df$year, df[[countries[i]]], col = colors[i])
  text(df$year[length(df$year)], df[[countries[i]]][length(df[[countries[i]]])], 
       names[i], pos = 3, col = colors[i])
}

# Dividir los datos en conjuntos de entrenamiento y prueba
set.seed(2024)
train_indices <- sample(seq_len(nrow(df)), size = 0.8 * nrow(df))

train_data <- df[train_indices, ]
test_data <- df[-train_indices, ]

# Verificar la división
print("Conjunto de entrenamiento:")
print(train_data)

print("Conjunto de prueba:")
print(test_data)

# Crear el modelo de regresión lineal
modelo <- lm(usa ~ germany + france + china + japan + uk + nld + finland, data = train_data)
summary(modelo)

#Ahora quiero ver midiendo cuánto error cuatrático medio tienen los datos de testeo.
predicciones <- predict(modelo, newdata = test_data)
ECM <- mean((test_data$usa - predicciones)^2)
print(ECM) #Tenemos un bajo ECM ya que los datos son muy pocos

#Ahora vamos a analizar la correlación entre las variables y si podemos pensar que algunas son redundantes (o se explican por otras)
cor(train_data)
#Vemos que china y germany están muy correlacionados (quizas podríamos sacar alguno)

matriz_diseño <- as.matrix(train_data[,-c(1, 2, 8, 10)])

ajuste.ridge <- glmnet(matriz_diseño, train_data$usa , alpha = 0)
summary(ajuste.ridge)

plot(ajuste.ridge)



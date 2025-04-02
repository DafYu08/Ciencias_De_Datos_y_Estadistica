
#Quiero estimar la densidad

buffalo <- scan("buffalo.txt")

#Estimo por ventana de Silverman
desviacion_estandar <- sd(buffalo)
iqr <- IQR(buffalo)
n <- length(buffalo)

h_sil <- 1.06 * min(desviacion_estandar, iqr/1.349) * (n**(-1/5))


seq(1, 7, 0.5)


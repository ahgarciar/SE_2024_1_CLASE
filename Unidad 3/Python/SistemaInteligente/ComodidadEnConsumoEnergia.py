
def calcula_Eo(voptimizados, vactuales, costos):
    # temperatura
    if voptimizados[0] < vactuales[0]:
         c_temp = costos[0] + costos[0] * (vactuales[0] - voptimizados[0])
    else:
         c_temp = 0

    # intensidad luminosa
    if vactuales[1] < voptimizados[1]:
         c_intensidad = costos[1] + costos[1] * (voptimizados[1] - vactuales[1])
    else:
         c_intensidad = 0

    # humedad
    if voptimizados[2] < vactuales[2]:
        c_humedad = costos[2] + costos[2] * (vactuales[2] - voptimizados[2])
    else:
        c_humedad = 0

    # ruido
    if voptimizados[3] < vactuales[3]:
        c_ruido = costos[3] + costos[3] * (vactuales[3] - voptimizados[3])
    else:
        c_ruido = 0

    costos_Eo = [c_temp, c_intensidad, c_humedad, c_ruido]
    return costos_Eo

def calcula_Emin(vmaximos, vminimos, vactuales, costos):
    # temperatura
    if vactuales[0] > vmaximos[0]:
         c_temp = costos[0] + costos[0] * (vactuales[0] - vmaximos[0])
    else:
         c_temp = 0

    # intensidad luminosa
    if vactuales[1] < vminimos[1]:
        c_intensidad = costos[1] + costos[1] * (vactuales[1] - vminimos[1])
    else:
        c_intensidad = 0

    # humedad
    if vactuales[2] > vmaximos[2]:
        c_humedad = costos[2] + costos[2] * (vactuales[2] - vmaximos[2])
    else:
        c_humedad = 0

    # ruido
    if vactuales[3] > vmaximos[3]:
        c_ruido = costos[3] + costos[3] * (vactuales[3] - vmaximos[3])
    else:
        c_ruido = 0

    costos_Emin = [c_temp, c_intensidad, c_humedad, c_ruido]
    return costos_Emin

def calcula_Emax(vmaximos, vminimos, vactuales, costos):
    # temperatura
    if vactuales[0] > vminimos[0]:
         c_temp = costos[0] + costos[0] * (vactuales[0] - vminimos[0])
    else:
         c_temp = 0

    # intensidad luminosa
    if vactuales[1] < vmaximos[1]:
        c_intensidad = costos[1] + costos[1] * (vmaximos[1] - vactuales[1])
    else:
        c_intensidad = 0

    # humedad
    if vactuales[2] > vminimos[2]:
        c_humedad = costos[2] + costos[2] * (vactuales[2] - vminimos[2])
    else:
        c_humedad = 0

    # ruido
    if vactuales[3] > vminimos[3]:
        c_ruido = costos[3] + costos[3] * (vactuales[3] - vminimos[3])
    else:
        c_ruido = 0

    costos_Emax = [c_temp, c_intensidad, c_humedad, c_ruido]
    return costos_Emax

def calcula_ganancia_energia(Eo, Emin, Emax):
    ganancia = 0
    for i in range(len(Eo)):  # Eo, Emin, Emax
        ganancia += 1-((Eo[i]-Emin[i])/(Emax[i]-Emin[i]))
    ganancia /= 4
    return round(ganancia, 4)


if __name__ == "__main__":
    #PREFERENCIAS MINIMAS Y MAXIMAS DE UN USUARIO...
    # C1 C2 C3 C4
    # C1 = TEMP
    # C2 = INTENSIDAD LUMINOSA
    # C3 = HUMEDAD
    # C4 = RUIDO
    valoresMinimos = [18, 50, 20, 15]
    valoresMaximos = [24, 400, 80, 200]

    #VALORES ACTUALES EN EL ENTORNO...
    valoresActuales = [22, 200, 50, 100]

    #VALORES OPTIMIZADOS... RECOMENDACION...
    valoresOptimizados = [20, 210, 40, 30]

    #PESOS(IMPORTANCIA) QUE TIENE QUE SE CUMPLA CADA CARACTERISTICA
    pesosPreferencias = [0.4, 0.3, 0.1, 0.2]

    #COSTO POR CAMBIAR UNA UNIDAD CADA CARACTERISTICA...
    costoCambio = [8, 3, 1, 5] #C1, C2,..., Cn

    vEo = calcula_Eo(valoresOptimizados, valoresActuales, costoCambio)
    vEmin = calcula_Emin(valoresMaximos, valoresMinimos, valoresActuales, costoCambio)
    vEmax = calcula_Emax(valoresMaximos, valoresMinimos, valoresActuales, costoCambio)
    ganancia = calcula_ganancia_energia(vEo, vEmin, vEmax)
    print("Ganancia: ", ganancia)

    #"MEJORES" VALORES OPTIMIZADOS
    valoresOptimizados = [18, 400, 20, 15]
    vEo = calcula_Eo(valoresOptimizados, valoresActuales, costoCambio)
    vEmin = calcula_Emin(valoresMaximos, valoresMinimos, valoresActuales, costoCambio)
    vEmax = calcula_Emax(valoresMaximos, valoresMinimos, valoresActuales, costoCambio)
    ganancia = calcula_ganancia_energia(vEo, vEmin, vEmax)
    print("Ganancia: ", ganancia)

    #"PEORES" VALORES OPTIMIZADOS
    valoresOptimizados = [24, 50, 80, 200]
    vEo = calcula_Eo(valoresOptimizados, valoresActuales, costoCambio)
    vEmin = calcula_Emin(valoresMaximos, valoresMinimos, valoresActuales, costoCambio)
    vEmax = calcula_Emax(valoresMaximos, valoresMinimos, valoresActuales, costoCambio)
    ganancia = calcula_ganancia_energia(vEo, vEmin, vEmax)
    print("Ganancia: ", ganancia)
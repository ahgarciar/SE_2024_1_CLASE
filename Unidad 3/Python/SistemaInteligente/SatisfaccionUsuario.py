
def calcula_satisfaccion(vminimos, vmaximos, voptimizados):
    s_temp = (vmaximos[0] - voptimizados[0]) / ( vmaximos[0] - vminimos[0] )
    s_intensidad = 1 - (vmaximos[1] - voptimizados[1]) / ( vmaximos[1] - vminimos[1] )
    s_humedad = (vmaximos[2] - voptimizados[2]) / ( vmaximos[2] - vminimos[2] )
    s_ruido = (vmaximos[3] - voptimizados[3]) / ( vmaximos[3] - vminimos[3] )
    satisfaccion = [s_temp, s_intensidad, s_humedad, s_ruido]
    return satisfaccion

def calcula_ganancia_satisfaccion(satisfaccion, pesos):
    ganancia = 0
    for i in range(len(satisfaccion)):
        ganancia += satisfaccion[i] * pesos[i]
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

    satisfaccion = calcula_satisfaccion(valoresMinimos, valoresMaximos, valoresOptimizados)
    ganancia = calcula_ganancia_satisfaccion(satisfaccion, pesosPreferencias)
    print("Ganancia: ", ganancia)

    #MEJORES VALORES OPTIMIZADOS
    valoresOptimizados = [18, 400, 20, 15]
    satisfaccion = calcula_satisfaccion(valoresMinimos, valoresMaximos, valoresOptimizados)
    ganancia = calcula_ganancia_satisfaccion(satisfaccion, pesosPreferencias)
    print("Ganancia: ", ganancia)

    #PEORES VALORES OPTIMIZADOS
    valoresOptimizados = [24, 50, 80, 200]
    satisfaccion = calcula_satisfaccion(valoresMinimos, valoresMaximos, valoresOptimizados)
    ganancia = calcula_ganancia_satisfaccion(satisfaccion, pesosPreferencias)
    print("Ganancia: ", ganancia)
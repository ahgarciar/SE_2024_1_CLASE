import SatisfaccionUsuario as s_usuario
import ComodidadEnConsumoEnergia as s_energia
import random as rnd

def calculaGanancia(alfa, beta, valoresAct, valoresOpt ,valoresMin, valoresMax, pesosPref, costosCambio):
    satisfaccion = s_usuario.calcula_satisfaccion(valoresMin, valoresMax, valoresOpt)
    ganancia_usuario = s_usuario.calcula_ganancia_satisfaccion(satisfaccion, pesosPref)
    #print("Ganancia Satisfaccion: ", ganancia_usuario)

    vEo = s_energia.calcula_Eo(valoresOpt, valoresAct, costosCambio)
    vEmin = s_energia.calcula_Emin(valoresMax, valoresMin, valoresAct, costosCambio)
    vEmax = s_energia.calcula_Emax(valoresMax, valoresMin, valoresAct, costosCambio)
    ganancia_energia = s_energia.calcula_ganancia_energia(vEo, vEmin, vEmax)
    #print("Ganancia Energia: ", ganancia_energia)

    ganancia_solucion = alfa * ganancia_usuario + beta * ganancia_energia

    return ganancia_solucion

if __name__ == "__main__":
    rnd.seed(5)

    #PREFERENCIAS MINIMAS Y MAXIMAS DE UN USUARIO...
    # C1 C2 C3 C4
    # C1 = TEMP
    # C2 = INTENSIDAD LUMINOSA
    # C3 = HUMEDAD
    # C4 = RUIDO
    valoresMinimos = [18, 50, 20, 15]
    valoresMaximos = [24, 400, 80, 200]

    #VALORES ACTUALES EN EL ENTORNO...
    valoresActuales = [22, 200, 50, 100] # sensores

    #PESOS(IMPORTANCIA) QUE TIENE QUE SE CUMPLA CADA CARACTERISTICA
    pesosPreferencias = [0.4, 0.3, 0.1, 0.2]

    # COSTO POR CAMBIAR UNA UNIDAD CADA CARACTERISTICA...
    costoCambio = [8, 3, 1, 5]  # C1, C2,..., Cn

    #busqueda local....
    tot_mejoras_buscadas = 10
    tot_iteraciones = 100

    mejorasRealizadas = 0
    iteracionesRealizadas = 0

    mejorGanancia = 0
    mejoresValoresEncontrados = []

    #alfa = 0.8
    #beta = 0.2

    alfa = 0.2
    beta = 0.8

    while iteracionesRealizadas<tot_iteraciones and mejorasRealizadas<tot_mejoras_buscadas:
        # VALORES OPTIMIZADOS...
        valoresOptimizados = [] # [20, 210, 40, 30]
        for i in range(len(valoresActuales)):
            val = rnd.randint(valoresMinimos[i], valoresMaximos[i])
            valoresOptimizados.append(val)

        gananciaModelo = calculaGanancia(alfa, beta, valoresActuales, valoresOptimizados ,
                                         valoresMinimos, valoresMaximos,
                                         pesosPreferencias, costoCambio)
        print("Ganancia del Modelo:" , gananciaModelo, end= "")

        if gananciaModelo > mejorGanancia:
            print("     Se actualizo la mejor ganancia", end="")
            mejorGanancia = gananciaModelo
            mejoresValoresEncontrados = valoresOptimizados.copy()
            mejorasRealizadas +=1
            iteracionesRealizadas = -1

        iteracionesRealizadas +=1
        print()

print("\nMejor Ganancia encontrada: ", mejorGanancia)
print("Mejores Valores Encontrados: ", mejoresValoresEncontrados)

## pip install requests   Fuente: https://pypi.org/project/requests/
import requests

url_base = "http://localhost:3000/api/v1"

def getAll_Historico_Dispositivos():
    #Get
    print("\nGET ALL REGISTROOS DE LOS DISPOSITIVOS: ")
    url = url_base + "/"
    response = requests.get(url, verify=False)
    result = response.json()
    print(result) #lista de diccionarios ...
    print(response.status_code)

    print("Table Info:")
    for register in result: # por cada diccionario de la lista...
        for key in register: # accede a cada propiedad del diccionario
            print("Attribute: ", key, " Value: ", register[key])
        print("\n")


#getAll_Historico_Dispositivos()
###############################################################################################################################
def getDispositivo_Historico(id):
    # Get
    print("\nGET REGISTROS DEL DISPOSITIVO: ")
    url = url_base + "/" + str(id)
    response = requests.get(url, verify=False)
    result = response.json()
    print(result)  # diccionario ...
    print(response.status_code)

    print("Table Info:")
    for register in result:
        for key in register:
            print("Attribute: ", key, " Value: ", register[key])
        print("\n")

#getDispositivo_Historico(3)
###############################################################################################################################
def getLastDispositivoHistorico(id):
    #Get with parameters
    print("GET LAST DECISION: ")
    url = url_base + "/dispositivos/" + str(id)
    response = requests.get(url, verify=False)
    result = response.json()
    print("Value of Device: ", result)
    print(response.status_code)
    for key in result:
        print("Attribute: ", key, " Value: ", result[key])
    print("\n")


getLastDispositivoHistorico(3)
###############################################################################################################################
def insertHistorico(idDispositivo, idHistorico, valor):
    #Post
    print("\n\nINSERT DISPOSITIVO")
    import json
    Id_Dispositivo = idDispositivo
    Id_Historico = idHistorico
    Valor = valor
    url = url_base + "/"
    headers = {"Content-Type":"application/json"}
    body = {"objetos":[{
        "Id_Dispositivo": Id_Dispositivo,
        "Id_Historico": Id_Historico,
        "Valor":Valor
        },
        {
            "Id_Dispositivo": Id_Dispositivo,
            "Id_Historico": Id_Historico,
            "Valor": Valor
        }
        ]
    }

    print(body)
    #{ objetos: [ { Id_Dispositivo: '3', Id_Historico: 5, Valor: 1000 } ] }
    response = requests.post(url, data=json.dumps(body), headers=headers, verify= False)
    print(response.json())
    print(response.status_code)


#insertHistorico("2", 7, 900)
###############################################################################################################################
def updateHistorico(idDispositivo, idHistorico, valor):
    #Put
    print("\n\nUPDATE DISPOSITIVO")
    import json
    Id_Dispositivo = idDispositivo
    Id_Historico = idHistorico
    Valor = valor
    url = url_base + "/" + str(Id_Historico)
    headers = {"Content-Type":"application/json"}
    body = {"objetos": [{
        "Id_Dispositivo": Id_Dispositivo,
        "Id_Historico": Id_Historico,
        "Valor": Valor
    }]
    }
    response = requests.put(url, data=json.dumps(body), headers=headers, verify= False)
    print(response.json())
    print(response.status_code)


#updateHistorico("2", 7, 100)
###############################################################################################################################
def deleteHistorico(idDispositivo, idHistorico, valor):
    #Post
    print("\n\nDELETE DISPOSITIVO")
    import json
    Id_Dispositivo = idDispositivo
    Id_Historico = idHistorico
    Valor = valor
    url = url_base + "/"
    headers =  {"Content-Type":"application/json"}
    body = {"objetos": [{
        "Id_Dispositivo": Id_Dispositivo,
        "Id_Historico": Id_Historico,
        "Valor": Valor
        }]
    }
    response = requests.delete(url, data=json.dumps(body), headers=headers, verify= False)
    print(response.json())
    print(response.status_code)


#deleteHistorico("2", 7, 100)
###############################################################################################################################








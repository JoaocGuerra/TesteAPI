import time
from datetime import datetime

import requests


def menu(data, numeropaciente):
    print("Data: ", data)
    print("Paciente em atendimento: ", numeropaciente)
    print("==========================")
    print("#OP#         Ação")
    print("#1#  Atendimento concluído")
    print("#2#  Encerrar aplicação")
    print("==========================")


def serviceCompleted(numeropaciente):
    print("Atendimento do Paciente " + numeropaciente + " encerrado", )
    time.sleep(1)
    print("Chamando próximo paciente")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)


dateVIEW = datetime.today().strftime('%d-%m-%Y')
dateURL = datetime.today().strftime('%d%m%Y')
dateURL = dateURL[:4] + dateURL[6:]

headers = {
    'Accept': '*/*',
    'User-Agent': 'request'
}

urlOA = "http://127.0.0.1:5000/atendimento/read/"

doctorRegistration = str(input("Insira sua mátricula: "))
patientInCare = urlOA + doctorRegistration + "/" + dateURL

while 1:
    patientPosition = str(requests.get(patientInCare).json()['paciente'])
    menu(dateVIEW, patientPosition)
    option = int(input("Insira a opcão desejada: "))
    if option == 1:
        serviceCompleted(patientPosition)
        nextPatient = {
            "codigo_medico": doctorRegistration,
            "dia_mes_ano": dateURL,
            "posicao_paciente_atendido": int(patientPosition)
        }
        urlPP = "http://127.0.0.1:5000/atendimento/update/paciente-atendido"
        requests.put(urlPP, headers=headers, json=nextPatient)

    elif option == 2:
        break

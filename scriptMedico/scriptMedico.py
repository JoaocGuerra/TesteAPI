import time
from datetime import datetime

import requests


def menu(data, numero_paciente):
    print("Data: ", data)
    print("Paciente em atendimento: ", numero_paciente)
    print("==========================")
    print("#OP#         Ação")
    print("#1#  Atendimento concluído")
    print("#2#  Encerrar aplicação")
    print("==========================")


def serviceCompleted(numero_paciente):
    print("Atendimento do Paciente " + numero_paciente + " encerrado", )
    time.sleep(1)
    print("Chamando próximo paciente")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)


date_view = datetime.today().strftime('%d-%m-%Y')
date_url = datetime.today().strftime('%d%m%Y')
date_url = date_url[:4] + date_url[6:]

headers = {
    'Accept': '*/*',
    'User-Agent': 'request'
}

url_oa = "http://127.0.0.1:5000/atendimento/read/"

doctor_registration = str(input("Insira sua mátricula: "))
patient_in_care = url_oa + doctor_registration + "/" + date_url

while 1:
    patient_position = str(requests.get(patient_in_care).json()['paciente'])
    menu(date_view, patient_position)
    option = int(input("Insira a opcão desejada: "))
    if option == 1:
        serviceCompleted(patient_position)
        nextPatient = {
            "codigo_medico": doctor_registration,
            "dia_mes_ano": date_url,
            "posicao_paciente_atendido": int(patient_position)
        }
        urlPP = "http://127.0.0.1:5000/atendimento/update/paciente-atendido"
        requests.put(urlPP, headers=headers, json=nextPatient)

    elif option == 2:
        break

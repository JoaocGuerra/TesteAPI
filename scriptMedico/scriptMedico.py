import requests
import time
from datetime import datetime

data = datetime.today().strftime('%d-%m-%Y')
dataURL = datetime.today().strftime('%d%m%Y')
dataURL = dataURL[:4] + dataURL[6:]

headers = {
    'Accept': '*/*',
    'User-Agent': 'request'
}

urlEA = "http://127.0.0.1:5000/atendimento/read/"

matriculaMedico = str(input("Insira sua mátricula: "))
pacienteEmAtendimento = urlEA + matriculaMedico + "/" + dataURL

while 1:
    numeroPaciente = str(requests.get(pacienteEmAtendimento).json()['paciente'])
    print("Data: ", data)
    print("Paciente em atendimento: ", numeroPaciente)
    print("==========================")
    print("#OP#         Ação")
    print("#1#  Atendimento concluído")
    print("#2#  Encerrar aplicação")
    print("==========================")
    opcao = int(input("Insira a opcão desejada: "))
    if opcao == 1:
        print("Atendimento do Paciente " + numeroPaciente + " encerrado", )
        time.sleep(1)
        print("Chamando próximo paciente")
        proximoPaciente = {
            "codigo_medico": matriculaMedico,
            "dia_mes_ano": dataURL,
            "posicao_paciente_atendido": int(numeroPaciente)
        }
        urlPP = "http://127.0.0.1:5000/atendimento/update/paciente-atendido"
        requests.put(urlPP, headers=headers, json=proximoPaciente)
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
    elif opcao == 2:
        break
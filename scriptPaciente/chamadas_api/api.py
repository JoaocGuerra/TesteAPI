import json

from scriptPaciente.constants.contant import URL_PATH, PATH_HORARIOS_DISPONIVEIS, PATH_INSERIR_PACIENTE, \
    PATH_POSICAO_FILA, PATH_POSICAO_EM_ATENDIMENTO, PATH_DELETE
import requests


class Api:

    def horarios_disponiveis(self, codigo_medico, dia_mes_ano):
        url = URL_PATH + PATH_HORARIOS_DISPONIVEIS + "/" + str(codigo_medico) + "/" + str(dia_mes_ano)

        return requests.get(url).json()['horarios_disponiveis']

    def inserir_paciente(self,contexto):
        url = URL_PATH + PATH_INSERIR_PACIENTE

        contexto_json = json.dumps(contexto.__dict__)

        retorno = requests.post(url,json=contexto_json)

        return retorno.status_code

    def read_posicao_fila(self,contexto):

        url = URL_PATH + PATH_POSICAO_FILA +"/"+contexto.codigo_medico+"/"+contexto.dia_mes_ano+"/"+str(contexto.codigo_paciente)

        return requests.get(url).json()

    def read_posicao_atendimento(self,contexto):

        url = URL_PATH + PATH_POSICAO_EM_ATENDIMENTO + "/" + contexto.codigo_medico + "/" + contexto.dia_mes_ano

        return requests.get(url).json()

    def desmarcar_consulta(self,contexto):

        url = URL_PATH + PATH_DELETE

        dict_delete = {
            'codigo_medico': contexto.codigo_medico,
            'dia_mes_ano': contexto.dia_mes_ano,
            'codigo_paciente': contexto.codigo_paciente
        }

        retorno = requests.delete(url, json=dict_delete)

        return retorno.status_code

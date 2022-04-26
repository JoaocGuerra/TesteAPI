from scriptPaciente.constants.contant import URL_PATH, PATH_HORARIOS_DISPONIVEIS
import requests


class APIHorariosDisponiveis:

    def horarios_disponiveis(self, codigo_medico, dia_mes_ano):
        url = URL_PATH + PATH_HORARIOS_DISPONIVEIS + "/" + str(codigo_medico) + "/" + str(dia_mes_ano)

        return requests.get(url).json()['horarios_disponiveis']

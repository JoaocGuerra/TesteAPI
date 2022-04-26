from scriptPaciente.chamadas_api.api import Api
from scriptPaciente.constants.contant import ESCOLHER_OPCAO
from scriptPaciente.get.get_informações import GetSetInformacoes
from scriptPaciente.menu.menu_principal import MenuPaciente
from scriptPaciente.model.contexto import Contexto


class Menu:

    def __init__(self):
        self.menu_paciente = MenuPaciente()
        self.get_set_informacoes = GetSetInformacoes.instance()
        self.api = Api()

    def executar(self):

        self.menu_paciente.menu_inicio()
        escolha_menu_paciente = int(input(ESCOLHER_OPCAO))

        if escolha_menu_paciente == 1:
            self.__marcar_consulta()
        if escolha_menu_paciente == 2:
            self.__situacao_fila()

    def __marcar_consulta(self):

        try:
            codigo_paciente = self.get_set_informacoes.getCodigoPaciente()

            self.menu_paciente.menu_marcar_consulta_medicos()
            opcao_medico = int(input(ESCOLHER_OPCAO)) - 1
            codigo_medico = self.get_set_informacoes.getMedicos()[opcao_medico]

            self.menu_paciente.menu_marcar_consulta_datas(codigo_medico)
            opcao_dia = int(input(ESCOLHER_OPCAO)) - 1
            dia_mes_ano = self.get_set_informacoes.getDias()[opcao_dia]

            self.menu_paciente.menu_marcar_consulta_horarios(codigo_medico, dia_mes_ano)
            opcao_horario = int(input(ESCOLHER_OPCAO)) - 1
            horario = self.get_set_informacoes.getHorarios()[opcao_horario]

            horario_split = horario.split(":")

            contexto = Contexto(
                codigo_medico=codigo_medico,
                dia_mes_ano=dia_mes_ano,
                codigo_paciente=codigo_paciente,
                hora=int(horario_split[0]),
                minuto=int(horario_split[1])
            )

            if self.api.inserir_paciente(contexto) == 200:
                print("Paciente inserido com sucesso!")

            else:
                print("Algo de errado aconteceu.")

        except:
            print("Algo de errado aconteceu.")

    def __situacao_fila(self):

        self.menu_paciente.menu_consulta_situacao_fila()
        opcao_consulta = int(input(ESCOLHER_OPCAO)) - 1
        consulta = self.get_set_informacoes.getListaConsultas()[opcao_consulta]

        contexto = Contexto(
            codigo_medico=consulta['codigo_medico'],
            dia_mes_ano=consulta['dia_mes_ano'],
            codigo_paciente=self.get_set_informacoes.getCodigoPaciente(),
            hora=None,
            minuto=None
        )

        self.menu_paciente.menu_situacao_fila(contexto)
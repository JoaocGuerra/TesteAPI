from scriptPaciente.menu.menu_secundario import MenuSecundario


class MenuPaciente:

    def __init__(self):
        self.menu_secundario = MenuSecundario()

    def menu_codigo_paciente(self):

        self.menu_secundario.menu_codigo_paciente()

    def menu_inicio(self):

        menu = ""

        menu += "==========================\n"
        menu += "1 - Marcar consulta\n"
        menu += "2 - Desmarcar Consulta\n"
        menu += "3 - Consultar Situação da Fila\n"
        menu += "=========================="

        print(menu)

    def menu_marcar_consulta_medicos(self):
        print(self.menu_secundario.menu_medicos())

    def menu_marcar_consulta_datas(self,codigo_medico):
        print(self.menu_secundario.menu_dias_mes_ano(codigo_medico))

    def menu_marcar_consulta_horarios(self,codigo_medico,dia_mes_ano):
        print(self.menu_secundario.menu_horarios_disponiveis(codigo_medico,dia_mes_ano))

    def menu_consultas(self):
        print(self.menu_secundario.menu_consultas())

    def menu_situacao_fila(self,contexto):
        print(self.menu_secundario.menu_situacao_fila(contexto))
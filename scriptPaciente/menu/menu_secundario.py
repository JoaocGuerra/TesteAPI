from scriptPaciente.banco_dados.firestore_database_singleton import FirestoreDatabaseSingleton
from scriptPaciente.chamadas_api.api import Api
from scriptPaciente.constants.contant import DIGITE_SEU_ID
from scriptPaciente.get.get_informações import GetSetInformacoes
from scriptPaciente.utilitarios.utils_time import UtilsTime


class MenuSecundario:

    def __init__(self):
        self.api = Api()
        self.get_set_informacoes = GetSetInformacoes.instance()
        self.db = FirestoreDatabaseSingleton.instance().db
        self.utils_time = UtilsTime()

    def menu_codigo_paciente(self):

        codigo_paciente = input(DIGITE_SEU_ID)
        self.get_set_informacoes.setCodigoPaciente(codigo_paciente)

    def menu_medicos(self):

        doc_ref = self.db.collection('funcionarios').document('medicos').collections()
        lista_medicos = []

        for collection in doc_ref:
            lista_medicos.append(collection.id)

        self.get_set_informacoes.setMedicos(lista_medicos)

        tamanho_lista_medicos = len(lista_medicos)

        menu = "==========================\n"
        menu += "Escolha um médico:\n"

        for i in range(tamanho_lista_medicos):
            menu += str(i + 1) + " - " + lista_medicos[i] + "\n"

        menu += "=========================="

        return menu

    def menu_dias_mes_ano(self,codigo_medico):

        doc_ref = self.db.collection('funcionarios').document('medicos').collection(codigo_medico).document('atendimentos').collections()
        lista_dia_mes_ano = []

        for collection in doc_ref:
            lista_dia_mes_ano.append(collection.id)

        self.get_set_informacoes.setDias(lista_dia_mes_ano)

        tamanho_lista_dia_mes_ano = len(lista_dia_mes_ano)

        menu = "==========================\n"
        menu += "Escolha uma data:\n"

        for i in range(tamanho_lista_dia_mes_ano):
            menu += str(i + 1) + " - " + self.utils_time.adicionar_barra_divisoria(lista_dia_mes_ano[i]) + "\n"

        menu += "=========================="

        return menu

    def menu_horarios_disponiveis(self, codigo_medico, dia_mes_ano):

        lista_horarios_disponiveis = self.api.horarios_disponiveis(codigo_medico, dia_mes_ano)
        self.get_set_informacoes.setHorarios(lista_horarios_disponiveis)

        tamanho_lista_horarios_disponiveis = len(lista_horarios_disponiveis)

        menu = "==========================\n"
        menu += "Escolha um dos horários disponiveis:\n"

        for i in range(tamanho_lista_horarios_disponiveis):
            menu += str(i + 1) + " - " + lista_horarios_disponiveis[i] + "\n"

        menu += "=========================="

        return menu

    def menu_consultas(self):

        doc_ref = self.db.collection('pacientes').document(str(self.get_set_informacoes.getCodigoPaciente())).collection('consultas').stream()
        lista_consultas = []
        i=0

        menu = "==========================\n"
        menu += "Escolha uma das consultas:\n"

        for collection in doc_ref:
            i+=1
            documento = collection.to_dict()
            menu+= str(i)+" - Médico: "+documento["codigo_medico"]+", Dia: "+self.utils_time.adicionar_barra_divisoria(documento["dia_mes_ano"])+"\n"
            lista_consultas.append(documento)

        menu += "=========================="

        self.get_set_informacoes.setListaConsultas(lista_consultas)

        return menu

    def menu_situacao_fila(self,contexto):

        informacoes_atendimento = self.api.read_posicao_atendimento(contexto)
        informacoes_paciente = self.api.read_posicao_fila(contexto)

        menu = "==========================\n"
        menu += "O paciente em atendimento é o de posição: " + str(informacoes_atendimento['paciente']) + "\n"
        menu += "Você está na posição: "+str(informacoes_paciente['posicao'])+"\n"
        menu += "=========================="

        return menu
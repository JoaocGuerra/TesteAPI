class GetSetInformacoes:
    _instance = None

    def __init__(self):
        self.lista_horarios = None
        self.lista_medicos = None
        self.lista_dias = None
        self.codigo_paciente = None
        self.lista_consultas = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def getHorarios(self):
        return self.lista_horarios

    def setHorarios(self,horarios):
        self.lista_horarios = horarios

    def getMedicos(self):
        return self.lista_medicos

    def setMedicos(self,medicos):
        self.lista_medicos = medicos

    def getDias(self):
        return self.lista_dias

    def setDias(self, dias):
        self.lista_dias = dias

    def getCodigoPaciente(self):
        return self.codigo_paciente

    def setCodigoPaciente(self, codigo_paciente):
        self.codigo_paciente = codigo_paciente

    def getListaConsultas(self):
        return self.lista_consultas

    def setListaConsultas(self, lista_consultas):
        self.lista_consultas = lista_consultas
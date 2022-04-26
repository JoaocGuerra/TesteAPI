from scriptPaciente.menu.gerenciamento_menu import Menu
from scriptPaciente.menu.menu_principal import MenuPaciente

menu = Menu()
menu_paciente = MenuPaciente()
menu_paciente.menu_codigo_paciente()

while(True):
    menu.executar()


class UtilsTime:

    def adicionar_barra_divisoria(self,data):

        data_com_barras_divisorias = ""
        j = 0

        for i in range(8):

            if i == 2 or i == 5:
                data_com_barras_divisorias += "/"

            else:
                data_com_barras_divisorias+=data[j]
                j+=1

        return data_com_barras_divisorias



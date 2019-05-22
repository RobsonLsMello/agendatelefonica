class TextoUtil:
    """
        Verificador de texto com caracteres especiais
    """

    def verificarTextoComCaracteresEspeciais(self, texto:str):
        caracteresEspeciaisEmAscii = []
        caracteresEspeciaisEmAscii.append([33,47])
        caracteresEspeciaisEmAscii.append([58,64])
        caracteresEspeciaisEmAscii.append([91,96])
        caracteresEspeciaisEmAscii.append([123,126])
        temCaracteresEspeciais = False
        for y in caracteresEspeciaisEmAscii:
            for x in range(y[0], y[1] + 1, 1):
                if(texto.find(chr(x)) != -1):
                    temCaracteresEspeciais = True
                    break
            if(temCaracteresEspeciais):
                break
        return temCaracteresEspeciais

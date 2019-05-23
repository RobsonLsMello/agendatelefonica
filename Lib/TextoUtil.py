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

    def verificarTextoComAlpha(self, texto:str):
        caracteresAlphaEmAscii = []
        caracteresAlphaEmAscii.append([65,90])
        caracteresAlphaEmAscii.append([97,122])
        temAlpha = False
        for y in caracteresAlphaEmAscii:
            for x in range(y[0], y[1] + 1, 1):
                if(texto.find(chr(x)) != -1):
                    temAlpha = True
                    break
            if(temAlpha):
                break
        return temAlpha

    def verificarTextoComNumeros(self, texto:str):
        temNumeros = False
        for x in range(48, 58, 1):
            if(texto.find(chr(x)) != -1):
                temNumeros = True
                break
        return temNumeros

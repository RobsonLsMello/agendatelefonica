class TextoUtil:
    """
        Verificador de texto
    """

    def verificarTextoComCaracteresEspeciais(self, texto:str, isEmail:bool = False):
        caracteresEspeciaisEmAscii = []
        caracteresEspeciaisEmAscii.append([0,31])
        caracteresEspeciaisEmAscii.append([33,47])
        caracteresEspeciaisEmAscii.append([58,64])
        caracteresEspeciaisEmAscii.append([91,96])
        caracteresEspeciaisEmAscii.append([123,127])
        if(isEmail):
            caracteresEspeciaisEmAscii.append([128,255])
        else:
            caracteresEspeciaisEmAscii.append([155,158]) 
            caracteresEspeciaisEmAscii.append([166,180]) 
            caracteresEspeciaisEmAscii.append([184,197]) 
            caracteresEspeciaisEmAscii.append([200,207]) 
            caracteresEspeciaisEmAscii.append([217,223]) 
            caracteresEspeciaisEmAscii.append([238,255]) 
            
        temCaracteresEspeciais = False
        for y in caracteresEspeciaisEmAscii:
            for x in range(y[0], y[1] + 1, 1):
                if(texto.find(chr(x)) != -1):
                    temCaracteresEspeciais = True
                    break
            if(temCaracteresEspeciais):
                break
        if(len(texto) > 0 and texto[0] == " "):
            temCaracteresEspeciais = True
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

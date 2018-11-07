"""
Instrucciones de uso:
Este programa esta en fase UltraPreAlfa, es decir, no esta acabado, estos son los ultimos avanzes que he
hecho este tiempo, de momento el programa SOLO sabe distinguir verbos conjugados en PRESENTE SIMPLE
y PRESENTE CONTINUO. Por ahora no puede distinguir mas tiempos verbales que esos 2, en el futuro soportará
todos. Att: TheRusher28
"""

__author__ = "TheRusher28"
__copyright__ = "Copyright 2018, TheRusher28"
__credits__ = "TheRusher28"

__mantainer__ = "TheRusher28"
__email__ = "therusher28@gmail.com"
__status__ = "Beginner"

class Verbo:
    def __init__(self):
        self.verbo = input('Introduzca el verbo: ')
        self.persona = 1
        self.numero = ''
        self.sujeto = ['I', 'You', 'He ', 'She', 'It ', 'We', 'You ', 'They']
        self.to_be = ['am ', 'are', 'is ', 'are', 'are', 'are']
        self.to_be_past = ['was ', 'were', 'was ', 'were', 'were', 'were']
        self.tiempo = ''
        self.suj = ''
        self.vb_sin_suj = ''
        self.vb_sin_tb = ''

    def identificar_sujeto(self, verbo, sujeto, persona):
        if self.verbo[0] == self.sujeto[0]:
            self.persona = 1
            self.numero = 'sing'
        elif self.verbo[0:3] == self.sujeto[1]:
            self.persona = 2
            self.numero = 'sing'
        elif self.verbo[0:2] == self.sujeto[2] or self.verbo[0:3] == self.sujeto[3] or self.verbo[0:2] == self.sujeto[4]:
            self.persona = 3
            self.numero = 'sing'
        elif self.verbo[0:2] == self.sujeto[5]:
            self.persona = 1
            self.numero = 'pl'
        elif self.verbo[0:4] == self.sujeto[6]:
            self.persona = 2
            self.numero = 'sing'
        elif self.verbo[0] == self.sujeto[7]:
            self.persona = 3
            self.numero = 'sing'

    def coger_sujeto(self, verbo, persona, numero, vb_sin_sujeto):
        if self.persona == 1 and self.numero == 'sing':
            self.suj = self.verbo[0:1]
            self.vb_sin_suj = self.verbo[1:15]
        elif self.persona == 2 and self.numero == 'sing':
            self.suj = self.verbo[0:3]
            self.vb_sin_suj = self.verbo[3:18]
        elif self.persona == 3 and self.numero == 'sing':
            self.suj = self.verbo[0:3]
            self.vb_sin_suj = self.verbo[3:18]
        elif self.persona == 1 and self.numero == 'pl':
            self.suj = self.verbo[0:2]
            self.vb_sin_suj = self.verbo[2:17]
        elif self.persona == 2 and self.numero == 'pl':
            self.suj = self.verbo[0:4]
            self.vb_sin_suj = self.verbo[4:19]
        elif self.persona == 3 and self.numero == 'pl':
            self.suj = self.verbo[0:4]
            self.vb_sin_suj = self.verbo[4:19]
        else:
            print('No tiene sujeto')
        return self.vb_sin_suj


    def identificar_presente(self, verbo, tiempo, suj, vb_sin_suj, vb_sin_tb):
        if self.vb_sin_suj[0:4] == ' am ' or self.vb_sin_suj[0:3] == ' are' or self.vb_sin_suj[0:3] == ' is ':
            self.tiempo = 'Presente Continuo'
        else:
            self.tiempo = 'Presente Simple'
        pass

verbo = Verbo()

verbo.identificar_sujeto(verbo.verbo, verbo.sujeto, verbo.persona)
verbo.coger_sujeto(verbo.verbo, verbo.persona, verbo.numero, verbo.vb_sin_suj)
print(verbo.identificar_presente(verbo.verbo, verbo.tiempo, verbo.suj, verbo.vb_sin_suj, verbo.vb_sin_tb))
print(verbo.verbo)
print(verbo.vb_sin_suj)
print(__copyright__)
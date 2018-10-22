"""
Por ahora el programa solo es capaz de analizar formas infinitivas pero ya me estoy poniendo
a trabajar para que identifique formas conjugadas de los verbos y tambien que pueda identificar
los gerundios y los participios :D Att:TheRusher28 
"""

__author__ = "TheRusher28"
__copyright__ = "Copyright 2018, TheRusher28"
__credits__ = "TheRusher28"

__mantainer__ = "TheRusher28"
__email__ = "therusher28@gmail.com"
__status__ = "Beginner"

class Verbo:
    def __init__(self):
        self.verbo = input('Introduzca su verbo en infinitivo, porfavor: ')
        self.lexema = None
        self.conjugacion = None
        self.desinencia = None

    def coger_lexema(self, verbo, lexema):
        if len(self.verbo) == 2:
            print('Tiene 2 letras/l')
            self.lexema = self.verbo[0:2]
        elif len(self.verbo) == 3:
            print('Tiene 3 letras/l')
            self.lexema = self.verbo[0:1]
        elif len(self.verbo) == 4:
            print('Tiene 4 letras/l')
            self.lexema = self.verbo[0:2]
        elif len(self.verbo) == 5:
            print('Tiene 5 letras/l')
            self.lexema = self.verbo[0:3]
        elif len(self.verbo) == 6:
            print('Tiene 6 letras/l')
            self.lexema = self.verbo[0:4]
        elif len(self.verbo) == 7:
            print('Tiene 7 letras/l')
            self.lexema = self.verbo[0:5]
        elif len(self.verbo) == 8:
            print('Tiene 8 letras/l')
            self.lexema = self.verbo[0:6]
        elif len(self.verbo) == 9:
            print('Tiene 9 letras/l')
            self.lexema = self.verbo[0:7]
        elif len(self.verbo) == 10:
            print('Tiene 10 letras/l')
            self.lexema = self.verbo[0:8]
        elif len(self.verbo) == 11:
            print('Tiene 11 letras/l')
            self.lexema = self.verbo[0:9]
        elif len(self.verbo) == 12:
            print('Tiene 12 letras/l')
            self.lexema = self.verbo[0:10]
        else:
            print('Tiene demasiadas letras/l')
        return self.lexema

    def coger_desinencia(self, verbo, desinencia):
        if len(self.verbo) == 2:
            print('Tiene 2 letras/d')
            self.desinencia = self.verbo[0:2]
        elif len(self.verbo) == 3:
            print('Tiene 3 letras/d')
            self.desinencia = self.verbo[2:3]
        elif len(self.verbo) == 4:
            print('Tiene 4 letras/d')
            self.desinencia = self.verbo[2:4]
        elif len(self.verbo) == 5:
            print('Tiene 5 letras/d')
            self.desinencia = self.verbo[3:5]
        elif len(self.verbo) == 6:
            print('Tiene 6 letras/d')
            self.desinencia = self.verbo[4:6]
        elif len(self.verbo) == 7:
            print('Tiene 7 letras/d')
            self.desinencia = self.verbo[5:7]
        elif len(self.verbo) == 8:
            print('Tiene 8 letras/d')
            self.desinencia = self.verbo[6:8]
        elif len(self.verbo) == 9:
            print('Tiene 9 letras/d')
            self.desinencia = self.verbo[7:9]
        elif len(self.verbo) == 10:
            print('Tiene 10 letras/d')
            self.desinencia = self.verbo[8:10]
        elif len(self.verbo) == 11:
            print('Tiene 11 letras/d')
            self.desinencia = self.verbo[9:11]
        elif len(self.verbo) == 12:
            print('Tiene 12 letras/d')
            self.desinencia = self.verbo[10:12]
        else:
            print('Tiene demasiadas letras/d')
        return self.desinencia

    def identificar_conjugacion(self, verbo, conjugacion):
        if self.desinencia == 'ar':
            print('Es de primera conjugacion')
            self.conjugacion = 1
        elif self.desinencia == 'er':
            print('Es de segunda conjugacion')
            self.conjugacion = 2
        elif self.desinencia == 'ir':
            print('Es de tercera conjugacion')
            self.conjugacion = 3
        return self.conjugacion


verbo = Verbo()
print(verbo.coger_lexema(verbo.verbo, verbo.lexema))
print(verbo.coger_desinencia(verbo.verbo, verbo.desinencia))
print(verbo.identificar_conjugacion(verbo.verbo, verbo.conjugacion))

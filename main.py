
"""
Version: Beta v0.4
El proyecto no está acabado, le faltan cosas por pulir todavia, he podido hacer que funcione con Presente Simple,
Presente Continuo, Pasado Simple (Junto con verbos irregulares), Pasado Continuo, Condicional Simple
y Condicional Continuo.jafsnfjasfiasofoiasjf
"""
__author__ = "TheRusher28"
__copyright__ = "Copyright 2018, TheRusher28"
__credits__ = "TheRusher28"

__mantainer__ = "TheRusher28"
__email__ = "therusher28@gmail.com"
__status__ = "Beginner"
__version__ = 'Beta v0.4'

class Verbo:
    def __init__(self):     #Esta es la clase donde se almacenará y analizara lo que tu escribas
        self.verbo = input('Introduzca el verbo: ')
        self.persona = 1
        self.numero = ''
        self.sujeto = ['I', 'You', 'He', 'She', 'it', 'We', 'You ', 'They']
        self.to_be = ['am ', 'are', 'is ', 'are', 'are', 'are']
        self.to_be_past = ['was ', 'were', 'was ', 'were', 'were', 'were']
        self.tiempo = ''
        self.suj = ''
        self.vb_sin_suj = ''
        self.vb_sin_tb = ''
        self.desinencia = ''

    def identificar_sujeto(self, verbo, sujeto, persona):      #En esta funcion se coge las primeras letras y se comparan con los distintos para poder designar self.numero y self.persona.
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
            self.numero = 'pl'
        elif self.verbo[0:4] == self.sujeto[7]:
            self.persona = 3
            self.numero = 'pl'

    def coger_sujeto(self, verbo, persona, numero, vb_sin_sujeto):      #En esta otra función se cogen los datos de identificar_sujeto() y dependiendo de estos se extrae parte del verbo que será self.suj y self.vb_sin_suj.
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

    def coger_desinencia(self, verbo, desinencia):      #Se cogen las ultimas tres letras, algo util para que el programa sepa diferenciar entre los tiempos verbales implementados.
        if len(self.verbo) == 2:
            print('Tiene 2 letras')
            self.desinencia = self.verbo[0:2]
        elif len(self.verbo) == 3:
            print('Tiene 3 letras')
            self.desinencia = self.verbo[0:3]
        elif len(self.verbo) == 4:
            print('Tiene 4 letras')
            self.desinencia = self.verbo[1:4]
        elif len(self.verbo) == 5:
            print('Tiene 5 letras')
            self.desinencia = self.verbo[2:5]
        elif len(self.verbo) == 6:
            print('Tiene 6 letras')
            self.desinencia = self.verbo[3:6]
        elif len(self.verbo) == 7:
            print('Tiene 7 letras')
            self.desinencia = self.verbo[4:7]
        elif len(self.verbo) == 8:
            print('Tiene 8 letras')
            self.desinencia = self.verbo[5:8]
        elif len(self.verbo) == 9:
            print('Tiene 9 letras')
            self.desinencia = self.verbo[6:9]
        elif len(self.verbo) == 10:
            print('Tiene 10 letras')
            self.desinencia = self.verbo[7:10]
        elif len(self.verbo) == 11:
            print('Tiene 11 letras')
            self.desinencia = self.verbo[8:11]
        elif len(self.verbo) == 12:
            print('Tiene 12 letras')
            self.desinencia = self.verbo[9:12]
        elif len(self.verbo) == 13:
            print('Tiene 13 letras')
            self.desinencia = self.verbo[10:13]
        elif len(self.verbo) == 14:
            print('Tiene 14 letras')
            self.desinencia = self.verbo[11:14]
        elif len(self.verbo) == 15:
            print('Tiene 15 letras')
            self.desinencia = self.verbo[12:15]
        elif len(self.verbo) == 16:
            print('Tiene 16 letras')
            self.desinencia = self.verbo[13:16]
        elif len(self.verbo) == 17:
            print('Tiene 17 letras')
            self.desinencia = self.verbo[14:17]
        elif len(self.verbo) == 19:
            print('Tiene 18 letras')
            self.desinencia = self.verbo[15:18]
        elif len(self.verbo) == 19:
            print('Tiene 19 letras')
            self.desinencia = self.verbo[16:19]
        elif len(self.verbo) == 20:
            print('Tiene 20 letras')
            self.desinencia = self.verbo[17:20]
        elif len(self.verbo) == 21:
            print('Tiene 21 letras')
            self.desinencia = self.verbo[18:21]
        else:
            print('Tiene demasiadas letras/d')
        return self.desinencia

    def identificar_presente(self, verbo, tiempo, suj, vb_sin_suj, vb_sin_tb):      #Esta funcion coge todos los datos anteriores como self.vb_sin_suj y self.desinencia para decir si el verbo en cuestion es o no de alguno de los tiempos verbales de presente.
        if self.vb_sin_suj[0:4] == ' am ' or self.vb_sin_suj[0:4] == ' are' or self.vb_sin_suj[0:3] == 'is ' or self.vb_sin_suj[0:4] == ' is ':
            self.tiempo = 'Present Continuous'
        elif self.desinencia != 'ing':
            self.tiempo = 'Present Simple'
        return self.tiempo

    def identificar_pasado(self, verbo, tiempo, suj, vb_sin_suj, vb_sin_tb):        #Esta funcion hace lo mismo que identificar_presente() pero con el pasado.
        if self.vb_sin_suj[0:4] == ' was' or self.vb_sin_suj[0:3] == 'was' or self.vb_sin_suj[0:5] == ' were':
            self.tiempo = 'Past continuous'
        elif self.desinencia[1:3] == 'ed':
            self.tiempo = 'Past Simple'
        return self.tiempo

    def identificar_condicional(self, vb_sin_suj, desinencia, tiempo):      #Esta funcion hace lo mismo que identificar_pasado() pero con el condicional.
        if vb_sin_suj[0:6] == ' would' and self.desinencia == 'ing' or vb_sin_suj[0:5] == 'would':
            self.tiempo = 'Condicional Continuo'
        if vb_sin_suj[0:6] == ' would' and self.desinencia != 'ing' or vb_sin_suj[0:5] == 'would':
            self.tiempo = 'Condicional Simple'
        return self.tiempo

    def identificar_regular(self, verbo, tiempo):       #Esta funcion es para identificar si nuestro verbo es irregular, en este caso tambien seria del pasado simple.
        if self.vb_sin_suj == ' abode' or self.vb_sin_suj == ' abided':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' arose':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' awoke':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' backbitten':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' backslid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' bore':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' beat':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' became':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' befell':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' begot' or self.vb_sin_suj == ' begat':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' began':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' begirt':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' beheld':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' bent':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' bereft' or self.vb_sin_suj == ' bereaved':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' besought' or self.vb_sin_suj == ' beseeched':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' beset':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' bespoke':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' bespat':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' bestrode':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' bet' or self.vb_sin_suj == ' betted':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' betook':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' bad' or self.vb_sin_suj == ' bade' or self.vb_sin_suj == ' bid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' bound':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' bit':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' bled':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' blessed':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' blew':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' broke':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' bred':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' brought':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' broadcast':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' browbeat':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' built':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' burnt' or self.vb_sin_suj == ' burned':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' burst':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' bust' or self.vb_sin_suj == ' busted':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' bought':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' could':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' cast':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' caught':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' chid' or self.vb_sin_suj == ' chided':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' chose':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' clove' or self.vb_sin_suj == ' cleft' or self.vb_sin_suj == ' cleaved':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' clung':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' came':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' cost':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' countersank':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' crept':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' crowed' or self.vb_sin_suj == ' crew':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' cut':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' durst' or self.vb_sin_suj == ' dared':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' dealt':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' dug':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' dived' or self.vb_sin_suj == ' dove':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' did':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' drew':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' dreamt' or self.vb_sin_suj == ' dreamed':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' drank':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' drove':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' dwelt':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' ate':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' fell':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' fed':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' felt':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' fought':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' found':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' fit':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' fled':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' flung':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' floodlighted' or self.vb_sin_suj == ' floodlit':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' flew':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' forbore':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' forbad' or self.vb_sin_suj == ' forbade':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' forecast' or self.vb_sin_suj == ' forecasted':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' foresaw':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' foretold':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' forgot':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' forgave':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' forsook':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' forswore':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' froze':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' gainsaid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' got':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' gilt' or self.vb_sin_suj == ' gilded':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' girded' or self.vb_sin_suj == ' girt':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' gave':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' went':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' graved':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' ground':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' grew':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' hamstringed' or self.vb_sin_suj == ' hamstrung':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' hung' or self.vb_sin_suj == ' hanged':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' had':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' heard':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' heaved' or self.vb_sin_suj == ' hove':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' hewed':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' hid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' held':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' hurt':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' inlaid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' input' or self.vb_sin_suj == ' inputted':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' inset':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' interwove':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' kept':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' kenned' or self.vb_sin_suj == ' kent':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' knelt' or self.vb_sin_suj == ' kneeled':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' knit' or self.vb_sin_suj == ' knitted':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' knew':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' laded':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' laid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' led':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' leant' or self.vb_sin_suj == ' leaned':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' leapt' or self.vb_sin_suj == ' leaped':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' learnt' or self.vb_sin_suj == ' learned':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' left':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' lent':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' let':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' lay':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' lit' or self.vb_sin_suj == ' lighted':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' lost':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' made':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' might':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' meant':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' met':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' miscast':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' misdealt':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' misgave':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' misheard':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' mishit':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' mislaid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' misled':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' misread':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' misspelt' or self.vb_sin_suj == ' misspeled':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' misspent':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' misstook':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' misunderstood':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' mowed':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' outbid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' outdid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' outfought':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' outgrew':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' output' or self.vb_sin_suj == ' outputted':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' outran':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' outsold':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' outshone':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' overbid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' overcame':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' overdid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' overdrew':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' overate':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' overflew':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' overhung':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' overheard':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' overlaid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' overpaid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' overrode':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' overran':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' oversaw':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' overshot':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' overslept':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' overtook':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' overthrew':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' partook':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' paid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' pleaded' or self.vb_sin_suj == ' pled':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' prepaid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' proved':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' put':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' quit' or self.vb_sin_suj == ' quitted':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' read':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' rebound':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' rebuilt':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' reacast':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' redid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' reheard':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' remade':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' rent':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' repaid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' reran':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' resold':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' reset':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' resat':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' retook':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' retold':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' rewrote':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' rid' or self.vb_sin_suj == ' ridded':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' rode':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' rang':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' rose':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' rived':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' ran':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' sawed':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' said':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' saw':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' sought':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' sold':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' sent':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' set':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' sewed':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' shook':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' shaved':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' sheared':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' shed':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' shone' or self.vb_sin_suj == ' shined':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' shod':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' shot':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' showed':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' shred' or self.vb_sin_suj == ' shredded':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' shrank' or self.vb_sin_suj == ' shrunk':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' shrove' or self.vb_sin_suj == ' shrived':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' shut':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' sang':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' sank':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' sat':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' slew':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' slept':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' slid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' slung':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' slunk':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' slit':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' smelt' or self.vb_sin_suj == ' smelled':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' smote':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' sowed':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' spoke':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' sped' or self.vb_sin_suj == ' speeded':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' spelt' or self.vb_sin_suj == ' spelled':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' spent':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' spilt' or self.vb_sin_suj == ' spilled':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' spun' or self.vb_sin_suj == ' span':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' spat' or self.vb_sin_suj == ' spit':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' split':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' spoilt' or self.vb_sin_suj == ' spoiled':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' spotlit' or self.vb_sin_suj == ' spotlighted':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' spread':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' sprang':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' stood':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' staved' or self.vb_sin_suj == ' stove':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' stole':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' stuck':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' stung':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' stank' or self.vb_sin_suj == ' stunk':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' strewed':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' strode':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' struck':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' strung':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' strove':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' sublet':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' swore':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' swept':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' swelled':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' swam':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' swung':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' took':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' taught':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' tore':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' told':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' thought':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' tore':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' told':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' thought':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' throve' or self.vb_sin_suj == ' trived':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' threw':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' thrust':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' trod':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' unbent':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' underbid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' undercut':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' underwent':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' underlay':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' underpaid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' undersold':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' understood':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' undertook':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' underwrote':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' undid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' unfroze':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' unsaid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' unwound':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' upheld':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' upset':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' woke' or self.vb_sin_suj == ' waked':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' waylaid':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' wore':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' wove' or self.vb_sin_suj == ' weaved':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' wed' or self.vb_sin_suj == ' wedded':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' wept':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' wet' or self.vb_sin_suj == ' wetted':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' won':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' wound':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' withdrew':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' withheld':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' withstood':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' worked' or self.vb_sin_suj == ' wrought':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' wrung':
            self.tiempo = 'Past simple(irr)'
        elif self.vb_sin_suj == ' wrote':
            self.tiempo = 'Past simple(irr)'
        return self.tiempo

#Ejecutacion de todas las funciones.
verbo = Verbo()
verbo.coger_desinencia(verbo.verbo, verbo.desinencia)
verbo.identificar_sujeto(verbo.verbo, verbo.sujeto, verbo.persona)
verbo.coger_sujeto(verbo.verbo, verbo.persona, verbo.numero, verbo.vb_sin_suj)
verbo.identificar_presente(verbo.verbo, verbo.tiempo, verbo.suj, verbo.vb_sin_suj, verbo.vb_sin_tb)
verbo.identificar_pasado(verbo.verbo, verbo.tiempo, verbo.suj, verbo.vb_sin_suj, verbo.vb_sin_tb)
verbo.identificar_condicional(verbo.vb_sin_suj, verbo.desinencia, verbo.tiempo)
verbo.identificar_regular(verbo.tiempo, verbo.vb_sin_suj)
#Printeo de datos utiles.
print('El tiempo verbal de {} es {}' .format(verbo.verbo, verbo.tiempo))
#print(verbo.vb_sin_suj)
#print(verbo.desinencia)
print(__copyright__)
print(__version__)

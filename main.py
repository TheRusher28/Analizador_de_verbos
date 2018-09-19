
pkmn_rival = input('¿Con qué pokemon quieres luchar? (Bulbasaur, Charmander, Squirtle): ')
vida_pikachu = 100
vida_enemigo = 0
dano_enemigo = 0
if pkmn_rival == 'Bulbasaur':
    vida_enemigo = 100
elif pkmn_rival == 'Charmander':
    vida_enemigo = 70
elif pkmn_rival == 'Squirtle':
    vida_enemigo = 80
else:
    print("No elegiste ninguno de los pokemon de la lista...")

if pkmn_rival == 'Bulbasaur':
    dano_enemigo = 10
elif pkmn_rival == 'Charmander':
    dano_enemigo = 7
elif pkmn_rival == 'Squirtle':
    dano_enemigo = 8
else:
    print("No te hicieron daño...")


while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input('¿Qué ataque usamos? (Chispazo, Bola Voltio): ')
    if ataque_elegido == 'Chispazo':
        vida_enemigo -= 10
    if ataque_elegido == 'Bola Voltio':
        vida_enemigo -= 12
    vida_pikachu = vida_pikachu - dano_enemigo
    print(pkmn_rival, 'te quito', dano_enemigo, 'PS')
    print('Usaste', ataque_elegido, 'y', pkmn_rival, 'perdio un poco de PS')
    print('PS', pkmn_rival , ':',  vida_enemigo)
    print('PS pikachu :', vida_pikachu)


print('El combate ha terminado')
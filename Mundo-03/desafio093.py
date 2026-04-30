print(f"{'PROGRAMA BOM DE BOLA':=^42}")
futebol = {}
futebol ['jogador'] = str(input('- Nome do jogador: '))
partidas = int(input(f'- Quantas partidas {futebol["jogador"]} jogou? '))
gols = []
for c in range(1, partidas +1):
    gols.append(int(input(f'- Quantos gols foram feitos no {c} jogo? ')))
futebol ['gols'] = gols[:]
print ('-='*21)
print (f'- O jogador {futebol["jogador"]} jogou {partidas} partidas.')
for k, v in enumerate(futebol['gols']):
    print (f'- Na partida {k + 1} fez {v} gols.')
total = sum(futebol['gols'])
print (f'- Foi no total das {partidas} partidas: {total} gols.')
print ('-='*21)
votos = ['AD', 'JG', 'JG', 'AD', 'AD', 'JG', 'JG', 'AD', 'JG', 'JG', 'AD', 'AD', 'JG', 'JG', 'JG', 'AD', 'JG', 'AD', 'JG', 'JG',
         'JG', 'AD', 'JG', 'JG', 'JG', 'AD', 'JG', 'JG', 'AD', 'JG', 'AD', 'JG', 'JG', 'JG', 'AD', 'AD', 'JG', 'AD', 'JG',
         'JG', 'AD', 'JG', 'AD', 'AD', 'AD', 'JG', 'AD', 'JG', 'JG', 'JG', 'JG', 'JG', 'JG', 'JG', 'AD', 'JG', 'JG', 'JG',
         'JG', 'JG', 'JG', 'JG', 'JG', 'JG', 'JG', 'AD', 'JG', 'AD', 'JG', 'JG', 'JG', 'JG', 'JG', 'AD', 'AD', 'JG', 'JG',
         'JG', 'AD', 'JG', 'JG', 'JG', 'AD', 'JG', 'JG', 'AD', 'AD', 'AD', 'JG', 'JG', 'JG', 'JG', 'AD', 'AD', 'JG', 'JG',
         'AD', 'JG', 'JG', 'JG', 'AD', 'AD', 'JG', 'JG', 'JG', 'AD', 'JG', 'JG', 'JG', 'JG', 'AD', 'JG', 'JG', 'JG', 'AD',
         'JG', 'JG', 'JG', 'AD', 'JG', 'AD', 'JG', 'JG', 'AD', 'AD', 'JG', 'JG', 'JG', 'JG', 'JG', 'JG', 'JG', 'JG', 'JG',
         'JG', 'JG', 'JG', 'JG', 'AD', 'JG', 'JG', 'JG', 'JG', 'JG', 'JG', 'JG', 'AD', 'AD', 'JG', 'JG', 'JG', 'JG', 'JG',
         'JG', 'AD', 'JG', 'AD', 'JG', 'JG', 'JG', 'JG', 'JG', 'JG', 'JG', 'JG', 'JG', 'AD', 'JG', 'AD', 'JG', 'JG', 'JG']

#Función para validar que en la lista solo muestran "AD"
def voto_por_ad(voto): 
    return voto=='AD'
# Filtrar los votos por Águila Dorada
votos_por_ad =[]
for voto in votos:
    if voto_por_ad(voto):
        votos_por_ad.append(voto)
# Filtrar los votos por Jaguar Guerrero usando lambda y not
votos_por_jg = []
voto_jg = lambda voto: not (voto == "AD")
for voto in votos:
    if voto_jg(voto):
        votos_por_jg.append(voto)
# Imprimir los resultados
print(f'== Resultados de la votación para la Mascota Oficial de la UAGro ==\n')
print(f'{("Mascota"):25}   Conteo')
print(f'---------------------------------------')
print(f'{("- Águila Dorada"):25} | {len(votos_por_ad)}')
print(f'{("- Jaguar Guerrero"):25} | {len(votos_por_jg)}')
print(f'---------------------------------------')
print(f'{("- Total Votos"):25} | {len(votos_por_ad) + len(votos_por_jg)}')
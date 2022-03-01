def contar_vogais(string):
    string = string.lower()
    result = {}
    vogais = 'aeiouàáôóêéíúüãõ'
    for i in vogais:
        if i in string:
            result[i] = string.count(i)
    return result

with open('faroeste_cabloco.txt','r') as musica:
    letra_musica = musica.read()

resultado = contar_vogais(letra_musica)

musica.close()

print(f'A quantidade de vogais na música Faroeste Cabloco é de: {resultado}')
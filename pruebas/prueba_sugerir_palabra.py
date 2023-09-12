from spylls.hunspell import Dictionary
import csv

if __name__ == '__main__':
    dic = Dictionary.from_files("../diccionarios/euskara")

    frase = 'zorioneku denek ebe'
    frase_dividida = frase.split()
    dic_words = {}
    for palabra in frase_dividida:
        palabras_sugerida = dic.suggest(palabra)
        print(palabra)
        print('----------')
        dic_words[palabra] = []
        for sugerencia in palabras_sugerida:
            print(sugerencia)
            dic_words[palabra].append(sugerencia)
        print('')






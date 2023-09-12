from spylls.hunspell import Dictionary


if __name__ == '__main__':
    dic = Dictionary.from_files("../diccionarios/euskara")

    for palabra in dic.dic.words:
        if palabra.stem == 'etxe':
            print(palabra)
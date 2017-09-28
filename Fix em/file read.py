from functools import lru_cache

@lru_cache()
def trojan():
    file = open("trouble_text.txt", "w")
    file.write("Hello Coder, It's been long. Tryna get tricked or what \n" * 20000000)

    file.close()

    file = open("trouble_text.txt", "r")
    print(file.read())

trojan()

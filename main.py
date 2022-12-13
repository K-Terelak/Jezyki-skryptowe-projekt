import sys


def algorytm(plik):
    try:
        with open("input/" + plik, "r") as f:
            lines = [int(line.rstrip()) for line in f]
        f.close()

        max_waga_kajaka = lines[0]

        if max_waga_kajaka > 200 or max_waga_kajaka < 80:
            raise Exception

        ile = int(lines[1])
        if ile < 1 or ile > 30000:
            raise Exception

        ludzie = lines[2:]
        if len(ludzie) != ile:
            raise Exception

        wynik = int(ile)
        k = ile - 1

        ludzie.sort()

        for i in range(0, ile):
            while True:
                if k <= i:
                    break
                if ludzie[k] + ludzie[i] <= max_waga_kajaka:
                    wynik -= 1
                    k -= 1
                    break
                if ludzie[k] + ludzie[i] > max_waga_kajaka:
                    k -= 1

    except Exception:
        wynik = "Bledne dane"
    f = open(f"output/out" + str(plik.replace("in", "")), "w")
    f.write(str(wynik))
    f.close()


pliki = sys.argv
for plik in pliki[1:]:
    algorytm(plik)

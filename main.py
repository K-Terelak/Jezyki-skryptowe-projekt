import calendar
import sys
import time


def algorytm(plik):
    try:
        with open(plik, "r") as f:
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

        wynik = ile
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
        f = open(f"output/"+str(calendar.timegm(time.gmtime())) + "_" + str(plik), "w")
        f.write(str(wynik))
        f.close()

    except Exception:
        print("Błędne dane")


pliki = sys.argv
algorytm(pliki[1])
algorytm(pliki[2])

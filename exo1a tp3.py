N = int(input("Entrez un entier N : "))
somme = 0

for i in range(N + 1):
    somme += i

print("La somme des N entiers naturels de 0 à", N, "est :", somme)

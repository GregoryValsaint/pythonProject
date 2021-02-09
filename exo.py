def is_palindrome(m):
    new_m = input('').join(reversed(m))
    if m != new_m:
        return print("Ce n'est pas un palindrome")
    return print("Ce n'est pas un palindrome")

def is_moyenne():
    moyenne= sum(tableau)/len(tableau)
    return str(moyenne)

liste = int(input("Note: "))
tableau = []
while 0 <= liste <= 20:
    tableau.append(liste)
    liste = input("Note: ")
    print("La moyenne est de:" + is_moyenne())




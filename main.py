# # # This is a sample Python script.
# #
# # # Press Maj+F10 to execute it or replace it with your code.
# # # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# #
# #
# # def print_hi(name):
# #     # Use a breakpoint in the code line below to debug your script.
# #     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# #
# #
# # # Press the green button in the gutter to run the script.
# # if __name__ == '__main__':
# #     print_hi('PyCharm')
# #
# # # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# #
# # x = 3j #complex
# #
# # x = True
# # x = False
# #
# # x = ["Bonjour", 5, -1, [1]] #list
# #
# # if "Bonjour" == test:
# #     print("Hello")
# #     print(x)
# # elif x < 10:
# #     print('Deuxième condition vraie')
# # else:
# #     print("condition fausse")
# #
# # i = 0
# # while i < 10:
# #     i += 1
# #     print(i)
# #
# # maListe = ["Bonjour", 5, 3, -1, "test"]
# # for mot in maListe:
# #     print(mot)
# #
# # print("Fin")
# #
# # x = range(10)
# # x = range(5, 10)
# #
# # for i in range(10):  # equivalent de for(i = 0; i<=10; i++)
# #     print(i)
# #
# # print(x)
#
# # print(a < b < c)
# tableau = ["Bonjour", 5, -1, 0.5, 'Salut', -1]
# print(len(tableau))  #taille d'un tableau
# print(tableau[2])
# print(tableau.append("new el")) # ajout d'un élément
# print(tableau)
#
# tableau.insert(2, "4")
# tableau.pop(0)
# tableau.remove('Salut')
#
# print(0.5 in tableau) # est-ce qu'un ele est dans mon tableau
#
# tableau2 = ["0", "2", "4", "6", "8", "10", "12", "14"]
#
# print(tableau2[:5]) # 4 premiers
# print(tableau2[:-2]) # sauf les deux premiers
#
# print(tableau2[4:]) #tout sauf les 4 premiers
#
# print(tableau2[4:6])
#
# for i in tableau2
#     print([i*2 for i in tableau2])
#
# print(tableau2 )
#
#
# first_name = input("Votre prénom: \n")
# print("bonjour %s" %first_name)

def is_moyenne():
    moyenne= sum(tableau)/len(tableau)
    return str(moyenne)

liste = int(input("Note: "))
tableau = []
while 0 <= liste <= 20:
    tableau.append(liste)
    liste = int(input("Note: "))
    if liste == -1:
        print("La moyenne est de:" + is_moyenne())

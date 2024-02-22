nversos = int(input())
verso1 = 'a'
verso2 = 'a'
verso3 = 'a'
verso4 = 'a'
pontuacao = 0
for i in range(nversos):
    maiusc1 = 'a'
    maiusc2 = 'a'
    maiusc3 = 'a'
    maiusc4 = 'a'
    if i == 0:
        verso1 = input()
        print("Cause, baby, now we've got")
        maiusc1 = verso1.upper()
        if maiusc1 == "BAD BLOOD":
            print("BAD BLOOD")
            pontuacao += 1
    elif i == 1:
        verso2 = input()
        print("You know it used to be")
        maiusc2 = verso2.upper()
        if maiusc2 == "MAD LOVE":
            print("MAD LOVE")
            pontuacao += 1
    elif i == 2:
        verso3 = input()
        print("So take a look what")
        maiusc3 = verso3.upper()
        if maiusc3 == "YOU'VE DONE":
            print("YOU'VE DONE")
            pontuacao += 1
    elif i == 3:
        verso4 = input()
        print("Cause, baby, now we've got")
        maiusc4 = verso4.upper()
        if maiusc4 == "BAD BLOOD, HEY":
            print("BAD BLOOD, HEY")
            pontuacao += 1

if (pontuacao / nversos) == 1:
    print("A plateia deu um show! Acertou tudo!")

elif (pontuacao / nversos) >= 0.5:
    print("A plateia acertou a maior parte da música")

else:
    print("Foi um dia atípico e a plateia se esqueceu de grande da música")
    
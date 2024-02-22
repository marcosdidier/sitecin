nversos = int(input())
palavra1 = ''
palavra2 = ''
palavra3 = ''
palavra4 = ''
pontuacao = 0
for i in range(nversos):
    if i == 0:
        verso1 = input()
        print("Cause, baby, now we've got")
        for m in verso1:
            maiusc1 = m.upper()
            palavra1 += maiusc1
        if palavra1 == "BAD BLOOD":
            print("BAD BLOOD")
            pontuacao += 1
    elif i == 1:
        verso2 = input()
        print("You know it used to be")
        for j in verso2:
            maiusc2 = j.upper()
            palavra2 += maiusc2
        if palavra2 == "MAD LOVE":
            print("MAD LOVE")
            pontuacao += 1
    elif i == 2:
        verso3 = input()
        print("So take a look what")
        for k in verso3:
            maiusc3 = k.upper()
            palavra3 += maiusc3
        if palavra3 == "YOU'VE DONE":
            print("YOU'VE DONE")
            pontuacao += 1
    elif i == 3:
        verso4 = input()
        print("Cause, baby, now we've got")
        for l in verso4:
            maiusc4 = l.upper()
            palavra4 += maiusc4
        if palavra4 == "BAD BLOOD, HEY":
            print("BAD BLOOD, HEY")
            pontuacao += 1

if (pontuacao / nversos) == 1:
    print("A plateia deu um show! Acertou tudo!")

elif (pontuacao / nversos) >= 0.5:
    print("A plateia acertou a maior parte da música")

else:
    print("Foi um dia atípico e a plateia se esqueceu de grande da música")
    
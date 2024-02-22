numero = int(input())
str_1 = str(input())
str_2 = str(input())
str_3 = str(input())
c1 = len(str_1)
c2 = len(str_2)
c3 = len(str_3)
str_campea = 'a'
str_lex_maior = 'a'

if numero == 1:
    if c1 > c2 and c1 > c3:
        print(str_1)
        print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
    elif c2 > c1 and c2 > c3:
        print(str_2)
        print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
    elif c3 > c1 and c3 > c2:
        print(str_3)
        print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
    elif c1 == c2 or c1 == c3 or c2 == c3:
      print('(Droga! Ainda não consegui descobrir o local que possui mais sinais desconhecidos! Vou ter que ficar mais um tempo nessa Mansão Mal-Assombrada...)')
      if str_1 > str_2 and str_1 > str_3:
          print(str_1)
          print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
      elif str_2 > str_1 and str_2 > str_3:
          print(str_2)
          print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
      elif str_3 > str_2 and str_3 > str_1:
          print(str_3)
          print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
      else:
        print('"AAAAAA! Um fantasma me assustou!"')
        print('(Uma mensagem apareceu no monitor que você estava usando. "Agente, um erro inesperado aconteceu. A EPF contactará você novamente quando tudo estiver funcionando da forma correta. Nosso sistema foi invadido por alguém que se identifica como Hubert P.Enguin")')


elif numero == 2:
    if c1 < c2 and c1 < c3:
        print(str_1)
        print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
    elif c2 < c1 and c2 < c3:
        print(str_2)
        print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
    elif c3 < c1 and c3 < c2:
        print(str_3)
        print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
    elif c1 == c2 or c1 == c3 or c2 == c3:
      print('(Droga! Ainda não consegui descobrir o local que possui mais sinais desconhecidos! Vou ter que ficar mais um tempo nessa Mansão Mal-Assombrada...)')
      if str_1 > str_2 and str_1 > str_3:
          print(str_1)
          print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
      elif str_2 > str_1 and str_2 > str_3:
          print(str_2)
          print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
      elif str_3 > str_2 and str_3 > str_1:
          print(str_3)
          print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
      else:
        print('"AAAAAA! Um fantasma me assustou!"')
        print('(Uma mensagem apareceu no monitor que você estava usando. "Agente, um erro inesperado aconteceu. A EPF contactará você novamente quando tudo estiver funcionando da forma correta. Nosso sistema foi invadido por alguém que se identifica como Hubert P.Enguin")')

print('(Depois de ler a mensagem, você dormiu. Ao acordar, você não estava mais no CIn de outubro de 2012, mas no CIn de 2023, sem acreditar na situação que vivenciou)')




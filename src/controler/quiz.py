print("Seja muito bem vindo ao quiz da Beh!")
answer_user = input("Quer começar? [S/N] ")

if answer_user != "S":
    quit()

print("começando...")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games "
      "\n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correto!")
else:
    print("Incorreto!")
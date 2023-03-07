from random import randint

n = (randint(0, 5)), (randint(0, 5)), (randint(0, 5)), (randint(0, 5)), (randint(0, 5)),

print(f"eu sorteei os numeros\033[1;33;44m{n}\033[m\no maior valor sorteado foi \033[1;34;41m {max(n)} \033[m e o menor foi \033[1;34;41m {min(n)} \033[m")
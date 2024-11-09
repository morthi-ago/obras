from math import sqrt 

while True:
    numero = input('\nDigite um valor positivo!\n')    
    try:
        if f'{numero}'.isnumeric() == False:
            raise ValueError
    except ValueError:
        print('\nDigite um número positivo!\n')
    else:
        break

print (f'\nO valor da raiz quadrada de {float(numero)} é {sqrt(float(numero))}.') 
print('Volte sempre que tiver dúvidas com raízes.')

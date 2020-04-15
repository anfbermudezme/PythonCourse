# -*- coding: utf-8 -*-

def run():
    print('CALCULADORA DE DIVISAS')
    print('convierte dolares a pesos colombianos')
    print('')

    ammount = float(input('Ingresa cantidad de dolares: '))

    result = f_calculator(ammount)

    print('${} dolares son ${} pesos colombianos'.format(ammount, result))
    print('')

def f_calculator(ammount):
    dolar_today=3920.01
    return dolar_today * ammount

if __name__ == '__main__':
    run()

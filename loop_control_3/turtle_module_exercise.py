# from turtle import Turtle
# # Inicializar
# t = Turtle()
# # Definir a velocidade
# t.speed(1)
# # Movimentar a turtle para frente
# t.forward(100)
# # Rotacionar em graus para a direita
# t.right(90)
# t.forward(100)
# # Rotacionar em graus para a esquerda
# t.left(90)
# t.forward(100)
# # Movimentar a turtle para tras
# t.backward(200)
# input()
from turtle import Turtle
t = Turtle()
while True:
    forward = t.forward
    backward = t.backward
    left = t.left
    right = t.right

    choose_direction = input(
        'Which direction? (forward, backward, left or right)')
    if choose_direction == 'forward':
        pixels = int(input('How many pixels? '))
        t.forward(pixels)
    elif choose_direction == 'backward':
        pixels = int(input('How many pixels? '))
        t.backward(pixels)
    elif choose_direction == 'left':
        angle = int(input('Choose the angle you wanna point? '))
        t.left(angle)
    elif choose_direction == 'right':
        angle = int(input('Choose the angle you wanna point? '))
        t.right(angle)

    continue_program = input('Do you want to continue? (yes or no)')
    if continue_program.lower() == 'no':
        break
    else:
        continue

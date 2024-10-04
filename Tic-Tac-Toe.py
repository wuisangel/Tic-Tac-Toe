# Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario.
# Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

#     la maquina (por ejemplo, el programa) jugará utilizando las 'X's;
#     el usuario (por ejemplo, tu) jugarás utilizando las 'O's;
#     el primer movimiento es de la maquina - siempre coloca una 'X' en el centro del tablero;
#     todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia)
#     el usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado;
#     el programa verifica si el juego ha terminado - existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana;
#     la maquina responde con su movimiento y se verifica el estado del juego;
#     no se debe implementar algún tipo de inteligencia artificial - la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.

from random import randrange

def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    j=0
    k=0
    for i in range(3):
        print("+-------+-------+-------+\n" + \
        "|       |       |       |\n" + \
        f"|   {board[j][k]}   |   {board[j][k+1]}   |   {board[j][+2]}   |\n" + \
        "|       |       |       |")
        j+=1
    print('+-------+-------+-------+')

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.

    while True:
        try:
            mov=int(input('Ingrese su movimiento: '))
        except ValueError:
            print("Igrese un valor valido")
            continue
        # Se verifica que el movimiento sea valido, que no se haya realizado y que este en el rango aceptable
        if (mov not in mov_re) and (mov>0) and (mov<10):
            # Se agrega el movimiento a la lista de movimientos realizados
            mov_re.append(mov)
            # Se actualiza el tablero
            r,c = coor[mov]
            board[r][c]='O'
            # Se imprime el tablero
            display_board(board)
            break
        else:
            print('Ingrese un movimiento valido')

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    free_fields=[]
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['X', 'O']:
                free_fields.append((r,c))    
    return free_fields

def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    
    # Se crea un diccionario para facilitar el srcipting
    boardD = {1: board[0][0], 2: board[0][1], 3: board[0][2], 4: board[1][0], 5: board[1][1], 6: board[1][2], 7: board[2][0], 8: board[2][1], 9: board[2][2]}
    
    # TODAS LAS POSIBLES COMBINACIONES DE GANAR
    # [1, 2, 3] [1, 4, 7] [1, 5, 9] [2, 5, 8] [3, 6, 9] [3, 5, 7] [4, 5, 6] [7, 8, 9]

    # Se calculan todas las posibles combinaciones para ganar el juego
    if (boardD[1] == boardD[2] == boardD[3] == sign) or \
    (boardD[1] == boardD[4] == boardD[7] == sign) or \
    (boardD[1] == boardD[5] == boardD[9] == sign) or \
    (boardD[2] == boardD[5] == boardD[8] == sign) or \
    (boardD[3] == boardD[6] == boardD[9] == sign) or \
    (boardD[3] == boardD[5] == boardD[7] == sign) or \
    (boardD[4] == boardD[5] == boardD[6] == sign) or \
    (boardD[7] == boardD[8] == boardD[9] == sign):
        return True

def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.

    while True:
        # Se busca  un numero random para la maquina
        mov=randrange(1, 10)
        # Se comprueba que el movimiento no haya sido realizado aun
        if (mov not in mov_re):
            # Se agrega el movimiento a la lista de movimientos realizados
            mov_re.append(mov)
            # Se actualiza el tablero
            r,c = coor[mov]
            board[r][c]='X'
            break

# En mov_re se guardaran los movimientos que se han realizado
#inicializando con rojo, ya que es el movimiento predefinido por la maquina
mov_re=[5]

# Se inicia el tablero
board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]
# Se crea un diccionario de coordenadas
coor = {1: [0,0], 2: [0,1], 3: [0,2], 4: [1,0], 5: [1,1], 6: [1,2], 7: [2,0], 8: [2,1], 9: [2,2]}

while True:
    display_board(board)
    # Se comprueba si se sigue jugando o se detiene el juego
    if victory_for(board, 'X'):
        print("Gano la maquina")
        break
    elif victory_for(board, 'O'):
        print("Has Ganado!")
        break
    elif len(mov_re) == 9:
        print("Sucedio un empate")
        break
    # Mueve el usuario
    enter_move(board)
    # Se comprueba si se sigue jugando o se detiene el juego
    if victory_for(board, 'X'):
        print("Gano la maquina")
        break
    elif victory_for(board, 'O'):
        print("Has Ganado!")
        break
    elif len(mov_re) == 9:
        print("Sucedio un empate")
        break
    # Mueve la maquina
    draw_move(board)

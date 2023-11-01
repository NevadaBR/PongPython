import turtle
import winsound
import time

wn = turtle.Screen()
wn.title("PING PONG @luan_euzebio")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

nome_a = wn.textinput("Pong", "Nome do jogador A:")
nome_b = wn.textinput("Pong", "Nome do jogador B:")

# Pontos
pontos_a = 0
pontos_b = 0


# Player a
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape("square")
player_a.color("white")
player_a.shapesize(stretch_wid=5, stretch_len=1)
player_a.penup()
player_a.goto(-350, 0)

# Player b
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape("square")
player_b.color("white")
player_b.shapesize(stretch_wid=5, stretch_len=1)
player_b.penup()
player_b.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.05
bola.dy = -0.05

# Placar
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("{}: 0   {}: 0".format(nome_a, nome_b), align="center", font=("Courier", 24, "normal"))

#menssagen ganhador 
# ganhador = turtle.Turtle()
# ganhador.speed(0)
# ganhador.color("white")
# ganhador.penup()
# ganhador.hideturtle()
# ganhador.goto(0, 260)

# Função para mover o jogador A para cima
def player_a_up():
    y = player_a.ycor()
    if y < 250:  # Limite superior para o jogador A
        y += 20
    player_a.sety(y)

# Função para mover o jogador A para baixo
def player_a_down():
    y = player_a.ycor()
    if y > -240:  # Limite inferior para o jogador A
        y -= 20
    player_a.sety(y)

# Função para mover o jogador B para cima
def player_b_up():
    y = player_b.ycor()
    if y < 250:  # Limite superior para o jogador B
        y += 20
    player_b.sety(y)

# Função para mover o jogador B para baixo
def player_b_down():
    y = player_b.ycor()
    if y > -240:  # Limite inferior para o jogador B
        y -= 20
    player_b.sety(y)

#função para reiniciar o jogo
def reiniciar_jogo():
    global pontos_a, pontos_b, bola, nome_a, nome_b
    nome_a = wn.textinput("Pong", "Nome do jogador A:")
    nome_b = wn.textinput("Pong", "Nome do jogador B:")
    pontos_a = 0
    pontos_b = 0
    bola.goto(0, 0)
    pen.clear()
    pen.write("{}: 0   {}: 0".format(nome_a, nome_b), align="center", font=("Courier", 24, "normal"))

# Mapeamento das teclas para os movimentos dos jogadores
wn.listen()
wn.onkeypress(player_a_up, 'w')
wn.onkeypress(player_a_down, 's')
wn.onkeypress(player_b_up, 'Up')
wn.onkeypress(player_b_down, 'Down')

# Game loop
jogo_ativo = True

while jogo_ativo:
   
    
    wn.update()

    # Movimento da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Verificar colisão com a borda superior
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
        winsound.PlaySound("toque.wav", winsound.SND_ASYNC)

    # Verificar colisão com a borda inferior
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
        winsound.PlaySound("toque.wav", winsound.SND_ASYNC)

    # Verificar pontuação para o jogador A
    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        pontos_a += 1
        pen.clear()
        winsound.PlaySound("ponto.wav", winsound.SND_ASYNC)
        pen.write("{}: {}   {}: {}".format(nome_a, pontos_a, nome_b, pontos_b), align="center", font=("Courier", 24, "normal"))

    # Verificar pontuação para o jogador B
    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        pontos_b += 1
        pen.clear()
        winsound.PlaySound("ponto.wav", winsound.SND_ASYNC)
        pen.write("{}: {}   {}: {}".format(nome_a, pontos_a, nome_b, pontos_b), align="center", font=("Courier", 24, "normal"))

    # Verificar colisão com os jogadores
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < player_b.ycor() + 50 and bola.ycor() > player_b.ycor() - 50):
        bola.setx(340)
        bola.dx *= -1
        winsound.PlaySound("toque.wav", winsound.SND_ASYNC)

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < player_a.ycor() + 50 and bola.ycor() > player_a.ycor() - 50):
        bola.setx(-340)
        bola.dx *= -1
        winsound.PlaySound("toque.wav", winsound.SND_ASYNC)
    
    # Verificar se um jogador ganhou
    if pontos_a == 5:
        pen.clear()
        pen.write("{} GANHOU, PARABÉNS".format(nome_a), align="center", font=("Courier", 24, "normal"))
        wn.update() 
        time.sleep(2)
        reiniciar_jogo()

    if pontos_b == 5:
        pen.clear()
        pen.write("{} GANHOU, PARABÉNS".format(nome_b), align="center", font=("Courier", 24, "normal"))
        wn.update()
        time.sleep(2)
        reiniciar_jogo()
        
        
    
    

from turtle import Screen, Turtle
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jogo da Cobra")



cobra = Turtle()
cobra.shape("square")
cobra.color("white")
cobra.penup()
cobra.goto(0, 0)
cobra.direction = "stop"
cobra.speed(10)


segmentos = []


for i in range(3):
    segmento = Turtle()
    segmento.shape("square")
    segmento.color("white")
    segmento.penup()
    segmento.goto(-20 * (i + 1), 0)
    segmentos.append(segmento)


comida = Turtle()
comida.shape("circle")
comida.color("red")
comida.penup()
comida.speed(0)
comida.goto(random.randint(-280, 280), random.randint(-280, 280))
comida.shapesize(stretch_wid=0.5, stretch_len=0.5)
comida.speed("fastest")


pontuacao = 0
marcador = Turtle()
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write(f"Pontuação: {pontuacao}", align="center", font=("Courier", 24, "normal"))


def mover():
    for i in range(len(segmentos) - 1, 0, -1):
        x = segmentos[i - 1].xcor()
        y = segmentos[i - 1].ycor()
        segmentos[i].goto(x, y)
    if len(segmentos) > 0:
        x = cobra.xcor()
        y = cobra.ycor()
        segmentos[0].goto(x, y)

    if cobra.direction == "up":
        y = cobra.ycor()
        cobra.sety(y + 20)
    if cobra.direction == "down":
        y = cobra.ycor()
        cobra.sety(y - 20)
    if cobra.direction == "left":
        x = cobra.xcor()
        cobra.setx(x - 20)
    if cobra.direction == "right":
        x = cobra.xcor()
        cobra.setx(x + 20)


def ir_cima():
    if cobra.direction != "down":
        cobra.direction = "up"
def ir_baixo():
    if cobra.direction != "up":
        cobra.direction = "down"
def ir_esquerda():
    if cobra.direction != "right":
        cobra.direction = "left"
def ir_direita():
    if cobra.direction != "left":
        cobra.direction = "right"


screen.listen()
screen.onkey(ir_cima, "w")
screen.onkey(ir_baixo, "s")
screen.onkey(ir_esquerda, "a")
screen.onkey(ir_direita, "d")


def loop_jogo():
    global pontuacao
    mover()
    screen.tracer(0)
    screen.update()
    
    if cobra.distance(comida) < 15:
        comida.goto(random.randint(-280, 280), random.randint(-280, 280))

        
        novo_segmento = Turtle()
        novo_segmento.shape("square")
        novo_segmento.color("white")
        novo_segmento.penup()
        novo_segmento.speed("fastest")
        segmentos.append(novo_segmento)

        
        pontuacao += 1
        marcador.clear()
        marcador.write(f"Pontuação: {pontuacao}", align="center", font=("Courier", 24, "normal"))
    
    if cobra.xcor() > 290 or cobra.xcor() < -290 or cobra.ycor() > 290 or cobra.ycor() < -290:
        marcador.clear()
        screen.update()
        marcador.goto(0, 0)
        marcador.write(f"Pontuação: {pontuacao}\n  Perdeste", align="center", font=("Courier", 24, "normal"))
        screen.update()
        return


    screen.ontimer(loop_jogo, 90)

loop_jogo()

screen.exitonclick()














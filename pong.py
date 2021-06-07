#Credit to: https://www.youtube.com/watch?v=XGf2GcyHPhc
import turtle

wn = turtle.Screen()
wn.title("Pong de Ramiro Javier Royo")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Izquierda
izquierda = turtle.Turtle()
izquierda.speed(0)
izquierda.shape("square")
izquierda.color("white")
izquierda.shapesize(stretch_wid=5, stretch_len=1)
izquierda.penup()
izquierda.goto(-350,0)

# Derecha
derecha = turtle.Turtle()
derecha.speed(0)
derecha.shape("square")
derecha.color("white")
derecha.shapesize(stretch_wid=5, stretch_len=1)
derecha.penup()
derecha.goto(350,0)
 
# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
pelota.dx = 0.3
pelota.dy = 0.3

#Resultado
resultado_izquierda = 0
resultado_derecha = 0

#Anotador
anotador= turtle.Turtle()
anotador.speed(0)
anotador.color("white")
anotador.penup()
anotador.hideturtle()
anotador.goto(0,260)
anotador.write("Jugador1: 0  Jugador2: 0", align="center", font=("Courier", 24, "normal"))

#Funciones
def izquierda_arriba():
    y= izquierda.ycor()
    y += 20
    izquierda.sety(y)
def izquierda_abajo():
    y= izquierda.ycor()
    y -= 20
    izquierda.sety(y)

def derecha_arriba():
    y= derecha.ycor()
    y += 20
    derecha.sety(y)
def derecha_abajo():
    y= derecha.ycor()
    y -= 20
    derecha.sety(y)

#Binding con el teclado
wn.listen()
wn.onkeypress(izquierda_arriba,"w")
wn.onkeypress(izquierda_abajo,"s")

wn.onkeypress(derecha_arriba,"Up")
wn.onkeypress(derecha_abajo,"Down")

#Loop para que ande
while True:
    wn.update()

    #Movimiento de pelota
    pelota.setx(pelota.xcor()+pelota.dx)
    pelota.sety(pelota.ycor()+pelota.dy)

    #Bordes
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy*= -1
    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy*= -1
    
    if izquierda.ycor() > 290:
        izquierda.sety(290)
    if izquierda.ycor() < -290:
        izquierda.sety(-290)
    
    if derecha.ycor() > 290:
        derecha.sety(290)
    if derecha.ycor() < -290:
        derecha.sety(-290)
    
    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        resultado_izquierda +=1
        anotador.clear()
        anotador.write("Jugador1: {}  Jugador2: {}".format(resultado_izquierda, resultado_derecha), align="center", font=("Courier", 24, "normal"))

    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        resultado_derecha +=1
        anotador.clear()
        anotador.write("Jugador1: {}  Jugador2: {}".format(resultado_izquierda, resultado_derecha), align="center", font=("Courier", 24, "normal"))

    #Colisiones
    if (pelota.xcor() > 340 and pelota.xcor() <350) and (pelota.ycor() < derecha.ycor()+50 and pelota.ycor() > derecha.ycor()-50):
        pelota.setx(340)
        pelota.dx *= -1
    if (pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < izquierda.ycor()+50 and pelota.ycor() > izquierda.ycor()-50):
        pelota.setx(-340)
        pelota.dx *= -1
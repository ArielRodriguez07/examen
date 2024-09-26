# zona de clases
class inventario0706:
        
# LISTAS
    print("***** Listas ***** \n")
    def lista_juegos_0706(self):
        Tipo_juego_0706 = ["","accion","pelea",
                            "equipo", "futbol", "nba"]
        print(Tipo_juego_0706)
        for y in Tipo_juego_0706:
            print(y)
        print("\n")

# TUPLAS
    def tupla_juegos_0706(self):
        print("***** Tuplas ***** \n")
        ## esto se refiere a la cantidad de pares de calzados que se necesita para una sucursal
        tarjetas_0706 = ("tarjeta1", "tarjeta2", "tarjeta3","tarjeta4", "tarjeta5", "tarjeta6","tarjeta7")
        print(tarjetas_0706)
        for a in tarjetas_0706:
            print(a)
        print("\n")

# CONJUNTOS
    def diccionario_videojuegos_0706(self):
        print("***** Diccionarios ***** \n")
        ## esto se refiere al precio que tiene cada calzado
        Precio_0706 = {
        "juego 1-":450, "juego5-":400,
        "juego2-":450 ,"juego6-":800,
        "juego3-":1500,"juego7-":200,
        "juego4-":300
        } 
        print(Precio_0706)
        for b, z in Precio_0706.items():
            print(b,z)
        print("\n")

# SETS
    def sets_juego0706(self):
        print("***** Sets ***** \n")
        ## esto se refiere a la capacidad maxima de calzados que puede tener una susucrsal
        existencias_0706 = {"3500 juegos","4005 juegos","4500 tarjetas","1620 juegos", "1500 juegos", "2020 juegos", "3000 juegos"}
        print(existencias_0706)
        for c in existencias_0706:
            print(c)

# utilizacion del objeto
x = inventario0706 ()
x.lista_juegos_0706()
x.tupla_juegos_0706()
x.diccionario_videojuegos_0706()
x.sets_juego0706()
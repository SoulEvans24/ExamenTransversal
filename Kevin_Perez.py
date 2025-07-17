productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}




stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}




def stock_marca(marca):
    total=0
    for modelo,datos in productos.items():
        if datos[0].lower()==marca.lower():
            total+=stock[modelo][1]
    print(f"El stock es: {total}")


#def búsqueda_precio(p_min,p_max)


def actualizar_precio(modelo,p):
    if modelo in stock:
        stock[modelo][0]=p
        return True
    else:
        return False
    


while True:
    print("*** MENÚ PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")

    opcion=input("Ingrese opción: ")

    match opcion:
        case "1":
            marca=input("Ingrese marca a consultar: ").upper()
            stock_marca(marca)
        case "2":
            while True:
                try:
                    p_min=int(input("Ingrese precio mínimo: "))
                    p_max=int(input("Ingrese precio máximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            pass

        case "3":
            modelo=input("Ingrese modelo a actualizar: ")
            p=int(input("Ingrese precio nuevo: "))
            actualizar_precio(modelo,p)
            print("Precio actualizado!!")
        case "4":
            print("Programa finalizado.")
            break
        case _:
            print("Debe seleccionar una opción válida!!")

#me dará tiempo? lol :p
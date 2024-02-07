from clases_modulos import Persona, Empleado, Jefe
import json
from clear import clear
def menu():
    opcion = str(input("""Ingrese el numero de la opcion que va a tomar:
    1 - Agregar empleado.
    2 - Agregar jefe.
    3 - Contratar empleado.
    4 - Actualizar info de empleados.
    5 - Actualizar info de jefes.
    6 - Eliminar jefes.
    7 - Eliminar empleados.
    8 - Mostrar jefes.
    9 - Mostrar empleados. """))

    
    if opcion == "1":
        print("Ingrese la informacion del empleado: ")
        nombre = input("Nombre: ").title()
        apellido = input("Apellido: ").title()
        edad = input("Edad: ")
        cargo = input("Cargo: ")
        salario = input("Salario: ")
        if len(nombre) == 0 or len(apellido) == 0 or len(edad) == 0 or len(cargo) == 0 or len(salario) == 0:
            print("\n• Se deben llenar todos los apartados •")
        else:
            emp = Empleado(nombre, apellido, edad, cargo, salario)
            emp.agregar_empleado()
   
    
    elif opcion == "2":
        print("Ingrese la informacion del jefe: ")
        nombre = input("Nombre: ").title()
        apellido = input("Apellido: ").title()
        edad = input("Edad: ")
        cargo = input("Cargo: ")
        salario = input("Salario: ")
        if len(nombre) == 0 or len(apellido) == 0 or len(edad) == 0 or len(cargo) == 0 or len(salario) == 0:
            print("\nSe deben llenar todos los apartados.")
        else:
            jef = Jefe(nombre, apellido, edad, cargo, salario)
            jef.agregar_jefe()
    
    elif opcion == "3":
        with open("jefes.json", "r") as data:
            info = json.load(data)
    
        lista_jefes = ""
        count = 0
        for n in info:
            o = info[n]
            nombre = o["nombre"]
            apellido = o["apellido"]
            edad = o["edad"]
            cargo = o["cargo"]
            salario = o["salario"]
            count += 1
            lista_jefes += str(count)+"- "+nombre+" "+apellido+", "+edad+" años"+", Cargo: "+cargo+". Salario: "+salario+"\n"
        print("\n" +lista_jefes)
        try:
            opcion = int(input("Elija el numero del jefe: ")) - 1
            print("")
            list_jefes = list(info.values())
            jefe_elegido = list_jefes[opcion]
            jef = Jefe(jefe_elegido["nombre"], jefe_elegido["apellido"], jefe_elegido["edad"], jefe_elegido["cargo"], jefe_elegido["salario"])
            jef.contratar_empleados()
        except ValueError:
            print("\n• Tiene que elegir un numero para seguir con el proceso •")
        except IndexError:
            print("\n• Este numero no se encuentra en la lista •")
            
    elif opcion == "4":
        with open("jefes.json", "r") as data:
            jefes = json.load(data)
        with open("empleados.json", "r") as data:
            empleados = json.load(data)
        jefes_lista = {}
        num = 0
        for n in jefes:
            info_jefes = jefes[n]
            empleados_jefes = info_jefes["empleados"]
            if len(empleados_jefes) == 0:
                pass
            else:
                for n in empleados_jefes:
                    jefes_lista[str(num)] = empleados_jefes[n]
                    num += 1
        lista_output = ""
        count = 0
        lista_empleados=[]
        for n in jefes_lista:
            o = jefes_lista[n]
            n = o["nombre"]
            a = o["apellido"]
            e = o["edad"]
            c = o["cargo"]
            s = o["salario"]
            lista_empleados.append(o)
            count += 1
            lista_output += str(count) + " - " + n + " " + a + ". Edad: " + e + " años, Cargo: " + c + ", Salario: " + s + "\n"
        
        len_jefes = len(jefes_lista)
        for n in empleados:
            o = empleados[n]
            n = o["nombre"]
            a = o["apellido"]
            e = o["edad"]
            c = o["cargo"]
            s = o["salario"]
            lista_empleados.append(o)
            count += 1
            lista_output += str(count) + " - " + n + " " + a + ". Edad: " + e + " años, Cargo: " + c + ", Salario: " + s + "\n"
        print("")
        print(lista_output)
        try:
            opcion = input("Elija el numero del empleado que desea actualizar: ")
            empleado_elegido = lista_empleados[int(opcion) - 1]
            emp = Empleado(empleado_elegido["nombre"], empleado_elegido["apellido"], empleado_elegido["edad"], empleado_elegido["cargo"], empleado_elegido["salario"])
            emp.actualizar_info()
        except ValueError:
            print("\n• Tiene que elegir un numero para seguir con el proceso •")
        except IndexError:
            print("\n• Este numero no se encuentra en la lista •")
    
    elif opcion == "5":
        try:
            with open("jefes.json", "r") as data:
                info = json.load(data)
            count = 0
            lista_output = ""
            lista_jefes = []
            for n in info:
                o = info[n]
                n = o["nombre"]
                a = o["apellido"]
                e = o["edad"]
                c = o["cargo"]
                s = o["salario"]
                count += 1
                lista_output += str(count) + " - " + n + " " + a + ". Edad: " + e + " años, Cargo: " + c + ", Salario: " + s + "\n"
                lista_jefes.append(o)
            print(lista_output)
            opcion = input("Elija el numero del jefe que desea actualizar: ")
            jefe_elegido = lista_jefes[int(opcion) - 1]
            jef =Jefe(jefe_elegido["nombre"], jefe_elegido["apellido"], jefe_elegido["edad"], jefe_elegido["cargo"], jefe_elegido["salario"])
            jef.actualizar_info_jefe()
        except ValueError:
            print("\n• Tiene que elegir un numero para seguir con el proceso •")
        except IndexError:
            print("\n• Este numero no se encuentra en la lista •")

    elif opcion == "6":
        try:
            with open("jefes.json", "r") as data:
                info = json.load(data)
            count = 0
            lista_output = ""
            lista_jefes = []
            for n in info:
                o = info[n]
                n = o["nombre"]
                a = o["apellido"]
                e = o["edad"]
                c = o["cargo"]
                s = o["salario"]
                count += 1
                lista_output += str(count) + " - " + n + " " + a + ". Edad: " + e + " años, Cargo: " + c + ", Salario: " + s + "\n"
                lista_jefes.append(o)
            print("")
            print("Estos son los jefes registrados actualmente:")
            print(lista_output)
            opcion = input("Elija el numero del jefe a eliminar: ")
            jefe_elegido = lista_jefes[int(opcion) - 1]
            jef =Jefe(jefe_elegido["nombre"], jefe_elegido["apellido"], jefe_elegido["edad"], jefe_elegido["cargo"], jefe_elegido["salario"])
            jef.borrar_jefe()
        except ValueError:
            print("\n• Tiene que elegir un numero para seguir con el proceso •")
        except IndexError:
            print("\n• Este numero no se encuentra en la lista •")
            
    elif opcion == "7":
        print("")
        with open("jefes.json", "r") as data:
            jefes = json.load(data)
        with open("empleados.json", "r") as data:
            empleados = json.load(data)
        jefes_lista = {}
        num = 0
        for n in jefes:
            info_jefes = jefes[n]
            empleados_jefes = info_jefes["empleados"]
            if len(empleados_jefes) == 0:
                pass
            else:
                for n in empleados_jefes:
                    jefes_lista[str(num)] = empleados_jefes[n]
                    num += 1
        lista_output = ""
        count = 0
        lista_empleados=[]
        for n in jefes_lista:
            o = jefes_lista[n]
            n = o["nombre"]
            a = o["apellido"]
            e = o["edad"]
            c = o["cargo"]
            s = o["salario"]
            lista_empleados.append(o)
            count += 1
            lista_output += str(count) + " - " + n + " " + a + ". Edad: " + e + " años, Cargo: " + c + ", Salario: " + s + "\n"
        
        len_jefes = len(jefes_lista)
        for n in empleados:
            o = empleados[n]
            n = o["nombre"]
            a = o["apellido"]
            e = o["edad"]
            c = o["cargo"]
            s = o["salario"]
            lista_empleados.append(o)
            count += 1
            lista_output += str(count) + " - " + n + " " + a + ". Edad: " + e + " años, Cargo: " + c + ", Salario: " + s + "\n"
        print(lista_output)
        try:
            opcion = input("Elija el numero del empleado que desea eliminar: ")
            empleado_elegido = lista_empleados[int(opcion) - 1]
            nombre = empleado_elegido["nombre"]
            apellido = empleado_elegido["apellido"]
            edad = empleado_elegido["edad"]
            cargo = empleado_elegido["cargo"]
            salario = empleado_elegido["salario"]
            dict_empleado = {
                "nombre": nombre,
                "apellido": apellido,
                "edad": edad,
                "cargo": cargo,
                "salario": salario
            }
            en_empleados = False
            for n in empleados:
                if dict_empleado == empleados[n]:
                    en_empleados = True
            
            if en_empleados == False:
                clave_en_empleado = None
                su_jefe = None
                for n in jefes:
                    dentro_jefes = jefes[n]
                    empleados_jefes = dentro_jefes["empleados"]
                    for clave, valor in empleados_jefes.items():
                        if dict_empleado == valor:
                            clave_en_empleado = clave
                dict = {}
                dict[clave_en_empleado] = dict_empleado
                pertenece = None
                for n in jefes:
                    jef = n
                    dentro_jefes = jefes[n]
                    empleados_jefes = dentro_jefes["empleados"]
                    for s in empleados_jefes:
                        if empleados_jefes[s] == dict_empleado:
                            pertenece = jef
                dentro_jefep = jefes[pertenece]
                dentro_empleados = dentro_jefep["empleados"]
                empleadop = dentro_empleados[clave_en_empleado]
                dentro_empleados.pop(clave_en_empleado)
                with open("jefes.json", "w") as data:
                    json.dump(jefes, data, indent = 4)
                print(f"Se ha eliminado a {nombre} {apellido} de la lista de empleados.")
            else:
                with open("empleados.json", "r") as data:
                    empleados = json.load(data)
                clave_empleado = None
                for clave, valor in empleados.items():
                    if dict_empleado == valor:
                        clave_empleado = clave
                empleados.pop(clave_empleado)
                with open("empleados.json", "w") as data:
                    json.dump(empleados, data, indent = 4)
                print(f"Se ha eliminado a {nombre} {apellido} de la lista de empleados.")
        
        except ValueError:
            print("\n• Tiene que elegir un numero para seguir con el proceso •")
        except IndexError:
            print("\n• Ese número no está en la lista •")

    
    elif opcion == "8":
        print("\nLista actual de jefes:\n")
        with open("jefes.json", "r") as data:
            jefes = json.load(data)
        lista_jefes = ""
        for n in jefes:
            o = jefes[n]
            n = o["nombre"]
            a = o["apellido"]
            e = o["edad"]
            c = o["cargo"]
            s = o["salario"]
            emplea = o["empleados"]
            jef = Jefe(n, a, e, c ,s)
            jef.mostrar_jefes()

    elif opcion == "9":
        print("\nLista actual de empleados:\n")
        with open("empleados.json", "r") as data:
            empleados = json.load(data)
        with open("jefes.json", "r") as data:
            jefes = json.load(data)
        for n in empleados:
            info_empleados = empleados[n]
            n = info_empleados["nombre"]
            a = info_empleados["apellido"]
            e = info_empleados["edad"]
            c = info_empleados["cargo"]
            s = info_empleados["salario"]
            jef = Jefe(n, a, e, c ,s)
            jef.mostrar_empleados()
        info_empleados = {}
        empleados_lista = {}
        num = 0
        for n in jefes:
            info_jefes = jefes[n]
            empleados_jefes = info_jefes["empleados"]
            if len(empleados_jefes) == 0:
                pass
            else:
                for n in empleados_jefes:
                    empleados_lista[str(num)] = empleados_jefes[n]
                    num += 1
        for n in empleados_lista:
            info_empleados = empleados_lista[n]
            n = info_empleados["nombre"]
            a = info_empleados["apellido"]
            e = info_empleados["edad"]
            c = info_empleados["cargo"]
            s = info_empleados["salario"]
            jef = Jefe(n, a, e, c ,s)
            jef.mostrar_empleados()
        
  
        
            
continuar = ""
while continuar == "":
    menu()
    print("")
    continuar = input("Presione enter para continuar, ingrese 'n' para finalizar y guardar. ")
    if continuar == "":
        clear()

    
    

from prueba.clases import Empleado, Jefe
from prueba.funciones import *


def menu():
    opcion = str(input("""Ingrese el numero de la opcion que va a tomar:
1 - Agregar empleado.
2 - Agregar jefe.
3 - Contratar empleado.
4 - Actualizar info de empleados.
5 - Actualizar info de jefes.
6 - Eliminar jefes.
7 - Eliminar empleados.
8 - Mostrar empleados.
9 - Mostrar jefes.
10 - Mostrar info individual de jefe. """))

    if opcion == "1":
        print("Ingrese la informacion del empleado: ")
        nombre = input("Nombre: ").title()
        apellido = input("Apellido: ").title()
        edad = input("Edad: ")
        cargo = input("Cargo: ")
        salario = input("Salario: ")
        emp = Empleado(nombre, apellido, edad, cargo, salario)
        emp.agregar_empleados()

    elif opcion == "2":
        print("Ingrese la informacion del jefe: ")
        nombre = input("Nombre: ").title()
        apellido = input("Apellido: ").title()
        edad = input("Edad: ")
        cargo = input("Cargo: ")
        salario = input("Salario: ")
        jef = Jefe(nombre, apellido, edad, cargo, salario)
        jef.agg_jefe()

    elif opcion == "3":
        try:
            jefes = read_json("jefes.json")
            print("\nElija el numero del jefe: \n")
            emp_list(jefes, "count")
            list_jefes = list(jefes.values())
            eleccion = int(input("")) - 1
            jefe_elegido = list_jefes[eleccion]
            n = jefe_elegido["nombre"]
            a = jefe_elegido["apellido"]
            e = jefe_elegido["edad"]
            c = jefe_elegido["cargo"]
            s = jefe_elegido["salario"]
            jef = Jefe(n, a, e, c, s)
            jef.contratar_empleado()
        except IndexError:
            print("• Ese numero no se encuentra en la lista •")
        except ValueError:
            print("• Debe ingresar un numero para continuar •")

    elif opcion == "4":
        jefes = read_json("jefes.json")
        empleados = read_json("empleados.json")
        lista_empleados = list(empleados.values())
        dict_empleados = {}
        for n in jefes:
            dentro_jefes = jefes[n]
            dentro_empleados = dentro_jefes["empleados"]
            dict_empleados.update(dentro_empleados)
        for n in dict_empleados:
            emps = dict_empleados[n]
            lista_empleados.append(emps)
        count = 0
        char_list = ""
        for n in range(0, len(lista_empleados)):
            dict_for = lista_empleados[n]
            nombre = dict_for["nombre"]
            apellido = dict_for["apellido"]
            edad = dict_for["edad"]
            cargo = dict_for["cargo"]
            salario = dict_for["salario"]
            count += 1
            char_list += f"{count} - {nombre} {apellido}, {edad} años. Cargo: {cargo}. Salario: {salario}\n"
        print("\nElija el numero del empleado al que va a actualizar: \n")
        print(char_list)
        opcion = int(input("")) - 1
        empleado_elegido = lista_empleados[opcion]
        n = empleado_elegido["nombre"]
        a = empleado_elegido["apellido"]
        e = empleado_elegido["edad"]
        c = empleado_elegido["cargo"]
        s = empleado_elegido["salario"]
        emp = Empleado(n, a, e, c, s)
        emp.actualizar_info_empleados()

    elif opcion == "5":
        jefes = read_json("jefes.json")
        lista_jefes = list(jefes.values())
        print("\nElija el número del jefe a actualizar: \n")
        emp_list(jefes, "count")
        opcion = int(input("")) - 1
        empleado_elegido = lista_jefes[opcion]
        jef = Jefe(empleado_elegido["nombre"], empleado_elegido["apellido"], empleado_elegido["edad"],
                    empleado_elegido["cargo"], empleado_elegido["salario"],)
        jef.actualizar_info_jefe()
        
    elif opcion == "6":
        jefes = read_json("jefes.json")
        lista_jefes = list(jefes.values())
        print("\nElija el número del jefe que va a eliminar:\n")
        emp_list(jefes, "count")
        opcion = int(input()) - 1
        jefe_elegido = lista_jefes[opcion]
        jef = Jefe(jefe_elegido["nombre"], jefe_elegido["apellido"], jefe_elegido["edad"],
                    jefe_elegido["cargo"], jefe_elegido["salario"],)
        jef.eliminar_jefe()

    elif opcion == "7":
        print("\n¿Quien es el jefe del empleado?:\n")
        jefes = read_json("jefes.json")
        empleados = read_json("empleados.json")
        emp_list(jefes, "count")
        ult_num = len(jefes) + 1
        print(f"{ult_num} Todavía no tiene jefe. ")
        opcion = int(input("\n"))
        if opcion == ult_num:
            print("\nEsta es la lista de los empleados disponibles, elija el numero del empleado a eliminar: \n")
            lista_empleados = list(empleados.values())
            emp_list(empleados, "count")
            empleado_elegido = int(input("")) - 1
            empleado_eliminado = lista_empleados[empleado_elegido]
            su_clave = info_in_dict(empleado_eliminado, empleados)
            nombre = empleado_eliminado["nombre"]
            apellido = empleado_eliminado["apellido"]
            seguir = input(f"""Se eliminará a {nombre} {apellido}. 
    Presione enter para continuar, 'n' para cancelar: \n""")
            if seguir == "":
                empleados.pop(su_clave)
                up_json("empleados.json", empleados)
                print("• Se ha eliminado al empleado •")
            else:
                print("• Se ha cancelado la operacion •")
        else:
            jefes_lista = list(jefes.values())
            jefe_elegido = jefes_lista[opcion - 1]
            empleados_del_jefe = jefe_elegido["empleados"]
            lista_de_empleados = list(empleados_del_jefe.values())
            print("""\nEstos sus los empleados,
    elija el numero del empleado que va a eliminar:\n""")
            emp_list(empleados_del_jefe, "count")
            empleado_a_eliminar = int(input("")) - 1
            empleado_elegido = lista_de_empleados[empleado_a_eliminar]
            clave_empleado = info_in_dict(empleado_elegido, empleados_del_jefe)
            clave_jefe = info_in_dict(jefe_elegido, jefes)
            su_jefe = jefes[clave_jefe]
            en_empleados = su_jefe["empleados"]
            nombre = empleado_elegido["nombre"]
            apellido = empleado_elegido["apellido"]
            seguir = input(f"""\nSe eliminará a {nombre} {apellido},
    esta accion es irreversible, presione enter para continuar o 'n' para cancelar el proceso: """)
            if seguir == "":
                en_empleados.pop(clave_empleado)
                up_json("jefes.json", jefes)
                print("• Se ha eliminado al empleado •")
            else:
                print("• Se ha cancelado el proceso •")

    elif opcion == "8":
        print("\nEstos son los empelados actualmente:\n")
        jefes = read_json("jefes.json")
        empleados = read_json("empleados.json")
        lista_empleados = list(empleados.values())
        dentro_empleados = {}
        for n in jefes:
            dentro_jefes = jefes[n]
            dentro_empleados.update(dentro_jefes["empleados"])
        for n in dentro_empleados:
            empleado = dentro_empleados[n]
            lista_empleados.append(empleado)
        for n in lista_empleados:
            emp = Empleado(n["nombre"], n["apellido"], n["edad"], n["cargo"], n["salario"])
            emp.mostrar_empleados()

    elif opcion == "9":
        print("")
        jefes = read_json("jefes.json")
        lista_jefes = list(jefes.values())
        for n in lista_jefes:
            jef = Jefe(n["nombre"], n["apellido"], n["edad"], n["cargo"], n["salario"])
            jef.mostrar_jefes()

    elif opcion == "10":
        jefes = read_json("jefes.json")
        print("\nElija el numero del jefe:\n")
        emp_list(jefes, "count")
        lista_jefes = list(jefes.values())
        opcion = int(input("")) - 1
        jefe_elegido = lista_jefes[opcion]
        jef = Jefe(jefe_elegido["nombre"], jefe_elegido["apellido"], jefe_elegido["edad"], jefe_elegido["cargo"], jefe_elegido["salario"])
        jef.mostrar_info_individual()


opcion = ""
while opcion == "":
    menu()
    opcion = input("""Presione enter para volver al menu 
Presione 'n' para guardar y salir. """)
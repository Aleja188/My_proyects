from prueba.funciones import id_rand, up_json, read_json, emp_list, info_in_dict
dictt = {}

class Empleado:
    def __init__(self, nombre, apellido, edad, cargo, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cargo = cargo
        self.salario = salario

    def agregar_empleados(self):
        empleados = read_json("empleados.json")
        id_empleado = id_rand(empleados)
        empleados[id_empleado] = {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "cargo": self.cargo,
            "salario": self.salario
        }
        up_json("empleados.json", empleados)
        print(f"• Se ha agregado a {self.nombre} {self.apellido} a la lista de empleados disponibles :)")

    def actualizar_info_empleados(self):
        empleados = read_json("empleados.json")
        jefes = read_json("jefes.json")
        empleados_lista = list(empleados.values())
        empleados_con_jefe = []
        dict_empleados_jefe = {}
        for n in jefes:
            dentro_jefes = jefes[n]
            dentro_empleados = dentro_jefes["empleados"]
            dict_empleados_jefe.update(dentro_empleados)
        for n in dict_empleados_jefe:
            empleado = dict_empleados_jefe[n]
            empleados_con_jefe.append(empleado)
        dict_elegido = {"nombre": self.nombre, "apellido": self.apellido, "edad": self.edad, "cargo": self.cargo, "salario": self.salario}
        
        if dict_elegido in empleados_lista:
            clave = info_in_dict(dict_elegido, empleados)
            info_dict = empleados[clave]
            print(f"\nSe actualizará la información de {self.nombre} {self.apellido}")
            opcion = input("""Digite el numero de la informacion que desee actualizar:
            1- nombre
            2- apellido
            3- edad
            4- cargo
            5- salario """)
            if opcion == "1":
                n = input("Ingrese el nombre actualizado: ").title()
                info_dict["nombre"] = n
            elif opcion == "2":
                n = input("Ingrese el apellido actualizado del ususario: ").title()
                info_dict["apellido"] = n
            elif opcion == "3":
                n = input("Ingrese la edad actualizada del ususario: ")
                info_dict["edad"] = n
            elif opcion == "4":
                n = input("Ingrese el cargo actualizado del ususario: ")
                info_dict["cargo"] = n
            elif opcion == "5":
                n = input("Ingrese el salario actualizado del ususario: ")
                info_dict["salario"] = n
            up_json("empleados.json", empleados)
            print(f"\n♥ Se han actualizado los datos del empleado ♥")
        
        elif dict_elegido in empleados_con_jefe:
            clave_empleado = None
            pertenece = None
            for n in jefes:
                dentro_jefe = jefes[n]
                en_empleados = dentro_jefe["empleados"]
                for s in en_empleados:
                    emp = s
                    if en_empleados[s] == dict_elegido:
                        clave_empleado = emp

            for n in jefes:
                jef = n
                dentro_jefes = jefes[n]
                empleados_jefes = dentro_jefes["empleados"]
                for s in empleados_jefes:
                    if empleados_jefes[s] == dict_elegido:
                        pertenece = jef
            su_jefe = jefes[pertenece]
            sj_empleados = su_jefe["empleados"]
            info_dict = sj_empleados[clave_empleado]
            print(f"\nSe actualizará la información de {self.nombre} {self.apellido}")
            opcion = input("""Digite el numero de la informacion que desee actualizar:
            1- nombre
            2- apellido
            3- edad
            4- cargo
            5- salario """)
            if opcion == "1":
                n = input("Ingrese el nombre actualizado: ").title()
                info_dict["nombre"] = n
            elif opcion == "2":
                n = input("Ingrese el apellido actualizado del ususario: ").title()
                info_dict["apellido"] = n
            elif opcion == "3":
                n = input("Ingrese la edad actualizada del ususario: ")
                info_dict["edad"] = n
            elif opcion == "4":
                n = input("Ingrese el cargo actualizado del ususario: ")
                info_dict["cargo"] = n
            elif opcion == "5":
                n = input("Ingrese el salario actualizado del ususario: ")
                info_dict["salario"] = n
            up_json("jefes.json", jefes)
            print(f"\n♥ Se han actualizado los datos del empleado ♥")
            
    def mostrar_empleados(self):
        empleados = read_json("empleados.json")
        jefes = read_json("jefes.json")
        lista_empleados = list(empleados.values())
        dict_empleados = {"nombre": self.nombre, "apellido": self.apellido, "edad": self.edad,
                          "cargo": self.cargo, "salario": self.salario}
        dentro_empleados = {}
        for n in jefes:
            dentro_jefes = jefes[n]
            dentro_empleados.update(dentro_jefes["empleados"])
        lista_empleados_con_jefe = list(dentro_empleados.values())
        if dict_empleados in lista_empleados:
            print(f"♥ {self.nombre} {self.apellido}, {self.edad} años. Cargo: {self.cargo}. Salario: {self.salario}.")
        if dict_empleados in lista_empleados_con_jefe:
            clave_empleado = info_in_dict(dict_empleados, dentro_empleados)
            clave_jefe = None
            for n in jefes:
                clave = n
                dentro_jefes = jefes[n]
                dentro_empleados = dentro_jefes["empleados"]
                for n in dentro_empleados:
                    if dict_empleados == dentro_empleados[n]:
                        clave_jefe = clave
            jefe = jefes[clave_jefe]
            jefe_nombre = jefe["nombre"]
            jefe_apellido = jefe["apellido"]
            print(f"♥ {self.nombre} {self.apellido}, {self.edad} años. Cargo: {self.cargo}. Salario: {self.salario}. Jefe: • {jefe_nombre} {jefe_apellido}.")

                


class Jefe(Empleado):
    def __init__(self, nombre, apellido, edad, cargo, salario):
        super().__init__(nombre, apellido, edad, cargo, salario)

    def agg_jefe(self):
        jefes = read_json("jefes.json")
        id_empleado = id_rand(jefes)
        jefes[id_empleado] = {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "cargo": self.cargo,
            "salario": self.salario,
            "empleados": {}
        }
        up_json("jefes.json", jefes)
        print(f"• Se ha agregado a {self.nombre} {self.apellido} a la lista de jefes :)")

    def contratar_empleado(self):
        empleados = read_json("empleados.json")
        jefes = read_json("jefes.json")
        if len(empleados) == 0:
            print("• En este momento no hay empleados disponibles para contratar :(")
        else:
            print("\nElija los numeros de los empleados a contratar separados por una coma:\n")
            emp_list(empleados, "count")
            list_empleados = list(empleados.values())
            opcion = input("")
            opcion_lista = opcion.split(", ")
            empleados_seleccionados = []
            claves_seleccionadas = []
            for n in opcion_lista:
                num = int(n) - 1
                empleados_seleccionados.append(list_empleados[num])
                info = list_empleados[num]
                claves = info_in_dict(info, empleados)
                claves_seleccionadas.append(claves)
            diccionario = {
                "nombre": self.nombre,
                "apellido": self.apellido,
                "edad": self.edad,
                "cargo": self.cargo,
                "salario": self.salario
            }
            clave_jefe = info_in_dict(diccionario, jefes)
            dentro_jefe = jefes[clave_jefe]
            dentro_empleados = dentro_jefe["empleados"]
            for n in range(0, len(empleados_seleccionados)):
                clave = claves_seleccionadas[n]
                dentro_empleados[clave] = empleados_seleccionados[n]
            for n in range(0, len(empleados_seleccionados)):
                empleados.pop(claves_seleccionadas[n])
            up_json("empleados.json", empleados)
            up_json("jefes.json", jefes)
            print("• Informacion actualizada •")

    def actualizar_info_jefe(self):
        jefes = read_json("jefes.json")
        dict_elegido = {"nombre": self.nombre, "apellido": self.apellido, "edad": self.edad, "cargo": self.cargo, "salario": self.salario}
        clave = info_in_dict(dict_elegido, jefes)
        jefe_elegido = jefes[clave]
        print(f"\nSe actualizará la información de {self.nombre} {self.apellido}")
        opcion = input("""Digite el numero de la informacion que desee actualizar:
        1- nombre
        2- apellido
        3- edad
        4- cargo
        5- salario """)
        if opcion == "1":
            n = input("Ingrese el nombre actualizado: ").title()
            jefe_elegido["nombre"] = n
            print(f"\n♥ Se han actualizado los datos del jefe ♥")    
        elif opcion == "2":
            n = input("Ingrese el apellido actualizado del ususario: ").title()
            jefe_elegido["apellido"] = n
            print(f"\n♥ Se han actualizado los datos del jefe ♥")    
        elif opcion == "3":
            n = input("Ingrese la edad actualizada del ususario: ")
            jefe_elegido["edad"] = n
            print(f"\n♥ Se han actualizado los datos del jefe ♥")    
        elif opcion == "4":
            n = input("Ingrese el cargo actualizado del ususario: ")
            jefe_elegido["cargo"] = n
            print(f"\n♥ Se han actualizado los datos del jefe ♥")    
        elif opcion == "5":
            n = input("Ingrese el salario actualizado del ususario: ")
            jefe_elegido["salario"] = n 
            print(f"\n♥ Se han actualizado los datos del jefe ♥")
        else:
            print("• Se ha cancelado la operacion •")    
        up_json("jefes.json", jefes)
            
    def eliminar_jefe(self):
        print(f"""Se eliminará a: {self.nombre} {self.apellido}
Esta acción no se puede devolver.""")
        continuar = input("Presione enter para continuar, escriba 'n' para cancelar el proceso: " )
        if continuar == "":
            jefes = read_json("jefes.json")
            dict_elegido = {"nombre": self.nombre, "apellido": self.apellido, "edad": self.edad,
                            "cargo": self.cargo, "salario": self.salario}
            clave = info_in_dict(dict_elegido, jefes)
            jefes.pop(clave)
            up_json("jefes.json", jefes)
            print("• Se ha eliminado al jefe seleccionado •")
        else:
            print("• Se ha cancelado el proceso •")

    def mostrar_jefes(self):
        dict_elegido = {"nombre": self.nombre, "apellido": self.apellido, 
                        "edad": self.edad, "cargo": self.cargo, "salario": self.salario}
        jefes = read_json("jefes.json")
        clave_jefe = info_in_dict(dict_elegido, jefes)
        jefe = jefes[clave_jefe]
        empleados_jefe = jefe["empleados"]
        print(f"{self.nombre} {self.apellido}, {self.edad} años. Cargo: {self.cargo}. Salario: {self.salario}")
        if len(empleados_jefe) == 0:
            print("Aun sin empleados")
        else:
            print("- Empleados:")
            emp_list(empleados_jefe, "♥")

    def mostrar_info_individual(self):
        dict_elegido = {"nombre": self.nombre, "apellido": self.apellido, 
                "edad": self.edad, "cargo": self.cargo, "salario": self.salario}
        jefes = read_json("jefes.json")
        clave = info_in_dict(dict_elegido, jefes)
        jefe = jefes[clave]
        empleados = jefe["empleados"]
        print(f"{self.nombre} {self.apellido}, {self.edad} años. Cargo: {self.cargo}. salario: {self.salario}")
        if len(empleados) == 0:
            print("Aun sin empleados.")
        else:
            print("- Empleados:")
            emp_list(empleados, "♥")
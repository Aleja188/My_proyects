import json
def info_user():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    cargo = input("Cargo: ")
    salario = input("Salario: ")


class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
 
class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, cargo, salario):
        super().__init__(nombre, apellido, edad)
        self.cargo = cargo
        self.salario = salario

    def agregar_empleado(self):
        with open("empleados.json", "r") as data:
            info = json.load(data)
        ultimo_numero = 0
        if len(info) == 0:
            info[f"empleado {str(int(ultimo_numero) + 1)}"] = {"nombre": self.nombre,
                                                           "apellido": self.apellido,
                                                           "edad": self.edad,
                                                           "cargo": self.cargo,
                                                           "salario": self.salario}
            print("\nSe ha agregado a", self.nombre, self.apellido, "a la lista de empleados disponibles para contratar.\n")
        else:
            for n in info:
                ultimo_numero = n[9]
            info[f"empleado {str(int(ultimo_numero) + 1)}"] = {"nombre": self.nombre,
                                                                "apellido": self.apellido,
                                                                "edad": self.edad,
                                                                "cargo": self.cargo,
                                                                "salario": self.salario}
            print("\nSe ha agregado a", self.nombre, self.apellido, "a la lista de empleados disponibles para contratar.\n")
        with open("empleados.json", "w") as data:
            json.dump(info, data, indent = 4)
        
        
    def actualizar_info(self):
        with open("jefes.json", "r") as data:
            jefes = json.load(data)
        with open("empleados.json", "r") as data:
            empleados = json.load(data)
        dict_empleado = {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "cargo": self.cargo,
            "salario": self.salario
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
            print("Editar informacion de: " + self.nombre + " " + self.apellido)
            opcion = str(input("""Digite el numero de la opcion que desea actualizar:
            1- Nombre
            2- apellido
            3- edad
            4- cargo
            5- salario"""))

            if opcion == "1":
                nombre = input("Escriba el nombre del empleado: ").title()
                empleadop["nombre"] = nombre
            if opcion == "2":
                apellido = input("Escriba el apellido del empleado: ").title()
                empleadop["apellido"] = apellido
            if opcion == "3":
                edad = input("Escriba la edad del empleado: ")
                empleadop["edad"] = edad
            if opcion == "4":
                cargo = input("Escriba el cargo del empleado: ")
                empleadop["cargo"] = cargo
            if opcion == "5":
                salario = input("Escriba el salario de lempleado: ")
                empleadop["salario"] = salario
            with open("jefes.json", "w") as data:
                json.dump(jefes, data, indent = 4)
            print("Informacion actualizada :)")
        else:
            clave_empleado = None
            for clave, valor in empleados.items():
                if dict_empleado == valor:
                    clave_empleado = clave
            print("Editar informacion de: " + self.nombre + " " + self.apellido)
            opcion = str(input("""Digite el numero de la opcion que desea actualizar:
            1- Nombre
            2- apellido
            3- edad
            4- cargo
            5- salario"""))
            empleado = empleados[clave_empleado]
            if opcion == "1":
                nombre = input("Escriba el nombre del empleado: ").title()
                empleado["nombre"] = nombre
            if opcion == "2":
                apellido = input("Escriba el apellido del empleado: ").title()
                empleado["apellido"] = apellido
            if opcion == "3":
                edad = input("Escriba la edad del empleado: ")
                empleado["edad"] = edad
            if opcion == "4":
                cargo = input("Escriba el cargo del empleado: ")
                empleado["cargo"] = cargo
            if opcion == "5":
                salario = input("Escriba el salario del empleado: ")
                empleado["salario"] = salario
            with open("empleados.json", "w") as data:
                json.dump(empleados, data, indent = 4)    
            print("Informacion actualizada :)")
                    
        
            



class Jefe(Persona):
    def __init__(self, nombre, apellido, edad, cargo, salario):
        super().__init__(nombre, apellido, edad)
        self.cargo = cargo
        self.salario = salario

    def agregar_jefe(self):
        with open("jefes.json", "r") as data:
            info = json.load(data)
        ultimo_numero = 0
        for n in info:
            ultimo_numero = n[5]
        info[f"jefe {str(int(ultimo_numero) + 1)}"] = {"nombre": self.nombre,
                                                            "apellido": self.apellido,
                                                            "edad": self.edad,
                                                            "cargo": self.cargo,
                                                            "salario": self.salario,
                                                            "empleados": {} } 
        with open("jefes.json", "w") as data:
            json.dump(info, data, indent = 4)

        print("Se ha agregado a", self.nombre, self.apellido, "a la lista de jefes")

    def contratar_empleados(self):
        with open("empleados.json", "r") as data:
            empleados = json.load(data)
        with open("jefes.json", "r") as data:
            jefes = json.load(data)
        lista_empleados = ""
        count = 0
        if len(empleados) == 0:
            print("No hay empleados para contratar en estos momentos...\n")
        else:
            for n in empleados:
                o = empleados[n]
                nombre = o["nombre"]
                apellido = o["apellido"]
                edad = o["edad"]
                cargo = o["cargo"]
                salario = o["salario"]
                count += 1
                lista_empleados += str(count)+"- "+nombre+" "+apellido+", "+edad+" años"+", Cargo: "+cargo+". Salario: "+salario+"\n"


            print("La lista de empleados disponibles es:\n" + lista_empleados)
            opcion = input("Elija el o los numeros de los empleados a contratar separados por una coma: ")
            opcion_lista = opcion.split(", ")
            lista_empleados = list(empleados.values())
            lista_empleados_2 = []
            for n in opcion_lista:
                num = int(n) - 1
                lista_empleados_2.append(lista_empleados[num])
    
    
            info_jefe = {
                "nombre": self.nombre,
                "apellido": self.apellido,
                "edad": self.edad,
                "cargo": self.cargo,
                "salario": self.salario,
            }
            clave_encontrada = None
            for n, datos_jefe in jefes.items():
    
                if all(info_jefe[clave] == datos_jefe.get(clave) for clave in info_jefe):
                    clave_encontrada = n
                    break
            inf_jefe = jefes[clave_encontrada]
            empleados_jefe = inf_jefe["empleados"]
            ultimo_numero = 0
            if len(empleados_jefe) == 0:
                for n in range(0, len(lista_empleados_2)):
                    empleados_jefe[f"empleado {str(ultimo_numero)}"] = lista_empleados_2[n]
                    ultimo_numero += 1
            else:
                for n in empleados_jefe:
                    ultimo_numero = int(n[9])
                for n in range(0, len(lista_empleados_2)):
                    ultimo_numero += 1
                    empleados_jefe[f"empleado {str(ultimo_numero)}"] = lista_empleados_2[n]
                    
                    
            
            len_lista = len(lista_empleados_2)
            with open("jefes.json", "w") as data:
                json.dump(jefes, data, indent = 4)
            if len(lista_empleados_2) == 1:
                print(self.nombre, self.apellido, "ha contratado 1 nuevo empleado.")
            else:
                print(self.nombre, self.apellido, "ha contratado " + str(len_lista) + " nuevos empleados.")
            def encontrar_claves_en_diccionario(info_a_buscar, diccionario_a_buscar):
                claves_encontradas = []
                for clave, datos in diccionario_a_buscar.items():
                    if all(info_a_buscar[clave] == datos.get(clave) for clave in info_a_buscar):
                        claves_encontradas.append(clave)
                return claves_encontradas
            for n in range(0, len(lista_empleados_2)):
                claves = encontrar_claves_en_diccionario(lista_empleados_2[n], empleados)
                str_claves = "".join(claves)
                empleados.pop(str_claves)
            with open("empleados.json", "w") as data:
                json.dump(empleados, data, indent = 4)

    def actualizar_info_jefe(self):
        with open("jefes.json", "r") as data:
            jefes = json.load(data)
        dict_jefe = {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "cargo": self.cargo,
            "salario": self.salario
        }
        clave_jefe = None
        for n, dentro_jefes in jefes.items():
            if dict_jefe.items() <= dentro_jefes.items():
                clave_jefe = n
                break
        info_jefe = jefes[clave_jefe]
        print("Editar informacion de: " + self.nombre + " " + self.apellido)
        opcion = str(input("""Digite el numero de la opcion que desea actualizar:
        1- Nombre
        2- apellido
        3- edad
        4- cargo
        5- salario"""))

        if opcion == "1":
            nombre = input("Escriba el nombre del jefe: ").title()
            info_jefe["nombre"] = nombre
        if opcion == "2":
            apellido = input("Escriba el apellido del jefe: ").title()
            info_jefe["apellido"] = apellido
        if opcion == "3":
            edad = input("Escriba la edad del jefe: ")
            info_jefe["edad"] = edad
        if opcion == "4":
            cargo = input("Escriba el cargo del jefe: ")
            info_jefe["cargo"] = cargo
        if opcion == "5":
            salario = input("Escriba el salario del jefe: ")
            info_jefe["salario"] = salario
        with open("jefes.json", "w") as data:
            json.dump(jefes, data, indent = 4)
        print("Informacion actualizada :)")

    def borrar_jefe(self):
         with open("jefes.json", "r") as data:
            jefes = json.load(data)
            dict_jefe = {
                "nombre": self.nombre,
                "apellido": self.apellido,
                "edad": self.edad,
                "cargo": self.cargo,
                "salario": self.salario
            }
            clave_jefe = None
            for n, dentro_jefes in jefes.items():
                if dict_jefe.items() <= dentro_jefes.items():
                    clave_jefe = n
                    break
            eliminar = input(f"""¿Seguro que desea eliminar a {self.nombre} {self.apellido} de la lista de jefes?
            Esta acción es irreversible.
            Escriba 'y' para continuar con la operación, 'n' para cancelar: """).lower()

            if eliminar == 'y': 
                print(f"Se ha eliminado a {self.nombre} {self.apellido} de la lista de jefes.")
                jefes.pop(clave_jefe)
                with open("jefes.json", "w") as data:
                    json.dump(jefes, data, indent = 4)
            else:
                print("Operación cancelada.")


    def mostrar_jefes(self):
        with open("jefes.json", "r") as data:
            jefes = json.load(data)
            dict_jefe = {
                "nombre": self.nombre,
                "apellido": self.apellido,
                "edad": self.edad,
                "cargo": self.cargo,
                "salario": self.salario
            }
            clave_jefe = None
            for n, dentro_jefes in jefes.items():
                if dict_jefe.items() <= dentro_jefes.items():
                    clave_jefe = n
                    break
            dentro_jefe = jefes[clave_jefe]
            dentro_empleados = dentro_jefes["empleados"]
            
            if len(dentro_empleados) != 0:
                cadena_empleados = ""
                for n in dentro_empleados:
                    info_empleados = dentro_empleados[n]
                    no = info_empleados["nombre"]
                    a = info_empleados["apellido"]
                    e = info_empleados["edad"]
                    c = info_empleados["cargo"]
                    s = info_empleados["salario"]
                    cadena_empleados += " - " + no + " " + a + " " + e + " años. " + "Cargo: " + c + ". Salario: " + s + "\n"
                print("•", self.nombre, self.apellido, ",", self.edad, "años. Cargo:", self.cargo, "Salario:", self.salario, f"\nEmpleados:\n{cadena_empleados}")
            else:
                print("•", self.nombre, self.apellido, ",", self.edad, "años. Cargo:", self.cargo, "Salario:", self.salario, ". Empleados:\nNo tiene empleados\n")


    def mostrar_empleados(self):
        with open("jefes.json", "r") as data:
            jefes = json.load(data)
        with open("empleados.json", "r") as data:
            empleados = json.load(data)
        emp_dict = {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "cargo": self.cargo,
            "salario": self.salario
        }
        jeff = False
        for clave, valor in empleados.items():
            if emp_dict == valor:
                print("♥", self.nombre, self.apellido, self.edad, "años.", f"Cargo: {self.cargo}. Salario: {self.salario}.")
            else:
                jeff = True
        if jeff == True:
            try:
                clave_en_empleado = None
                su_jefe = None
                for n in jefes:
                    dentro_jefes = jefes[n]
                    empleados_jefes = dentro_jefes["empleados"]
                    for clave, valor in empleados_jefes.items():
                        if emp_dict == valor:
                            clave_en_empleado = clave
                dict = {}
                dict[clave_en_empleado] = emp_dict
                pertenece = None
                for n in jefes:
                    jef = n
                    dentro_jefes = jefes[n]
                    empleados_jefes = dentro_jefes["empleados"]
                    for s in empleados_jefes:
                        if empleados_jefes[s] == emp_dict:
                            pertenece = jef
                dentro_jefe = jefes[pertenece]
                nj = dentro_jefe["nombre"]
                aj = dentro_jefe["apellido"]
                print("♥", f"{self.nombre} {self.apellido}, {self.edad} años. Cargo: {self.cargo}. Salario: {self.salario}. Jefe: • {nj} {aj}.")
            except KeyError:
                pass

        

            
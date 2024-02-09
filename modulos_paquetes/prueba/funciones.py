import json
import random

def up_json(file_name, info):
    with open(file_name, "w") as data:
        json.dump(info, data, indent = 4)

def read_json(file_name):
    with open(file_name, "r") as data:
        return json.load(data)

def id_rand(dictionary):
    final_id = random.randint(1000, 3000)
    list = []
    for n in dictionary:
        list.append(int(n))
    while final_id in list:
        final_id = random.randint(1000, 3000)
    return final_id

def info_in_dict(diccionario_a_buscar, diccionario_a_analizar):
    for n, s in diccionario_a_analizar.items():
        if diccionario_a_buscar.items() <= s.items():
            return n
            break

def emp_list(emp_dict, marcador):
    char_list = ""
    count = 0
    for keys in emp_dict:
        onto = emp_dict[keys]
        nombre = onto["nombre"]
        apellido = onto["apellido"]
        edad = onto["edad"]
        cargo = onto["cargo"]
        salario = onto["salario"]
        count += 1
        if marcador == "count":
            char_list += f"{count} {nombre} {apellido}, {edad} años. Cargo: {cargo}. Salario: {salario}\n"
        else:
            char_list += f"{marcador} {nombre} {apellido}, {edad} años. Cargo: {cargo}. Salario: {salario}\n"
    print(char_list)
    

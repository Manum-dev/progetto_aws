#dizionario

personaggio1:dict[str, str] = {
    "nome" :"Pippo",
    "tipo": "cane",
    "email" : "pippo@disney.com"
}

personaggio1["telefono"] = "09712334"

personaggio1["telefono"] = "09712335"

print(personaggio1.get("telefono"))


"""
stringhe: list[str] = ["Pippo"]
stringhe.append("Pluto")
stringhe.append("Minnie")


deleted_values: list[str] = []

value_to_check_and_delete: str ="pluto"

is_value_in_the_list: bool = value_to_check_and_delete in stringhe

if is_value_in_the_list ==True:
    index_value_to_delete = stringhe.index(value_to_check_and_delete)
    deleted_value = stringhe.pop(index_value_to_delete)
    deleted_values.append(deleted_value)

deleted_values.append(deleted_values)


print(deleted_values)
print(stringhe)

"""



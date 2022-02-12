# all the import:
import json
from string_simplified_functions import full_to_full, full_name_to_first, full_name_to_last, security_code_formatation
from string_simplified_functions import year_formatation, month_formatation, cpf_formatation, card_formatation
from string_simplified_functions import card_brand_formatation

# Opening, getting the data and closing the input json file
with open('input_card.json')as file:
    brute_data = json.load(file)
    file.close()

# Formatting the brute_data values:
new_dict_2 = {}
cont = 0
key_iter = iter(brute_data.keys())
for n in brute_data.values():
    if cont == 3:
        break
    new_dict = {}
    full_name = full_to_full(n['full_name'])
    first_name = full_name_to_first(n['full_name'])
    last_name = full_name_to_last(n['full_name'])
    cpf = cpf_formatation(n['cpf'])
    card_number = card_formatation(n['card_number'])
    expiration_mm = month_formatation(n['expiration_mm'])
    expiration_yyyy = year_formatation(n['expiration_yyyy'])
    card_brand = card_brand_formatation(n['card_brand'])
    security_code = security_code_formatation(n['security_code'])
    new_dict['full_name'] = full_name
    new_dict['first_name'] = first_name
    new_dict['last_name'] = last_name
    new_dict['cpf'] = cpf
    new_dict['card_number'] = card_number
    new_dict['expiration__mm'] = expiration_mm
    new_dict['expiration_yyyy'] = expiration_yyyy
    new_dict['card_brand'] = card_brand
    new_dict['security_code'] = security_code
    # print(new_dict)
    new_dict_2[key_iter.__next__()] = new_dict
    cont += 1

# converting the new_dict_2(formatted dictionary) to a new Json file
json_output = json.dumps(new_dict_2)
print(json_output)


# exporting to a new json file
with open('output_card.json', 'w') as output_card:
    output_card.write(json_output)



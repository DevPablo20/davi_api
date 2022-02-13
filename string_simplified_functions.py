''' All the formatation delivers a simplified data containning upper string types values'''

# Name formatation:
def full_to_full(full_name):
    """
    Convert a full_name variable to an upper string.
    :param full_name: variable from the JSON dictionary
    :return: a string type upper full_name
    """
    new_full = full_name.strip().upper()
    return new_full

def full_name_to_first(full_name):
    """
    Convert a full_name vabiable to an upper first_name string
    :param full_name: variable from the JSON dictionary
    :return: a string type upper first_name
    """
    breaked = full_name.strip().split(' ')
    first_name = breaked[0].upper()
    return first_name

def full_name_to_last(full_name):
    """
    Convert a full_name vabiable to an upper last_name string
    :param full_name: variable from the JSON dictionary
    :return: a string type upper last_name
    """
    breaked = full_name.strip().split(' ')
    last_name = breaked[-1].upper()
    return last_name

# Cpf formatation:
def cpf_formatation(cpf):
    """
    Convert an string or integrer to a string removing all symbols.
    :param cpf: variable from the JSON dictionary
    :return: a cleaned string type cpf
    """
    new_cpf = cpf.replace('.', '')
    new_cpf = new_cpf.replace('-', '')
    return new_cpf

# Card Number Formatation:
def card_formatation(card_number):
    """
    Convert full o last four numbers of a string or integrer variable to a string removing all symbols
    :param card_number: variable from the JSON dictionary
    :return: string type last four characters
    """
    card_number = card_number.strip()
    card_number = card_number.replace('.', '')
    card_number = card_number.replace('-', '')
    n = len(card_number)
    return card_number[n-4:n]

# Month formatation:
def month_formatation(expiration_mm):
    """
    Convert a string or integrer containing the month to a string type value
    :param expiration_mm: variable from the JSON dictionary
    :return: a string type value that represents the month in number representation
    """
    portuguese = {
        'janeiro': '01',
        'fevereiro': '02',
        'março': '03',
        'abril': '04',
        'maio': '05',
        'junho': '06',
        'julho': '07',
        'agosto': '08',
        'setembro': '09',
        'outubro': '10',
        'novembro': '11',
        'dezembro': '12'
    }
    portuguese_abbreviated = {
        'jan': '01',
        'fev': '02',
        'mar': '03',
        'abr': '04',
        'mai': '05',
        'jun': '06',
        'jul': '07',
        'ago': '08',
        'set': '09',
        'out': '10',
        'nov': '11',
        'dez': '12'
    }
    if isinstance(expiration_mm, str):
        if expiration_mm.strip().lower() in portuguese.values():
            return expiration_mm
        elif expiration_mm.strip().lower() in portuguese.keys():
            return portuguese[expiration_mm][0:2]
        elif expiration_mm.strip().lower() in portuguese_abbreviated.keys():
            return portuguese_abbreviated[expiration_mm]

# Year formatation
def year_formatation(expiration_yyyy):
    """
    Convert a string or integrer value containing the year to a string type value
    :param expiration_yyyy: variable from the JSON dictionary
    :return: a string type value that represents the year in number representation
    """
    n = len(expiration_yyyy)
    return expiration_yyyy[n-2:n]

# Card Brand Formatation
def card_brand_formatation(card_brand):
    """
    Convert a string value containing card's brand to a cleaned string.
    :param card_brand: variable from the JSON dictionary
    :return: a string type value the represents the card's brand.
    """
    card_brand = card_brand.strip()
    card_brand = card_brand.replace(' ', '')
    card_brand = card_brand.replace('-', '')
    card_brand = card_brand.upper()
    return card_brand

# Security Code formatation
def security_code_formatation(security_code):
    """
    Convert a string or integrer value to a 3 digits string.
    :param security_code: variable from the JSON dictionary
    :return: a string type value the represents the security code
    """
    n = len(security_code)
    if n == 1:
        return '0' + '0' + security_code
    elif n == 2:
        return '0' + security_code
    elif n == 3:
        return security_code
    else:
        return security_code[n - 3:n]







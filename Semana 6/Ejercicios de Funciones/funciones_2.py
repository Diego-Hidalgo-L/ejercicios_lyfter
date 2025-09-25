# Experimente con el concepto de scope:
    


# Intente accesar a una variable definida dentro de una función desde afuera.

# def test_local_var():
    # local_var = 2
    # return local_var

# print(local_var) # "local_var" is not defined


# Intente accesar a una variable global desde una función y cambiar su valor.

global_var = 3

def test_global_var():
    global global_var
    global_var += 7


test_global_var()

print(global_var)
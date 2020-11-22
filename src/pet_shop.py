# WRITE YOUR FUNCTIONS HERE

# 1./
# We are accessing the value "Camelot of Pets" 
# in the dictionary cc_pet_shop by it's key "name":

def get_pet_shop_name(shop):
    return shop["name"]

# 2./
# We are accessing the value of the "total_cash" key
# by accessing the internal dictionary "admin" inside 
# the nested dictionary 'cc_pet_shop by'.

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

# 3./
# We are adding a variable "cash_to_add_or_remove" 
# to the function as a second parameter which would be called 
# by the argument 10. Then we add this variable to the value
# of ["total_cash"] key, and then we use addition assignment
# to assign the result to the key ["total_cash"].

def add_or_remove_cash(shop, cash_to_add_or_remove):
    shop["admin"]["total_cash"] += cash_to_add_or_remove

# 4./
# We are using the same function, as the test uses a negative 
# number as argument at the place of the parameter 
# 'cash_to_add_or_remove'. And adding a negative number will
# result subtraction.

def add_or_remove_cash(shop, cash_to_add_or_remove):
    shop["admin"]["total_cash"] += cash_to_add_or_remove
        
# 5./
# ....

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

# 6./
# ....

def increase_pets_sold(shop, num_of_sold_pets):
    shop["admin"]["pets_sold"] += num_of_sold_pets

# 7./
# ....

def get_stock_count(shop):
    return len(shop["pets"])

# 8./
# ....

def get_pets_by_breed(shop, breed):
    list = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            list.append(pet["name"])
        else:
            return list

# 9./
# ....

def get_pets_by_breed(shop, breed):
    list = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            list.append(pet["name"])
        else:
            return list

# 10./
# ....

def find_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            return pet

# 11./
# ....

def find_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            return pet

# 12./ NO
# ....

# def remove_pet_by_name(shop, pet_name):
#     for pet in shop["pets"]:
#         if pet["name"] == pet_name:
#             pet.clear()

# 13./ WORKS!!!
# ....

def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)


# 14./ WORKS!!!
# ....

def get_customer_cash(customer):
        return (customer["cash"])


# 15./ WORKS!!!
# ....

def remove_customer_cash(customer, cash_to_remove):
    customer["cash"] -= cash_to_remove


# 16./ WORKS!!!
# ....

def get_customer_pet_count(customer):
        return len(customer["pets"])

# 17./ WORKS!!!
# ....

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    
# 18./ WORKS!!!
# ....

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    
# 19./ WORKS!!!
# ....

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

# 20./ WORKS!!!
# ....

def test_customer_can_afford_pet__exact_funds(self):
    return customer["cash"] == new_pet["price"]
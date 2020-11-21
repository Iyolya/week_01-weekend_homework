# WRITE YOUR FUNCTIONS HERE

# 1./
# We are accessing the value "Camelot of Pets" 
# in the dictionary cc_pet_shop by it's key "name":

def get_pet_shop_name(shop):
    return shop["name"]

# 2./
# We are accessing the value of the "total_cash" key
# by accessing the internal dictionary "admin" inside 
# the nested dictionary 'cc_pet_shop by':

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
        



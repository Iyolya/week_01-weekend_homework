# WRITE YOUR FUNCTIONS HERE

# 1./
# We are accessing the value "Camelot of Pets" 
# in the dictionary cc_pet_shop by it's key "name":

def get_pet_shop_name(shop):
    return shop["name"]

# 2./
#We are accessing the value of the "total_cash" key
# by accessing the internal dictionary "admin" inside 
# the nested dictionary 'cc_pet_shop by':

def get_total_cash(shop):
    return shop["admin"]["total_cash"]



#property value
value=int(input("kindly enter value of your property : "))

#specify type of property
print("Type of Property \n(a)owner occupied residential property \n(b)owner occupied pensioners property \n(c)lagos state govt property \n(d)industrial premises of manufacturing \n(e)residential property owner &3rd party \n(f)residential property commercial \n(g)commercial property \n(h)vacant property and open land")
prpty_typ = input("kindly select your type with option a, b, c, d, e, f, g, h : ")


#make each option a variable
#owner occupied residential property
a = 0.065/100
#owner occupied pensioners property
b = 0
#lagos state govt property
c = 0
#industrial premises of manufacturing
d = 0.192/100
#residential property owner &3rd party
e = 0.192/100
#residential property commercial
f = 0.380/100
#commercial property
g = 0.380/100
#vacant property and open land
h = 0.076/100
if (prpty_typ.lower() == "a" ):
    value_a = (a * value)
elif(prpty_typ.lower() == "b" ):
    value_a =(b*value)
elif(prpty_typ.lower() == "c" ):
    value_a = (c*value)
elif(prpty_typ.lower() == "d" ):
    value_a = (d*value)
elif(prpty_typ.lower() == "e" ):
    value_a = (e*value)  
elif(prpty_typ.lower() == "f" ):
    value_a = (f*value)
elif(prpty_typ.lower() == "g" ):
    value_a = (g*value)
elif(prpty_typ.lower() == "h" ):
    value_a = (h*value)




# relief rate
#general relief rate
gen_rel_rate = 40/100
...
...

#special relief rate with yes or no conditions
print("INSTRUCTION \n type Y for yes and N for no ")
pensioner= input("Are you a pensioner owner occupied- 60 years and above: ")
pensioners = 100/100
if (pensioner.lower() == "y"):
    total_p = (pensioners*value)
elif (pensioner.lower() == "n"):
    total_p = 0
else:
    print ("refresh and type Y or N")
    
disability= input ("Are you a person with disability(owner occupied): ")
disabilitys = 10/100
if (disability.lower() == "y"):
    total_d =(disabilitys*value)
elif (disability.lower() == "n"):
    total_d =0
else:
    print ("refresh and type Y or N")
    
aged = input("Are you an aged persons(owner ocopied-70 years and above): ")
ageds = 10/100
if (aged.lower() == "y"):
    total_a =(ageds*value)
elif (aged.lower() == "n"):
    total_a = 0
else:
    print ("refresh and type Y or N")
    
age_of_prpty_abv_25 = input("Is the age of property (25 years and above): ")
age_of_prpty_abv_25s = 10/100
if (age_of_prpty_abv_25.lower() == "y"):
    total_25 =(age_of_prpty_abv_25s*value)
elif (age_of_prpty_abv_25.lower() == "n"):
    total_25 = 0
else:
    print ("refresh and type Y or N")
    
long_ocpnt = input("Are you a long occupation by owners(12 years and above): ")
long_ocpnts = 5/100
if (long_ocpnt.lower() == "y"):
    total_l =(long_ocpnts*value)
elif (long_ocpnt.lower() == "n"):
    total_l = 0
else:
    print ("refresh and type Y or N")
    
nonprofitmaking = input("Are you on  a partial relief under land use charge law(non profit making): ")
nonprofitmakings = 20/100
if (nonprofitmaking.lower() == "y"):
    total_n =(nonprofitmakings*value)
elif (nonprofitmaking.lower() == "n"):
    total_n = 0
else:
    print ("refresh and type Y or N")
#total relief
pymnt_wthn_15 = input("Do you intend tp pay within 15 days of assesment: ")
pymnt_wthn_15s = 15/100
if (pymnt_wthn_15.lower() == "y"):
    total_15 =(pymnt_wthn_15s*value)
elif (pymnt_wthn_15.lower() == "n"):
    total_15 = 0
else:
    print ("refresh and type Y or N")

actual_value = (value * value_a)    
actual_total = ((total_p ) + (total_a ) + (total_d ) + (total_25 ) + (total_l ) + (total_n ) + (total_15 ))
print (actual_total * actual_value)

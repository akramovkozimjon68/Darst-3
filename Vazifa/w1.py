pul = int(input("Boshlangich pul: "))
hafta= int(input("Haftalik qo`shimcha: "))

hafta = 0

while pul <= 500000:
    pul += hafta
    hafta += 1
    
print( "Kerakli hafta: ", hafta)
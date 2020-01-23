from PIL import Image
from delOpp import delOpp

path = "obamium.jpg"

im = Image.open(path)

bredde = im.size[0]
høyde = im.size[1]



LedigeEmojier = 50 #antall ledige emojier på serveren
print(f"Bildet er {bredde} px bredt og {høyde} px høyt. Det er {LedigeEmojier} ledige emojiplasser på serveren.")

OppdelingBredde = int(input("Hvor mange emojier skal bildet deles opp i vannrett? "))
OppdelingHøyde = int(input("Hvor mange emojier skal bildet deles opp i loddrett? "))

TotaleEmojier = OppdelingBredde * OppdelingHøyde
ProsentEmojier = TotaleEmojier/LedigeEmojier*100



print(f"Dette bildet vil ta opp {TotaleEmojier} emojier på serveren.")

if TotaleEmojier <= LedigeEmojier:
    print(f"Det er {ProsentEmojier}% av de ledige emojiene.")
    if input("Fortsette? (y/n) ") == "y":
        fortsette = True
    else:
        fortsette = False

else:
    print(f"Det er {TotaleEmojier-LedigeEmojier} emojier for mye. Husk at det bare er ledig plass til {TotaleEmojier} på serveren.")
    print("Prøv å fjerne emojier på serveren, eller å dele opp bildet i færre biter.")
    fortsette = False



if fortsette:
    print("fortsetter...")
    delOpp(path, OppdelingBredde, OppdelingHøyde)
    
else:
    print("avbryter...")
    exit()
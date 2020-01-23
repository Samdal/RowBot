


def delOpp(path, BreddeOppdeling, HøydeOppdeling):
    import os
    from PIL import Image
    
    bilde = Image.open(path)
    bredde, høyde = bilde.size

    miniatyrBredde = int(bredde / BreddeOppdeling)
    miniatyrHøyde = int(høyde / HøydeOppdeling)


    os.mkdir("./emojify/1")
    liste = []



    for n in range(0, int(høyde / miniatyrHøyde)):
        i = n * miniatyrHøyde
        for g in range(0, int(bredde / miniatyrBredde)):
            j = g * miniatyrBredde
            print(i, j)
            
            miniatyr = (j, i, j + miniatyrBredde, i + miniatyrHøyde)
            a = bilde.crop(miniatyr)

            # a.show()
            filnavn = f"{n+1}-{g+1}"

            liste.append([])
            liste[n].append(filnavn)
            print(liste)
            a.save(f"./emojify/1/{filnavn}.jpg")

            # try:
            #     o = a.crop(area)
            #     o.save(os.path.join(navn, "PNG", "%s" %
            #                         page, "IMG-%s.png" % k))
            # except:
            #     pass
            # k += 1

    print(liste)

delOpp("obamium.jpg", 3, 3)
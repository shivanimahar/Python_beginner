st = "Hey Harry you are amazing"

f = open("myfile.txt", "a") # append means adding, the upper string will add to the pre existing file(myfile.txt)

f.write(st)

f.close()
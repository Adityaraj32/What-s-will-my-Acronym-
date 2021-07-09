senten = input("Enter What you want to enter: ")
def acronym(string):
    acro = string[0]
    for i in range(1,len(senten)):
        if string[i-1] == " ":
            acro += string[i]
    print(acro.upper())
acronym(senten)
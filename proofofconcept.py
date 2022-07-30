text = input("Type the text you would like to output on the LMC: ")

print("Enter the below program into the LMC at https://peterhigginson.co.uk/lmc\n")
print("// BEGIN PROGRAM".format(text))
print("\tLDA 8\n\tBRZ end\n\tOTC\n\tLDA 0\n\tADD 7\n\tSTA 0\n\tBRA 0\nend\tDAT 1")

for c in text:
    print("\tDAT {}".format(ord(c)))

print("// END PROGRAM".format(text))
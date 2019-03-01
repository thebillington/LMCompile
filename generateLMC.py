text = input("Type the text you would like to output on the LMC: ")
filename = input("Enter the name of the file you would like to store the text in (e.g. lmc_data): ")

f = open("{}.txt".format(filename), "w")
f.write("\tLDA 8\n\tBRZ end\n\tOTC\n\tLDA 0\n\tADD 7\n\tSTA 0\n\tBRA 0\nend\tDAT 1")

for c in text:
    f.write("\n\tDAT {}".format(ord(c)))

f.close()

f = open("{}.txt".format(filename), "r")
print(f.read())

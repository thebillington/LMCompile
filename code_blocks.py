data_entry = "{id}\tDAT\t{value}\n"
print_integer = "\tlda {id}\n\tout\n"
print_string = "\tLDA\t{inst}\n\tSTA\tsp\nBRA\tsp\n"
print_string_function_call = "sp\tLDA\t0\n\tBRZ\tsp_end\n\tOTC\n\tLDA\tsp\n\tADD\tone\n\tSTA\tsp\n\tBRA\tsp\nsp_end\tLDA\t0\n"
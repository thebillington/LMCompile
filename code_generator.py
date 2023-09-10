import code_blocks
import nodes

class CodeGenerator:

    def __init__(self, program):
        self.program = program
        self.symbol_table = {"one":1}
        self.output = "p_start\tLDA\t0\n"
        self.has_string_print = False

    def generate(self):
        for statement in self.program:
            self.generate_statement(statement)

        if not self.has_string_print:
            self.output += code_blocks.print_string_function_call
            self.has_string_print = True

        self.output = "\tBRA\tp_start\n" + self.generate_data_table() + self.output
        return self.output
    
    def generate_statement(self, statement):
        if not hasattr(statement, "child"):
            return
        
        if isinstance(statement, nodes.PrintI):
            self.generate_print_i(statement.child)
        if isinstance(statement, nodes.PrintC):
            self.generate_print_c(statement.child)

        self.generate_statement(statement.child)

    def generate_data_table(self):
        symbols = ""
        for k in self.symbol_table.keys():
            symbols += code_blocks.data_entry.format(id=k, value=self.symbol_table[k])
        return symbols
        
    def get_symbol(self, value):
        existing_symbol = self.check_symbol_table(value)
        if existing_symbol:
            return existing_symbol
        
        symbol_no = len(self.symbol_table)
        symbol_key = f'id{symbol_no}'
        if isinstance(value, int):
            self.symbol_table[symbol_key] = value
        if isinstance(value, str):
            self.symbol_table[symbol_key] = ord(value)
        return (symbol_key, symbol_no)

    def check_symbol_table(self, value):
        for k in self.symbol_table.keys():
            if self.symbol_table[k] == value:
                return k
        return False

    def generate_print_i(self, statement):
        value = statement.child
        symbol, symbol_no = self.get_symbol(value)
        self.output += code_blocks.print_integer.format(id=symbol)

    def generate_print_c(self, statement):
        value = list(statement.child + "\0")
        symbol, symbol_no = self.get_symbol(value.pop(0))
        for char in value:
            self.get_symbol(char)
        instruction, inst_no = self.get_symbol(int(f'5{symbol_no+1:02d}'))
        self.output += code_blocks.print_string.format(inst=instruction)

    def generate_print_c_string(self, statement):
        return
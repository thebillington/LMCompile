import code_blocks
import nodes

class CodeGenerator:

    def __init__(self, program):
        self.program = program
        self.symbol_table = {"one":"\tDAT\t1"}
        self.blocks = []
        self.has_string_print = False
        self.calling_blocks = 0

    def generate(self):
        for statement in self.program:
            self.generate_statement(statement)

        output = \
            "\tBRA\tp_start\n" \
            + self.generate_data_table() \
            + "{instruction_callbacks}" \
            + "p_start\tLDA\t0\n"
        
        callback_table = {}
        for block in self.blocks:
            if isinstance(block, code_blocks.IntegerPrint):
                output += block.compile()
            elif isinstance(block, code_blocks.StringPrint):
                callback_no = len(callback_table)
                callback_id = f"cb{callback_no}"
                n = output.count("\n")
                callback_table[callback_id] = f'\tBRA\t{n+self.calling_blocks+block.code_lines}'
                output += block.compile(f"{callback_id}")

        output += "\tHLT\n"

        if self.has_string_print:
            output += code_blocks.StringPrintRoutine.compile()

        return output.format(instruction_callbacks=self.generate_callback_table(callback_table))
    
    def generate_statement(self, statement):
        if not hasattr(statement, "child"):
            return
        
        if isinstance(statement, nodes.PrintI):
            self.generate_print_i(statement.child)
        if isinstance(statement, nodes.PrintC):
            self.generate_print_s(statement.child)

        self.generate_statement(statement.child)

    def generate_data_table(self):
        data_table = ""
        for k in self.symbol_table.keys():
            data_table += f"{k}{self.symbol_table[k]}\n"
        return data_table
    
    def generate_callback_table(self, callback_table):
        c_table = ""
        for k in callback_table.keys():
            c_table += f"{k}{callback_table[k]}\n"
        return c_table
        
    def get_symbol(self, value):
        symbol_no = len(self.symbol_table)
        symbol_key = f'id{symbol_no}'
        self.symbol_table[symbol_key] = value
        return (symbol_key, symbol_no)

    def check_symbol_table(self, value):
        for k in self.symbol_table.keys():
            if self.symbol_table[k] == value:
                return k
        return False

    def generate_print_i(self, statement):
        value = statement.child
        symbol, symbol_no = self.get_symbol(f"\tDAT\t{value}")
        self.blocks.append(code_blocks.IntegerPrint(symbol))

    def generate_print_s(self, statement):
        self.has_string_print = True
        self.calling_blocks += 1
        value = list(statement.child + "\0")
        first_char = ord(value.pop(0))
        symbol, symbol_no = self.get_symbol(f"\tDAT     {first_char}") # 5 spaces here because for some reason a \t breaks??????
        for char in value:
            self.get_symbol(f"\tDAT\t{ord(char)}")
        inst_symbol, _ = self.get_symbol(f"\tLDA\t{symbol_no+1}")
        self.blocks.append(code_blocks.StringPrint(inst_symbol))

    def generate_print_c_string(self, statement):
        return
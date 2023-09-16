class IntegerPrint:
    def __init__(self, data_id):
        self.data_id = data_id
    def compile(self):
        return f"\tLDA\t{self.data_id}\n\tout\n"
    
class StringPrint:
    def __init__(self, calling_inst_id):
        self.calling_inst_id = calling_inst_id
        self.code_lines = 5
    def compile(self, return_inst_id):
        return f"\tLDA\t{self.calling_inst_id}\n\tSTA\tsp\n\tLDA\t{return_inst_id}\n\tSTA\tsp_end\n\tBRA\tsp\n"
    
class StringPrintRoutine:
    @staticmethod
    def compile():
        return "sp\tLDA\t0\n\tBRZ\tsp_end\n\tOTC\n\tLDA\tsp\n\tADD\tone\n\tSTA\tsp\n\tBRA\tsp\nsp_end\tLDA\t0\n"
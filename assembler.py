#assembler
def assemble(file_name):
    CAL_OPS = {
        "add": "10000000",
        "sub": "10000001",
        "and": "10000010",
        "nand": "10000011",
        "or": "10000100",
        "nor": "10000101",
    }
    JMP_OPS = {
        "nvr": "11000000",
        "gtz": "11000001",
        "gez": "11000010",
        "isz": "11000011",
        "lez": "11000100",
        "ltz": "11000101",
        "noz": "11000110",
        "all": "11000111",
    }
    instruction_set = []
    with open(file_name) as f:
        lines = f.readlines()
    for line in lines:
        line = line.split(';')[0].strip()
        if not line or line.startswith(";"):
            continue
        inst = line.split()
        bin = ''

        if inst[0] == "imm":
            if not (0 <= int(inst[1]) < 64):
                raise ValueError("Immediate out of range (0–63)")
            bin = f"00{int(inst[1]):06b}"

        elif inst[0] == "mov":
            reg_a = f"{int(inst[1][-1]):03b}" if inst[1] != "out" else '111'
            reg_b = f"{int(inst[2][-1]):03b}" if inst[2] != "out" else '111'
            bin += "01"+reg_a+reg_b

        elif inst[0] == "cal":
            bin = CAL_OPS[inst[1]] 

        elif inst[0] == "jmp":
            bin = JMP_OPS[inst[1]]

        else:
            raise ValueError(f"Unknown instruction: {inst}")
        instruction_set.append(bin)
    return instruction_set
    

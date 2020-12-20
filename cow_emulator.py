
cmds = {"moo": "end",
        "mOo": "mp-",
        "moO": "mp+",
        "mOO": "mex",  # execute memory
        "Moo": "prs",  # print ascii from mem, or read ascii
        "MOo": "mv-",
        "MoO": "mv+",
        "MOO": "for",
        "OOO": "zer",
        "MMM": "reg",  # mem -> reg, or reg->mem + clear
        "OOM": "prn",  # print number from mem
        "oom": "inp"}  # read an int

order = ["moo" ,"mOo" ,"moO" ,"mOO" ,"Moo" ,"MOo" ,"MoO" ,"MOO" ,"OOO" ,"MMM" ,"OOM" ,"oom"]

def translate_from(program: str):
    program = program.replace(' ', '')
    program = program.replace('\n', '')
    prog_list = []
    i = 0
    while i < len(program):
        cmd = program[i: i + 3]
        prog_list.append(cmds[cmd])
        i += 3
    return prog_list

def translate_to(prog):
    reverse = {}
    for k, v in cmds.items():
        reverse[v] = k
    moo = []
    for cmd in prog:
        moo.append(reverse[cmd])
    return " ".join(moo)


class Memory:
    def __init__(self):
        self.mp = 0
        self.values = {}

    def inc(self):
        if self.mp in self.values:
            self.values[self.mp] += 1
        else:
            self.values[self.mp] = 1

    def dec(self):
        if self.mp in self.values:
            self.values[self.mp] -= 1
        else:
            self.values[self.mp] = -1

    def left(self):
        self.mp -= 1

    def right(self):
        self.mp += 1

    def get(self):
        if self.mp in self.values:
            return self.values[self.mp]
        else:
            return 0

    def set(self, value):
        self.values[self.mp] = value

    def __str__(self):
        row0 = []
        for i in range(self.mp - 10, self.mp + 11):
            val = 0
            if i in self.values:
                val = self.values[i]
            s0 = str(val)
            s1 = str(i)
            if i == self.mp:
                s1 = "*" + s1 + "*"
            row0.append(s1 + ":" + s0)
        return "|".join(row0)


def run(prog):
    print("start")
    steps = 0
    reg = None
    pp = 0
    mem = Memory()
    while pp < len(prog) and steps < 10000:
        cmd = prog[pp]
        if cmd == "mex":
            cmd = cmds[order[mem.get()]]

        if cmd == "end":
            pp -= 1
            level = 1
            while level > 0:
                pp -= 1
                if prog[pp] == "for":
                    level -= 1
                elif prog[pp] == "end":
                    level += 1
            pp -= 1
        elif cmd == "mp-":
            mem.dec()
        elif cmd == "mp+":
            mem.right()
        elif cmd == "prs":
            print(chr(mem.get()))
        elif cmd == "mv-":
            mem.dec()
        elif cmd == "mv+":
            mem.inc()
        elif cmd == "for" and mem.get() == 0:
            pp += 1
            level = 1
            while level > 0:
                pp += 1
                if prog[pp] == "for":
                    level += 1
                elif prog[pp] == "end":
                    level -= 1
        elif cmd == "for" and mem.get() != 0:
            pass
        elif cmd == "zer":
            mem.set(0)
        elif cmd == "reg" and reg is None:
            reg = mem.get()
        elif cmd == "reg" and reg is not None:
            mem.set(reg)
            reg = None
        elif cmd == "prn":
            print(mem.get())
        else:
            print(cmd)
            raise
        pp += 1
        steps += 1  # break from infinite loops
    print(steps)
    print("end")
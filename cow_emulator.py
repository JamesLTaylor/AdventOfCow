
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
        self.values = {}

    def inc(self, mp):
        if mp in self.values:
            self.values[mp] += 1
        else:
            self.values[mp] = 1

    def dec(self, mp):
        if mp in self.values:
            self.values[mp] -= 1
        else:
            self.values[mp] = -1

    def get(self, mp):
        if mp in self.values:
            return self.values[mp]
        else:
            return 0

    def set(self, mp, value):
        self.values[mp] = value

    def __str__(self):
        return str(self.values)

def run(prog):
    print("start")
    steps = 0
    reg = None
    mp = 0
    pp = 0
    mem = Memory()
    while pp < len(prog) and steps < 10000:
        cmd = prog[pp]
        if cmd == "mex":
            cmd = cmds[order[mem.get(mp)]]

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
            mp -= 1
        elif cmd == "mp+":
            mp += 1
        elif cmd == "prs":
            print(chr(mem.get(mp)))
        elif cmd == "mv-":
            mem.dec(mp)
        elif cmd == "mv+":
            mem.inc(mp)
        elif cmd == "for" and mem.get(mp) == 0:
            pp += 1
            level = 1
            while level > 0:
                pp += 1
                if prog[pp] == "for":
                    level += 1
                elif prog[pp] == "end":
                    level -= 1
        elif cmd == "for" and mem.get(mp) != 0:
            pass
        elif cmd == "zer":
            mem.set(mp, 0)
        elif cmd == "reg" and reg is None:
            reg = mem.get(mp)
        elif cmd == "reg" and reg is not None:
            mem.set(mp, reg)
            reg = None
        elif cmd == "prn":
            print(mem.get(mp))
        else:
            print(cmd)
            raise
        pp += 1
        steps += 1  # break from infinite loops
    print(steps)
    print("end")
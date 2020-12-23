from typing import List

command_lookup = {"moo": "end",
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

command_order = ["moo", "mOo", "moO", "mOO", "Moo", "MOo", "MoO", "MOO", "OOO", "MMM", "OOM", "oom"]


def get_reverse_commands():
    reverse = {}
    for k, v in command_lookup.items():
        reverse[v] = k
    reverse["dbg"] = ""
    reverse["brk"] = ""
    return reverse


class Program:
    """
    Based on https://github.com/BigZaphod/COW/blob/master/source/cow.cpp
    """
    def __init__(self, commands, mem, stop, debug):
        self.pp = 0
        self.prog = commands
        self.mem = mem
        self.stop = stop
        self.debug = debug

    def run(self):
        steps = 0
        reg = None
        while self.pp < len(self.prog) and steps < self.stop:
            cmd = self.prog[self.pp]
            if cmd == "mex":
                cmd = command_lookup[command_order[self.mem.get()]]

            if cmd == "end":
                self.pp -= 1
                level = 1
                while level > 0:
                    self.pp -= 1
                    if self.prog[self.pp] == "for":
                        level -= 1
                    elif self.prog[self.pp] == "end":
                        level += 1
                self.pp -= 1
            elif cmd == "mp-":
                self.mem.left()
            elif cmd == "mp+":
                self.mem.right()
            elif cmd == "prs":
                print(chr(self.mem.get()))
            elif cmd == "mv-":
                self.mem.dec()
            elif cmd == "mv+":
                self.mem.inc()
            elif cmd == "for" and self.mem.get() == 0:
                self.pp += 1
                level = 1
                while level > 0:
                    self.pp += 1
                    if self.prog[self.pp] == "for":
                        level += 1
                    elif self.prog[self.pp] == "end":
                        level -= 1
                        # this is to handle the interleaved for-end so that a 'for' immediately before an
                        # 'end' is neutralized.
                        if self.prog[self.pp - 1] == "for":
                            level -= 1
            elif cmd == "for" and self.mem.get() != 0:
                pass
            elif cmd == "zer":
                self.mem.set(0)
            elif cmd == "reg" and reg is None:
                reg = self.mem.get()
            elif cmd == "reg" and reg is not None:
                self.mem.set(reg)
                reg = None
            elif cmd == "prn":
                print(self.mem.get())
            elif cmd == "dbg": # a debug print that can be toggled and will not be translated to cow
                if self.debug:
                    print(self.mem.get())
            elif cmd == "brk": # a place to put a breakpoint
                variable_that_exists_for_a_breakpoint = 1
            else:
                print(cmd)
                raise
            self.pp += 1
            steps += 1  # break from infinite loops
        if steps == self.stop:
            print(f"Program force exited after {steps} steps. Check for infinite loops or increase maximum steps.")
        print("end")

    def __str__(self):
        row0 = []
        for i in range(self.pp - 10, self.pp + 11):
            if i < 0:
                continue
            if i >= len(self.prog):
                continue

            val = 0
            s0 = self.prog[i]
            if i == self.pp:
                s0 = "|" + s0 + "|"
            row0.append(s0)
        return " ".join(row0)


class Memory:
    def __init__(self, mem_init=None):
        self.values = {}
        self.mp = 0
        if mem_init is not None:
            for i in range(len(mem_init)):
                self.values[i] = mem_init[i]
        self.mp = len(mem_init) - 1


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
            if i == self.mp:
                s0 = "*" + s0 + "*"
            row0.append(s0)
        return "|".join(row0)


def run(prog, stop, is_in_cow, mem_init, debug):
    if is_in_cow:
        prog = [command_lookup[cmd] for cmd in prog]
    print("start")
    mem = Memory(mem_init)
    program = Program(prog, mem, stop, debug)
    program.run()


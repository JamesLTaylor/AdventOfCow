import unittest

import cow
import cow_emulator

# https://frank-buss.de/cow.html
frank = """OOOMoOMoOMoOMoOMoOMoOMoOMoOMMMmoOMMMMMMmoOMMMMOOMOomOoMoOmoOmoomOo
MMMmoOMMMMMMmoOMMMMOOMOomOoMoOmoOmoomOoMMMmoOMMMMMMmoOMMMMOOMOomOo
MoOmoOmooOOOMoOMoOMoOMoOMoOMoOmOoMMMmoOmoOMMMMOOMOomOoMoOmoOmoomOo
MoomOoMMMmoOMMMmOomOoMMMmoOmoOmoOMMMMOOMOomOoMoOmoOmoomOoMMMmoOMMM
MoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoomOoMMMmoO
MMMMoOMoomOoMMMmoOMMMMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoo
MOoMOoMOoMoo"""

# https://esolangs.org/wiki/COW
fib_wiki = " MoO moO MoO mOo MOO OOM MMM moO moO MMM mOo mOo moO MMM mOo MMM moO moO " \
           "MOO MOo mOo MoO moO moo mOo mOo moo"

# https://bigzaphod.github.io/COW/
fib_main = "MoO moO MoO mOo MOO OOM MMM moO moO MMM mOo mOo moO MMM mOo MMM moO moO " \
           "MOO MOo mOo MoO moO moo mOo mOo moo"

own = "mv+ prn mv+ prn mv+ prn".split(" ")

nest_loop_test = "mv+ mv+ mp+ mv+ for mv- mp- for mv- end mp+ mp- end prn mp- prn".split(" ")

# sets mem0 to 2 and mem1 to 3. Prints 0 if mom0 == mem1 and 1 otherwise
a_equal_b = "mv+ mv+ mp+ mv+ mv+ mv+ " \
            "for mv- mp- mv- mp+ end " \
            "mv+ mp- " \
            "for zer mv+ prn mv- mp+ zer mp- end " \
            "mp+ " \
            "for zer prn end".split(" ")


# cow_emulator.run(own)
# print(cow_emulator.translate_to(nest_loop_test))
# cow_emulator.run(nest_loop_test)
# prog = cow_emulator.translate_from(fib_main)
class Args:
    pass


cow_emulator.run(fib_main, 10000, True)
# cow_emulator.run(own, 10000, False)
# args = Args()
# args.file = "fibonacci.cow"
# args.stop = 10000
# args.format = "cow"
# cow.run(args)


import unittest

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
fib_main = "MoO moO MoO mOo MOO OOM MMM moO moO MMM mOo mOo moO MMM mOo MMM moO moO MOO MOo mOo MoO moO moo mOo mOo moo"

own = "mv+ prn mv+ prn mv+ prn".split(" ")
# add m1 to m2 and put in m3, copy m1 to m4 and m2 to m5 loop  , move m3 to m2 and m2 to m1
own_fib = "mv+ mp+ mv+ " \
          "mp- reg mp+ mp+ mp+ reg mp- mp- reg mp+ mp+ mp+ reg" \
          "".split(" ")

nest_loop_test = "mv+ mv+ mp+ mv+ for mv- mp- for mv- end mp+ mp- end prn mp- prn".split(" ")

"""
a=2, b=3
a-b, 0
a-b, 1
"""
a_equal_b = "mv+ mv+ mp+ mv+ mv+ mv+ " \
            "for mv- mp- mv- mp+ end " \
            "mv+ mp- " \
            "for zer mv+ prn mv- mp+ zer mp- end " \
            "mp+ " \
            "for zer prn end".split(" ")


# cow_emulator.run(own)
print(cow_emulator.translate_to(nest_loop_test))
cow_emulator.run(nest_loop_test)
prog = cow_emulator.translate_from(fib_main)
cow_emulator.run(prog)


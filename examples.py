import cow
import translate

translate.translate("a_equal_b.own")
translate.translate("a_equal_b.cow")
cow.run("a_equal_b.own", "own", 10000)
cow.run("a_equal_b.cow", "cow", 10000)
cow.run("frank.cow", "cow", 10000)
translate.translate("frank.cow")


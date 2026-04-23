from selector import Selection
from comparator import Comparator
from reactiontest import Reaction
from scheduler import Schedule

# testando as coisas

tmpinput = "https://www.worldometers.info/"
#url = input("Cole aqui a url que será monitorada:")
#tmpinput = url
s = Selection(tmpinput)
reaction = Reaction()
comparator = Comparator(s, reaction, 1)
print()
print(comparator)

schedule = Schedule()
schedule.start(comparator)
while True:
    x = input()
    if x != "":
        schedule.stop()
        break

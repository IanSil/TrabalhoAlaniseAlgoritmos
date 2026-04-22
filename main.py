from selector import Selection
from comparator import Comparator
from notifier import Notify
from scheduler import Schedule

# testando as coisas

tmpinput = "https://impostometro.com.br/"
# url = input("Cole aqui a url que será monitorada:")
s = Selection(tmpinput)
notifier = Notify()
comparator = Comparator(s, notifier, 1)
print()
print(comparator)

schedule = Schedule()
schedule.start(comparator)
while True:
    x = input()
    if x != "":
        schedule.stop()
        break

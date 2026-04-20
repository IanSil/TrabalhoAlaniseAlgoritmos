from selector import Selection
from monitor import Monitor
from notifier import Notify

# testando as coisas

tmpinput = "https://impostometro.com.br/"
# url = input("Cole aqui a url que será monitorada:")
s = Selection(tmpinput)
notifier = Notify()
monitor = Monitor(s, notifier, 1)
print()
print(monitor)

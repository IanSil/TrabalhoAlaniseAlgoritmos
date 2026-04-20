from selector import Selection

# testando as coisas
tmpimpt = "https://store.steampowered.com/app/582010/Monster_Hunter_World/"
url = input("Cole aqui a url que será monitorada:")
s = Selection(tmpimpt)

print(s.url)
print(s.xpath)
print(s.conteudo)


print(s)

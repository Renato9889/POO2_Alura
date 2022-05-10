from modelo import Filme
from modelo import Serie
from modelo import Playlist

filme1 = Filme("X-men - dias de um futuro esquecido", 2015,160)

print(filme1)

serie1 = Serie("love victor",2020,2)

print(serie1)

filme1.dar_like()
filme1.dar_like()
filme1.dar_like()

serie1.dar_like()
serie1.dar_like()

print(filme1)

print(serie1)


serie1.nome = "Love, Victor"

print(serie1)

serie2 = Serie("Heartstopper",2022,1)
serie2.dar_like()
serie2.dar_like()
serie2.dar_like()
print(serie2)

filmes_e_series = [filme1,serie2,serie1]

print("LUPOEEEE")
for programa in filmes_e_series:
    print(programa)


print("Playlist")

filme2 = Filme("Vingadores - Guerra Infinita",2018,200)
filme3 = Filme("Interestelar",2013,190)
serie3 = Serie("WandaVision", 2020,1)

serie3.dar_like()
serie3.dar_like()
serie3.dar_like()
serie3.dar_like()
serie3.dar_like()
serie3.dar_like()
filme2.dar_like()
filme3.dar_like()
filme2.dar_like()
filme3.dar_like()
filme2.dar_like()
filme3.dar_like()
filme3.dar_like()

filmes_e_series = [filme1, filme2, filme3, serie1, serie2, serie3]
filmes_favs = Playlist("Favoritos",filmes_e_series)


print("Aqui:")
print("Tamanho:",len(filmes_favs))
for programa in filmes_favs:
    print(programa)

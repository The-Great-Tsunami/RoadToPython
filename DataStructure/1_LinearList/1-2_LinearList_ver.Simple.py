Pokemons = ["Pikachu", "Pairi", "Ggobogi", "Chicorita", "Lizamong"]

print(Pokemons)

Pokemons.append(None)
print(Pokemons)

Pokemons[-1] = "yadoran"
print(Pokemons)

# 3번자리에 "Hitoshi" 삽입
print('# 3번자리에 "Hitoshi" 삽입')

Pokemons.append(None)
print(Pokemons)

Pokemons[-1] = Pokemons[-2]
Pokemons[-2] = None1
print(Pokemons)

Pokemons[-2] = Pokemons[-3]
Pokemons[-3] = None
print(Pokemons)

Pokemons[-3] = Pokemons[-4]
Pokemons[-4] = None
print(Pokemons)

Pokemons[-4] = Pokemons[-5]
Pokemons[-5] = None
print(Pokemons)

Pokemons[-5] = "Hitoshi"
print(Pokemons)

# 4번 원소 삭제
print("# 4번 원소 삭제")

Pokemons[3] = None
print(Pokemons)

Pokemons[3] = Pokemons[4]
Pokemons[4] = None
print(Pokemons)

Pokemons[4] = Pokemons[5]
Pokemons[5] = None
print(Pokemons)

Pokemons[5] = Pokemons[6]
Pokemons[6] = None
print(Pokemons)

del[Pokemons[6]]
print(Pokemons)

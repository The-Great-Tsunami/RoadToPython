pokemons = []

## 데이터 생성

def add_data(pokenmon):

	pokemons.append(None)
	pLen = len(pokemons)
	pokemons[pLen-1] = pokenmon

add_data('Pikachu')
add_data('Pairi')
add_data('Ggobugi')
add_data('Lizamog')
add_data('Yadoran')

print(pokemons)

## 데이터 삽입

#중간데이터 삽입

def insert_data(pokemon, idx_choice):

	if idx_choice < 0 or idx_choice > len(pokemons):

		print("something is wrong")

	else:
		pokemons.append(None)
		pLen = len(pokemons)

		for i in range(pLen-1, idx_choice, -1):
			pokemons[i] = pokemons[i-1]
			pokemons[i-1] = None

		pokemons[idx_choice] = pokemon

insert_data("test", 3)
print(pokemons)

def delete_data(idx_choice):

	if idx_choice < 0 or idx_choice > len(pokemons):

		print("something is wrong")

	else:
		pLen = len(pokemons)
		pokemons[idx_choice] = None

		for i in range(idx_choice, pLen-1):
			pokemons[i] = pokemons[i+1]
			pokemons[i+1] = None

		del [pokemons[-1]]
delete_data(3)
print(pokemons)
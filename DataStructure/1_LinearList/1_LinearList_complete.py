pokemons = []

def add_data(pokenmon):

	pokemons.append(None)
	pLen = len(pokemons)
	pokemons[pLen-1] = pokenmon

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

if __name__ == "__main__":
    while True:
        menu = input("1 -> Append | 2 -> Insert | 3 -> Delete | 4 -> Exit")
        if (menu == '1'):
            data = input("Data --> ")
            add_data(data)
            print(pokemons)
        elif (menu == '2'):
            idx = int(input("Index? --> "))
            data = input("Data --> ")
            insert_data(data, idx)
            print(pokemons)
        elif (menu == '3'):
            idx = int(input("Index? --> "))
            delete_data(idx)
            print(pokemons)
        elif (menu == '4'):
            print(pokemons)
            # exit()
            break
        else:
            print("Choose in menu")
            continue
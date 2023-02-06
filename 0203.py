def poke_find(name, p_hp):
    pokePos = -1
    for i in range(len(theList)):
        pair = theList[i]
        if p_hp >= pair[1]:
            pokePos = i
            break
        if pokePos == -1:
            pokePos = len(theList)

        poke_insert(pokePos, (name, p_hp))


def poke_insert(idx, name):
    if idx < 0 or idx > len(theList):
        print("Out of range!")
        return

    theList.append(None)
    kLen = len(theList)

    for i in range(kLen - 1, idx, -1):
        theList[i] = theList[i - 1]
        theList[i-1] = None

    theList[idx] = name


Pokemons = {'피카츄': 200, '라이츄': 150, '파이리': 90, '꼬부기': 30, '버터풀': 15}
theList = list(Pokemons.items())
P_key = Pokemons.keys()
P_values = Pokemons.values()

print(theList)
if __name__ == "__main__":

    while True:
        pokemon = input("이름 : ")
        hp = int(input("체력 : "))
        poke_find(pokemon, hp)
        print(theList)
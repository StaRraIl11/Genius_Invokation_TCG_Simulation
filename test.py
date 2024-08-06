def createCharacter():
    import random
    characterList = []
    Character = {
        'HP': 20,
        'DEF': 100,
        'ATK': 1,
        'atkELE': '',
        'WS': ''
        }

    j = list(range(1,8,1))
    
    for n in range(1,4):
        
        a = random.sample(j,1)
        i = a[0]
        
        atkELE = i
        j.remove(i)
        b = random.sample(j,3)       

        Character['atkELE'] = atkELE
        Character['WS'] = sorted(b[:])
        characterList.append(Character.copy())
        n += 1        
                
        print(type(Character['HP']))
    

    return characterList

print(createCharacter())

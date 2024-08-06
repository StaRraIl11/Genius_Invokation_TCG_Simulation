def attack(myCharacter, myCharacters ,enemyCharacter, enemyCharacters):
    """进行攻击操作，形参分别是进行攻击的角色序号(数字)，该角色所在的方面的全部角色(列表)，受到攻击的角色序号(数字)，该角色所在的方面的全部角色(列表)"""
    atk = 1 #默认攻击力
    myCharacter -= 1
    enemyCharacter -= 1
    attackCharacter = myCharacters[myCharacter] #进行攻击的角色
    attackedCharacter = enemyCharacters[enemyCharacter] #被攻击的角色
    if attackCharacter['atkELE'] in attackedCharacter['WS']:
        atk *= 2
        #print(atk)
        a = int(attackedCharacter['HP'])
        a -= (atk * (int(attackedCharacter['DEF'])/100))
        attackedCharacter['HP'] = float(a)
        #print(attackedCharacter['HP'])
    else:
        a = int(attackedCharacter['HP'])
        a -= (atk * (int(attackedCharacter['DEF'])/100))
        attackedCharacter['HP'] = float(a)
        #print(attackedCharacter['HP'])

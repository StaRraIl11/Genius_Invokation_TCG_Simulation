import createCharacter
import attack
import random

my_movePoint = random.randint(4 , 8)
enemy_movePoint = random.randint(4 , 8)
myCharacter = createCharacter.createCharacter()
enemyCharacter = createCharacter.createCharacter()
print("我方角色:",myCharacter)
print("对方角色:",enemyCharacter)
print("我方行动点数：", my_movePoint)

attack_MymoveCharacter = int(input("选择我方出战角色(输入数字): "))
while attack_MymoveCharacter > 3:
    print("角色数字不能大于3！")
    attack_MymoveCharacter = int(input("选择我方出战角色(输入数字): "))
print("我方先手")

alive = True

while (my_movePoint != 0 and enemy_movePoint != 0) and alive:
    attackedCharacter = int(input('选择你要攻击的对方角色: '))
    print("我方攻击")
    attack.attack(attack_MymoveCharacter , myCharacter , attackedCharacter , enemyCharacter)
    my_movePoint -= 1
    print("我方行动点数：", my_movePoint , "\n")
    print("对方攻击\n")
    attack.attack(1 , enemyCharacter , 1 , myCharacter)
    enemy_movePoint -= 1

    
    if (myCharacter[attack_MymoveCharacter])['HP'] == 0:
        alive = False

else:
    if enemy_movePoint == 0 and my_movePoint != 0:
        print("本轮结束，我方剩余行动点数：" , my_movePoint)

    elif my_movePoint == 0 and enemy_movePoint != 0:
        print("本轮结束")
        print(enemy_movePoint)
    elif my_movePoint == 0 and enemy_movePoint == 0:
        print("本轮结束!")

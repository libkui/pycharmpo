import random
print("Enter card number:")
x = y = int(input())
print("Card number:", x)
poker_num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
poker_king = ['king', 'queen']
poker_color = ['红桃', '黑桃', '方块', '梅花']
pokers = ['%s%s' % (i, j) for i in poker_color for j in poker_num]+poker_king
while y > 1:
  pokers.extend(['%s%s' % (i, j) for i in poker_color for j in poker_num] + poker_king)
  y -= 1
print('洗牌前：', pokers)

random.shuffle(pokers)
print('洗牌后：', pokers)

player1_list = []
player2_list = []
player3_list = []
k1 = k2 = k3 = 0
while len(pokers) > 0:
  k1 = pokers.pop()
  player1_list.append(k1)
  k2 = pokers.pop()
  player2_list.append(k2)
  k3 = pokers.pop()
  player3_list.append(k3)
print('player1手牌：',player1_list)
print('player2手牌：',player2_list)
print('player3手牌：',player3_list)

num1 = str(player1_list).count("king")
num2 = str(player2_list).count("king")
num3 = str(player3_list).count("king")
if (num1 != 0):
    print('Player1 have king')
if (num2 != 0):
    print('Player2 have king')
if (num3 != 0):
    print('Player3 have king')


def Hua(s):
    if s[:2] == "红桃":
        return 1
    elif s[:2] == "黑桃":
        return 2
    elif s[:2] == "梅花":
        return 3
    elif s[:2] == "方块":
        return 4

def Shu(s):
    if s[2:] == "A":
        return 14
    elif s[2:] == "K":
        return 13
    elif s[2:] == "Q":
        return 12
    elif s[2:] == "J":
        return 11
    else:
        return int(s[2:])

def m1():
    L = player1_list
    l = []
    c1 = s1 = str(L).count("king")
    c2 = s2 = str(L).count("queen")
    while c1 > 0:
        L.remove("king")
        c1 -= 1
    while c2 > 0:
        L.remove("queen")
        c2 -= 1
    L.sort(key=Shu)
    n = 0
    m = 0
    p = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for k in range(13):
        n = m
        while m < int(len(L)) and p[k] in L[m]:
            m = m + 1
        s = L[n:m]
        s.sort(key=Hua)
        l = l+s
    while s1 > 0:
        l.append("king")
        s1 -= 1
    while s2 > 0:
        l.append("queen")
        s2 -= 1
    print(l)

def m2():
    L = player2_list
    l = []
    c1 = s1 = str(L).count("king")
    c2 = s2 = str(L).count("queen")
    while c1 > 0:
        L.remove("king")
        c1 -= 1
    while c2 > 0:
        L.remove("queen")
        c2 -= 1
    L.sort(key=Shu)
    n = 0
    m = 0
    p = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for k in range(13):
        n = m
        while m < int(len(L)) and p[k] in L[m]:
            m = m + 1
        s = L[n:m]
        s.sort(key=Hua)
        l = l+s
    while s1 > 0:
        l.append("king")
        s1 -= 1
    while s2 > 0:
        l.append("queen")
        s2 -= 1
    print(l)

def m3():
    L = player3_list
    l = []
    c1 = s1 = str(L).count("king")
    c2 = s2 = str(L).count("queen")
    while c1 > 0:
        L.remove("king")
        c1 -= 1
    while c2 > 0:
        L.remove("queen")
        c2 -= 1
    L.sort(key=Shu)
    n = 0
    m = 0
    p = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for k in range(13):
        n = m
        while m < int(len(L)) and p[k] in L[m]:
            m = m + 1
        s = L[n:m]
        s.sort(key=Hua)
        l = l+s
    while s1 > 0:
        l.append("king")
        s1 -= 1
    while s2 > 0:
        l.append("queen")
        s2 -= 1
    print(l)

m1()
m2()
m3()




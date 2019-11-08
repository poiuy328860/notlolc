# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:49:39 2019

@author: Notlolc
"""

def Stat(Str, Dex, Int, Luk, Strp, Dexp, Intp, Lukp, Allstatp): #只算屬性，記得加後續
    stat = 0
    if number == 1:
        if class1 == 87:
            print('87234不給我公式嗚嗚嗚嗚')
        else:
            stat = 4*Str*(1 + Strp*0.01 + Allstatp*0.01) + Dex*(1+ Dexp*0.01 + Allstatp*0.01)
    elif number == 2:
        stat = Str*(1 + Strp*0.01 + Allstatp*0.01) + 4*Dex*(1+ Dexp*0.01 + Allstatp*0.01)
    elif number == 3:
        stat = 4*Int*(1 + Intp*0.01 + Allstatp*0.01) + Luk*(1+ Lukp*0.01 + Allstatp*0.01)
    elif number == 4:
        if class1 == 28:
            stat = 4*Luk*(1+ Lukp*0.01 + Allstatp*0.01)+Dex*(1+ Dexp*0.01 + Allstatp*0.01)+Str*(1 + Strp*0.01 + Allstatp*0.01)
        elif class1 == 30:
            stat = 4*Luk*(1+ Lukp*0.01 + Allstatp*0.01)+Dex*(1+ Dexp*0.01 + Allstatp*0.01)+Str*(1 + Strp*0.01 + Allstatp*0.01)
        elif class1 == 31:
            stat = 4*Luk*(1+ Lukp*0.01 + Allstatp*0.01)+Dex*(1+ Dexp*0.01 + Allstatp*0.01)+Str*(1 + Strp*0.01 + Allstatp*0.01)
        else:
            stat = 4*Luk*(1+ Lukp*0.01 + Allstatp*0.01)+Dex*(1+ Dexp*0.01 + Allstatp*0.01)
    elif number == 5:
        if class1 == 35:
            stat = Str*(1 + Strp*0.01 + Allstatp*0.01) + 4*Dex*(1+ Dexp*0.01 + Allstatp*0.01)
        elif class1 == 38:
            stat = Str*(1 + Strp*0.01 + Allstatp*0.01) + 4*Dex*(1+ Dexp*0.01 + Allstatp*0.01)
        elif class1 == 39:
            stat = Str*(1 + Strp*0.01 + Allstatp*0.01) + 4*Dex*(1+ Dexp*0.01 + Allstatp*0.01)
        else:
            stat = 4*Str*(1 + Strp*0.01 + Allstatp*0.01) + Dex*(1+ Dexp*0.01 + Allstatp*0.01)
    return stat;

def Damagestat(stat, Atk, Atkp, Bossp, Final, Weaponstat):  #尚未加爆傷跟無視，記得加上
    damagestat = stat*Atk*(1 + Atkp*0.01)*(1 + Bossp*0.01)*(1 + Final*0.01)*Weaponstat
    return damagestat;

def Bossdamage(damagestat, Ignorep, Critical, Bossdef, P2):
    if Ignorep > 100:
        print('無視不能超過100%')
    elif Ignorep <=100:
        if P2 == 'y':
            if (1 - Bossdef* 0.01 * (1-Ignorep* 0.01))>=0:
                bossdamage = damagestat*(1.35 + Critical * 0.01)*(1 - Bossdef* 0.01 * (1-Ignorep* 0.01))/2
            else:
                bossdamage = 0
        elif P2 == 'Y':
            if (1 - Bossdef* 0.01 * (1-Ignorep* 0.01))>=0:
                bossdamage = damagestat*(1.35 + Critical * 0.01)*(1 - Bossdef* 0.01 * (1-Ignorep* 0.01))/2
            else:
                bossdamage = 0
        else:
            if (1 - Bossdef* 0.01 * (1-Ignorep* 0.01))>=0:
                bossdamage = damagestat*(1.35 + Critical * 0.01)*(1 - Bossdef* 0.01 * (1-Ignorep* 0.01))
            else:
                bossdamage = 0
    return bossdamage;

def Level(Calevel,Bosslevel):
    if Calevel-Bosslevel>=5:
        Levelfinal = 1.2
    elif Calevel-Bosslevel>=0:
        Levelfinal = 1.1 + 0.02*(Calevel-Bosslevel)
    elif Calevel-Bosslevel>= -4:
        Levelfinal = 1.0 + 0.05*(Calevel-Bosslevel+2)
    elif Calevel-Bosslevel>= -40:
        Levelfinal = 0.9 + 0.025*(Calevel-Bosslevel+4)
    else:
        Levelfinal = 0
    return  Levelfinal;

print('請輸入類別 劍:1 弓:2 法:3 賊:4 海:5 捷諾:6')
number = int(input())

print('計算時一律以高武器係數的武器計算')
class1=None
if number == 1:
    print('請輸入職業 英雄:1 聖騎:2 黑騎:3 劍豪:4 神子:5 惡殺:6 凱薩:7 聖魂:8 米哈:9 狂狼:10 惡復:87')
    class1 = int(input())
elif number == 2:
    print('請輸入職業 箭神:11 神射:12 開拓:13 狂豹:14 破風:15 精靈:16')
    class1 = int(input())
elif number == 3:
    print('請輸入職業 火毒:17 冰雷:18 主教:19 陰陽:20 幻獸:21 煉獄:22 烈焰:23 凱內:24 龍魔:25 夜光:26 伊利恩:27')
    class1 = int(input())
elif number == 4:
    print('請輸入職業 神偷:28 夜使:29 影武:30 卡蒂娜:31 暗夜:33 幻影:34')#神偷 影武
    class1 = int(input())
elif number == 5:
    print('請輸入職業 槍神:35 拳霸:36 重砲:37 蒼龍:38 機甲:39 爆拳:40 閃雷:41 隱月:42 亞克:43 天破:44')
    class1 = int(input())    
elif number == 6:
    class1 = 123
else:
    print('爆ㄍㄌㄌㄎ')
    
#parameter=1.34 [1,2,7,8,21]
#parameter=1.2 [6,9,17,18,19,23,26,27]
#parameter=1.49 [3,10]    
#parameter=1.5 [35,37,38,39]
#parameter=1.0 [22,24,25]
#parameter=1.7 [36,40,41,42,43,44]
#parameter=1.25 [4]
#parameter=1.75 [29,33]
#parameter=1.35 [12,14,20]
#parameter=1.34 1.49[5]  
#parameter=1.3 [87,11,13,15,16,28,30,31,34]    
if class1 == 1 or 2 or 7 or 8 or 21:
    Weaponstat = 1.34
elif class1 == 6 or 9 or 17 or 18 or 19 or 23 or 26 or 27:
    Weaponstat = 1.2
elif class1 == 3 or 10:
    Weaponstat = 1.49
elif class1 == 35 or 37 or 38 or 39:
    Weaponstat = 1.5
elif class1 == 22 or 24 or 25:
    Weaponstat = 1.0
elif class1 == 36 or 40 or 41 or 42 or 43 or 44:
    Weaponstat = 1.7
elif class1 == 4:
    Weaponstat = 1.25
elif class1 == 29 or 33:
    Weaponstat = 1.75
elif class1 == 12 or 14 or 20:
    Weaponstat = 1.35
elif class1 == 5:
    Weaponstat = (1.34+1.49)/2
elif class1 == 123:
    Weaponstat = 1.3125
else:
    Weaponstat = 1.3
    
Str = 0 
Dex = 0 
Int = 0 
Luk = 0 
Strp = 0 
Dexp = 0 
Intp = 0 
Lukp = 0 
Allstatp = 0

if number == 1:
    if class1 == 87:
        print('87234不給我公式嗚嗚嗚嗚')
    else:
        print('請輸入職業各項數值 無則寫0 不用打%進輸入欄位')
        print('請輸入原始Str值')
        Str = int(input())
        print('請輸入原始Dex值')
        Dex = int(input())
        print('請輸入Str%')
        Strp = int(input())
        print('請輸入Dex%')
        Dexp = int(input())
        print('請輸入Allstat%')
        Allstatp = int(input())
        print('請輸入ATK值')
        Atk = int(input())
        print('請輸入ATK%')
        Atkp = int(input())            
        print('請輸入B+總')
        Bossp = int(input())
        print('請輸入無視%')
        Ignorep = int(input())
        print('請輸入終傷%')
        Final = int(input()) 
        print('請輸入爆傷%')
        Critical = int(input())
elif number == 2:
    print('請輸入職業各項數值 無則寫0 不用打%進輸入欄位')
    print('請輸入原始Str值')
    Str = int(input())
    print('請輸入原始Dex值')
    Dex = int(input())
    print('請輸入Str%')            
    Strp = int(input())
    print('請輸入Dex%')
    Dexp = int(input())
    print('請輸入Allstat%')
    Allstatp = int(input())
    print('請輸入ATK值')
    Atk = int(input())
    print('請輸入ATK%')
    Atkp = int(input())        
    print('請輸入B+總')
    Bossp = int(input())
    print('請輸入無視%')
    Ignorep = int(input())
    print('請輸入終傷%')
    Final = int(input())             
    print('請輸入爆傷%')
    Critical = int(input())   
elif number == 3:
    print('請輸入職業各項數值 無則寫0 不用打%進輸入欄位')
    print('請輸入原始Int值')
    Int = int(input())
    print('請輸入原始Luk值')
    Luk = int(input())
    print('請輸入Int%')
    Intp = int(input())
    print('請輸入Luk%')
    Lukp = int(input())
    print('請輸入Allstat%')
    Allstatp = int(input())
    print('請輸入ATK值')
    Atk = int(input())
    print('請輸入ATK%')
    Atkp = int(input())
    print('請輸入B+總')
    Bossp = int(input())
    print('請輸入無視%')
    Ignorep = int(input())
    print('請輸入終傷%')
    Final = int(input())                        
    print('請輸入爆傷%')
    Critical = int(input())
elif number == 4:
    if class1 == 28:
        print('請輸入職業各項數值 無則寫0 不用打%進輸入欄位')
        print('請輸入原始Str值')
        Str = int(input())
        print('請輸入原始Dex值')
        Dex = int(input())
        print('請輸入原始Luk值')
        Luk = int(input())
        print('請輸入Str%')
        Strp = int(input())
        print('請輸入Dex%')
        Dexp = int(input())
        print('請輸入Luk%')
        Lukp = int(input())
        print('請輸入Allstat%')
        Allstatp = int(input())
        print('請輸入ATK值')
        Atk = int(input())
        print('請輸入ATK%')
        Atkp = int(input())
        print('請輸入B+總')
        Bossp = int(input())
        print('請輸入無視%')
        Ignorep = int(input())
        print('請輸入終傷%')
        Final = int(input())                        
        print('請輸入爆傷%')
        Critical = int(input())
    elif class1 == 30:
        print('請輸入職業各項數值 無則寫0 不用打%進輸入欄位')
        print('請輸入原始Str值')
        Str = int(input())
        print('請輸入原始Dex值')
        Dex = int(input())
        print('請輸入原始Luk值')
        Luk = int(input())
        print('請輸入Str%')
        Strp = int(input())
        print('請輸入Dex%')
        Dexp = int(input())
        print('請輸入Luk%')
        Lukp = int(input())
        print('請輸入Allstat%')
        Allstatp = int(input())
        print('請輸入ATK值')
        Atk = int(input())
        print('請輸入ATK%')
        Atkp = int(input())      
        print('請輸入B+總')
        Bossp = int(input())
        print('請輸入無視%')
        Ignorep = int(input())
        print('請輸入終傷%')
        Final = int(input())                     
        print('請輸入爆傷%')
        Critical = int(input())   
    else:
        print('請輸入職業各項數值 無則寫0 不用打%進輸入欄位')
        print('請輸入原始Dex值')
        Dex = int(input())
        print('請輸入原始Luk值')
        Luk = int(input())
        print('請輸入Dex%')
        Dexp = int(input())
        print('請輸入Luk%')
        Lukp = int(input())
        print('請輸入Allstat%')
        Allstatp = int(input())
        print('請輸入ATK值')
        Atk = int(input())
        print('請輸入ATK%')
        Atkp = int(input())
        print('請輸入B+總')
        Bossp = int(input())
        print('請輸入無視%')
        Ignorep = int(input())
        print('請輸入終傷%')
        Final = int(input())               
        print('請輸入爆傷%')
        Critical = int(input())         
elif number == 5:
    if class1 == 35:
        print('請輸入職業各項數值 無則寫0 不用打%進輸入欄位')
        print('請輸入原始Str值')
        Str = int(input())
        print('請輸入原始Dex值')
        Dex = int(input())
        print('請輸入Str%')
        Strp = int(input())
        print('請輸入Dex%')
        Dexp = int(input())
        print('請輸入Allstat%')
        Allstatp = int(input())
        print('請輸入ATK值')
        Atk = int(input())
        print('請輸入ATK%')
        Atkp = int(input())
        print('請輸入B+總')
        Bossp = int(input())
        print('請輸入無視%')
        Ignorep = int(input())
        print('請輸入終傷%')
        Final = int(input())                        
        print('請輸入爆傷%')
        Critical = int(input())
    elif class1 == 38:
        print('請輸入職業各項數值 無則寫0 不用打%進輸入欄位')
        print('請輸入原始Str值')
        Str = int(input())
        print('請輸入原始Dex值')
        Dex = int(input())
        print('請輸入Str%')
        Strp = int(input())
        print('請輸入Dex%')
        Dexp = int(input())
        print('請輸入Allstat%')
        Allstatp = int(input())
        print('請輸入ATK值')
        Atk = int(input())
        print('請輸入ATK%')
        Atkp = int(input())
        print('請輸入B+總')
        Bossp = int(input())
        print('請輸入無視%')
        Ignorep = int(input())
        print('請輸入終傷%')
        Final = int(input())              
        print('請輸入爆傷%')
        Critical = int(input())
    elif class1 == 39:
        print('請輸入職業各項數值 無則寫0 不用打%進輸入欄位')
        print('請輸入原始Str值')
        Str = int(input())
        print('請輸入原始Dex值')
        Dex = int(input())
        print('請輸入Str%')
        Strp = int(input())
        print('請輸入Dex%')
        Dexp = int(input())
        print('請輸入Allstat%')
        Allstatp = int(input())
        print('請輸入ATK值')
        Atk = int(input())
        print('請輸入ATK%')
        Atkp = int(input())
        print('請輸入B+總')
        Bossp = int(input())
        print('請輸入無視%')
        Ignorep = int(input())
        print('請輸入終傷%')
        Final = int(input())   
        print('請輸入爆傷%')
        Critical = int(input())            
    else:
        print('請輸入職業各項數值 無則寫0 不用打%進輸入欄位')
        print('請輸入原始Str值')
        Str = int(input())
        print('請輸入原始Dex值')
        Dex = int(input())
        print('請輸入Str%')
        Strp = int(input())
        print('請輸入Dex%')
        Dexp = int(input())
        print('請輸入Allstat%')
        Allstatp = int(input())
        print('請輸入ATK值')
        Atk = int(input())
        print('請輸入ATK%')
        Atkp = int(input())
        print('請輸入B+總')
        Bossp = int(input())
        print('請輸入無視%')
        Ignorep = int(input())
        print('請輸入終傷%')
        Final = int(input())
        print('請輸入爆傷%')
        Critical = int(input())
        

stat = Stat(Str, Dex, Int, Luk, Strp, Dexp, Intp, Lukp, Allstatp)
damagestat = Damagestat(stat, Atk, Atkp, Bossp, Final, Weaponstat)
print('你打王表攻為:')
print(damagestat,'-' ,damagestat)

print('是否要計算你打王100%的傷害(Y/N)')
x1 = input()

if x1 == 'y':
    print('你打的王防禦為多少')
    Bossdef = int(input())
    print('你打的王有沒有P2屬性 (Y/N)')
    P2 = input()
elif x1 == 'Y':
    print('你打的王防禦為多少')
    Bossdef = int(input())
    print('你打的王有沒有P2屬性 (Y/N)')
    P2 = input()

bossdamage = Bossdamage(damagestat, Ignorep, Critical, Bossdef, P2)
print('你打王 普攻的傷害為')
print(bossdamage)

print('是否要計算等差增減傷(Y/N)')
x2 = input()

if x2 == 'y':
    print('boss等級為多少')
    Bosslevel = float(input())
    print('你的角色等級為多少')
    Calevel = float(input())  
    level = Level(Calevel,Bosslevel)
    print('最終普攻傷害為')
    print(bossdamage * level)
elif x2 == 'Y':
    print('boss等級為多少')
    Bosslevel = float(input())
    print('你的角色等級為多少')
    Calevel = float(input()) 
    level = Level(Calevel,Bosslevel)
    print('最終普攻傷害為')
    print(bossdamage * level)
else:
    print('野野野野野')



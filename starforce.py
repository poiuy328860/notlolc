import msvcrt
import numpy as np
import random as rm
import pandas as pd


#計算金額
x = input('要保護嗎，不保護可能會炸裝 (Y/N):')
if x == 'Y':
    money = 50
elif x == 'y':
    money = 50
else:
    money = 9
    
t = int(input('重複試驗幾次:'))
#星數種類
states15 = ["15","16","17","18","19","20"]
states20 = ["20","21","22","23"]                                     
#    elif start =='23':    
        i = i+1

#星力轉移矩陣
Matrix_trans15 = np.array([[0.7,0.3,0,0,0,0],[0.7,0,0.3,0,0,0],[0,0.7,0,0.3,0,0],[0,0,0.7,0,0.3,0],[0,0,0,0.7,0,0.3],[0,0,0,0,0,1]])
Matrix_trans20 = np.array([[0.7,0.3,0,0],[0.7,0,0.3,0],[0,0.97,0,0.03],[0,0,0,1]])
Matrix_trans15_2 = np.array([[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0.1],[0,0,0,0,0,1]])
#星力轉移矩陣代表意義
transnames15 = [['1515','1516','1517','1518','1519','1520'],['1615','1616','1617','1618','1619','1620'],['1715','1716','1717','1718','1719','1720'],['1815','1816','1817','1818','1819','1820'],['1915','1916','1917','1918','1919','1920'],['2015','2016','2017','2018','2019','2020']]
transnames20 = [['2020','2021','2022','2023'],['2120','2121','2122','2123'],['2220','2221','2222','2223'],['2320','2321','2322','2323']]
i=0
totalmoney = 0
totalmoneylist = []
timeslist = []

start = str(input('從幾星開始:'))
startlist = [start]
failcount = 0
while i != t:
    if failcount >=2:
        if start =='20':
            start ='21'
            startlist.append('21')
            totalmoney = totalmoney + 9 
            failcount = 0            
        elif start =='17':
            start ='18'
            startlist.append('18')
            totalmoney = totalmoney + 9 
            failcount = 0
        elif start =='16':
            start ='17'
            startlist.append('17')
            totalmoney = totalmoney + 9     
            failcount = 0
        elif start =='15':
            start ='16'
            startlist.append('16')
            totalmoney = totalmoney + 9      
            failcount = 0    
    elif start =='15':
        change = np.random.choice(transnames15[0],replace=True,p=Matrix_trans15[0])
        if change =='1515':
            start = '15'
            startlist.append('15')
            totalmoney = totalmoney + money
        elif change =='1516':
            start = '16'
            startlist.append('16')
            totalmoney = totalmoney + money
            failcount = 0
    elif start =='16':
        change = np.random.choice(transnames15[1],replace=True,p=Matrix_trans15[1])
        if change =='1615':
            start = '15'
            startlist.append('15')
            totalmoney = totalmoney + money
        elif change =='1617':
            start = '17'
            startlist.append('17')
            totalmoney = totalmoney + money
            failcount = 0
    elif start =='17':
        change = np.random.choice(transnames15[2],replace=True,p=Matrix_trans15[2])
        if change =='1716':
            start ='16'
            startlist.append('16')
            totalmoney = totalmoney + money
            failcount = failcount + 1
        elif change =='1718':
            start ='18'
            startlist.append('18')
            totalmoney = totalmoney + money
            failcount = 0
    elif start =='18':
        change = np.random.choice(transnames15[3],replace=True,p=Matrix_trans15[3])
        if change =='1817':
            start ='17'
            startlist.append('17')
            totalmoney = totalmoney + money
            failcount = failcount + 1
        elif change =='1819':
            start ='19'
            startlist.append('19')
            totalmoney = totalmoney + money
            failcount = 0
    elif start =='19':
        change = np.random.choice(transnames15[4],replace=True,p=Matrix_trans15[4])
        if change =='1918':
            start ='18'
            startlist.append('18')
            totalmoney = totalmoney + money
            failcount = failcount + 1
        elif change =='1920':
            start ='20'
            startlist.append('20')
            totalmoney = totalmoney + money
            failcount = 0
    elif start =='20':
        change = np.random.choice(transnames20[0],replace=True,p=Matrix_trans20[0])
        if change =='2020':
            start ='20'
            startlist.append('20')
            totalmoney = totalmoney + money
        elif change =='2021':
            start ='21'
            startlist.append('21')
            totalmoney = totalmoney + money
            failcount = 0
    elif start =='21':
        change = np.random.choice(transnames20[1],replace=True,p=Matrix_trans20[1])
        if change =='2120':
            start ='20'
            startlist.append('20')
            totalmoney = totalmoney + money
            failcount = failcount + 1
        elif change =='2122':
            start ='22'
            startlist.append('22')
            totalmoney = totalmoney + money
            failcount = 0
#需要23星時，將22區井字號消去       
    elif start =='22':     
#        change = np.random.choice(transnames20[2],replace=True,p=Matrix_trans20[2])
#        if change =='2221':
#            start ='21'
#            startlist.append('21')
#            totalmoney = totalmoney + money
#            failcount = failcount + 1
#        elif change =='2223':
#            start ='23'
#            startlist.append('23')
#            totalmoney = totalmoney + money                                                                               
#    elif start =='23':    
        i = i+1
        totalmoneylist.append(totalmoney)
        timeslist.append(len(startlist))
        totalmoney = 0
        startlist.clear()
        start ='15' #此區更改起始星數
A={'SPENDMONEY':totalmoneylist,'SPENDTIMES':timeslist}
df=pd.DataFrame(A)
df.to_csv('staroutput15.csv')

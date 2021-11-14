#!/usr/bin/env python
# coding: utf-8




from bs4 import BeautifulSoup
import requests
import pandas as pd





# VOLLEY BALL





# Brooklyn College Men’s Volleyball Team 
URL1 = "https://www.brooklyncollegeathletics.com/sports/mens-volleyball/roster/2019"
page1 = requests.get(URL1)
soup1 = BeautifulSoup( page1.content , 'html.parser')





brooklynVolleyMenHeight=[]
brooklynVolleyMenNames=[]
for height in soup1.find_all( class_ = "sidearm-roster-player-height" ):
    try:
        num=height.contents[0].split("'")[0]
        frac=height.contents[0].split("'")[1].replace('"','')
        brooklynVolleyMenHeight.append(float(f'{num}.{frac}'))
    except:
        pass
    
names=soup1.find_all(class_="sidearm-roster-player-name")
for name in names:
    try:
        player_name=name.h3.a.contents
        brooklynVolleyMenNames.append(player_name[0])
    except:
        pass
brooklynVolleyMen=list(zip(brooklynVolleyMenNames,brooklynVolleyMenHeight))

dfBrooklynVolleyMen = pd.DataFrame (brooklynVolleyMen, columns = ['Names','Height']) 
print(dfBrooklynVolleyMen)





# Brooklyn College Women’s Volleyball Team 
URL2 = "https://www.brooklyncollegeathletics.com/sports/womens-volleyball/roster/2019"
page2 = requests.get(URL2)
soup2 = BeautifulSoup( page2.content , 'html.parser')





brooklynVolleyWomenHeight=[]
brooklynVolleyWomenNames=[]
for height in soup2.find_all( class_ = "sidearm-roster-player-height" ):
    try:
        num=height.contents[0].split("'")[0]
        frac=height.contents[0].split("'")[1].replace('"','')
        brooklynVolleyWomenHeight.append(float(f'{num}.{frac}'))
    except:
        pass
    
names=soup2.find_all(class_="sidearm-roster-player-name")
for name in names:
    try:
        player_name=name.h3.a.contents
        brooklynVolleyWomenNames.append(player_name[0])
    except:
        pass
brooklynVolleyWomen=list(zip(brooklynVolleyWomenNames,brooklynVolleyWomenHeight))

dfBrooklynVolleyWomen = pd.DataFrame (brooklynVolleyWomen, columns = ['Names','Height']) 
print(dfBrooklynVolleyWomen)





# Baruch College Men’s Volleyball Team
URL3 = "https://athletics.baruch.cuny.edu/sports/mens-volleyball/roster"
page3 = requests.get(URL3)
soup3 = BeautifulSoup( page3.content , 'html.parser')





baruchVolleyMenHeight=[]
baruchVolleyMenNames=[]
for height in soup3.find_all( class_ = "sidearm-roster-player-height" ):
    try:
        num=height.contents[0].split("'")[0]
        frac=height.contents[0].split("'")[1].replace('"','')
        baruchVolleyMenHeight.append(float(f'{num}.{frac}'))
    except:
        pass
    
names=soup3.find_all(class_="sidearm-roster-player-name")
for name in names:
    try:
        player_name=name.h3.a.contents
        baruchVolleyMenNames.append(player_name[0])
    except:
        pass
baruchVolleyMen=list(zip(baruchVolleyMenNames,baruchVolleyMenHeight))

dfBaruchVolleyMen = pd.DataFrame (baruchVolleyMen, columns = ['Names','Height']) 
print(dfBaruchVolleyMen)





# Baruch College Women’s Volleyball Team 
URL4 = "https://athletics.baruch.cuny.edu/sports/womens-volleyball/roster"
page4 = requests.get(URL4)
soup4 = BeautifulSoup( page4.content , 'html.parser')





baruchVolleyWomenHeight=[]
baruchVolleyWomenNames=[]
for height in soup4.find_all( class_ = "sidearm-roster-player-height" ):
    try:
        num=height.contents[0].split("'")[0]
        frac=height.contents[0].split("'")[1].replace('"','')
        baruchVolleyWomenHeight.append(float(f'{num}.{frac}'))
    except:
        pass
    
names=soup4.find_all(class_="sidearm-roster-player-name")
for name in names:
    try:
        player_name=name.h3.a.contents
        baruchVolleyWomenNames.append(player_name[0])
    except:
        pass
baruchVolleyWomen=list(zip(baruchVolleyWomenNames,baruchVolleyWomenHeight))

dfBaruchVolleyWomen = pd.DataFrame (baruchVolleyWomen, columns = ['Names','Height']) 
print(dfBaruchVolleyWomen)





# York College Men’s Volleyball Team
URL5 = "https://yorkathletics.com/sports/mens-volleyball/roster"
page5 = requests.get(URL5)
soup5 = BeautifulSoup( page5.content , 'html.parser')





yorkVolleyMenHeight=[]
yorkVolleyMenNames=[]
for height in soup5.find_all( class_ = "height" ):
    try:
        num=height.contents[0].split("-")[0]
        frac=height.contents[0].split("-")[1]
        yorkVolleyMenHeight.append(float(f'{num}.{frac}'))
    except:
        pass
    
    
names=soup5.find_all(class_="sidearm-table-player-name")
for name in names:
    try:
        yorkVolleyMenNames.append(name.contents[1].contents[0])
    except:
        pass
yorkVolleyMen=list(zip(yorkVolleyMenNames,yorkVolleyMenHeight))

dfYorkVolleyMen = pd.DataFrame (yorkVolleyMen, columns = ['Names','Height']) 
print(dfYorkVolleyMen)





# John Jay College Women’s Volleyball Team
URL6 = "https://johnjayathletics.com/sports/womens-volleyball/roster"
page6 = requests.get(URL6)
soup6 = BeautifulSoup( page6.content , 'html.parser')





johnjayVolleyWomenHeight=[]
johnjayVolleyWomenNames=[]
for height in soup6.find_all( class_ = "sidearm-roster-player-height" ):
    try:
        num=height.contents[0].split("'")[0]
        frac=height.contents[0].split("'")[1].replace('"','')
        johnjayVolleyWomenHeight.append(float(f'{num}.{frac}'))
    except:
        pass
    
names=soup6.find_all(class_="sidearm-roster-player-name")
for name in names:
    try:
        player_name=name.h3.a.contents
        johnjayVolleyWomenNames.append(player_name[0])
    except:
        pass
johnjayVolleyWomen=list(zip(johnjayVolleyWomenNames,johnjayVolleyWomenHeight))

dfJohnjayVolleyWomen = pd.DataFrame (johnjayVolleyWomen, columns = ['Names','Height']) 
print(dfJohnjayVolleyWomen)





























# Swimming





# Brooklyn College Men’s Volleyball Team 
URL7 = "https://www.brooklyncollegeathletics.com/sports/mens-swimming-and-diving/roster"
page7 = requests.get(URL7)
soup7 = BeautifulSoup( page7.content , 'html.parser')





brooklynSwimmingMenNames=[]
brooklynSwimmingMenHeight=[]

for height in soup7.find_all( class_ = "sidearm-roster-player-height" ):
    try:
        num=height.contents[0].split("'")[0]
        frac=height.contents[0].split("'")[1].replace('"','')
        brooklynSwimmingMenHeight.append(float(f'{num}.{frac}'))
    except:
        pass
    
names=soup7.find_all(class_="sidearm-roster-player-name")
for name in names:
    try:
        player_name=name.h3.a.contents
        brooklynSwimmingMenNames.append(player_name[0])
    except:
        pass
brooklynSwimmingMen=list(zip(brooklynSwimmingMenNames,brooklynSwimmingMenHeight))

dfBrooklynSwimmingMen = pd.DataFrame (brooklynSwimmingMen, columns = ['Names','Height']) 
print(dfBrooklynSwimmingMen)





# Brooklyn College Women’s Swimming Team
URL8 = "https://www.brooklyncollegeathletics.com/sports/womens-swimming-and-diving/roster"
page8 = requests.get(URL8)
soup8 = BeautifulSoup( page8.content , 'html.parser')





brooklynSwimmingWomenNames=[]
brooklynSwimmingWomenHeight=[]

for height in soup8.find_all( class_ = "sidearm-roster-player-height" ):
    try:
        num=height.contents[0].split("'")[0]
        frac=height.contents[0].split("'")[1].replace('"','')
        brooklynSwimmingWomenHeight.append(float(f'{num}.{frac}'))
    except:
        pass
    
names=soup8.find_all(class_="sidearm-roster-player-name")
for name in names:
    try:
        player_name=name.h3.a.contents
        brooklynSwimmingWomenNames.append(player_name[0])
    except:
        pass
brooklynSwimmingWomen=list(zip(brooklynSwimmingWomenNames,brooklynSwimmingWomenHeight))

dfBrooklynSwimmingWomen = pd.DataFrame (brooklynSwimmingWomen, columns = ['Names','Height']) 
print(dfBrooklynSwimmingWomen)





# Baruch College Men’s Swimming Team 
page9 = requests.get("https://athletics.baruch.cuny.edu/sports/mens-swimming-and-diving/roster")
soup9 = BeautifulSoup( page9.content , 'html.parser')





baruchSwimmingMenNames=[]
baruchSwimmingMenHeight=[]

for height in soup9.find_all( class_ = "sidearm-roster-player-height" ):
    try:
        num=height.contents[0].split("'")[0]
        frac=height.contents[0].split("'")[1].replace('"','')
        baruchSwimmingMenHeight.append(float(f'{num}.{frac}'))
    except:
        pass
    
names=soup9.find_all(class_="sidearm-roster-player-name")
for name in names:
    try:
        player_name=name.h3.a.contents
        baruchSwimmingMenNames.append(player_name[0])
    except:
        pass
baruchSwimmingMen=list(zip(baruchSwimmingMenNames,baruchSwimmingMenHeight))

dfBaruchSwimmingMen = pd.DataFrame (baruchSwimmingMen, columns = ['Names','Height']) 
print(dfBaruchSwimmingMen)





# -Baruch College Women’s Swimming Team 
page10 = requests.get("https://athletics.baruch.cuny.edu/sports/womens-swimming-and-diving/roster")
soup10 = BeautifulSoup( page10.content , 'html.parser')





baruchSwimmingWomenNames=[]
baruchSwimmingWomenHeight=[]

for height in soup10.find_all( class_ = "sidearm-roster-player-height" ):
    try:
        num=height.contents[0].split("'")[0]
        frac=height.contents[0].split("'")[1].replace('"','')
        baruchSwimmingWomenHeight.append(float(f'{num}.{frac}'))
    except:
        pass
    
names=soup10.find_all(class_="sidearm-roster-player-name")
for name in names:
    try:
        player_name=name.h3.a.contents
        baruchSwimmingWomenNames.append(player_name[0])
    except:
        pass
baruchSwimmingWomen=list(zip(baruchSwimmingWomenNames,baruchSwimmingWomenHeight))

dfBaruchSwimmingWomen = pd.DataFrame (baruchSwimmingWomen, columns = ['Names','Height']) 
print(dfBaruchSwimmingWomen)





# -York College Men’s Swimming Team 
page11 = requests.get("https://yorkathletics.com/sports/mens-swimming-and-diving/roster")
soup11 = BeautifulSoup( page11.content , 'html.parser')





yorkSwimmingMenHeight=[]
yorkSwimmingMenNames=[]
for height in soup11.find_all( class_ = "height" ):
    try:
        num=height.contents[0].split("-")[0]
        frac=height.contents[0].split("-")[1]
        yorkVolleyMenHeight.append(float(f'{num}.{frac}'))
    except:
        pass
    
    
names=soup11.find_all(class_="sidearm-table-player-name")
for name in names:
    try:
        yorkSwimmingMenNames.append(name.contents[1].contents[0])
    except:
        pass
yorkSwimmingMen=list(zip(yorkSwimmingMenNames,baruchSwimmingMenHeight))

dfYorkSwimmingMen = pd.DataFrame (yorkSwimmingMen, columns = ['Names','Height']) 
print(dfYorkSwimmingMen)





# Queens College Women’s Swimming Team 
page12 = requests.get("https://queensknights.com/sports/womens-swimming-and-diving/roster")
soup12 = BeautifulSoup( page12.content , 'html.parser')





QueensSwimmingWomenHeight=[]
QueensSwimmingWomenNames=[]
for height in soup12.find_all( class_ = "height" ):
    try:
        num=height.contents[0].split("-")[0]
        frac=height.contents[0].split("-")[1]
        QueensSwimmingWomenHeight.append(float(f'{num}.{frac}'))
    except:
        pass
    
    
names=soup12.find_all(class_="sidearm-table-player-name")
for name in names:
    try:
        QueensSwimmingWomenNames.append(name.contents[1].contents[0])
    except:
        pass
QueensSwimmingWomen=list(zip(QueensSwimmingWomenNames,QueensSwimmingWomenHeight))

dfQueensSwimmingWomen = pd.DataFrame (QueensSwimmingWomen, columns = ['Names','Height']) 
print(dfQueensSwimmingWomen)























# Men Volley Ball DF
mensVolleyDfs=[dfBrooklynVolleyMen,dfBaruchVolleyMen,dfYorkVolleyMen]
dfVolleyMen=pd.concat(mensVolleyDfs)
print(dfVolleyMen)





# Women Volley Ball DF
womenVolleyDfs=[dfBrooklynVolleyWomen,dfBaruchVolleyWomen,dfJohnjayVolleyWomen]
dfVolleyWomen=pd.concat(womenVolleyDfs)
print(dfVolleyWomen)





# Mens Swimming DF
mensSwimmingDfs=[dfBrooklynSwimmingMen,dfBaruchSwimmingMen,dfYorkSwimmingMen]
dfSwimmingMen=pd.concat(mensSwimmingDfs)
print(dfSwimmingMen)





# Women Swimming DF
womenSwimmingDfs=[dfBrooklynSwimmingWomen,dfBaruchSwimmingWomen,dfQueensSwimmingWomen]
dfSwimmingWomen=pd.concat(womenSwimmingDfs)
print(dfSwimmingWomen)





# Men Volley Ball Average
dfVolleyMen.mean()





# Women Volley Ball Average
dfVolleyWomen.mean()





# Men Swimming Average
dfSwimmingMen.mean()





# Women Swimming Average
dfSwimmingWomen.mean()





# Top 5 tallest men Volley Ball
dfVolleyMen.nlargest(5, 'Height')





# Top 5 shortest men Volley Ball
dfVolleyMen.nsmallest(5, 'Height')





# Top 5 tallest women Volley Ball
dfVolleyWomen.nlargest(5, 'Height')





# Top 5 shortest women Volley Ball
dfVolleyWomen.nsmallest(5, 'Height')





# Top 5 tallest men Swimmer
dfSwimmingMen.nlargest(5, 'Height')





# Top 5 shortest men Swimmers
dfSwimmingMen.nsmallest(5, 'Height')





# Top 5 tallest women swimmers
dfSwimmingWomen.nlargest(5, 'Height')





# Top 5 shortest women swimmers
dfSwimmingWomen.nsmallest(5, 'Height')


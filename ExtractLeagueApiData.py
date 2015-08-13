import urllib2
import json

PreAPGameIDs = []
PostAPGameIDs = []
PreAPItems = []
PostAPItems = []

key = 'This is secured somewhere no one sees'
urlBase = 'https://na.api.pvp.net/api/lol/na/v2.2/match/'
f1 = open('AP_ITEM_DATASET/5.11/RANKED_SOLO/NA.json', 'r')
f2 = open('AP_ITEM_DATASET/5.14/RANKED_SOLO/NA.json', 'r')
itemText = ['item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6']

for line in f1:
    PreAPGameIDs.append(line)
f1.close()
for line in f2:
    PostAPGameIDs.append(line)
f2.close()

for i in range(1, 5):
    PreAPGameIDs[i] = int(PreAPGameIDs[i].translate(None, ',[] '))
    PostAPGameIDs[i] = int(PostAPGameIDs[i].translate(None, ',[] '))

    url1 = urlBase + str(PreAPGameIDs[i]) + "?api_key=" + key
    url2 = urlBase + str(PostAPGameIDs[i]) + "?api_key=" + key
    print url1, url2
    temp1 = urllib2.urlopen(url1).read()
    temp2 = urllib2.urlopen(url2).read()
    jsonData1 = json.loads(temp1)
    jsonData2 = json.loads(temp2)

    for attrib in jsonData1['participants']:
        for n in range(0, 7):
            PreAPItems.append(attrib['stats'][itemText[n]])

    for attrib in jsonData2['participants']:
        for n in range(0, 7):
            PostAPItems.append(attrib['stats'][itemText[n]])

f1 = open("PreAPItemIDs.txt", 'a')
f2 = open('PostAPItemIDs.txt', 'a')
for x in range(len(PreAPItems)):
    f1.write(str(PreAPItems[x]) + '\n')
    f2.write(str(PostAPItems[x]) + '\n')
    

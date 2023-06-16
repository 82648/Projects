import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

wordnet_lemmatizer = WordNetLemmatizer()


library ={

                "hello": "hello welcome to supermarket",
                "hi": "hi welcome to supermarket",
                "i want to buy some goods": "give your list of goods"

            }


GoodList = {
                "dhal": "Shelf No:1 => Location: right side",
                "samba rice": "Shelf No:2 => Location: right side",
                "naadu rice": "Shelf No:3 => Location: right side",
                "rice": "Shelf No:2 and 3 => Location: right side",
                "green gram": "Shelf No:4 => Location: right side",
                "bean": "Shelf No:5 => Location: right side",
                "cowpea": "Shelf No:6 => Location: right side",
                "soya meat": "Shelf No:7 => Location: right side",
                "chicken": "Shelf No:8 => Location: left side",
                "egg": "Shelf No:9 => Location: left side",
                "fish": "Shelf No:10 => Location: left side",
                "cuttlefish": "Shelf No:11 => Location: left side",
                "prawn": "Shelf No:12 => Location: left side",
                "sugar": "Shelf No:13 => Location: middle",
                "noodle": "Shelf No:14 => Location: middle",
                "salt": "Shelf No:15 => Location: middle",
                "spice": "Shelf No:16 => Location: middle",
                "papadam": "Shelf No:17 => Location: middle",
                "biscuit": "Shelf No:18 => Location: middle",
                "chocolate": "Shelf No:19 => Location: middle",
                "milk": "Shelf No:20 => Location: middle",
                "spinach": "Shelf No:21 => Location: backward side",
                "lettuce": "Shelf No:22 => Location: backward side",
                "silverbeet": "Shelf No:23 => Location: backward side",
                "gotukola": "Shelf No:24 => Location: backward side",
                "cabbage": "Shelf No:25 => Location: backward side",
                "cauliflower": "Shelf No:26 => Location: backward side",
                "broccoli": "Shelf No:27 => Location: backward side",
                "pumpkin": "Shelf No:28 => Location: backward side",
                "cucumber": "Shelf No:29 => Location: backward side",
                "potato": "Shelf No:30 => Location: backward side",
                "sweet potato": "Shelf No:31 => Location: backward side",
                "yam": "Shelf No:32 => Location: backward side",
                "celery": "Shelf No:33 => Location: backward side",
                "asparagus": "Shelf No:34 => Location: backward side",
                "onion": "Shelf No:35 => Location: backward side",
                "garlic": "Shelf No:36 => Location: backward side",
                "shallot": "Shelf No:37 => Location: backward side",
                "apple": "Shelf No:38 => Location: backward right side",
                "pear": "Shelf No:39 => Location: backward right side",
                "orange": "Shelf No:40 => Location: backward right side",
                "grapefruit": "Shelf No:41 => Location: backward right side",
                "mandarin": "Shelf No:42 => Location: backward right side",
                "lime": "Shelf No:43 => Location: backward right side",
                "nectarine": "Shelf No:44 => Location: backward right side",
                "apricot": "Shelf No:45 => Location: backward right side",
                "plum": "Shelf No:46 => Location: backward right side",
                "banana": "Shelf No:47 => Location: backward right side",
                "mango": "Shelf No:48 => Location: backward right side",
                "strawberry": "Shelf No:49 => Location: backward right side",
                "watermelon": "Shelf No:50 => Location: backward right side",
                "tomato": "Shelf No:51 => Location: backward right side",
                "avocado": "Shelf No:52 => Location: backward right side",
                "ice": "Shelf No:53 => Location: front right side",
                "drink": "Shelf No:53 => Location: front right side",
                "yoghurt": "Shelf No:53 => Location: front right side",
                "curd": "Shelf No:53 => Location: front right side",
                "brisling": "Shelf No:57 => Location: backward left side",
                "mushroom": "Shelf No:59 => Location: backward left side",
                "tea leaf": "Shelf No:60 => Location: middle",
                "coconut milk": "Shelf No:61 => Location: middle",
                "soseja": "Shelf No: 70 => Location: left side",

}


ListItem = []

for values in GoodList.keys():
    ListItem.append(values)

#print(ListItem)


def wordtokenze(sentence):
    List = []
    lemmatizer = wordnet_lemmatizer
    sentence = word_tokenize(sentence)

    for word in sentence:
        List.append(lemmatizer.lemmatize(word.replace("_", " ")))

    #print(List)

    list3 = []
    for l1 in List:
        for l2 in ListItem:
            if l2 == l1:
                list3.append(l2)

    #print(list3)
    print("____________Details of Goods____________")
    for v in list3:
        print(v, GoodList[v])

    print(" ")
    print("Thank You__Come again__Bye")


print(" ")
print("___Smart SuperMarket ChatBot___")
print(" ")

specialword1 = "good"
specialword2 = "Good"


while True:

    x = input("Customer : ")

    if(x == "hello" or x == "hi"):
        print("ChatBot:", library[x])
        continue

    if (x =="quit" or x =="exit" or x == "Thank"):
            print("Bye")
            break

    if((specialword1 in x) or (specialword2 in x)):

        print("ChatBot:", "Give your list of goods")
        sentence = input("Customer => my list of goods:")
        print(" ")
        wordtokenze(sentence)
        break
    else:

        print("ChatBot:", "Plz tell how can help you in supermarket ")



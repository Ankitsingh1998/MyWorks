def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

file = open("newfile2.txt", "w")
file.write("My Anime Lists : Big Order Netsuzou Trap Ore ga suki nano wa imouto dakedo imouto ja nai Akikan! Assassins pride Azur Lane Beelzebub-jou no okinimesu mama.Boku no kanojo ga majimesugiru sho-bitch na Glasslip Hacka Doll Ro-Kyu-Bu! Seikon no Qwaser Taboo Tattoo Takunomi")
file.close()
filename = "newfile2.txt"
with open(filename) as f:
    text = f.read()
character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,'*-()!/\_: "


for char in character:
    perc = 100*count_char(text,char)/len(text) 
    print("{0} - {1} - {2}".format(char,count_char(text,char),str(round(perc,2))+"%"))


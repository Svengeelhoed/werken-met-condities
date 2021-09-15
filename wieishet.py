print("Welkom bij het spel: Wie is het! (maar dan met kaas)")
print("Spelregels: Neem een soort kaas in gedachte, en ik zal jouw kaas proberen te raden!")
print("Hier komt de eerste vraag..")


antwoord1 = input("Is de kaas geel? ")
if antwoord1 == "ja": 
    antwoord_a2 : input("zitten er gaten in? ")
else: antwoord_c2 = input("Zitten er blauwe schimmels op?")

if antwoord_a2 == "ja":
    antwoord_a3 : input("Is de kaas belachelijk duur? ")
else: antwoord_a2 = input("Is de kaas zo hard als steen? ")

if antwoord_a3 == "ja":
    antwoord_a4 : input("Jouw kaas is een Emmenthaler!")
if antwoord_a2 == "ja":
    antwoord_b4 : input("Jouw kaas is een Parmigiano Reggiano!")
else: antwoord_b5 = input("Jouw kaas is een Goudse kaas!")


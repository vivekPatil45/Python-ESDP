class  Team:
    def __init__(self,Country_name,nameofPlayer,age,no_of_matches,batting_avg,balling_avg) :
        self.Country_name = Country_name
        self.nameofPlayer = nameofPlayer
        self.age = age
        self.no_of_matches = no_of_matches
        self.batting_avg = batting_avg
        self.balling_avg = balling_avg

    def showInfo(self):
        print(f"{self.Country_name}\t\t{self.nameofPlayer}\t\t{self.age}\t{self.no_of_matches}\t{self.batting_avg}\t\t{self.balling_avg}")


Players = []

print("--------------------------------------------------")
for _ in range(3):
    Country_name = input("Enter The Country Name : ")
    nameofPlayer = input("Enter The Player Name : ")
    age = int(input("Enter The Ege Of Player : "))
    no_of_matches = int(input("Enter The No.Of Matches : "))
    batting_avg = float(input("Enter The Batting Average : "))
    balling_avg = float(input("Enter The Balling Average : "))

    Players.append(Team(Country_name,nameofPlayer,age,no_of_matches,batting_avg,balling_avg))
    print("--------------------------------------------------")



print("CountryName\tPlayerName\tMathes\tAge\tBattingAvg\tBallingAvg\t")  
for obj in Players:
    obj.showInfo()
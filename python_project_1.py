print("Welcome to the World of Games.")

player_name=input("\nKindly enter your ingame name:\n")
player_age=int(input("\nKindly enter your age:\n"))
character_height=int(input("\nKindly enter  ingame Character height in meters:\n"))
Favourite_game=input("\nPlease enter your favourite game:\n")
Current_level=int(input("\nPlease enter your game level\n"))

print("\n\nThank you gamers for your time,Here is the data we collected:")

print("\nYour Player Name is ",player_name,"[class type:",type(player_name),",Memory address:",id(player_name),"]")
print("\nYour Player Age is ",player_age,"[class type:",type(player_age),",Memory address:",id(player_age),"]")
print("\nYour Character Height is ",character_height,"[class type:",type(character_height),",Memory address:",id(character_height),"]")
print("\nYour Favourite game is ",Favourite_game,"[class type:",type(Favourite_game),",Memory address:",id(Favourite_game),"]")
print("\nYour Current level  is ",Current_level,"[class type:",type(Current_level),",Memory address:",id(Current_level),"]")

import datetime
current_year = datetime.datetime.now().year
birth_year = current_year -  player_age               
print("\nYour birth year is approximately:\n ",birth_year)

print("Thank you! for using this Personal Data Collector for Gaming.\n See you in the next game.\n")



#variables = containers for storing the values. 
#The variables will behave as the value it contains.

#string variable
odi_player = "Virat Kohli"
competition = "V/S"
test_player = "Kane Williamson"

cricket=odi_player+" "+competition+" "+test_player
print(cricket)
print(type(cricket))

#integer variable
rank_1 =1
rank_2 =2
rank_1+=1
rank_2+=2
print("virat kohli odi rank is:"+""+str(rank_1))     #Look! here we performed type casting where integer(rank_1) is converted into string for concatenation purpose 
print("kane williamson test rank is:"+""+str(rank_2))
print(type(rank_1))
print(type(rank_2))

#floating variable
WTC_standing_points_1= 3.65
WTC_standing_points_2= 3.40
print("the wtc standings of INDIA is:"+str(WTC_standing_points_1))
print("the wtc standings of NEWZEALAND is:"+str(WTC_standing_points_2))
print(type(WTC_standing_points_1))
print(type(WTC_standing_points_2))

#boolean variable
finals = True
print(finals)
print(type(finals))
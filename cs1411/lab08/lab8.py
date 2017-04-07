#Name:Zachary Carson
#Course:CS 1411
#Date:04/04/2017
#
#
#Problem:
#
#Efficiency = ( ( pts + reb + asts + stl + blk ) -( ( fga –fgm ) + ( fta –ftm ) + turnover ) ) / gp
#1.Find the top 50 players with the best efficiency results and Display those 50 from best to
#worst.
#2.Find and display the Player who played the most minutes
#3.Find and display the player who play the most games
#4.Find and display the Player who scored the most points
#5.Find and display the Player who got the most penalties.
#6.Find and display the Player who made the most free throws.
#Given:
#Efficiency = ( ( pts + reb + asts + stl + blk ) -( ( fga –fgm ) + ( fta –ftm ) + turnover ) ) / gp
#List of players and their stats
#
#Analysis
#Input: player_regular_season.cvs
#Outputs:
#Top 50 players witht he higest Efficiency raiting
#The player with the most minutes
#The player with the most games
#The player with the most points
#The player with the most penalties
#The player with the most free throws
#
#Method/Algorithm:
# playerList:
#Step 1: for line in cvs_file:
#Step 2:    index = 0
#Step 3:    line_list = line.split(',')
#Step 4:    if len(line_list) == 1: continue
#Step 5:    if line_list[0] == "\ufeffilkid": continue
#Step 6:    if line_list[4] == " Jr.": line_list.remove(" Jr."), line_list[3] += " Jr"
#Step 7:    for i in linne_list:
#Step 8:            if i == "NULL": line_list[index] = 0
#Step 9:            index ++
#Step 10:    player_tuple = (line_list[1], line_list[2], line_list[3],int(line_list[6]),
#                        int(line_list[7]),int(line_list[8]),int(line_list[9]),
#                        int(line_list[10]),int(line_list[11]),int(line_list[12]),
#                        int(line_list[13]),int(line_list[15]),int(line_list[15]),
#                        int(line_list[16]),int(line_list[17]),int(line_list[18]),
#                        int(line_list[19]),int(line_list[20]),int(line_list[21]),
#                        int(line_list[22]))
#Step 11:    player_list.append(player_tuple)
#Step 12:return player_list
#
# efficiency(player_list):
#Step 1: for player_tuple in player_list
#Step 2:    efficiency = (((player_tuple[5]+player_tuple[8]+player_tuple[9]+player_tuple[10]+player_tuple[11])
#                        -((player_tuple[14]-player_tuple[15])+
#                        (player_tuple[16]-player_tuple[17])+player_tuple[12]))/
#                        player_tuple[3])
#Step 3:    player = (player_tuple[0],player_tuple[1], player_tuple[2], efficiency)
#Step 4:    players_efficiency.append(player)
#Step 5:players_efficiency = sorted(players_efficiency, key=lambda players:players[3])
#Step 6:palyers_efficiency = players_efficiency[-1:-52:-1]
#Step 7: print("Top 50 players with the best efficiency rating in a single season")
#Step 8:i = 1
#Step 9:print("{}.{} {} {}:\t{}".format(i,palyers_efficiency[i][0],palyers_efficiency[i][1],palyers_efficiency[i][2],palyers_efficiency[i][3]))
#Step 10: if i != 50: goto 9
#
# most_minutes(player_list):
#Step 1: count = 0
#Step 2: for players in player_list:
#Step 3:    if count == 0: most_ft = player_list[0], count +=1, continue
#Step 4:    if most_ft[4] < players[4]: most_ft = players, count +=1, continue
#Step 5:    if most_ft[4] > players [4]: count +=1, continue
#Step 6: print("\nThe player with the most made free throws in a single season is", most_ft[1], most_ft[2], "with a total of", most_ft[17], "free throws in", most_ft[0], ".")
#
# most_games(player_list):
#Step 1: count = 0
#Step 2: for players in player_list:
#Step 3:    if count == 0: most_games = player_list[0], count +=1, continue
#Step 4:    if most_ft[3] < players[3]: most_games = players, count +=1, continue
#Step 5:    if most_ft[3] > players [3]: count +=1, continue
#Step 6: print("\nThe player with the most games played in a single season is", most_gp[1], most_gp[2], "with a total of", most_gp[3], "games in", most_gp[0], ".")
#
# most_points(player_list):
#Step 1: count = 0
#Step 2: for players in player_list:
#Step 3:    if count == 0: most_pt = player_list[0], count +=1, continue
#Step 4:    if most_ft[5] < players[5]: most_pt = players, count +=1, continue
#Step 5:    if most_ft[5] > players [5]: count +=1, continue
#Step 6: print("\nThe player with the most points in a single season is", most_pt[1], most_pt[2], "with a total of", most_pt[5], "pints in", most_pt[0], ".")
#
# most_penalites(player_list):
#Step 1: count = 0
#Step 2: for players in player_list:
#Step 3:    if count == 0: most_pen = player_list[0], count +=1, continue
#Step 4:    if most_ft[13] < players[13]: most_pen = players, count +=1, continue
#Step 5:    if most_ft[13] > players [13]: count +=1, continue
#Step 6: print("\nThe player with the most points in a single season is", most_pt[1], most_pt[2], "with a total of", most_pt[5], "pints in", most_pt[0], ".")
#
# most_ft(player_list):
#Step 1: count = 0
#Step 2: for players in player_list:
#Step 3:    if count == 0: most_ft = player_list[0], count +=1, continue
#Step 4:    if most_ft[17] < players[17]: most_ft = players, count +=1, continue
#Step 5:    if most_ft[17] > players [17]: count +=1, continue
#Step 6: print("\nThe player with the most made free throws in a single season is", most_ft[1], most_ft[2], "with a total of", most_ft[17], "free throws in", most_ft[0], ".")
#
#
#Step 1: player_file = open('player_regular_season.csv', 'r')
#Step 2: player_list = playerList(player_file)
#Step 3: efficiency(player_list)
#Step 4: most_minutes(player_list)
#Step 5: most_games(player_list)
#Step 6: most_points(player_list)
#Step 7: most_penalites(player_list)
#Step 8: most_ft(player_list)
#
#TestCases:
#Input:player_regular_season.cvs_file
#Expected OutPut:
#
# Top 50 players with the best efficiency rating in a single season
# 1.Wilt Chamberlain:1962 50.5875
# 2.Wilt Chamberlain:1965 45.75949367088607
# 3.Wilt Chamberlain:1960 45.58227848101266
# 4.Wilt Chamberlain:1966 45.54320987654321
# 5.Wilt Chamberlain:1963 44.6
# 6.Wilt Chamberlain:1959 43.833333333333336
# 7.Wilt Chamberlain:1967 42.80487804878049
# 8.Kareem Abdul-jabbar:1971 42.592592592592595
# 9.Wilt Chamberlain:1964 41.026315789473685
# 10.Wilt Chamberlain:1964 40.61643835616438
# 11.Oscar Robertson:1961 40.50632911392405
# 12.Elgin Baylor:1960 40.19178082191781
# 13.Wilt Chamberlain:1964 40.17142857142857
# 14.Michael Jordan:1988 39.76543209876543
# 15.Elgin Baylor:1961 39.3125
# 16.Oscar Robertson:1963 39.151898734177216
# 17.Kareem Abdul-jabbar:1972 39.11842105263158
# 18.Kareem Abdul-jabbar:1970 38.8780487804878
# 19.Kareem Abdul-jabbar:1975 38.86585365853659
# 20.Walt Bellamy:1961 37.962025316455694
# 21.Spencer Haywood:1969 37.80952380952381
# 22.Oscar Robertson:1964 37.49333333333333
# 23.Bob Mcadoo:1973 37.432432432432435
# 24.Bob Pettit:1961 37.30769230769231
# 25.Bob Mcadoo:1974 37.30487804878049
# 26.Magic Johnson:1988 37.077922077922075
# 27.Michael Jordan:1989 36.926829268292686
# 28.George Mcginnis:1974 36.848101265822784
# 29.Oscar Robertson:1962 36.8125
# 30.Charles Barkley:1986 36.661764705882355
# 31.Larry Bird:1986 36.58108108108108
# 32.Michael Jordan:1987 36.52439024390244
# 33.Oscar Robertson:1960 36.42253521126761
# 34.Oscar Robertson:1965 36.4078947368421
# 35.Larry Bird:1984 36.2625
# 36.Kareem Abdul-jabbar:1973 36.18518518518518
# 37.Bob Pettit:1960 36.171052631578945
# 38.Julius Erving:1972 36.15492957746479
# 39.Larry Bird:1987 36.06578947368421
# 40.Elgin Baylor:1962 35.975
# 41.Kareem Abdul-jabbar:1974 35.646153846153844
# 42.Bill Russell:1959 35.391891891891895
# 43.Bill Russell:1961 35.38157894736842
# 44.Artis Gilmore:1971 35.333333333333336
# 45.Julius Erving:1975 35.25
# 46.Moses Malone:1981 35.20987654320987
# 47.Oscar Robertson:1966 35.12658227848101
# 48.Moses Malone:1978 35.1219512195122
# 49.Rick Barry:1968 35.114285714285714
# 50.Magic Johnson:1986 35.0875
#
# The player with the most playing time in a single season is Wilt Chamberlain with a total of 3882 minutes in 1961 .
# The player with the most games played in a single season is Chuck Williams with a total of 90 games in 1973 .
# The player with the most points in a single season is Wilt Chamberlain with a total of 4029 pints in 1961 .
# The player with the most penalites in a single season is Darryl Dawkins with a total of 386 penalites in 1983 .
# The player with the most made free throws in a single season is Jerry West with a total of 840 free throws in 1965 .
# #
#Input:N/A
#Expected Output:N/A
#Write a comment about passing Testing results
#Sucessful
#Program:

#Sorts through player_list to find the player with the most made freethrows in a season
def playerList(cvs_file):
    player_list = [] #List that the sorted data of the plaers will be stored
    for line in cvs_file:# Index through each line in cvs_file
        index = 0 # keeps count of loop itteration
        line_list = line.split(',')# Slip data in line by commas
        if len(line_list) == 1 : #Excludes anything that is not valid player information
            continue
        if line_list[0] == "\ufeffilkid": #Excludes header of file
            continue
        if line_list[4] == " Jr.":
            line_list.remove(" Jr.")
            line_list[3] += " Jr"
        for i in line_list: # If data field is NUll, replace memory with 0
            if i == "NULL":
                line_list[index] = 0
            index+=1

        # Apply valid player information into a tuple
        player_tuple = (line_list[1], line_list[2], line_list[3],int(line_list[6]),
                        int(line_list[7]),int(line_list[8]),int(line_list[9]),
                        int(line_list[10]),int(line_list[11]),int(line_list[12]),
                        int(line_list[13]),int(line_list[15]),int(line_list[15]),
                        int(line_list[16]),int(line_list[17]),int(line_list[18]),
                        int(line_list[19]),int(line_list[20]),int(line_list[21]),
                        int(line_list[22]))

        player_list.append(player_tuple) # add this player information to the list of players
    return player_list#Returns a list of players

#Calcuates each players efficiency and sorts them from higest to lowest
def efficiency(player_list):
    players_efficiency = [] # List of player's efficiency raiting
    for player_tuple in player_list:#Goes through every player and claculate efficiency
        # Pulls values from player's information and calculates their efficiency
        efficiency = (((player_tuple[5]+player_tuple[8]+player_tuple[9]+player_tuple[10]+player_tuple[11])
                        -((player_tuple[14]-player_tuple[15])+
                        (player_tuple[16]-player_tuple[17])+player_tuple[12]))/
                        player_tuple[3])
        player = (player_tuple[0],player_tuple[1], player_tuple[2], efficiency)
        players_efficiency.append(player) #Add player and their efficiency raiting to a List

    #Sortes the list of players by efficiency rate
    players_efficiency = sorted(players_efficiency, key=lambda players:players[3])

    #Rearanges the list so the players efficiency is ranked from higest to lowest
    palyers_efficiency = players_efficiency[-1:-52:-1]

    print("Top 50 players with the best efficiency rating in a single season")
    #prints top 50 olayers names, year they played, and their efficiency raiting
    for i in range(1,51):
        print("{}.{} {} {}:\t{}".format(i,palyers_efficiency[i][0],palyers_efficiency[i][1],palyers_efficiency[i][2],palyers_efficiency[i][3]))
        #print(repr(i).rjust(2),repr(palyers_efficiency[i][1]).rjust(3),repr(palyers_efficiency[i][2]).rjust(4),repr(palyers_efficiency[i][0]).rjust(5),repr(palyers_efficiency[i][3]).rjust(5))

#Sorts through player_list to find the player with the most minutes in a season
def most_minutes(player_list):
    count = 0#number of itterations
    most_min = []# Stores all thelemenets of the player it the most minutes in a season
    # Goes throught the list of players in search of the most minutes
    for players in player_list:
        if count == 0:# If  first itteration, assign first player to most_min
            most_min = player_list[0]
            count+=1
            continue
        #If the minutes int most_min is less thant the player of the itteration, they swap positions
        if most_min[4] < players[4]:
            most_min = players
            count+=1
            continue
        #If most_min's player's number of minutes is greater than the itterated player, continue
        elif most_min[4] > players[4]:
            count +=1
            continue

    print("\nThe player with the most playing time in a single season is", most_min[1], most_min[2], "with a total of", most_min[4], "minutes in", most_min[0], ".")

#Sorts through player_list to find the player with the most games in a season
def most_games(player_list):
    count = 0#number of itterations
    most_gp = []# Stores all thelemenets of the player it the most games  in a season
    # Goes throught the list of players in search of the most games played
    for players in player_list:
        if count == 0:# If  first itteration, assign first player to most_gp
            most_gp = player_list[0]
            count+=1
            continue
        #If the minutes int most_gp is less than the player of the itteration, they swap positions
        if most_gp[3] < players[3]:
            most_gp = players
            count+=1
            continue
        #If most_min's player's number of games played is greater than the itterated player, continue
        elif most_gp[3] > players [3]:
            count +=1
            continue

    print("\nThe player with the most games played in a single season is", most_gp[1], most_gp[2], "with a total of", most_gp[3], "games in", most_gp[0], ".")

#Sorts through player_list to find the player with the most points in a season
def most_points(player_list):
    count = 0
    most_pt = []
    for players in player_list:
        if count == 0:
            most_pt = player_list[0]
            count+=1
            continue
        if most_pt[5] < players[5]:
            most_pt = players
            count+=1
            continue
        elif most_pt[5] > players [5]:
            count +=1
            continue

    print("\nThe player with the most points in a single season is", most_pt[1], most_pt[2], "with a total of", most_pt[5], "pints in", most_pt[0], ".")

#Sorts through player_list to find the player with the most penalites in a season
def most_penalites(player_list):
    count = 0
    for players in player_list:
        if count == 0:
            most_pen = player_list[0]
            count+=1
            continue
        if most_pen[13] < players[13]:
            most_pen = players
            count+=1
            continue
        elif most_pen[13] > players [13]:
            count +=1
            continue

    print("\nThe player with the most penalites in a single season is", most_pen[1], most_pen[2], "with a total of", most_pen[13], "penalites in", most_pen[0], ".")

#Sorts through player_list to find the player with the most made freethrows in a season
def most_ft(player_list):
    count = 0
    most_ft = []
    for players in player_list:
        if count == 0:
            most_ft = player_list[0]
            count+=1
            continue
        if most_ft[17] < players[17]:
            most_ft = players
            count+=1
            continue
        elif most_ft[17] > players [17]:
            count +=1
            continue

    print("\nThe player with the most made free throws in a single season is", most_ft[1], most_ft[2], "with a total of", most_ft[17], "free throws in", most_ft[0], ".")

player_file = open("player_regular_season.csv", 'r')#Oepn and read csv file

player_list = playerList(player_file)#Converts csv into a readable list

efficiency(player_list)
most_minutes(player_list)
most_games(player_list)
most_points(player_list)
most_penalites(player_list)
most_ft(player_list)

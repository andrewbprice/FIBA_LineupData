print('Importing libraries...')

import urllib.request as urllib
from bs4 import BeautifulSoup
import csv

print("Connecting to URL...")

#######################################################################################
#######################################################################################
###################### INSERT URL OF GAME AND COUNTRY TRIGRAMS ########################
#######################################################################################

page = urllib.urlopen("http://www.fiba.basketball/asiacup/2017/1008/New-Zealand-Lebanon")

countryTri = "NZL"
oppTri = "LBN"

#######################################################################################
#######################################################################################
#######################################################################################
#######################################################################################

soup = BeautifulSoup(page, "html.parser")

print("Locating Play By Play...")

content = soup.find_all('div', {'id': 'play_by_play_feed_list'})

pbpQ1 = content[0].find_all('div', {'class': 'feed_item'})
pbpQ2 = content[1].find_all('div', {'class': 'feed_item'})
pbpQ3 = content[2].find_all('div', {'class': 'feed_item'})
pbpQ4 = content[3].find_all('div', {'class': 'feed_item'})

Lineup = []
OpponentLineup = []

def pbpParser(actions, players, times, team, quarter):

	for action in actions:
		action = (action.get_text())

	for player in players:
		player = (player.get_text()).strip()
		player = player.split('#', 1)[-1]

	for time in times:
		time = (time.get_text())

	for team in team:
		team = team.get('title')

	if (action == "Substitution in"
		and team == countryTri):
			Lineup.append(player)

	if (action == "Substitution out"
	and team == countryTri):
		Lineup.remove(player)

	if (action == "Substitution in"
	and team != countryTri):
		OpponentLineup.append(player)

	if (action == "Substitution out"
	and team != countryTri):
		OpponentLineup.remove(player)

	if (action in ("2pt jump shot made", "tip in made", "layup made", "dunk made")
	and team == countryTri):
		points = 2
		OPPpoints = -2

	elif (action in ("3pt shot made")
	and team == countryTri):
		points = 3
		OPPpoints = -3

	elif (action in ("2pt jump shot made", "tip in made", "layup made", "dunk made")
	and team != countryTri):
		points = -2
		OPPpoints = 2

	elif (action in ("3pt shot made")
	and team != countryTri):
		points = -3
		OPPpoints = 3

	elif (action in ("1st free throw made","1st of 2 free throws made","1st of 3 free throws made", "2nd of 2 free throws made","2nd of 3 free throws made", "3rd of 3 free throws made")
	and team != countryTri):
		points = -1
		OPPpoints = 1

	elif (action in ("1st free throw made","1st of 2 free throws made","1st of 3 free throw made", "2nd of 2 free throws made","2nd of 3 free throws made", "3rd of 3 free throws made")
	and team == countryTri):
		points = 1
		OPPpoints = -1				
	else:
		points = 0
		OPPpoints = 0

	if (action in ("2pt jump shot missed", "3pt shot missed", "2pt jump shot made", "3pt shot missed",\
		"tip in made", "layup made", "dunk made", "3pt shot made", "tip in missed", "layup missed", "dunk missed")
	and team == countryTri):
		FGA = 1
	else:
		FGA = 0

	if (action in ("2pt jump shot missed", "3pt shot missed", "2pt jump shot made", "3pt shot missed",\
		"tip in made", "layup made", "dunk made", "3pt shot made", "tip in missed", "layup missed", "dunk missed")
	and team != countryTri):
		OPPFGA = 1
	else:
		OPPFGA = 0

	if (action in ("1st free throw made","1st free throw missed","1st of 2 free throws made", "1st of 3 free throws made", "2nd of 2 free throws made",\
		"2nd of 3 free throws made", "3rd of 3 free throws made", "1st of 2 free throws missed",\
		"1st of 3 free throws missed", "2nd of 2 free throws missed","2nd of 3 free throws missed", "3rd of 3 free throws missed")
	and team == countryTri):
		FTA = 1
	else:
		FTA = 0

	if (action in ("1st free throw made","1st free throw missed","1st of 2 free throws made", "1st of 3 free throws made", "2nd of 2 free throws made",\
		"2nd of 3 free throws made", "3rd of 3 free throws made", "1st of 2 free throws missed",\
		"1st of 3 free throws missed", "2nd of 2 free throws missed","2nd of 3 free throws missed", "3rd of 3 free throws missed")
	and team != countryTri):
		OPPFTA = 1
	else:
		OPPFTA = 0

	if action in ("offensive rebound", "team offensive rebound") and team == countryTri:
		oREB = 1
	else:
		oREB = 0

	if action in ("offensive rebound", "team offensive rebound") and team != countryTri:
		OPPoREB = 1
	else:
		OPPoREB = 0

	if action in ("defensive rebound", "team defensive rebound") and team == countryTri:
		dREB = 1
	else:
		dREB = 0

	if action in ("defensive rebound", "team defensive rebound") and team != countryTri:
		OPPdREB = 1
	else:
		OPPdREB = 0

	if action.startswith("turnover") and team == countryTri:
		TOV = 1
	else:
		TOV = 0

	if action.startswith("turnover") and team != countryTri:
		OPPTOV = 1
	else:
		OPPTOV = 0

	Lineup.sort()
	LineupFormatted = ' | '.join(Lineup)
	OpponentLineup.sort()
	OppLineupFormatted = ' | '.join(OpponentLineup)

	#if(len(Lineup) == 5 and len(OpponentLineup) == 5):
	outputWriter.writerow([quarter, time, player, team, action, LineupFormatted, OppLineupFormatted, points, OPPpoints, FGA, OPPFGA, FTA, OPPFTA, oREB, OPPoREB, dREB, OPPdREB, TOV, OPPTOV])

def Q1():

	for item in pbpQ1:
		actions = item.find_all('p', {'class' : 'description'})
		players = item.find_all('p', {'class' : 'name'})
		times = item.find_all('p', {'class' : 'time'})
		team = item.find_all('img')
		quarter = 1

		pbpParser(actions, players, times, team, quarter)

def Q2():

	for item in pbpQ2:
		actions = item.find_all('p', {'class' : 'description'})
		players = item.find_all('p', {'class' : 'name'})
		times = item.find_all('p', {'class' : 'time'})
		team = item.find_all('img')
		quarter = 2

		pbpParser(actions, players, times, team, quarter)			

def Q3():

	for item in pbpQ3:
		actions = item.find_all('p', {'class' : 'description'})
		players = item.find_all('p', {'class' : 'name'})
		times = item.find_all('p', {'class' : 'time'})
		team = item.find_all('img')
		quarter = 3

		pbpParser(actions, players, times, team, quarter)

def Q4():

	for item in pbpQ4:
		actions = item.find_all('p', {'class' : 'description'})
		players = item.find_all('p', {'class' : 'name'})
		times = item.find_all('p', {'class' : 'time'})
		team = item.find_all('img')
		quarter = 4

		pbpParser(actions, players, times, team, quarter)		

def calculate():

	print("")
	print("Processing Quarter 1...")
	Q1()
	print("Processing Quarter 2...")	
	Q2()
	print("Processing Quarter 3...")	
	Q3()
	print("Processing Quarter 4...")	
	Q4()
	print("")
	print("Game Successfully Exported")

outputFile = open(countryTri +'_vs_'+oppTri +'.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(["Quarter", "Clock", "Player", "Team", "Action", "TeamLineup", "OpponentLineup", "Points", "OPPpoints", "FGA", "OPPFGA", "FTA", "OPPFTA", "oREB", "OPPoREB", "dREB", "OPPdREB", "TOV", "OPPTOV"])

calculate()
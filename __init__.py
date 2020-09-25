import os
import json
import csv

data = {}
data['teams'] = []
data['players'] = []
data['leagues'] = []
def Generate(kind):
	if kind == "Teams":
		print("Generating Teams")
		for x in range(len(aData)-1):
			data['teams'].append({
			    'name': f'{aData[x][3]} National Football Team',
			    'tag': f'{aData[x][2]}',
			    'short': f'{aData[x][1]}',
			    'long': f'{aData[x][0]}'
			})
			print("["+str(data['teams'][x]['tag'])+"]: Added",data['teams'][x]['name'],"from",data['teams'][x]['short'],"(" + str(data['teams'][x]['long']) + ")")
	elif kind == "Players":
		print("Generating Players")
	elif kind == "Leagues":
		print("Generating Leagues")

if not os.path.exists(os.getcwd() + "/Data"):
	os.mkdir(os.getcwd() + "/Data")
	if not os.path.exists(os.getcwd() + "/Data/TeamData"):
		os.mkdir(os.getcwd() + "/Data/TeamData")
	if not os.path.exists(os.getcwd() + "/Data/PlayerData"):
		os.mkdir(os.getcwd() + "/Data/PlayerData")
	if not os.path.exists(os.getcwd() + "/Data/LeagueData"):
		os.mkdir(os.getcwd() + "/Data/LeagueData")

if os.path.exists(os.getcwd() + "/Data"):
	aData = []
	with open(os.getcwd() + "/Data/english.csv") as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			aData.append([row[0],row[1],row[2],row[3]])
	print(f'Processed {line_count} lines.')
	del aData[0]
	if os.path.exists(os.getcwd() + "/Data/TeamData"):
		Generate("Teams")
	if os.path.exists(os.getcwd() + "/Data/PlayerData"):
		Generate("Players")
	if os.path.exists(os.getcwd() + "/Data/LeagueData"):
		Generate("Leagues")


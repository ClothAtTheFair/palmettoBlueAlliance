import requests
import json
import pandas as pd

headers = {
    'user-agent': 'X-TBA-Auth-Key'
}

payload = {
    'X-TBA-Auth-Key': "mlFlMYqAlTWZfnPYv3gRqJCW8V1FbRDFhL2N3Z52b1ser4jliNxJtUjeb8coIn2k"
}

def teamsAtEvent():
    url = "https://www.thebluealliance.com/api/v3/event/2020scmb/teams/simple"
    palmettoRequest = requests.get(url, params=payload)
    # jprint(palmettoTeams.json()[1]['team_number'])
    palmettoTeams = palmettoRequest.json()

    teams = []

    for t in palmettoTeams:
        names = t['team_number']
        teams.append(names)

    return teams

#2019 for testing, need to change before actual Palmetto
def matchesAtPalmetto():
    url = "https://www.thebluealliance.com/api/v3/event/2019scmb/matches"
    matchRequest = requests.get(url, params=payload)
    matches = matchRequest.json()

    return matches

def showAllOPR(comp):
    url = "https://www.thebluealliance.com/api/v3/event/" + comp + "/oprs"
    oprURL = requests.get(url, params=payload)
    oprjson = oprURL.json()['oprs']
    jprint(oprjson)

#Need a way to break down more to maybe only score or search for certain parts of the breakdown. Pull from the doc
#What kind of information is stored and add to a dictionary then ask user which they want to display in a grapH??
def parseBlueAlliance(matches):

    blue_breakdowns = []

    for j in matches:
        blue_alliance = j['alliances']['blue']
        level = j['comp_level']
        number = j['match_number']
        title = str(level) + str(number)
        breakdown = j['score_breakdown']['blue']
        blue_breakdowns.append(title)
        blue_breakdowns.append(blue_alliance)
        blue_breakdowns.append(breakdown)
    #jprint(blue_breakdowns)
    return blue_breakdowns


def parseRedAlliance(matches):
    red_breakdowns = []

    for j in matches:
        red_alliance = j['alliances']['red']
        level = j['comp_level']
        number = j['match_number']
        title = str(level) + str(number)
        breakdown = j['score_breakdown']['red']
        red_breakdowns.append(title)
        red_breakdowns.append(red_alliance)
        red_breakdowns.append(breakdown)
    #jprint(red_breakdowns)
    return red_breakdowns

def jprint(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)





if __name__ == "__main__":
    response = requests.get('https://www.thebluealliance.com/api/v3/status', params=payload)
    if response.status_code == 404:
        print('Cannot connect to the server at the moment, please try again later')
    else:
        ahh = teamsAtEvent()
        yikes = matchesAtPalmetto()
        forever = parseBlueAlliance(yikes)
        jprint(forever)
        #testBlue(forever)
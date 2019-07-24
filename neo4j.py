from py2neo import Graph


graph = Graph(ip_addr="http://localhost:7474", username="neo4j", password="Whistle")


loadschool ="""
LOAD CSV WITH HEADERS FROM "https://docs.google.com/spreadsheets/d/1VKcxlOQtxCGMw27wdkVcO1a2Ic0Il8S5cPzqP748-hA/export?format=csv&id=1VKcxlOQtxCGMw27wdkVcO1a2Ic0Il8S5cPzqP748-hA&gid=1495138042" AS row
create (s:School {school: row.school, mascot: row.mascot, abbreviation: 
row.abbreviation, division: row.division, color: row.color, alt_color: row.alt_color})

"""
graph.run(loadschool)

loadconference="""
LOAD CSV WITH HEADERS FROM "https://docs.google.com/spreadsheets/d/1VKcxlOQtxCGMw27wdkVcO1a2Ic0Il8S5cPzqP748-hA/export?format=csv&id=1VKcxlOQtxCGMw27wdkVcO1a2Ic0Il8S5cPzqP748-hA&gid=1495138042" AS row
CREATE (c:Conference {conference: row.conference})
"""
graph.run(loadconference)

matchconference="""
LOAD CSV WITH HEADERS FROM "https://docs.google.com/spreadsheets/d/1VKcxlOQtxCGMw27wdkVcO1a2Ic0Il8S5cPzqP748-hA/export?format=csv&id=1VKcxlOQtxCGMw27wdkVcO1a2Ic0Il8S5cPzqP748-hA&gid=1495138042" AS row
MATCH (s:School {school: row.school})
MATCH (c:Conference {conference: row.conference})
MERGE (s)-[:PLAYS_IN]->(c)
"""
graph.run(matchconference)

#loadvenue ="""
#LOAD CSV WITH HEADERS FROM "file:///venues.csv" as row
#create (v:Venue {venue_name: row.name, venue_capacity: row.capacity, venue_id: row.id})
#"""
#graph.run(loadvenue)


loadseason ="""
LOAD CSV WITH HEADERS FROM "file:///seasons.csv" as row
create (sea:Season {season:row.Season})
"""
graph.run(loadseason)

loadgames ="""
Using periodic commit 1000
LOAD CSV WITH HEADERS FROM "file:///games.csv" as row
create (g:Game {game_id:row.id, season:row.season, week:row.week,
start_date: row.start_date, neutral_site: row.neutral_site,
conference_game: row.conference_game, attendance: row.attendance,
venue_id: row.venue_id, venue: row.venue, home_team: row.home_team,
home_conference:row.home_conference, home_points: row.home_points,
home_line_scores_0: row.home_line_scores_0, home_line_scores_1: row.home_line_scores_1,
home_line_scores_2: row.home_line_scores_2, home_line_scores_3: row.home_line_scores_3,
away_team: row.away_team, away_conference: row.away_conference, away_points: row.away_points,
away_line_scores_0: row.away_line_scores_0, away_line_scores_1: row.away_line_scores_1,
away_line_scores_2: row.away_line_scores_2, away_line_scores_3: row.away_line_scores_3,
home_line_scores_4: row.home_line_scores_4, away_line_scores_4: row.away_line_scores_4,
home_line_scores_5: row.home_line_scores_5, home_line_scores_6: row.home_line_scores_6,
away_line_scores_5: row.away_line_scores_5, away_line_scores_6: row.away_line_scores_6,
home_line_scores_7: row.home_line_scores_7, home_line_scores_8: row.home_line_scores_8,
away_line_scores_7: row.away_line_scores_7, away_line_scores_8: row.away_line_scores_8,
home_line_scores_9: row.home_line_scores_9, home_line_scores_10: row.home_line_scores_10,
away_line_scores_9: row.away_line_scores_9, away_line_scores_10: row.away_line_scores_10})
"""
graph.run(loadgames)

matchseason ="""
LOAD CSV WITH HEADERS FROM "file:///games.csv" as row
match (g:Game),(sea:Season)
where g.season = sea.season
merge (sea)-[:GAMES_PLAYED]->(g)
"""
graph.run(matchseason)

matchhometeam ="""
LOAD CSV WITH HEADERS FROM "file:///games.csv" as row
match (g:Game), (s:School)
where g.home_team = s.school
merge (s)-[:HOME_TEAM]->(g)
"""
graph.run(matchhometeam)

matchawayteam ="""
LOAD CSV WITH HEADERS FROM "file:///games.csv" as row
match (g:Game), (s:School)
where g.away_team = s.school
merge (s)-[:AWAY_TEAM]->(g)
"""
graph.run(matchawayteam)

loaddrives ="""
using periodic commit 1000
LOAD CSV WITH HEADERS FROM "file:///drives.csv" as row
create (d:Drives {drives_id:row.id, offense: row.offense,
offense_conference: row.offense_conference, defense: row.defense,
defense_conference: row.defence_conference, game_id: row.game_id,
scoring: row.scoring, start_period: row.start_period, 
start_yardline: row.start_yardline, start_time_minutes: row.start_time_minutes,
end_period: row.end_period, end_yardline: row.end_yardline, 
end_time_minutes: row.end_time_minutes, end_time_seconds: row.end_time_seconds, 
plays: row.plays, yards: row.yards, drive_results: row.drive_results, 
start_time_seconds: row.start_time_seconds})
"""
graph.run(loaddrives)

matchdrives="""
using periodic commit 1000
LOAD CSV WITH HEADERS FROM "file:///drives.csv" as row
match (d:Drives), (g:Game)
where g.game_id = d.game_id
merge (g)-[:HAS_DRIVES]->(d)
"""
graph.run(matchdrives)

loadplays="""
using periodic commit 1000
LOAD CSV WITH HEADERS FROM "file:///plays.csv" as row
create (p:Plays {plays_id:row.id, position_in_week: row.position_in_week,
clock: row.clock, defense: row.defense, 
defense_conference: row.defense_conference, defense_score: row.defense_score,
distance: row.distance, down: row.down, drive_id: row.drive_id,
offense: row.offense, offense_conference: row.offense_conference,
offense_score: row.offense_score, period: row.period,
play_text: row.play_text, play_type: row.play_type,
yard_line: row.yard_line, yards_gained: row.yards_gained})
"""
graph.run(loadplays)

matchplays="""
using periodic commit 1000
LOAD CSV WITH HEADERS FROM "file:///plays.csv" as row
match (d:Drives), (p:Plays)
where d.drives_id = p.drive_id
merge (d)-[:HAS_PLAYS]->(p)
"""
graph.run(matchplays)
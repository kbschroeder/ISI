from py2neo import Graph


graph = Graph(ip_addr="http://localhost:7474", username="neo4j", password="Whistle")

query = """

CREATE 
    (player:Player {id:'Player'}),
    (game:Game {id:'Game'}),
    (venue:Venue {id:'Venue'}),
    (season:Season {id:'Season'}),
    (NCAA:Governing {id:'NCAA'}),
    (division:Division {id: 'Division'}),
    (schoolgamestats:SchoolGameStats {id:'SchoolGameStats'}),
    (playergamestats:PlayerGameStats {id:'PlayerGameStats'}),
    (drives:Drives {id:'Drives'}),
    (plays:Plays {id:'Plays'})
CREATE
    (ACC:Conference {id:'ACC'}),
    (Division1FBSInd:Conference {id:'Ind'}),
    (Big12:Conference {id:'Big 12'}),
    (SEC:Conference {id:'SEC'}),
    (MidAmerican:Conference {id:'Mid-American'}),
    (Pac12:Conference {id:'Pac-12'}),
    (ConferenceUSA:Conference {id:'Conference USA'}),
    (TheAmerican:Conference {id:'The American'}),
    (FCTeams:Conference {id:'FCS Teams'}),
    (MountainWest:Conference {id:'Mountain West'}),
    (BigTen:Conference {id:'Big Ten'}),
    (SunBelt:Conference {id:'Sun Belt'}) 
CREATE
    (ACC)-[:PLAYS_IN]->(division),
    (Division1FBSInd)-[:PLAYS_IN]->(division),
    (Big12)-[:PLAYS_IN]->(division),
    (SEC)-[:PLAYS_IN]->(division),
    (MidAmerican)-[:PLAYS_IN]->(division),
    (Pac12)-[:PLAYS_IN]->(division),
    (ConferenceUSA)-[:PLAYS_IN]->(division),
    (TheAmerican)-[:PLAYS_IN]->(division),
    (MountainWest)-[:PLAYS_IN]->(division),
    (BigTen)-[:PLAYS_IN]->(division),
    (SunBelt)-[:PLAYS_IN]->(division)


CREATE (playergamestats)-[:HAS_PLAYER_GAME_STATS_FOR_SCHOOL]->(USC)
CREATE (USC)-[:HAS_GAME_STATS]->(schoolgamestats)
CREATE (USC)-[:AWAY_TEAM]->(game)
CREATE (USC)-[:HOME_TEAM]->(game)
CREATE (playergamestats)-[:HAS_PLAYER_GAME_STATS]->(game)
CREATE (playergamestats)-[:HAS_PLAYER_GAME_STATS_FOR_GAME]->(game)
CREATE (playergamestats)-[:HAS_PLAYER_GAME_STATS]->(player)
CREATE (player)-[:HAS_PLAYER_GAME_STATS]->(game)
CREATE (game)-[:PLAYED_AT]->(venue)
CREATE (game)-[:HAS_PLAYER_GAME_STATS]->(schoolgamestats)
CREATE (game)-[:PLAYED_IN_SEASON]->(season)
CREATE (division)-[:GOVERNED_BY]->(NCAA)
CREATE (playergamestats)-[:HAS_PLAYER_GAME_STATS]->(playergamestats)
CREATE (game)-[:HAS_DRIVES]->(drives)
CREATE (drives)-[:HAVE_PLAYS]->(plays)

"""

graph.run(query)


from re import compile as regex

foi = {
    "Associations.json": [".*/Name$",".*Tooltip",".*Description"],
    "CombatAttacks.json": [".*/Description$"],
    "CombatItems.json": [".*/Name$",".*/Description$"],
    "Tutorials.json": [".*/Name$",".*/Description$"],
    "areas.json": [".*/Name$",".*/Description$",".*MoveMessage$"],
    "events.json": [".*/Name$",".*/Description$",".*Teaser$",".*ButtonText$"],
    "SpawnedEntities.json": [".*HumanName$"],
    "exchanges.json": [".*/Name$",".*/Description$"],
    "qualities.json": [".*/Name$",".*/Description$",".*/AvailableAt$",".*/ChangeDescriptionText$",".*/LevelDescriptionText$"],
    "Tiles.json": [".*/HumanName$",".*/Description$",".*/Label$"],
}
files_of_interest = dict()
for ext, poi in foi.items():
    files_of_interest[ext] = list()
    for p in poi:
        # print(p)
        files_of_interest[ext].append(regex(p))

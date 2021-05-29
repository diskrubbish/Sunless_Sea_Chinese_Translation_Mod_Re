from re import compile as regex

foi = {
    "Associations.json": [".*/(LegacyUnlockQualities|JettisonEvents)/[0-9]+/(Name|Tooltip|Description)$"],
    "CombatAttacks.json": [".*/Description$"],
    "CombatItems.json": [".*/(Name|Description)$"],
    "exchanges.json": [".*/(Name|Description)$"],
    "SpawnedEntities.json": [".*HumanName$"],
    "Tutorials.json": [".*/(Name|Description)$"],
    "areas.json": [".*/(Name|Description|MoveMessage)$"],
    "events.json": [".*/(Name|Description|Teaser|ButtonText)$"],
    "qualities.json": [".*/(Name|Description|AvailableAt|ChangeDescriptionText|LevelDescriptionText)$"],
    "Tiles.json": [".*/(HumanName|Description|Label)$"],



}
files_of_interest = dict()
for ext, poi in foi.items():
    files_of_interest[ext] = list()
    for p in poi:
        # print(p)
        files_of_interest[ext].append(regex(p))
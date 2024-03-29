from django.apps import AppConfig


class ToolsConfig(AppConfig):
    name = 'tools'

RACES_LIST = [
    {
        'name': 'Humans',
        'icon': 'UI/Glues/Loading/Backgrounds/Campaigns/HumanSymbol.blp',
    },
    {
        'name': 'Orcs',
        'icon': 'UI/Glues/Loading/Backgrounds/Campaigns/OrcSymbol.blp',
    },
    {
        'name': 'Night-Elves',
        'icon': 'UI/Glues/Loading/Backgrounds/Campaigns/NightElfSymbol.blp',
    },
    {
        'name': 'Undead',
        'icon': 'UI/Glues/Loading/Backgrounds/Campaigns/UndeadSymbol.blp',
    },
    {
        'name': 'Neutral (hostile)',
        'icon': 'UI/Glues/ScoreScreen/ScoreScreen-Defeat/scorescreen-defeat.blp',  # NOQA
    },
    {
        'name': 'Neutral (passive)',
        'icon': 'UI/Glues/ScoreScreen/ScoreScreen-Defeat/scorescreen-defeat.blp',  # NOQA
    },
]

RACES_DEFAULT_MAPPING = {
    'Human': 'Humans',
    'Orc': 'Orcs',
    'NightElf': 'Night-Elves',
    'Undead': 'Undead',
    'Creeps': 'Neutral (hostile)',
    'Critters': 'Neutral (passive)',
}

REPLACEABLE_ICONS_DIR = 'ReplaceableTextures/CommandButtons'

UNITS_MAPPING = {
    'AbominationCIN': {
        'ignore': True,
        'categorization': ('campaign'),
        'replaceable_icon': 'Abomination',
    },
    'AncestralGuardian': {
        'categorization': ('special'),
        'replaceable_icon': 'SelectHeroOn',
    },
    'Arthas': {
        'categorization': ('campaign', 'heroic'),
    },
    'ArthaswithSword': {
        'name': 'Arthas (with Frostmourne)',
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'Arthas',
    },
    'AzureDragonWelp': {
        'replaceable_icon': 'AzureDragon',
    },
    'BansheeGhost': {
        'replaceable_icon': 'Ghost',
    },
    'BlackDragonWelp': {
        'replaceable_icon': 'BlackDragon',
    },
    'BlackStagMale': {
        'replaceable_icon': 'Stag',
    },
    'BristleBack': {
        'replaceable_icon': 'Razorback',
    },
    'BronzeDragonWelp': {
        'replaceable_icon': 'BronzeDragon',
    },
    'BrownWolf': {
        'replaceable_icon': 'DireWolf',
    },
    'BurningArcher': {
        'replaceable_icon': 'SkeletonArcher',
    },
    'Cairne': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HeroTaurenChieftain',
    },
    'ChaosGrunt': {
        'race': 'Orcs',
        'categorization': ('campaign'),
    },
    'ChaosHellscream': {
        'race': 'Orcs',
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'ChaosGrom',
    },
    'ChaosKotoBeast': {
        'race': 'Orcs',
        'categorization': ('campaign'),
    },
    'ChaosOrcRange': {
        'ignore': True,
        'race': 'Orcs',
        'categorization': ('campaign'),
        'replaceable_icon': 'SelectHeroOn',
    },
    'ChaosPeon': {
        'race': 'Orcs',
        'categorization': ('campaign'),
    },
    'ChaosSpaceOrc': {
        'categorization': ('campaign'),
    },
    'ChaosWarlock': {
        'race': 'Orcs',
        'categorization': ('campaign'),
    },
    'ChaosWarlockGreen': {
        'race': 'Orcs',
        'categorization': ('campaign'),
    },
    'ChaosWarlord': {
        'race': 'Orcs',
        'categorization': ('campaign'),
    },
    'ChaosWolfrider': {
        'race': 'Orcs',
        'categorization': ('campaign'),
        'replaceable_icon': 'ChaosWolfRider',
    },
    'DoomGuard': {
        'race': 'Neutral (hostile)',
    },
    'ElfVillagerWoman': {
        'categorization': ('campaign'),
        'replaceable_icon': 'FemaleElfVillager',
    },
    'Ent': {
        'categorization': ('special'),
    },
    'EvilArthas': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HeroDeathKnight',
    },
    'felhound': {
        'name': 'Felhound',
        'race': 'Neutral (hostile)',
        'replaceable_icon': 'FelHound',
    },
    'FlyingSheep': {
        'categorization': ('campaign', 'special'),
    },
    'Furion': {
        'categorization': ('campaign', 'heroic'),
    },
    'FlyingSheep': {
        'replaceable_icon': 'Sheep',
    },
    'ForestTrollTrapper': {
        'icon': 'ReplaceableTextures/WorldEditUI/Editor-Random-Unit.blp',
    },
    'GnollOverSeer': {
        'replaceable_icon': 'GnollKing',
    },
    'GoblinLandMine': {
        'categorization': ('special'),
    },
    'GolemStatue': {
        'replaceable_icon': 'ArmorGolem',
    },
    'GreenDragonWelp': {
        'replaceable_icon': 'GreenDragon',
    },
    'GyroCopter': {
        'name': 'Gyrocopter',
        'replaceable_icon': 'Gyrocopter',
    },
    'HeadHunter': {
        'replaceable_icon': 'Headhunter',
    },
    'HealingWard': {
        'categorization': ('special'),
    },
    'Hellscream': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HellScream',
    },
    'HeroArchMage': {
        'name': 'Archmage',
        'categorization': ('heroic'),
    },
    'HeroBladeMaster': {
        'name': 'Blade Master',
        'categorization': ('heroic'),
        'replaceable_icon': 'HeroBlademaster',
    },
    'HeroChaosBladeMaster': {
        'name': 'Blade Master of the Blackrock Clan',
        'race': 'Orcs',
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'ChaosBlademaster',
    },
    'HeroDeathKnight': {
        'name': 'Death Knight',
        'categorization': ('heroic'),
    },
    'HeroDemonHunter': {
        'name': 'Demon Hunter',
        'categorization': ('heroic'),
    },
    'HeroDreadLord': {
        'name': 'Dread Lord',
        'categorization': ('heroic'),
    },
    'HeroFarseer': {
        'name': 'Far Seer',
        'categorization': ('heroic'),
    },
    'HeroKeeperOfTheGrove': {
        'name': 'Keeper of the Grove',
        'categorization': ('heroic'),
        'replaceable_icon': 'KeeperOfTheGrove',
    },
    'HeroKeeperoftheGroveGhost': {
        'name': 'Keeper of the Grove (Ghost)',
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'KeeperGhostBlue',
    },
    'HeroLich': {
        'name': 'Lich',
        'categorization': ('heroic'),
    },
    'HeroLichCIN': {
        'ignore': True,
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'LichVersion2',
    },
    'HeroMoonPriestess': {
        'name': 'Moon Priestess',
        'categorization': ('heroic'),
    },
    'HeroMountainKing': {
        'name': 'Mountain King',
        'categorization': ('heroic'),
    },
    'HeroPaladin': {
        'name': 'Paladin',
        'categorization': ('heroic'),
    },
    'HeroPaladinBoss': {
        'ignore': True,
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HeroPaladin',
    },
    'HeroPaladinBoss2': {
        'ignore': True,
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HeroPaladin',
    },
    'HeroTaurenChieftain': {
        'name': 'Tauren Chieftain',
        'categorization': ('heroic'),
    },
    'HeroTaurenChieftainCIN': {
        'ignore': True,
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HeroTaurenChieftain',
    },
    'HighElfArcher': {
        'replaceable_icon': 'HighElvenArcher',
    },
    'HighElfPeasant': {
        'categorization': ('campaign'),
        'replaceable_icon': 'ElfVillager',
    },
    'HippoGryph': {
        'name': 'Hippogryph',
        'replaceable_icon': 'Hippogriff',
    },
    'HumanMage': {
        'replaceable_icon': 'BanditMage',
    },
    'Hydralisk': {
        'categorization': ('campaign'),
    },
    'IronGolem': {
        'replaceable_icon': 'ArmorGolem',
    },
    'Illidan': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HeroDemonHunter',
    },
    'Infernal': {
        'race': 'Neutral (hostile)',
    },
    'Jaina': {
        'categorization': ('campaign', 'heroic'),
    },
    'Kelthuzad': {
        'ignore': True,
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'KelThuzad',
    },
    'KelthuzadGhost': {
        'ignore': True,
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'GhostOfKelThuzad',
    },
    'KelThuzadLich': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'KelThuzad',
    },
    'KelThuzadNecro': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'GhostOfKelThuzad',
    },
    'KnightNoRider': {
        'categorization': ('campaign', 'special'),
        'replaceable_icon': 'RiderlessHorse',
    },
    'KotoBeastNoRider': {
        'name': 'Koto Beast (no rider)',
        'categorization': ('campaign'),
        'replaceable_icon': 'RiderlessKodo',
    },
    'Mannoroth': {
        'race': 'Undead',
        'categorization': ('campaign', 'heroic'),
    },
    'Marine': {
        'categorization': ('campaign'),
    },
    'Meatwagon': {
        'name': 'Meat Wagon',
        'replaceable_icon': 'MeatWagon',
    },
    'Medivh': {
        'categorization': ('campaign', 'heroic'),
    },
    'Militia': {
        'categorization': ('special'),
    },
    'Muradin': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HeroMountainKing',
    },
    'MurlocWarrior': {
        'replaceable_icon': 'Murloc',
    },
    'NerubianSpiderLord': {
        'replaceable_icon': 'nerubianSpiderLord',
    },
    'OrcJuggernaught': {
        'categorization': ('campaign'),
        'replaceable_icon': 'Juggernaut',
    },
    'Owlbear': {
        'name': 'Owl',
        'replaceable_icon': 'OwlBear',
    },
    'Owl': {
        'name': 'Owl (huntress)',
        'categorization': ('special'),
        'replaceable_icon': 'OwlBear',
    },
    'OwlSCOUT': {
        'name': 'Owl Scout',
        'categorization': ('special'),
        'replaceable_icon': 'Scout',
    },
    'Pitlord': {
        'race': 'Neutral (passive)',
        'categorization': ('heroic'),
        'replaceable_icon': 'PitLord',
    },
    'PlagueCloud': {
        'categorization': ('special'),
    },
    'Rat': {
        'replaceable_icon': 'YouDirtyRat!',
    },
    'RazorMane': {
        'replaceable_icon': 'Razorback',
    },
    'RazorManeChief': {
        'replaceable_icon': 'RazormaneChief',
    },
    'RedDragonWelp': {
        'replaceable_icon': 'RedDragon',
    },
    'RiddenHippoGryph': {
        'name': 'Ridden Hippogryph',
        'categorization': ('special'),
        'replaceable_icon': 'HippogriffRider',
    },
    'RiderlessWyvern': {
        'categorization': ('campaign'),
        'replaceable_icon': 'Wyvern',
    },
    'SammyCube': {
        'categorization': ('special'),
        'replaceable_icon': 'SelectHeroOn',
    },
    'satyrhellcaller': {
        'name': 'Satyr Hellcaller',
        'replaceable_icon': 'SatyrTrickster',
    },
    'SentryWard': {
        'categorization': ('special'),
    },
    'Shandris': {
        'categorization': ('campaign', 'heroic'),
    },
    'Shoveler': {
        'categorization': ('special'),
    },
    'Skeleton': {
        'categorization': ('special'),
        'replaceable_icon': 'SkeletonWarrior',
    },
    'SludgeMonster': {
        'replaceable_icon': 'SludgeCreature',
    },
    'SpiritPig': {
        'categorization': ('special'),
        'replaceable_icon': 'Pig',
    },
    'Spiritwolf': {
        'name': 'Spirit Wolf',
        'categorization': ('special'),
        'replaceable_icon': 'SpiritWolf',
    },
    'StasisTotem': {
        'categorization': ('special'),
        'replaceable_icon': 'StasisTrap',
    },
    'SylvanusWindrunner': {
        'name': 'Sylvanas Windrunner',
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'SylvanusWindRunner',
    },
    'TempArt': {
        'ignore': True,
        'categorization': ('special'),
        'replaceable_icon': 'SelectHeroOn',
    },
    'TheCaptain': {
        'categorization': ('campaign'),
    },
    'Thrall': {
        'categorization': ('heroic'),
    },
    'Tichondrius': {
        'categorization': ('campaign', 'heroic'),
    },
    'Tyrande': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HeroMoonPriestess',
    },
    'Uther': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HeroPaladin',
    },
    'VillagerKid': {
        'name': 'Kid',
        'categorization': ('campaign'),
    },
    'VillagerKid1': {
        'name': 'Kid (2)',
        'categorization': ('campaign'),
        'replaceable_icon': 'VillagerKid2',
    },
    'VillagerMan': {
        'name': 'Villager (Man)',
        'categorization': ('campaign'),
    },
    'VillagerMan1': {
        'name': 'Villager (Man 2)',
        'categorization': ('campaign'),
    },
    'VillagerWoman': {
        'name': 'Villager (Woman)',
        'categorization': ('campaign'),
    },
    'Warlock': {
        'race': 'Neutral (hostile)',
        'icon': 'ReplaceableTextures/WorldEditUI/Editor-Random-Unit.blp',
    },
    'WarWagon': {
        'categorization': ('campaign', 'special'),
        'replaceable_icon': 'SteamTank',
    },
    'Watcher': {
        'icon': 'ReplaceableTextures/WorldEditUI/Editor-Random-Unit.blp',
    },
    'WaterElemental': {
        'categorization': ('special'),
        'replaceable_icon': 'SummonWaterElemental',
    },
    'WendigoShaman': {
        'replaceable_icon': 'Wendigo',
    },
    'WhiteWolf': {
        'replaceable_icon': 'TimberWolf',
    },
    'WindSerpent': {
        'categorization': ('special'),
        'replaceable_icon': 'SelectHeroOn',
    },
    'Wolfrider': {
        'replaceable_icon': 'Raider',
    },
    'zergling': {
        'name': 'Zergling',
        'categorization': ('campaign'),
        'replaceable_icon': 'Zergling',
    },
}

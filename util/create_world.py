from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

room_001 = Room(title='Kingler', description="Safe and secure. I feel protected in this space.")
room_002 = Room(title='Krabby', description="This space feels so imature.")
room_003 = Room(title='Hypno', description='I didn’t know anybody read anymore.')
room_004 = Room(title='Drowzee', description="Blue walls, two cradles, this must be a baby room.")
room_005 = Room(title='Onix', description="A grand piano sits in the middle of the room, music seems to be playing on its own...")
room_006 = Room(title='Gengar', description="Who needs a study when you already have a library?")
room_007 = Room(title='Haunter', description='Who needs a library if you already have an office?!')
room_008 = Room(title='Gastly', description="I wonder if they would mind if I cooked something to eat in here...")
room_009 = Room(title='Cloyster', description='Rather plain, if I had to guess, this would be the guest bedroom.')
room_010 = Room(title='Shellder', description="Well, I don’t need to use it anymore...")
room_011 = Room(title='Muk', description="Snow everywhere. There's also a pack of wolves roaming around.")
room_012 = Room(title='Grimer', description="There’s billiards, darts, but no time to play when I’m already practically playing clue.")
room_013 = Room(title='Dewgong', description='No thanks, I’m practically dripping sweat just by being here.')
room_014 = Room(title='Seel', description="Didn’t I already see a pool outside when I walked in?")
room_015 = Room(title='Dodrio', description="I’ve been walking in a straight line for so long it feels like I’m walking in a spiral...")
room_016 = Room(title='Doduo', description="There’s guns and swords, what would you need all that for?.")
room_017 = Room(title='Farfetchd', description='Well, I guess this is where they test out their stuff from the armory.')
room_018 = Room(title='Magneton', description="Painted bright orange, with a huge bed in the middle of the room and nothing else.")
room_019 = Room(title='Magnemite', description='Have never been one for sciencey things, myself.')
room_020 = Room(title='Slowbro', description="These plants are alive, someone has to be around to maintain them.")
room_021 = Room(title='Tentacruel', description="A lot of moldy bread, the smell is unbearable.")
room_022 = Room(title='Weepinbell', description="A blank canvas and an empty chair sits in the middle of the room.")
room_023 = Room(title='Machoke', description='I wonder who painted these...they’re not very good.')
room_024 = Room(title='Bellsprout', description="No thanks, I already went.")
room_025 = Room(title='Machamp', description="Best not to drink while on the job.")
room_026 = Room(title='Machop', description="This closet is about the size of my bedroom at home!")
room_027 = Room(title='Alakazam', description='I bet this room is bigger than most peoples homes, I don’t think I’m alone in here.')
room_028 = Room(title='Kadabra', description="White walls, the room is empty but the outlines of where furniture used to be, stain the walls and floor.")
room_029 = Room(title='Abra', description='The first time I’ve seen a screen in this whole house, and this wall is full of them, they’re all just static though.')
room_030 = Room(title='Poliwag', description="Nothing but towels in here.")
room_031 = Room(title='Poliwrath', description="This would’ve been useful earlier.")
room_032 = Room(title='Arcanine', description="Christmas lights adorn the wall, under each light is a letter. Strange.")
room_033 = Room(title='Growlithe', description='I suppose during the day this is where you’d go to see some sun, now its more like The Twilight Zone.')
room_034 = Room(title='Primeape', description="No washing machine nor dryer, just buckets and washing boards.")
room_035 = Room(title='Mankey', description="Lots of nice suits and shoes, all hung up and proper, whoever this guy was, he had some taste.")
room_036 = Room(title='Golduck', description="In the middle of the room is a large glass case with a bunch of toy soldiers, looks like it's supposed to be The Great War.")
room_037 = Room(title='Psyduck', description='A big screen with a projector in the back, uses good old fashioned film.')
room_038 = Room(title='Persian', description="Nothing in the room except a table with a house of cards in the middle. Odd.")
room_039 = Room(title='Meowth', description='Another gymnasium, except with a small boxing ring in the middle, gotta get those frustrations out somehow.')
room_040 = Room(title='Dugtrio', description="An empty room with a small box in the middle, it almost sounds like there's a bird chirping in there.")
room_041 = Room(title='Diglett', description="Quiet, spacious. Whoever owns this place must be rich.(2)")
room_042 = Room(title='Venomoth', description="Enough to seat at least 100 people, who would need a dining room this big?(2)")
room_043 = Room(title='Parasect', description='I didn’t know anybody read anymore.(2)')
room_044 = Room(title='Venonat', description="Blue walls, two cradles, this must be a baby room.(2)")
room_045 = Room(title='Vileplume', description="A grand piano sits in the middle of the room, music seems to be playing on its own...(2)")
room_046 = Room(title='Gloom', description="Who needs a study when you already have a library?(2)")
room_047 = Room(title='Oddish', description='Who needs a library if you already have an office?!(2)')
room_048 = Room(title='Golbat', description="I wonder if they would mind if I cooked something to eat in here...(2)")
room_049 = Room(title='Zubat', description='Rather plain, if I had to guess, this would be the guest bedroom.(2)')
room_050 = Room(title='Jigglypuff', description="Well, I don’t need to use it anymore...(2)")
room_051 = Room(title='Wigglytuff', description="Snow everywhere. There's also a pack of wolves roaming around.(2)")
room_052 = Room(title='Ninetales', description="There’s billiards, darts, but no time to play when I’m already practically playing clue.(2)")
room_053 = Room(title='Vulpix', description='No thanks, I’m practically dripping sweat just by being here.(2)')
room_054 = Room(title='Clefable', description="Didn’t I already see a pool outside when I walked in?(2)")
room_055 = Room(title='Clefairy', description="I’ve been walking in a straight line for so long it feels like I’m walking in a spiral...(2)")
room_056 = Room(title='Nidoking', description="There’s guns and swords, what would you need all that for?.(2)")
room_057 = Room(title='Nidorino', description='Well, I guess this is where they test out their stuff from the armory.(2)')
room_058 = Room(title='Nidoran♂', description="Painted bright orange, with a huge bed in the middle of the room and nothing else.(2)")
room_059 = Room(title='Nidoqueen', description='Have never been one for sciencey things, myself.(2)')
room_060 = Room(title='Nidorina', description="These plants are alive, someone has to be around to maintain them.(2)")
room_061 = Room(title='Nidoran♀', description="A lot of moldy bread, the smell is unbearable.(2)")
room_062 = Room(title='Sandslash', description="A blank canvas and an empty chair sits in the middle of the room.(2)")
room_063 = Room(title='Sandshrew', description='I wonder who painted these...they’re not very good.(2)')
room_064 = Room(title='Raichu', description="No thanks, I already went.(2)")
room_065 = Room(title='Arbok', description="Best not to drink while on the job.(2)")
room_066 = Room(title='Pikachu', description="This closet is about the size of my bedroom at home!(2)")
room_067 = Room(title='Ekans', description='I bet this room is bigger than most peoples homes, I don’t think I’m alone in here.(2)')
room_068 = Room(title='Fearow', description="White walls, the room is empty but the outlines of where furniture used to be, stain the walls and floor.(2)")
room_069 = Room(title='Spearow', description='The first time I’ve seen a screen in this whole house, and this wall is full of them, they’re all just static though.(2)')
room_070 = Room(title='Raticate', description="Nothing but towels in here.(2)")
room_071 = Room(title='Rattata', description="This would’ve been useful earlier.(2)")
room_072 = Room(title='Pokémon', description="Christmas lights adorn the wall, under each light is a letter. Strange.(2)")
room_073 = Room(title='Bulbasaur', description='I suppose during the day this is where you’d go to see some sun, now its more like The Twilight Zone.(2)')
room_074 = Room(title='Ivysaur', description="No washing machine nor dryer, just buckets and washing boards.(2)")
room_075 = Room(title='Venusaur', description="Lots of nice suits and shoes, all hung up and proper, whoever this guy was, he had some taste.(2)")
room_076 = Room(title='Charmander', description="In the middle of the room is a large glass case with a bunch of toy soldiers, looks like it's supposed to be The Great War.(2)")
room_077 = Room(title='Charmeleon', description='A big screen with a projector in the back, uses good old fashioned film.(2)')
room_078 = Room(title='Charizard', description="Nothing in the room except a table with a house of cards in the middle. Odd.(2)")
room_079 = Room(title='Squirtle', description='Another gymnasium, except with a small boxing ring in the middle, gotta get those frustrations out somehow.(2)')
room_080 = Room(title='Wartortle', description="An empty room with a small box in the middle, it almost sounds like there's a bird chirping in there.(2)")
room_081 = Room(title='Blastoise', description="Quiet, spacious. Whoever owns this place must be rich.(3)")
room_082 = Room(title='Caterpie', description="Enough to seat at least 100 people, who would need a dining room this big?(3)")
room_083 = Room(title='Metapod', description='I didn’t know anybody read anymore.(3)')
room_084 = Room(title='Butterfree', description="Blue walls, two cradles, this must be a baby room.(3)")
room_085 = Room(title='Weedle', description="A grand piano sits in the middle of the room, music seems to be playing on its own...(3)")
room_086 = Room(title='Kakuna', description="Who needs a study when you already have a library?(3)")
room_087 = Room(title='Beedrill', description='Who needs a library if you already have an office?!(3)')
room_088 = Room(title='Pidgey', description="I wonder if they would mind if I cooked something to eat in here...(3)")
room_089 = Room(title='Pidgeot', description='Rather plain, if I had to guess, this would be the guest bedroom.(3)')
room_090 = Room(title='Pidgeotto', description="Well, I don’t need to use it anymore...(3)")
room_091 = Room(title='Ferrothorn', description="Snow everywhere. There's also a pack of wolves roaming around.(3)")
room_092 = Room(title='Slowpoke', description="There’s billiards, darts, but no time to play when I’m already practically playing clue.(3)")
room_093 = Room(title='Goodra', description='No thanks, I’m practically dripping sweat just by being here.(3)')
room_094 = Room(title='Mew', description="Didn’t I already see a pool outside when I walked in?(3)")
room_095 = Room(title='Sylveon', description="I’ve been walking in a straight line for so long it feels like I’m walking in a spiral...(3)")
room_096 = Room(title='Togekiss', description="There’s guns and swords, what would you need all that for?.(3)")
room_097 = Room(title='Gyrados', description='Well, I guess this is where they test out their stuff from the armory.(3)')
room_098 = Room(title='Ditto', description="Painted bright orange, with a huge bed in the middle of the room and nothing else.(3)")
room_099 = Room(title='Celebi', description='Have never been one for sciencey things, myself.(3)')
room_100 = Room(title='Paras', description="These plants are alive, someone has to be around to maintain them.(3)")


room_001.save()
room_002.save()
room_003.save()
room_004.save()
room_005.save()
room_006.save()
room_007.save()
room_008.save()
room_009.save()
room_010.save()
room_011.save()
room_012.save()
room_013.save()
room_014.save()
room_015.save()
room_016.save()
room_017.save()
room_018.save()
room_019.save()
room_020.save()
room_021.save()
room_022.save()
room_023.save()
room_024.save()
room_025.save()
room_026.save()
room_027.save()
room_028.save()
room_029.save()
room_030.save()
room_031.save()
room_032.save()
room_033.save()
room_034.save()
room_035.save()
room_036.save()
room_037.save()
room_038.save()
room_039.save()
room_040.save()
room_041.save()
room_042.save()
room_043.save()
room_044.save()
room_045.save()
room_046.save()
room_047.save()
room_048.save()
room_049.save()
room_050.save()
room_051.save()
room_052.save()
room_053.save()
room_054.save()
room_055.save()
room_056.save()
room_057.save()
room_058.save()
room_059.save()
room_060.save()
room_061.save()
room_062.save()
room_063.save()
room_064.save()
room_065.save()
room_066.save()
room_067.save()
room_068.save()
room_069.save()
room_070.save()
room_071.save()
room_072.save()
room_073.save()
room_074.save()
room_075.save()
room_076.save()
room_077.save()
room_078.save()
room_079.save()
room_080.save()
room_081.save()
room_082.save()
room_083.save()
room_084.save()
room_085.save()
room_086.save()
room_087.save()
room_088.save()
room_089.save()
room_090.save()
room_091.save()
room_092.save()
room_093.save()
room_094.save()
room_095.save()
room_096.save()
room_097.save()
room_098.save()
room_099.save()
room_100.save()

# Link rooms together

room_001.connectRooms(room_002, "e")

room_002.connectRooms(room_001, "w") # SE Corner
room_002.connectRooms(room_003, "n")

room_003.connectRooms(room_002, "s") # NE Corner
room_003.connectRooms(room_004, "w")

room_004.connectRooms(room_003, "e")
room_004.connectRooms(room_005, "w")

room_005.connectRooms(room_004, "e") # NW Corner
room_005.connectRooms(room_006, "s")

room_006.connectRooms(room_005, "n")
room_006.connectRooms(room_007, "s")

room_007.connectRooms(room_006, "n") # SW Corner
room_007.connectRooms(room_008, "e")

room_008.connectRooms(room_007, "w")
room_008.connectRooms(room_009, "e")

room_009.connectRooms(room_008, "w")
room_009.connectRooms(room_010, "e")

room_010.connectRooms(room_009, "w") # SE Corner
room_010.connectRooms(room_011, "n")

room_011.connectRooms(room_010, "s")
room_011.connectRooms(room_012, "n")

room_012.connectRooms(room_011, "s")
room_012.connectRooms(room_013, "n")

room_013.connectRooms(room_012, "s") # NE Corner
room_013.connectRooms(room_014, "w")

room_014.connectRooms(room_013, "e")
room_014.connectRooms(room_015, "w")

room_015.connectRooms(room_014, "e")
room_015.connectRooms(room_016, "w")

room_016.connectRooms(room_015, "e")
room_016.connectRooms(room_017, "w")

room_017.connectRooms(room_016, "e") # NW Corner
room_017.connectRooms(room_018, "s")

room_018.connectRooms(room_017, "n")
room_018.connectRooms(room_019, "s")

room_019.connectRooms(room_018, "n")
room_019.connectRooms(room_020, "s")

room_020.connectRooms(room_019, "n")
room_020.connectRooms(room_021, "s")

room_021.connectRooms(room_020, "n") # SW Corner
room_021.connectRooms(room_022, "e")

room_022.connectRooms(room_021, "w")
room_022.connectRooms(room_023, "e")

room_023.connectRooms(room_022, "w")
room_023.connectRooms(room_024, "e")

room_024.connectRooms(room_023, "w")
room_024.connectRooms(room_025, "e")

room_025.connectRooms(room_024, "w")
room_025.connectRooms(room_026, "e")

room_026.connectRooms(room_025, "w") # SE Corner
room_026.connectRooms(room_027, "n")

room_027.connectRooms(room_026, "s")
room_027.connectRooms(room_028, "n")

room_028.connectRooms(room_027, "s")
room_028.connectRooms(room_028, "n")

room_029.connectRooms(room_028, "s")
room_029.connectRooms(room_030, "n")

room_030.connectRooms(room_029, "s")
room_030.connectRooms(room_031, "n")

room_031.connectRooms(room_030, "s") # NE Corner
room_031.connectRooms(room_032, "w")

room_032.connectRooms(room_031, "e")
room_032.connectRooms(room_033, "w")

room_033.connectRooms(room_031, "e")
room_033.connectRooms(room_034, "w")

room_034.connectRooms(room_033, "e")
room_034.connectRooms(room_035, "w")

room_035.connectRooms(room_034, "e")
room_035.connectRooms(room_036, "w")

room_036.connectRooms(room_035, "e")
room_036.connectRooms(room_037, "w")

room_037.connectRooms(room_036, "e") # NW Corner
room_037.connectRooms(room_038, "s")

room_038.connectRooms(room_037, "n")
room_038.connectRooms(room_039, "s")

room_039.connectRooms(room_038, "n")
room_039.connectRooms(room_040, "s")

room_040.connectRooms(room_039, "n")
room_040.connectRooms(room_041, "s")

room_041.connectRooms(room_040, "n")
room_041.connectRooms(room_042, "s")

room_042.connectRooms(room_041, "n")
room_042.connectRooms(room_043, "s")

room_043.connectRooms(room_042, "n") # SW Corner
room_043.connectRooms(room_044, "e")

room_044.connectRooms(room_043, "w")
room_044.connectRooms(room_045, "e")

room_045.connectRooms(room_044, "w")
room_045.connectRooms(room_046, "e")

room_046.connectRooms(room_045, "w")
room_046.connectRooms(room_047, "e")

room_047.connectRooms(room_046, "w")
room_047.connectRooms(room_048, "e")

room_048.connectRooms(room_047, "w")
room_048.connectRooms(room_049, "e")

room_049.connectRooms(room_048, "w")
room_049.connectRooms(room_050, "e")

room_050.connectRooms(room_049, "w") # SE Corner
room_050.connectRooms(room_051, "n")

room_051.connectRooms(room_050, "s")
room_051.connectRooms(room_052, "n")

room_052.connectRooms(room_051, "s")
room_052.connectRooms(room_053, "n")

room_053.connectRooms(room_052, "s")
room_053.connectRooms(room_054, "n")

room_054.connectRooms(room_053, "s")
room_054.connectRooms(room_055, "n")

room_055.connectRooms(room_054, "s")
room_055.connectRooms(room_056, "n")

room_056.connectRooms(room_055, "s")
room_056.connectRooms(room_057, "n")

room_057.connectRooms(room_056, "s")
room_057.connectRooms(room_058, "w")

room_058.connectRooms(room_057, "e")
room_058.connectRooms(room_059, "w")

room_059.connectRooms(room_058, "e")
room_059.connectRooms(room_060, "w")

room_060.connectRooms(room_059, "e")
room_060.connectRooms(room_061, "w")

room_061.connectRooms(room_060, "e")
room_061.connectRooms(room_062, "w")

room_062.connectRooms(room_061, "e")
room_062.connectRooms(room_063, "w")

room_063.connectRooms(room_062, "e")
room_063.connectRooms(room_064, "w")

room_064.connectRooms(room_063, "e")
room_064.connectRooms(room_065, "w")

room_065.connectRooms(room_064, "e") # NW Corner
room_065.connectRooms(room_066, "s")

room_066.connectRooms(room_065, "n")
room_066.connectRooms(room_067, "s")

room_067.connectRooms(room_066, "n")
room_067.connectRooms(room_068, "s")

room_068.connectRooms(room_067, "n")
room_068.connectRooms(room_069, "s")

room_069.connectRooms(room_068, "n")
room_069.connectRooms(room_070, "s")

room_070.connectRooms(room_069, "n")
room_070.connectRooms(room_071, "s")

room_071.connectRooms(room_070, "n")
room_071.connectRooms(room_072, "s")

room_072.connectRooms(room_071, "n")
room_072.connectRooms(room_073, "s")

room_073.connectRooms(room_072, "n") # SW Corner
room_073.connectRooms(room_074, "e")

room_074.connectRooms(room_073, "w")
room_074.connectRooms(room_075, "e")

room_075.connectRooms(room_074, "w")
room_075.connectRooms(room_076, "e")

room_076.connectRooms(room_075, "w")
room_076.connectRooms(room_077, "e")

room_077.connectRooms(room_076, "w")
room_077.connectRooms(room_078, "e")

room_078.connectRooms(room_077, "w")
room_078.connectRooms(room_079, "e")

room_079.connectRooms(room_078, "w")
room_079.connectRooms(room_080, "e")

room_080.connectRooms(room_079, "w")
room_080.connectRooms(room_081, "e")

room_081.connectRooms(room_080, "w")
room_081.connectRooms(room_082, "e")

room_082.connectRooms(room_081, "w") # SE Corner
room_082.connectRooms(room_083, "n")

room_083.connectRooms(room_082, "s")
room_083.connectRooms(room_084, "n")

room_084.connectRooms(room_083, "s")
room_084.connectRooms(room_085, "n")

room_085.connectRooms(room_084, "s")
room_085.connectRooms(room_086, "n")

room_086.connectRooms(room_085, "s")
room_086.connectRooms(room_087, "n")

room_087.connectRooms(room_086, "s")
room_087.connectRooms(room_088, "n")

room_088.connectRooms(room_087, "s")
room_088.connectRooms(room_089, "n")

room_089.connectRooms(room_088, "s")
room_089.connectRooms(room_090, "n")

room_090.connectRooms(room_089, "s")
room_090.connectRooms(room_091, "n")

room_091.connectRooms(room_090, "s") # NE Corner
room_091.connectRooms(room_092, "w")

room_092.connectRooms(room_091, "e")
room_092.connectRooms(room_093, "w")

room_093.connectRooms(room_092, "e")
room_093.connectRooms(room_094, "w")

room_094.connectRooms(room_093, "e")
room_094.connectRooms(room_095, "w")

room_095.connectRooms(room_094, "e")
room_095.connectRooms(room_096, "w")

room_096.connectRooms(room_095, "e")
room_096.connectRooms(room_097, "w")

room_097.connectRooms(room_096, "e")
room_097.connectRooms(room_098, "w")

room_098.connectRooms(room_097, "e")
room_098.connectRooms(room_099, "w")

room_099.connectRooms(room_098, "e")
room_099.connectRooms(room_100, "w")

room_100.connectRooms(room_099, "e") # The End NE Corner

players=Player.objects.all()
for p in players:
    p.currentRoom=room_001.id
    p.save()


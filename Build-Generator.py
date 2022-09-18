import random

champions = ["Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu",
             "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion Sol","Azir",
             "Bard", "Blitzcrank","Brand","Braum","Caitlyn","Camille","Cassiopeia",
             "Cho'Gath","Corki","Darius","Diana","Mundo","Draven","Ekko",
             "Elise","Evelynn","Ezreal","Fiddlesticks","Fiora","Fizz","Galio","Gangplank",
             "Garen", "Gnar","Gragas","Graves","Gwen","Hecarim","Heimerdinger","Illaoi",
             "Irelia","Ivern","Janna","Jarvan IV","Jax","Jayce","Jhin","Jinx","Kai'Sa",
             "Kalista","Karma","Karthus","Kassadin","Katarina","Kayle","Kayn",
             "Kennen","Kha'Zix","Kindred","Kled","Kog'Maw","LeBlanc","LeeSin","Leona",
             "Lillia","Lissandra","Lucian","Lulu","Lux","Malphite","Malzahar","Maokai",
             "Master Yi","Miss Fortune","Mordekaiser","Morgana","Nami","Nasus","Nautilus",
             "Neeko","Nidalee","Nilah","Nocturne","Nunu & Willump","Olaf","Orianna","Ornn","Pantheon",
             "Poppy","Pyke","Qiyana","Quinn","Rakan","Rammus","Rek'Sai","Rell","Renata Glasc",
             "Renekton","Rengar","Riven","Rumble","Ryze","Samira","Sejuani","Senna","Seraphine",
             "Sett","Shaco","Shen","Shyvana","Singed","Sion","Sivir","Skarner","Sona","Soraka","Swain",
             "Sylas","Syndra","Tahm Kench","Taliyah","Talon","Taric","Teemo","Thresh","Tristana",
             "Trundle","Tryndamere","Twisted Fate","Twitch","Udyr","Urgot","Varus","Vayne",
             "Veigar","Vel'Koz","Vex","Vi","Viego","Viktor","Vladimir","Volibear","Warwick",
             "Wukong","Xayah","Xerath","Xin Zhao","Yasuo","Yone","Yorick","Yuumi","Zac",
             "Zed","Zeri","Ziggs","Zilean","Zoe","Zyra"]

mythics = ["Crown of the Shattered Queen","Divine Sunderer","Duskblade of Draktharr","Eclipse","Evenshroud","Everfrost",
           "Frostfire Gauntlet","Galeforce","Goredrinker","Hextech Rocketbelt","Immortal Shieldbow","Imperial Mandate",
           "Kraken Slayer","Liandry's Anguish","Locket of the Iron Solari","Luden's Tempest","Moonstone Renewer",
           "Night Harvester","Prowler's Claw","Riftmaker","Shurelya's Battlesong","Strikebreaker","Sunfire Aegis",
           "Trinity Force","Turbo Chemtank"]

legendaries = ["Abyssal Mask","Anathema's Chains","Ardent Censer","Axiom Arc","Banshee's Veil",
               "Black Cleaver","Blade of the Ruined King","Bloodthirster","Chempunk Chainsword","Chemtech Putrifier",
               "Cosmic Drive","Dead Man's Plate","Death's Dance","Demonic Embrace","Edge of Night","Essence Reaver",
               "Fimbulwinter","Force of Nature","Frozen Heart","Gargoyle Stoneplate","Guardian Angel","Guinsoo's Rageblade",
               "Horizon Focus","Hullbreaker","Infinity Edge","Knight's Vow","Lich Bane","Lord Dominik's Regards",
               "Maw of Malmortius","Mejai's Soulstealer","Mercurial Scimitar","Mikael's Blessing","Morellonomicon",
                "Mortal Reminder","Muramana","Nashor's Tooth","Navori Quickblades","Phantom Dancer","Rabadon's Deathcap",
               "Randuin's Omen","Rapid Firecannon","Ravenous Hydra","Redemption","Runaan's Hurricane","Rylai's Crystal Scepter",
               "Seraph's Embrace","Serpent's Fang","Serylda's Grudge","Shadowflame","Silvermere Dawn","Spirit Visage",
               "Sterak's Gage","Stormrazor","The Collector","Thornmail","Titanic Hydra","Umbral Glaive",
               "Void Staff","Warmog's Armor","Winter's Approach","Wit's End","Youmuu's Ghostblade","Zeke's Convergence",
               "Zhonya's Hourglass"]

boots = ["Berserker's Greaves","Mobility Boots","Boots of Swiftness","Plated Steelcaps","Ionian Boots of Lucidity",
         "Sorcerer's Shoes","Mercury's Treads"]

sum_spell = ["Flash","Teleport","Ignite","Cleanse","Ghost","Exhaust","Smite","Heal","Barrier"]


position = ["Top","Jungle","Mid","ADC","Support"]

def another_Build():
    print()
    another_Build = input("Would you like another build? yes/no ")
    while another_Build != "yes" or "no":
        if another_Build == "yes":
            legendaries.append(first_legendary)
            legendaries.append(second_legendary)
            legendaries.append(third_legendary)
            legendaries.append(fourth_legendary)
            generate_Build(input("Choose a position: "))
            break
        elif another_Build == "no":
            quit()
        elif another_Build != "yes" or "no":
            print("Error: please answer yes/no ")
            another_Build = input("Would you like another build? yes/no ")

def generate_Build(lane):
    while True:
        while True:
        #INPUT A LANE THAT WILL DETERMINE THE SUMMONER SPELLS YOU ACQUIRE
            #IF TYPED INCORRECTLY, IT WILL ASK AGAIN
            if lane in position:
                print("Position: " + lane)
                break
            elif lane not in position:
                print("Error: Please type a correct position")
                print(position)
                lane = input("Choose a position: ")

    #CALIBRATE THE CHANCES OF GETTING CERTAIN SUMMONER SPELLS
        if lane == position[0]:
            print()
            a = str((random.choices(sum_spell, weights=(45,0,0,0,45,0,0,0,0), k=1)))
            print("First Summoner Spell: " +a)
            b = str((random.choices(sum_spell, weights=(0,45,45,33,0,33,1,33,35), k=1)))
            print("Second Summoner Spell: " +b)

        elif lane == position[1]:
            print()
            a = str((random.choices(sum_spell, weights=(46, 35, 44, 0, 45, 0, 0, 0, 0), k=1)))
            print("First Summoner Spell: " + a)
            b = str((random.choices(sum_spell, weights=(0, 0, 0, 0, 0, 0, 100, 0, 0), k=1)))
            print("Second Summoner Spell: " + b)

        elif lane == position[2]:
            print()
            a = str((random.choices(sum_spell, weights=(45, 40, 0, 0, 45, 0, 0, 0, 0), k=1)))
            print("First Summoner Spell: " + a)
            b = str((random.choices(sum_spell, weights=(0, 45, 45, 33, 0, 33, 0, 33, 35), k=1)))
            while a == b:
               b = str((random.choices(sum_spell, weights=(0, 45, 45, 33, 0, 33, 0, 33, 35), k=1)))
            print("Second Summoner Spell: " + b)

        elif lane == position[3]:
            print()
            a = str((random.choices(sum_spell, weights=(45, 0, 0, 0, 45, 0, 0, 0, 0), k=1)))
            print("First Summoner Spell: " + a)
            b = str((random.choices(sum_spell, weights=(0, 37, 30, 43, 0, 40, 0, 45, 43), k=1)))
            while a == b:
               b = (random.choices(sum_spell, weights=(0, 37, 30, 43, 0, 40, 0, 45, 43), k=1))
            print("Second Summoner Spell: " + b)

        elif lane == position[4]:
            print()
            a = str((random.choices(sum_spell, weights=(45, 0, 0, 0, 45, 0, 0, 0, 0), k=1)))
            print("First Summoner Spell: " + a)
            b = str((random.choices(sum_spell, weights=(0, 0, 45, 20, 15, 45, 0, 35, 35), k=1)))
            while a == b:
               b = (random.choices(sum_spell, weights=(0, 0, 45, 20, 15, 45, 0, 35, 35), k=1))
            print("Second Summoner Spell: " + b)

    #GET RANDOM CHAMPION, BOOTS, AND MYTHIC
        print()
        print("Champion: "+random.choice(champions))
        print()
        print("Boots: "+random.choice(boots))
        print("Mythic: " +random.choice(mythics))

    #GET FIRST LEGENDARY
        global first_legendary
        first_legendary = random.choice(legendaries)
        print("First Legendary: " +first_legendary)
        legendaries.remove(first_legendary)

    #GET THE SECOND LEGENDARY
        global second_legendary
        second_legendary = random.choice(legendaries)
        if first_legendary == "Titanic Hydra" or "Ravenous Hydra":
            second_legendary = random.choice(legendaries)
        print("Second Legendary: "+second_legendary)
        legendaries.remove(second_legendary)

    #GET THE THIRD LEGENDARY
        global third_legendary
        third_legendary = random.choice(legendaries)
        if second_legendary or first_legendary == "Titanic Hydra" or "Ravenous Hydra":
            third_legendary = random.choice(legendaries)
        print("Third Legendary: "+third_legendary)
        legendaries.remove(third_legendary)

    #GET THE FOURTH LEGENDARY
        global fourth_legendary
        fourth_legendary = random.choice(legendaries)
        if third_legendary or second_legendary or first_legendary == "Titanic Hydra" or "Ravenous Hydra":
            fourth_legendary = random.choice(legendaries)
        print("Fourth Legendary: "+fourth_legendary)
        legendaries.remove(fourth_legendary)

    #ASK IF THEY WANT ANOTHER BUILD
        another_Build()


#CALLING FUNCTION
print("League of Legends Random Build Generator")
generate_Build(input("Choose a position: "))




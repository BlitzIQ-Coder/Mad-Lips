import random
print()
print("███╗   ███╗ █████╗ ██████╗       ██╗     ██╗██████╗ ███████╗")
print("████╗ ████║██╔══██╗██╔══██╗      ██║     ██║██╔══██╗██╔════╝")
print("██╔████╔██║███████║██║  ██║█████╗██║     ██║██████╔╝███████╗")
print("██║╚██╔╝██║██╔══██║██║  ██║╚════╝██║     ██║██╔═══╝ ╚════██║")
print("██║ ╚═╝ ██║██║  ██║██████╔╝      ███████╗██║██║     ███████║")
print("╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝       ╚══════╝╚═╝╚═╝     ╚══════╝  Created By: BlitzIQ")
print()
print("Fill the below details to make a story")
print()
gender=int(input("Which gender is your character? 1. MALE 2. FEMALE\n"))
print()
name=str(input("Enter the name of your character:\n"))
print()
genre=int(input("What genre do you want your story to be? 1. Romantic 2. Action 3. Adventure\n"))
print()
while True:
    if gender == 1:
        if genre == 1:
            Sentence_starter_romantic = ['In a quaint little town,', 'On a warm summer evening,', 'Under the starry sky,']
            character_romantic = [' there lived a young man named '+ str(name)+'.', ' there was a man named '+ str(name)+'.', ' there was a poet named '+ str(name)+'.']
            time_romantic = [' One beautiful morning', ' During a sunset stroll']
            story_plot_romantic = [' he was wandering through', ' he was lost in thought while walking around']
            place_romantic = [' the blooming gardens', ' the serene lake']
            second_character_romantic = [' he met a charming stranger', ' he encountered a mysterious lady']
            age_romantic = [' who was in her early 20s', ' who looked around the same age']
            work_romantic = [' sketching the landscape.....', ' reading a book on a bench......']

            print(random.choice(Sentence_starter_romantic)+random.choice(character_romantic)+random.choice(time_romantic)+random.choice(story_plot_romantic) +random.choice(place_romantic)+random.choice(second_character_romantic)+random.choice(age_romantic)+random.choice(work_romantic)) 
            print("To Be Continued...>_<")
            break                                                                                                                               

        elif genre == 2:
            Sentence_starter_action = ['In the heart of the city', 'On a stormy night', 'Amidst the chaos of war']
            character_action = [' there was a fearless soldier named '+ str(name)+'.', ' there was a rogue agent named '+ str(name)+'.', ' there was a skilled martial artist named'+ str(name)+'.']
            time_action = [' One intense evening', ' During a high-speed chase']
            story_plot_action = [' he was tracking down', ' he was escaping from']
            place_action = [' the abandoned warehouse', ' the dark alley']
            second_character_action = [' he encountered an enemy spy', ' he crossed paths with a rival gang member']
            age_action = [' who was in his mid-30s', ' who was battle-hardened and tough']
            work_action = [' planning an ambush......', ' preparing for a fight......']

            print(random.choice(Sentence_starter_action)+random.choice(character_action)+random.choice(time_action)+random.choice(story_plot_action) +random.choice(place_action)+random.choice(second_character_action)+random.choice(age_action)+random.choice(work_action)) 
            print("To Be Continued...>_<")
            break 

        elif genre == 3:
            Sentence_starter_adventure = ['Long ago in a distant land', 'On a remote island', 'In the middle of a vast desert']
            character_adventure = [' there lived an explorer named '+ str(name)+'.', ' there was a brave warrior named '+ str(name)+'.', ' there was a skilled hunter named '+ str(name)+'.']
            time_adventure = [' One day during a dangerous journey', ' On a stormy night']
            story_plot_adventure = [' he was searching for', ' he was venturing into']
            place_adventure = [' the hidden cave', ' the dense jungle']
            second_character_adventure = [' he encountered a wild beast', ' he met a fellow traveler']
            age_adventure = [' who was seasoned and wise', ' who was young and eager']
            work_adventure = [' guarding a secret treasure....', ' looking for a way out....']

            print(random.choice(Sentence_starter_adventure)+random.choice(character_adventure)+random.choice(time_adventure)+random.choice(story_plot_adventure) +random.choice(place_adventure)+random.choice(second_character_adventure)+random.choice(age_adventure)+random.choice(work_adventure)) 
            print("To Be Continued...>_<")
            break 
    
    elif gender == 2:
        if genre == 1:
            Sentence_starter_romantic = ['In a charming village', 'On a tranquil evening', 'Under the moonlit sky']
            character_romantic = [' there lived a young woman named '+ str(name)+'.', ' there was a girl named '+ str(name)+'.', ' there was an artist named '+ str(name)+'.']
            time_romantic = [' One peaceful morning', ' During a quiet walk']
            story_plot_romantic = [' she was strolling through', ' she was daydreaming while wandering around']
            place_romantic = [' the blossoming gardens', ' the quiet riverside']
            second_character_romantic = [' she encountered a handsome stranger', ' she met a mysterious man']
            age_romantic = [' who was in his late 20s', ' who appeared to be her age']
            work_romantic = [' painting the scenery....', ' playing a soft melody on a guitar....']

            print(random.choice(Sentence_starter_romantic)+random.choice(character_romantic)+random.choice(time_romantic)+random.choice(story_plot_romantic) +random.choice(place_romantic)+random.choice(second_character_romantic)+random.choice(age_romantic)+random.choice(work_romantic)) 
            print("To Be Continued...>_<")
            break

        elif genre == 2:
            Sentence_starter_action = ['In a bustling city', 'On a dark and stormy night', 'Amidst the chaos of a battle']
            character_action = [' there was a fearless woman named '+ str(name)+'.', ' there was a rogue operative named '+ str(name)+'.', ' there was a skilled fighter named '+ str(name)+'.']
            time_action = [' One intense afternoon', ' During a high-stakes mission']
            story_plot_action = [' she was hunting down', ' she was running from']
            place_action = [' the deserted warehouse', ' the shadowy alley']
            second_character_action = [' she confronted an enemy agent', ' she clashed with a rival operative']
            age_action = [' who was in her 30s', ' who was experienced and tough']
            work_action = [' setting a trap....', ' getting ready for a showdown....']

            print(random.choice(Sentence_starter_action)+random.choice(character_action)+random.choice(time_action)+random.choice(story_plot_action) +random.choice(place_action)+random.choice(second_character_action)+random.choice(age_action)+random.choice(work_action)) 
            print("To Be Continued...>_<")
            break

        elif genre == 3:
            Sentence_starter_adventure = ['In a faraway kingdom', 'On an uncharted island', 'In the depths of a mysterious forest']
            character_adventure = [' there lived a daring adventurer named '+ str(name)+'.', ' there was a brave warrior named '+ str(name)+'.', ' there was a resourceful huntress named Nora'+ str(name)+'.']
            time_adventure = [' One day during a perilous quest', ' On a foggy morning']
            story_plot_adventure = [' she was searching for', ' she was exploring']
            place_adventure = [' the hidden temple', ' the ancient ruins']
            second_character_adventure = [' she encountered a mystical creature', ' she met a fellow explorer']
            age_adventure = [' who was wise beyond years', ' who was young but determined']
            work_adventure = [' protecting a sacred relic....', ' mapping out the terrain....']

            print(random.choice(Sentence_starter_adventure)+random.choice(character_adventure)+random.choice(time_adventure)+random.choice(story_plot_adventure) +random.choice(place_adventure)+random.choice(second_character_adventure)+random.choice(age_adventure)+random.choice(work_adventure)) 
            print("To Be Continued...>_<")
            break 

#Edit the Contents if you want more stories, Use Chatgpt in case
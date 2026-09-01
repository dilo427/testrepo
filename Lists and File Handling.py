# Final Project: Lists and File Handling
# Ratings of Various Parts of my Favorite Video Games on a 1-10 scale
# Yogi Chopra

# Elements
print("Games:","\t","\t","\t","\t","\t","Gameplay:","\t","Story:","\t",
      "Characters:","\t","Fun:","\t\t\t\t","Replayability:",
      "\t","Game/Art Design:","\t","Music/Soundtrack:","\t","Recommend:"
      ,"\t","Overall Rating:")
games = ["Portal 1/2","Sekiro: SDT","God of War Series","Call of Duty BO1",
         "Persona 5 Royal","Street Fighter 4", "TWD: Telltale",
         "Bioshock Series","Witcher 3: Wild Hunt","Asura's Wrath"]

# Attributes
rating_gameplay = ["\t\t 8","\t\t 10","6","\t 6",
                   "\t 5","\t 9","\t 3","\t 7","4","\t 8"]

rating_story = ["\t 8","\t 5","\t 10","\t 6","\t 9","\t 2",
                "\t 8","\t 10","\t 10","\t 7"]

rating_characters = ["\t\t 5","\t\t 6","\t 9","\t\t 8","\t\t 7",
                     "\t\t 8","\t\t 10","\t 8","\t 10","\t\t 5"]

rating_fun = ["\t\t\t 10","\t\t\t 10","\t\t\t 7","\t\t\t 8","\t\t\t 7",
              "\t\t\t 7","\t\t 6","\t\t\t 7","\t\t 7","\t\t\t 10"]

rating_replayability = ["\t\t\t 10","\t\t\t 6","\t\t\t\t 4","\t\t\t\t 10",
                 "\t\t\t\t 5", "\t\t\t\t 10","\t\t\t\t 3","\t\t\t\t 7",
                 "\t\t\t\t 9","\t\t\t 5"]

rating_game_and_art_design = ["\t\t\t 10","\t\t\t\t 7","\t\t\t\t 9",
                              "\t\t\t 6","\t\t\t\t 10","\t\t\t 8",
                              "\t\t\t\t 7","\t\t\t\t 10","\t\t\t\t 10",
                              "\t\t\t\t 8"]

rating_music_and_soundtrack = ["\t\t\t 7","\t\t\t\t 6","\t\t\t\t 10",
                               "\t\t\t\t 8","\t\t\t 10","\t\t\t\t 5",
                               "\t\t\t\t 4","\t\t\t 4","\t\t\t 10",
                               "\t\t\t\t 3"]

rating_recommend = ["\t\t\t\t 10","\t\t\t\t 5","\t\t\t 8","\t\t\t\t 6",
               "\t\t\t 4","\t\t\t\t 5","\t\t\t\t 9","\t\t\t\t 10",
               "\t\t\t 7","\t\t\t\t 6"]

rating_overall_rating = ["\t\t 10","\t\t\t 8","\t\t\t 10","\t\t\t 8",
                         "\t\t\t 8","\t\t\t 7","\t\t\t 10","\t\t 9",
                         "\t\t\t 9","\t\t\t 8"]

# Parallel Array
for i in range(len(games)):
    print(games[i],"  \t",rating_gameplay[i],"  \t",rating_story[i],
          "\t", rating_characters[i], "\t", rating_fun[i],
          "\t", rating_replayability[i],"\t",
          rating_game_and_art_design[i],"\t",
          rating_music_and_soundtrack[i],
          "\t", rating_recommend[i],"\t", rating_overall_rating[i],)
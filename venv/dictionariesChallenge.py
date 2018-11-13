# Modify the program so that the exits is a dictionary rather than a list,
# with the keys being the numbers of the locations and the values being
# dictionaries holding the exits (as they do at present). No change should
# be needed to the actual code.
#
# Once that is working, create another dictionary that contains words that
# players may use. These words will be the keys, and their values will be
# a single letter that the program can use to determine which way to go.

locations = {1: "You are in the Road",
             2: "You are in the Hill",
             3: "You are in a Building",
             4: "You are in a Valley",
             5: "You are in a Forest"}

exits = {0: {"Q": 0},
         1: {"N": 5, "W": 2, "E": 3, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W"}

# loc = 1
# while True:
#     availableExits = ", ".join(exits[loc].keys())
#     print("Available exits are: {}".format(availableExits))
#     user_input = input("Enter the direction you want to go from the above choices: ").upper()
#     if len(user_input) > 1:
#         for word in vocabulary:
#             if word in user_input:
#                 user_input = vocabulary[word]
#     loc = exits[loc][user_input]
#     if user_input == "Q":
#         break
#     if user_input in availableExits:
#         usr_location = locations[loc]
#         print(usr_location)
#     else:
#         print("You cannot go in that direction.")
    
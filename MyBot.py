# keep these three import statements
import game_API
import fileinput
import json

# your import statements here
import random
import utils

stances = ["Rock", "Paper", "Scissors"]

first_line = True # DO NOT REMOVE
first_node = True # Used for decision making on the first node 
turn_counter = 0 

def duel(game): 
    # https://math.stackexchange.com/questions/803488/optimal-strategy-for-rock-paper-scissors-with-different-rewards
    # First try
    # Reward metric for a move is move damage - enemy trumping move damage
    op = game.get_opponent()
    me = game.get_self()
    
    rock_weight = me.rock - op.paper
    paper_weight = me.paper - op.scissors
    scissors_weight = me.scissors - op.rock
    
    rand = random.randint(1, rock_weight + paper_weight + scissors_weight)
    chosen_stance = null
    if rand <= rock_weight:
        chosen_stance = stances[0]
    elif rand <= rock_weight + paper_weight:
        chosen_stance = stances[1]
    else:
        chosen_stance = stances[2]

"""
Move these to Utils 
"""
def initialize_paths(game): 
    paths = [] 
    for path in utils.cycles: 
        paths.append(utils.Path(path, game))
    return paths

def rank_paths(paths, game): 
    path_rankings = dict()
    for index in range(len(paths)): 
        path_rankings[index] = paths[index].evaluate_path_score(game)
    sort = sorted(path_rankings.items(), key = lambda x: x[1], reverse = True)
    return paths[sort[0][0]]
    # return [x[0] for x in sort]

def select_path(paths, game):   
    ranking = rank_paths(paths, game)
    return ranking[0] # Greedy selection -> maybe do something more sophisticated later

def get_strongest_stance(player): 
    if player.paper >= player.rock and player.paper >= player.scissors:
        return "Paper"
    elif player.scissors >= player.rock and player.scissors > player.paper:
        return "Scissors"
    else: 
        return "Rock"

next_node_index = -1
path = None 
paths = None 

# main player script logic
# DO NOT CHANGE BELOW ----------------------------
for line in fileinput.input():
    if first_line:
        game = game_API.Game(json.loads(line))
        first_line = False
        continue
    game.update(json.loads(line))
# DO NOT CHANGE ABOVE ---------------------------

    # code in this block will be executed each turn of the game

    op = game.get_opponent()
    me = game.get_self()

    if paths == None: 
        paths = initialize_paths(game)
    if path == None: 
        path = rank_paths(paths, game)

    """ 
    Code for choosing stance
    """ 
    current_monster = game.get_monster(me.location) 
    if me.movement_counter == me.speed + 1: # We are going to move next turn 
        next_monster = game.get_monster(me.destination)
        if not next_monster.dead: 
            chose_stance = utils.stance_counters[next_monster.stance]
    else: 
        if not current_monster.dead: 
            chosen_stance = utils.stance_counters[current_monster.stance]
        else: 
            chose_stance = get_strongest_stance(me)


    """ 
    Code for determining the next destination
    """
    for i in range(path.length): 
       game.log(str(path[i]))

    if me.location == me.destination: 
        if me.location == 0: 
            path = rank_paths(paths, game) 
            next_node_index = 0 
            destination_node = path[next_node_index]
        else: 
            next_node_index += 1 
            destination_node = path[next_node_index]
    else: 
        destination_node = path[next_node_index] # This could be made more efficient for sure 

    turn_counter += 1

    # submit your decision for the turn (This function should be called exactly once per turn)
    game.submit_decision(destination_node, chosen_stance)

    if turn_counter > 300: 
        duel(game) 

""" 
    if me.location == me.destination: # check if we have moved this turn
        # get all living monsters closest to me
        monsters = game.nearest_monsters(me.location, 1)

        # choose a monster to move to at random
        monster_to_move_to = monsters[random.randint(0, len(monsters)-1)]

        # get the set of shortest paths to that monster
        paths = game.shortest_paths(me.location, monster_to_move_to.location)
        destination_node = paths[random.randint(0, len(paths)-1)][0]
    else:
        destination_node = me.destination

    if game.has_monster(me.location):
        # if there's a monster at my location, choose the stance that damages that monster
        chosen_stance = get_winning_stance(game.get_monster(me.location).stance)
    else:
        # otherwise, pick a random stance
        chosen_stance = stances[random.randint(0, 2)]
"""

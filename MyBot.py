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
health_respawn_timer = -1

def duel(game): 
    # https://math.stackexchange.com/questions/803488/optimal-strategy-for-rock-paper-scissors-with-different-rewards
    # First try
    # Reward metric for a move is move damage - enemy trumping move damage
    op = game.get_opponent()
    me = game.get_self()
    
    rock_weight = me.rock - op.paper if me.rock - op.paper > 0 else 1
    paper_weight = me.paper - op.scissors if me.paper - op.scissors > 0 else 1
    scissors_weight = me.scissors - op.rock if me.scissors - op.rock > 0 else 1
    
    rand = random.randint(1, rock_weight + paper_weight + scissors_weight)
    chosen_stance = null
    if rand <= rock_weight:
        chosen_stance = stances[0]
    elif rand <= rock_weight + paper_weight:
        chosen_stance = stances[1]
    else:
        chosen_stance = stances[2]
        
    game.submit_decision(0, chosen_stance)

"""
Move these to Utils 
"""
def get_paths_to_zero(game):
    maxdist = health_respawn_timer / (7 - game.get_self().speed)
    curr = [[game.get_self().location]]
    dist = 0
    while dist < maxdist:
        next = []
        for elem in curr:
            neighbors = game.get_adjacent_nodes(elem[-1])
            for neighbor in neighbors:
                copy = elem.copy()
                copy.append(neighbor)
                next.append(copy)
        curr = next
        dist += 1
    
    paths = []
    for path in curr:
        if path[-1] == 0:
            paths.append(path)
            
    return paths
    
def initialize_paths(game): 
    paths = [] 
    for path in utils.possible_paths: 
        paths.append(utils.Path(path, game))
    return paths

def rank_paths(paths, game): 
    path_rankings = dict()
    for index in range(len(paths)): 
        path_rankings[index] = paths[index].evaluate_path_score(game)
        # game.log("Path {} score: {}".format(index, paths[index].evaluate_path_score(game)))
    sort = sorted(path_rankings.items(), key = lambda x: x[1], reverse = True)
    return paths[sort[0][0]]

def select_path(paths, game):   
    ranking = rank_paths(paths, game)
    return ranking[0] # Greedy selection -> maybe do something more sophisticated later
    game.log(ranking[0])
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
    
    """
    if game.get_monster(0).dead and health_respawn_timer == -1:
        health_respawn_timer = 7 - game.get_monster(0).speed
    else if game.get_monster(0).dead:
        health_respawn_timer--
    else:
        health_respawn_timer = -1
    """

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
    if me.location == me.destination: # We just finished moving
        if me.location == 0: 
            path = rank_paths(paths, game) 
            next_node_index = 0 
        else: 
            next_node_index += 1 

    destination_node = path[next_node_index]
    turn_counter += 1

    # submit your decision for the turn (This function should be called exactly once per turn)
    if turn_counter > 300:
        duel(game)
    else:
        game.submit_decision(destination_node, chosen_stance)

import game_API 

# General Imports 
import math 

""" 
Utility functions for the AI Bot
""" 

stances = ["Rock", "Paper", "Scissors"]
stance_counters = {"Rock": "Paper", 
					"Paper": "Scissors",
					"Scissors": "Rock",
					"Invalid Stance": "Paper"}

cycles = [['Node_6', 'Node_7', 'Node_8', 'Node_9', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_2', 'Node_4', 'Node_5', 'Node_6', 'Node_0'], 
		  ['Node_6', 'Node_5', 'Node_4', 'Node_2', 'Node_1', 'Node_0'], 
		  ['Node_10', 'Node_9', 'Node_8', 'Node_7', 'Node_6', 'Node_0'], 
		  ["Node_1", 'Node_3', "Node_2", "Node_4", "Node_5", "Node_6", "Node_0"],
		  ['Node_6', 'Node_5', 'Node_4', 'Node_13', 'Node_12', 'Node_11', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_2', 'Node_4', 'Node_13', 'Node_12', 'Node_11', 'Node_10', 'Node_0'], 
		  ['Node_10', 'Node_11', 'Node_12', 'Node_13', 'Node_4', 'Node_5', 'Node_6', 'Node_0'], 
		  ['Node_10', 'Node_11', 'Node_12', 'Node_13', 'Node_4', 'Node_2', 'Node_1', 'Node_0'], 
		  ['Node_1', 'Node_3', 'Node_2', 'Node_4', 'Node_13', 'Node_12', 'Node_11', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_5', 'Node_4', 'Node_13', 'Node_14', 'Node_8', 'Node_9', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_2', 'Node_4', 'Node_13', 'Node_14', 'Node_8', 'Node_9', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_2', 'Node_4', 'Node_13', 'Node_14', 'Node_8', 'Node_7', 'Node_6', 'Node_0'], 
		  ['Node_10', 'Node_9', 'Node_8', 'Node_14', 'Node_13', 'Node_4', 'Node_5', 'Node_6', 'Node_0'], 
		  ['Node_10', 'Node_9', 'Node_8', 'Node_14', 'Node_13', 'Node_4', 'Node_2', 'Node_1', 'Node_0'],
		  ['Node_6', 'Node_7', 'Node_8', 'Node_14', 'Node_13', 'Node_4', 'Node_2', 'Node_1', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_13', 'Node_4', 'Node_2', 'Node_3', 'Node_1', 'Node_0'],
		  ['Node_6', 'Node_7', 'Node_8', 'Node_14', 'Node_13', 'Node_12', 'Node_11', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_3', 'Node_2', 'Node_4', 'Node_13', 'Node_12', 'Node_16', 'Node_10', 'Node_0'],
		  ['Node_10', 'Node_11', 'Node_12', 'Node_13', 'Node_14', 'Node_8', 'Node_7', 'Node_6', 'Node_0'], 
		  ['Node_1', 'Node_3', 'Node_2', 'Node_4', 'Node_13', 'Node_14', 'Node_8', 'Node_9', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_3', 'Node_2', 'Node_4', 'Node_13', 'Node_14', 'Node_8', 'Node_7', 'Node_6', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_22', 'Node_19', 'Node_20', 'Node_13', 'Node_4', 'Node_5', 'Node_6', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_22', 'Node_19', 'Node_20', 'Node_13', 'Node_4', 'Node_2', 'Node_1', 'Node_0'], 
		  ['Node_6', 'Node_5', 'Node_4', 'Node_13', 'Node_20', 'Node_21', 'Node_22', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_2', 'Node_4', 'Node_13', 'Node_20', 'Node_21', 'Node_22', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_7', 'Node_8', 'Node_14', 'Node_19', 'Node_20', 'Node_13', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_5', 'Node_4', 'Node_13', 'Node_20', 'Node_19', 'Node_22', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_2', 'Node_4', 'Node_13', 'Node_20', 'Node_19', 'Node_22', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_5', 'Node_4', 'Node_13', 'Node_12', 'Node_16', 'Node_10', 'Node_0', 'Node_10', 'Node_0', 'Node_10'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_22', 'Node_21', 'Node_20', 'Node_13', 'Node_4', 'Node_5', 'Node_6', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_22', 'Node_21', 'Node_20', 'Node_13', 'Node_4', 'Node_2', 'Node_1', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_13', 'Node_20', 'Node_19', 'Node_14', 'Node_8', 'Node_7', 'Node_6', 'Node_0'], 
		  ['Node_1', 'Node_3', 'Node_2', 'Node_4', 'Node_13', 'Node_20', 'Node_21', 'Node_22', 'Node_12', 'Node_16', 'Node_10', 'Node_0'],
		  ['Node_1', 'Node_3', 'Node_2', 'Node_4', 'Node_13', 'Node_20', 'Node_19', 'Node_22', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_5', 'Node_4', 'Node_13', 'Node_12', 'Node_16', 'Node_17', 'Node_18', 'Node_15', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_2', 'Node_4', 'Node_13', 'Node_12', 'Node_16', 'Node_17', 'Node_18', 'Node_15', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_7', 'Node_8', 'Node_14', 'Node_13', 'Node_20', 'Node_21', 'Node_22', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_5', 'Node_4', 'Node_13', 'Node_20', 'Node_19', 'Node_14', 'Node_13', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_2', 'Node_4', 'Node_13', 'Node_20', 'Node_19', 'Node_14', 'Node_13', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_7', 'Node_8', 'Node_14', 'Node_13', 'Node_20', 'Node_19', 'Node_22', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_7', 'Node_8', 'Node_14', 'Node_13', 'Node_12', 'Node_16', 'Node_10', 'Node_0', 'Node_10', 'Node_0', 'Node_10'],
		  ['Node_10', 'Node_16', 'Node_15', 'Node_18', 'Node_17', 'Node_16', 'Node_12', 'Node_13', 'Node_4', 'Node_5', 'Node_6', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_15', 'Node_18', 'Node_17', 'Node_16', 'Node_12', 'Node_13', 'Node_4', 'Node_2', 'Node_1', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_22', 'Node_21', 'Node_20', 'Node_13', 'Node_14', 'Node_8', 'Node_7', 'Node_6', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_13', 'Node_14', 'Node_19', 'Node_20', 'Node_13', 'Node_4', 'Node_5', 'Node_6', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_13', 'Node_14', 'Node_19', 'Node_20', 'Node_13', 'Node_4', 'Node_2', 'Node_1', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_22', 'Node_19', 'Node_20', 'Node_13', 'Node_14', 'Node_8', 'Node_7', 'Node_6', 'Node_0'],  
		  ['Node_1', 'Node_3', 'Node_2', 'Node_4', 'Node_13', 'Node_12', 'Node_16', 'Node_17', 'Node_18', 'Node_15', 'Node_16', 'Node_10', 'Node_0'],
 		  ['Node_1', 'Node_3', 'Node_2', 'Node_4', 'Node_13', 'Node_20', 'Node_19', 'Node_14', 'Node_13', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_7', 'Node_8', 'Node_14', 'Node_13', 'Node_12', 'Node_16', 'Node_17', 'Node_18', 'Node_15', 'Node_16', 'Node_10', 'Node_0'],
		  ['Node_10', 'Node_16', 'Node_15', 'Node_18', 'Node_17', 'Node_16', 'Node_12', 'Node_13', 'Node_14', 'Node_8', 'Node_7', 'Node_6', 'Node_0']] 
		  
class Path: 
	"""
	A class that represents a path through a sequence of nodes 
	"""
	def __init__(self, nodes, game):
		"""
		Nodes can just be the list of strings from the cycles global variable 
		"""
		self.path = []
		self.path_indices = [] 
		for node in nodes: 
			self.path.append(game.nodes[int(node[node.index("_") + 1:])]) # Assuming that the list of nodes in the game variable is in order. It should be, based on how the API generates it...
			self.path_indices.append(int(node[node.index("_") + 1:]))

		self.length = len(nodes) # Might want to do len(nodes) - 1 to exclude Node_0
		self.current_node = 0 

	def get_next_node(self):
		if self.current_node + 1 < self.total_num_nodes:
			return self.path[self.current_node + 1]
		else:
			return None

	def move_next_node(self):
		self.current_node += 1

	def __getitem__(self, key): 
		return self.path_indices[key]

	""" 
	Overloading comparison operators
	"""
	def __lt__(self, other):
		ps_self = self.evaluate_path_score()
		ps_other = other.evaluate_path_score()
		if ps_self < ps_other: 
			return True 
		else: 
			return False

	def __le__(self, other): 
		ps_self = self.evaluate_path_score()
		ps_other = other.evaluate_path_score()
		if ps_self <= ps_other: 
			return True 
		else: 
			return False

	def __gt__(self, other):
		ps_self = self.evaluate_path_score()
		ps_other = other.evaluate_path_score()
		if ps_self > ps_other: 
			return True 
		else: 
			return False

	def __ge__(self, other): 
		ps_self = self.evaluate_path_score()
		ps_other = other.evaluate_path_score()
		if ps_self >= ps_other: 
			return True 
		else: 
			return False

	def __eq__(self, other):
		if other == None: 
			return False
		ps_self = self.evaluate_path_score()
		ps_other = other.evaluate_path_score()
		if ps_self == ps_other: 
			return True 
		else: 
			return False		

	def __ne__(self, other): 
		ps_self = self.evaluate_path_score()
		ps_other = other.evaluate_path_score()
		if ps_self != ps_other: 
			return True 
		else: 
			return False		

	def evaluate_path_score(self, game):
		"""
		Allows us to rank this path based on current board conditions 
		This is hard
		"""
		monsters = game.get_all_monsters()
		my_monsters = []
		for node in self.path:
			monster = game.get_monster(node)
			if monster.name != "No Monster": 
				my_monsters.append(game.get_monster(node))

		# my_monsters[i].dead
		player = game.get_self()


		weight_sum = 0

		for monster in my_monsters:
			stance = stance_counters[monster.stance]
			if stance is 'Rock':
				attack = player.rock
			elif stance is 'Paper':
				attack = player.paper
			elif stance is 'Scissors':
				attack = player.scissors

			speed = player.speed


			val = weight_cal(monster, attack, speed)
			weight_sum = weight_sum + val

		""" 
		for node in self.path:
			monster = my_monsters[node]
			stance = stance_counters[monster.stance]
			if stance is 'Rock':
				attack = player.rock
			elif stance is 'Paper':
				attack = player.paper
			elif stance is 'Scissors':
				attack = player.scissors

			speed = player.speed


			val = weight_cal(monster, attack, speed)
			weight_sum = weight_sum + val
		""" 

		return weight_sum

def weight_cal(monster, attack, speed):
	hpl = hp_loss(monster, attack, speed)
	R_gain, P_gain, S_gain, Spd_gain = gain(monster, attack, speed)
	time = time_spend(monster, attack, speed)

	score = (-10) * hpl + 3 * (R_gain + P_gain + S_gain) + 5 * Spd_gain + (-2) * time

	return score


def time_spend(monster, attack, speed):
	# attack value is the corresponding resources you have
	move_time = 7 - speed
	kill_time = monster.health / attack

	if move_time <= kill_time:
		time = move_time
	else:
		time = kill_time
	return time

def hp_loss(monster, attack, speed):
	time = time_spend(monster, attack, speed)
	hp_loss = monster.attack * time

	return hp_loss

def gain(monster, attack, speed):
	move_time = 7 - speed
	kill_time = monster.health / attack

	if move_time <= kill_time:
		R_gain = 0
		P_gain = 0
		S_gain = 0
		Spd_gain = 0
	else:
		R_gain = monster.death_effects.rock
		P_gain = monster.death_effects.paper
		S_gain = monster.death_effects.scissors
		Spd_gain = monster.death_effects.speed

	return R_gain, P_gain, S_gain, Spd_gain







def get_player_strength(player, stance): 
	"""
	Returns the stat value associated with a certain stance. Can be used for either player. 
	"""
	if stance == "Rock": 
		return player.rock
	elif stance == "Paper": 
		return player.paper
	elif stance == "Scissors": 
		return player.scissors

def calc_num_turns_to_kill_monster(player, monster):
	""" 
	Calculates how many turns it would take to kill a specific monster. Useful for either player.

	Input player should be of type Player 
	Input monster should be of type Monster
	""" 
	monster_hp = monster.health
	monster_stance = monster.stance
	player_strength = get_player_strength(player, stance_counters[monster_stance])
	return math.ceil(monster_hp / player_strength) # Round up on the number of turns needed 
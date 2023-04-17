
#################################################################
# FILE : ex11.py
# WRITER : yoav schneider , yoav.schneider , 313594087
# EXERCISE : intro2cs2 ex11 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH: yonatan levy, shir giat, , gabriel dubin
# WEB PAGES I USED: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# NOTES:
#################################################################

import copy, itertools

class Node:
	"""
	creates a node in the tree
	"""
	def __init__(self, data, positive_child=None, negative_child=None):
		"""
		a Node object constructor
		:param data: the data the node holds
		:param positive_child: left son of the node
		:param negative_child: right son of the node
		"""
		self.data = data
		self.positive_child = positive_child
		self.negative_child = negative_child


class Record:
	def __init__(self, illness, symptoms):
		self.illness = illness
		self.symptoms = symptoms


def parse_data(filepath):
	with open(filepath) as data_file:
		records = []
		for line in data_file:
			words = line.strip().split()
			records.append(Record(words[0], words[1:]))
		return records


class Diagnoser:
	def __init__(self, root: Node):
		self.root = root

	def diagnose(self, symptoms):
		travler = self.root
		copy_symptoms = copy.deepcopy(symptoms)
		return self.__diagnose_helper(copy_symptoms, travler)

	def __diagnose_helper(self, symptoms, travler):
		"""
		sub function of diagnose, runs through the tree and returns the right illness according to the symptoms
		:param symptoms: a list a symptoms
		:param travler: a node object that runs through the tree
		:return: a string which is the name of the disease
		"""
		if travler is None:
			return
		if travler.positive_child is None and travler.negative_child is None:
			return travler.data
		for symptom in symptoms:
			if symptom == travler.data:
				travler = travler.positive_child
				return self.__diagnose_helper(symptoms, travler)
		travler = travler.negative_child
		return self.__diagnose_helper(symptoms, travler)

	def calculate_success_rate(self, records):
		if len(records) == 0:
			raise ValueError("error empty tree")
		success = 0
		for record in records:
			disease = self.diagnose(record.symptoms)
			if disease == record.illness:
				success += 1
		return success/len(records)
###############################

	def all_illnesses(self):
		retrun_lst = self.rearrange(self.__all_illnesses_helper([]))
		for element in retrun_lst:
			if element == None:
				retrun_lst.remove(element)
		return retrun_lst

	def __all_illnesses_helper(self, lst_disease):
		"""
		all_illnesses sub function, returns a list of all the diseases in the tree
		:param lst_disease: a list of strings of all the disease in the tree
		:return: returns lst_disease, see above ^
		"""
		if self.root is None:
			return None
		if self.root.data is None:
			return None
		if self.root.positive_child is None and self.root.negative_child is None:
			lst_disease.append(self.root.data)
		Diagnoser(self.root.negative_child).__all_illnesses_helper(lst_disease)
		Diagnoser(self.root.positive_child).__all_illnesses_helper(lst_disease)
		return lst_disease

	def rearrange(self, lst):
		"""
		all_illnesses sub function, take an unorganized list and returns organized one: deletes duplicates and arranges
		the diseases by number of times each one is appeared in the list
		:param lst: list of diseases
		:return: organized list of diseases
		"""
		if len(lst) == 0:
			return []
		dicty = {}
		return_lst = []
		for element in lst:
			dicty[element] = lst.count(element)
		dicty = sorted(dicty.items(), key=lambda dicty: dicty[1])
		for item in dicty:
			return_lst.append(item[0])
		return return_lst[::-1]
################################33

	def paths_to_illness(self, illness):
		cursor = Diagnoser(self.root)
		return self.__path_to_illness_core(illness, [], [], cursor)

	def __path_to_illness_core(self, illness, illnes_lst, path, cursor):
		"""
		sub function of paths_to_illness, runs through the tree toward a certain disease and document the path to it
		:param illness: string, what illness are we looking for in th tree
		:param illnes_lst: a list of lists, a list contains the paths to the illness
		:param path: a list of boolean variables, a single path to the illenss. True = left, False = right
		:param cursor: an Diagnoser object, runs through the tree
		:return: returns the list of lists illnes_lst, see above ^
		"""
		if cursor.root is None:
			return
		if cursor.root.data == illness:
			path_copy = copy.deepcopy(path)
			illnes_lst.append(path_copy)
			return illnes_lst
		back_cursor = cursor.root
		path, cursor = self.go_left(path, cursor)
		cursor.__path_to_illness_core(illness, illnes_lst, path, cursor)
		path.pop()
		cursor.root = back_cursor
		path, cursor = self.go_right(path, cursor)
		cursor.__path_to_illness_core(illness,illnes_lst, path, cursor)
		path.pop()
		return illnes_lst

	def go_left(self, path, cursor):
		"""
		__path_to_illness_core sub function, goes left (assign the left son to the cursor's root) in the tree
		and document the action (adds True to the path list)
		:param path: a list of boolean variable, what path have we taken until now
		:param cursor: a Diagnoser object, our "vehicle" which we use to run through the tree
		:return: a list of boolean variables (path) and a Diagnoser object with it's newly assign root (cursor)
		"""
		path.append(True)
		cursor.root = cursor.root.positive_child
		return path, cursor

	def go_right(self, path, cursor):
		"""
		__path_to_illness_core sub function, goes right (assign the right son to the cursor's root) in the tree
		and document the action (adds False to the path list)
		:param path: a list of boolean variable, what path have we taken until now
		:param cursor: a Diagnoser object, our "vehicle" which we use to run through the tree
		:return: a list of boolean variables (path) and a Diagnoser object with it's newly assign root (cursor)
		"""
		path.append(False)
		cursor.root = cursor.root.negative_child
		return path, cursor

	def minimize(self, remove_empty=False):
		"""
		this function remove unhelpful junctions in the tree
		:param remove_empty: boolean value, remove junction with 1 None son if True. keeps them if false
		:return: doesn't return anything
		"""
		self.__minimize_core(remove_empty, self.root)

	def __minimize_core(self, remove_empty, cursor):
		"""
		minimie sub function, runs through the tree and gets rid of unhelpful junctions.
		:param remove_empty: see minimize function
		:param cursor: a Diagnoser object that runs through the tree
		:return: None
		"""
		if cursor is None or cursor.data is None:
			return
		if cursor.positive_child is None and cursor.negative_child is None:
			return
		self.__minimize_core(remove_empty, cursor.negative_child)
		self.__minimize_core(remove_empty, cursor.positive_child)
		if self.is_equal(cursor.positive_child, cursor.negative_child):
			cursor.data = cursor.positive_child.data
			cursor.positive_child, cursor.negative_child = cursor.positive_child.positive_child,\
															cursor.positive_child.negative_child
		elif remove_empty:
			copy_cursor = copy.deepcopy(cursor)
			temp_cursor = self.is_junction_none(cursor)
			cursor.data = temp_cursor.data
			if copy_cursor.data != cursor.data:
				cursor.positive_child, cursor.negative_child = temp_cursor.positive_child, temp_cursor.negative_child

	def is_junction_none(self, cursor: Node):
		"""
		__minimize_core sub function. tells you if one of the sons is None. if there is, returns the other son.
		if both of them are None or none of them are None, returns the current junction
		:param cursor: the Diagnoser object that points to the junction
		:return: a pointer
		"""
		if cursor.positive_child.data is None and cursor.negative_child.data is None:
			return cursor
		elif cursor.negative_child.data is None:
			return cursor.positive_child
		elif cursor.positive_child.data is None:
			return cursor.negative_child
		else:
			return cursor

	def is_equal(self, pos: Node, neg: Node):
		"""
		__minimize_core sub function that returns True if the current junction sub trees are equal. returns False if
		thy're not
		:param pos: a Diagnoser object that points to the positive son of the junction
		:param neg: a Diagnoser object that points to the negative son of the junction
		:return: Boolean value
		"""
		if pos is None or neg is None:
			return True
		if pos.data != neg.data:
			return False
		return self.is_equal(pos.positive_child, neg.positive_child) and\
			self.is_equal(pos.negative_child, neg.negative_child)


def build_tree(records, symptoms):
	if not(records_legal(records)):
		raise TypeError("not legal records")
	if not (symptoms_legal(symptoms)):
		raise TypeError("not legal symptoms")
	root = trunk(symptoms)
	leaf_path = Diagnoser(root).paths_to_illness(None)
	profile_lst = []
	for path in leaf_path:
		profile_lst.append(leaf_profile(path, symptoms))
	for profile in profile_lst:
		leaf = leaves(profile, root, symptoms)
		illness_dict = build_illness_dict(records)
		for record in records:
			if leaf == leaves(record.symptoms, root, symptoms):
				illness_dict[record.illness] += 1
				if leaf.data is None:
					leaf.data = record.illness
				elif illness_dict[leaf.data] < illness_dict[record.illness]:
					leaf.data = record.illness
	return Diagnoser(root)


def symptoms_legal(symptoms):
	"""
	build_tree sub function, checks if all the elements in the symptoms list are strings
	:param symptoms: a list of string (hopefully)
	:return: True if all the elements are strings, False if there's one or more that are not strings
	"""
	for symptom in symptoms:
		if type(symptom) != str:
			return False
	return True


def records_legal(records):
	"""
	build_tree sub function, checks if all the elements in the records list are Records
	:param records: a list of Records (hopefully)
	:return: True if all the elements are Record, False if there's one or more that are not Record
	"""
	for record in records:
		if type(record) != Record:
			return False
	return True


def leaf_profile(path, symptoms):
	"""
	returns what symptoms you need to have in order to reach the leaf
	:param path: a list of boolean values
	:param symptoms: a list of strings
	:return: a list of strings (symptoms)
	"""
	lst = []
	counter = 0
	for element in path:
		if element:
			lst.append(symptoms[counter])
		counter += 1
	return lst


def build_illness_dict(records):
	"""
	builds a dictionary of illnesses
	:param records: a list of Record
	:return: a dictionary of illnesses, each one assign with the value 0
	"""
	records_dict = {}
	for record in records:
		records_dict[record.illness] = 0
	return records_dict


def trunk(symptoms):
	"""
	builds the trunk of the tree. means builds the tree without the leaves (only symptoms, no illnesses)
	:param symptoms: a list of strings
	:return: a pointer to a root of a tree
	"""
	if len(symptoms) == 0:
		return Node(None, None, None)
	branch = Node(symptoms[0], trunk(symptoms[1:]), trunk(symptoms[1:]))
	return branch


def leaves(symptoms, travler, all_symptoms):
	"""
	finds a leaf according to a list of symptoms
	:param symptoms: a list of strings (symptoms)
	:param travler: a Diagnoser object that runs through the tree
	:param all_symptoms: a list of strings (symptoms from the function build_tree)
	:return:
	"""
	if travler.data is None:
		return travler
	if travler.positive_child is None or travler.negative_child is None:
		return travler
	if travler.data in symptoms:
		travler = travler.positive_child
		return leaves(symptoms, travler, all_symptoms)
	travler = travler.negative_child
	return leaves(symptoms, travler, all_symptoms)


def optimal_tree(records, symptoms, depth):
	if not(0 <= depth <= len(symptoms)):
		raise ValueError("tree depth is not legal")
	if not(records_legal(records)):
		raise TypeError("records not legal")
	if not(symptoms_legal(symptoms)):
		raise TypeError("symptoms not legal")
	permutations = []
	for combination in itertools.combinations(symptoms, depth):
		permutations.append(list(combination))
	tree = build_tree(records, symptoms)
	for permutation in permutations:
		temp_tree = build_tree(records, permutation)
		if tree.calculate_success_rate(records) <= temp_tree.calculate_success_rate(records):
			tree = temp_tree
	return tree


if __name__ == "__main__":

	pass
	# Manually build a simple tree.
	#                cough
	#          Yes /       \ No
	#        fever           healthy
	#   Yes /     \ No
	# covid-19   cold

	# flu_leaf = Node("covid-19", None, None)
	# cold_leaf = Node("cold", None, None)
	# inner_vertex = Node("fever", flu_leaf, cold_leaf)
	# healthy_leaf = Node("healthy", None, None)
	# root = Node("cough", inner_vertex, healthy_leaf)
	#
	# diagnoser = Diagnoser(root)

	# Simple test
	# diagnosis = diagnoser.diagnose(["cough"])
	# if diagnosis == "cold":
	# 	print("Test passed")
	# else:
	# 	print("Test failed. Should have printed cold, printed: ", diagnosis)
	#
	# diagnosis = diagnoser.diagnose(['cough', 'fever'])
	# if diagnosis == "covid-19":
	# 	print("Test passed")
	# else:
	# 	print("Test failed. Should have printed cold, printed: ", diagnosis)
	#
	# diagnosis = diagnoser.diagnose([])
	# if diagnosis == "healthy":
	# 	print("test passed")
	# else:
	# 	print("failure")
	#
	#
	# # Add more tests for sections 2-7 here.
	# covid19 = Record("covid-19", ["cough", "fever"])
	# cold = Record("cold", ["cough"])
	# records_lst = [covid19, cold]
	# rrr = diagnoser.calculate_success_rate(records_lst)
	# if rrr == 1:
	# 	print("Test Passed")
	# else:
	# 	print("test failed")
	# try:
	# 	rrr = diagnoser.calculate_success_rate([])
	# 	print("test failed")
	# except ValueError:
	# 	print("Test passed")

	# records = parse_data("tiny_data.txt")
	# symptoms = records[0].symptoms
	# gog = trunk(symptoms)
	# print(build_tree(records, symptoms).paths_to_illness(None))

# if leaf.positive_child is None:
# 	for symptom in record.symptoms:
# 		if leaf.data == symptom:
# 			leaf.positive_child = record_node
# 			break
# 		leaf.negative_child = record_node
# elif not (leaf.positive_child is None):
# 	if records_dict[leaf.positive_child.data] < records_dict[record.illness]:
# 		leaf.positive_child = record_node
# 	else:
# 		pass
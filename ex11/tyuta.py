def rearrange(self, lst):
    """
	all_illnesses sub function, take an unorganized list and returns organized one: deletes duplicates and arranges
	the diseases by number of times each one is appeared in the list
	:param lst: list of diseases
	:return: organized list of diseases
	"""
    if len(lst) == 0:
        return
    dicty = {}
    return_lst = [lst[0]]
    for element in lst:
        dicty[element] = lst.count(element)
    for key in dicty.keys():
        if not (key in return_lst):
            previous_length = len(return_lst)
            for i in range(len(return_lst) - 1, 0, -1):
                if dicty[key] < dicty[return_lst[i]]:
                    return_lst.insert(i + 1, key)
                    break
            if previous_length == len(return_lst):
                return_lst.append(key)
    return return_lst
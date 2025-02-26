def create_an_empty_list():
    return []

def create_a_list():
    numbers_list = [1, 2, 3, 4]
    return numbers_list

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l):
    l.pop()
    return l

def remove_element_from_start_of_list(l):
    del l[0]
    return l

def retrieve_first_element_from_list(l):
    if l: 
        return l[0]
    else:
        return None

def retrieve_element_from_index(l, index):
     if l: 
        return l[index]

def retrieve_last_element_from_list(l):
     if l: 
        return l[-1]

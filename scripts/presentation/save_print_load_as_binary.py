import pickle

def save_to_binary_file(object, filepath): 
    with open(filepath, "wb") as file:
        pickle.dump(object, file)

def print_object_as_binary(object):
    print(pickle.dumps(object))
    return pickle.dumps(object)

def load_binary_file(filepath):
    with open(filepath, "rb") as file:
        content = pickle.load(file)
        # print(content)
        return content
import os
from WordExtractor import WordExtractor # Import the external WordExtractor !
from WordTracker import WordTracker   # Import the external WordTracker class 

class PathIterator:
    """
    An iterator which iterates over all the directories and files
    in a given path (note - in the path only, not in the
    full depth). There is no importance to the order of iteration.
    """

    def __init__(self, path):
        """
        Initializer
        """
        self._path = path
        self._items_list = os.listdir(self._path)

        self._current_item = 0
        self._items_size = len(self._items_list)

    def __iter__(self):
        """ 
        """
        return self

    def __next__(self):
        if self._current_item < self._items_size:

            res = self._items_list[self._current_item]
            self._current_item += 1

            return self._path + '/' + res

        else:
            raise StopIteration


    # Set some getters 

    def items_list(self):
        """
        Getter function for the _items_list attribute
        """
        return self._items_list


def path_iterator(path):
    """
    Returns an iterator to the current path's filed and directories.
    Note - the iterator class is not outlined in the original
     version of this file - but rather is should be designed
     and implemented by you.
    :param path: A (relative or an absolute) path to a directory.
    It can be assumed that the path is valid and that indeed it
    leads to a directory (and not to a file).
    :return: An iterator which returns all the files and directories
    in the *current* path (but not in the *full depth* of the path).
    """
    return PathIterator(path) 

def print_tree(path, sep='  '):
    """
    Print the full hierarchical tree of the given path.
    Recursively print the full depth of the given path such that
    only the files and directory names should be printed (and not
    their full path), each in its own line preceded by a number
    of separators (indicated by the sep parameter) that correlates
    to the hierarchical depth relative to the given path parameter.
    :param path: A (relative or an absolute) path to a directory.
    It can be assumed that the path is valid and that indeed it
    leads to a directory (and not to a file).
    :param sep: A string separator which indicates the depth of
     current hierarchy.
    """
    print_tree_helper(path, sep, 0)

def print_tree_helper(path, sep, depth):
    for item in path_iterator(path): 
        # For every file/dir in the mentioned path
        title = os.path.basename(item) # Get the basename of the path
                                       # i.e. the file/dir (foo/bar => bar)
        if os.path.isdir(item):
            # If the item is a directory, call the print_tree_helper again
            # and print the directory title

            print((depth)*sep + title)

            print_tree_helper(item, sep, depth + 1) # Increase depth by 1
        elif os.path.isfile(item):
            # Item is a file, print its title with the depth*sep 
            print((depth)*sep + title)

def file_with_all_words(path, word_list):
    """
    Find a file in the full depth of the given path which contains
    all the words in word_list.
    Recursively go over  the files in the full depth of the given
    path. For each, check whether it contains all the words in
     word_list and if so return it.
    :param path: A (relative or an absolute) path to a directory.
    In the full path of this directory the search should take place.
    It can be assumed that the path is valid and that indeed it
    leads to a directory (and not to a file).
    :param word_list: A list of words (of strings). The search is for
    a file which contains this list of words.
    :return: The path to a single file which contains all the
    words in word_list if such exists, and None otherwise.
    If there exists more than one file which contains all the
    words in word_list in the full depth of the given path, just one
    of theses should be returned (does not matter which).
    """
    entities = path_iterator(path).items_list()
    
    x = traverse_tree(path, entities, word_list, 0)

    print(x)
    return x




def traverse_tree(path, entities, word_list, position):
    """
    Recursively traversing the tree in input: path
    for each item in the iterator (pathiterator) it checks if it's a dir/file
    if it's a dir, call the function recursively in a bigger depth.
    Otherwise, check the file if it contains word_list
    """

    if position < len(entities):
    #`for entity in entities:
        # Recursively go through the files until no more files in path
        new_path = os.path.join(path, entities[position])
        
        #print(new_path)

        if os.path.isdir(new_path):
            # In case the current file is a directory
            pp = path_iterator(new_path)
            return traverse_tree(new_path, pp.items_list(), word_list, 0)

        elif os.path.isfile(new_path):
            # In case it's a file and not a directory, cross with word_list
            # and return accordingly

            #print(new_path)
            if check_file(word_list, new_path):
                return new_path 

            else:
                # Call the function again with position += 1 to go to next
                # file in the path
                return traverse_tree(path, entities, word_list, position + 1)


def check_file(word_list, f):
    we = WordExtractor(f)
    wt = WordTracker(word_list)

    for word in we:
    # Using the efficient iterator from WordExtractor
        if word in wt:
            wt.encounter(word)
    
    res = wt.encountered_all()
    wt.reset()

    return res

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
        The __iter__ function that handles interation process of the 
        current object.
        returns the iterator.
        """
        return self

    def __next__(self):
        """
        This function is part of the iteration functionality of the object
        it decides how to iterate the object and which is the next entity
        in the iteration.

        """
        if self._current_item < self._items_size:
            # As long as it didn't pass the item_size in the directory
            # it returns the current_item set by class and increment it
            # for next iteration.
            res = self._items_list[self._current_item]
            self._current_item += 1

            return os.path.join(self._path, res) # Return the path

        else:
            # End of files
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
    """
    recursive function to print the tree of the given path with a "graphical"
    addon of seperation.
    It iterates the path_iterator iterator that we built and for each file
    in the iterator, it prints it with the amount of sep needed, depends
    on the depth of the iteration.
    The function returns nothing, but prints recursively the items.
    """
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
    return traverse_tree(path, word_list)

def traverse_tree(path, word_list):
    """
    A function to traverse the directory tree of the given path input.
    It uses the path_iterator function we build to easily go through
    each file and directory.
    If it's a directory, call traverse_tree recursively.
    If it's a file, compare word lists and return the path if it's a match.
    Otherwise, return None
    """
    for item in path_iterator(path):
        # For each entity / item in the directory path.
        if os.path.isdir(item):
            # if it's a directory, call this function again in the new path
            return traverse_tree(item, word_list)

        elif os.path.isfile(item):
            # It's a file, check for word_list
            if check_file(word_list, item):
                # Passed matching ! return the item path
                return (item)

    return None # Return None if no results

def check_file(word_list, f):
    """
    Test file for matching word_list. It is a function that uses iter
    of WordExtractor to go through on each word in the file efficiently
    and it compares the word with WordTracker.__contain__ .
    """
    we = WordExtractor(f) # Create the WordExtractor object
    wt = WordTracker(word_list) # Create WT object
    wt.reset() # Reset the wt instance 

    for word in we:
    # Using the efficient iterator from WordExtractor
        if word in wt:
            # The word appears in dictionary, append it to the encounter
            # list.
            wt.encounter(word)
    
    return wt.encountered_all() # Returns true/false accordingly

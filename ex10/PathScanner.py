import os
import WordExtractor # Import the external WordExtractor !
import WordTracker   # Import the external WordTracker class 

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
            raise StopIteration()


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
    iterations = len(os.listdir(path))

    return print_tree_helper(path, sep, 0)

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

    pp = PathIterator(path)
    
    if pp._items_list:
        pp._items_list.pop()
        curr = pp._items_list[-1]
        print(curr) 

        if os.path.isdir(path + curr):
            return file_with_all_words(path + curr, word_list)

        elif os.path.isfile(path + curr):
            # The entity is a file, read it and count encounters

            for word in WordExtractor(path + curr):
                # Using the efficient iterator from WordExtractor
                wt = WordTracker(word_list)

                if word in wt:
                    wt.encounter(word)
                    if wt.encountered_all:
                        return path
                else:
                    wt.reset
                    break

            return find_with_all_words(path, word_list)

        else:
            return None

    def traverse_tree():
        pass

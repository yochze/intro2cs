#!/usr/bin/env python3
import random # Used to randomly select a pivot value for Quicksort

class WordTracker(object):
    """
    This class is used to track occurrences of words.
     The class uses a fixed list of words as its dictionary
     (note - 'dictionary' in this context is just a name and does
     not refer to the pythonic concept of dictionaries).
     The class maintains the occurrences of words in its
     dictionary as to be able to report if all dictionary's words
     were encountered.
    """

    def __init__(self, word_list):
        """
        Initiates a new WordTracker instance.
        :param word_list: The instance's dictionary.
        """
        self._word_list = word_list
        self._sorted_list = word_list[:]
        x = len(self._sorted_list) - 1
        self.quicksort(0, x)

    def __contains__(self, word):
        """
        Check if the input word in contained within dictionary.
         For a dictionary with n entries, this method guarantees a
         worst-case running time of O(n) by implementing a
         binary-search.
        :param word: The word to be examined if contained in the
        dictionary.
        :return: True if word is contained in the dictionary,
        False otherwise.
        """
        pass

    def encounter(self, word):
        """
        A "report" that the give word was encountered.
        The implementation changes the internal state of the object as
        to "remember" this encounter.
        :param word: The encountered word.
        :return: True if the given word is contained in the dictionary,
        False otherwise.
        """
        pass

    def encountered_all(self):
        """
        Checks whether all the words in the dictionary were
        already "encountered".
        :return: True if for each word in the dictionary,
        the encounter function was called with this word;
        False otherwise.
        """
        pass

    def reset(self):
        """
        Changes the internal representation of the instance such
        that it "forget" all past encounters. One implication of
        such forgetfulness is that for encountered_all function
        to return True, all the dictionaries' entries should be
        called with the encounter function (regardless of whether
        they were previously encountered ot not).
        """
        pass


    def binary_search(self):
        pass


    def quicksort(self, low, high):

        if low < high:
            # Continue iterating until low == high which means
            # partitions number reached its limit
            pivot = self.partition(low, high)
            self.quicksort(low, pivot -1)
            self.quicksort(pivot + 1, high)


    def partition(self, low, high):
        mylist = self._sorted_list

        pivot_id, pivot_val = self.choose_pivot(low,high) # Select pivot point
        self.swap(pivot_id, high)
        pivot_id = high

        while low < high:
            if mylist[low] < pivot_val:
                low += 1
            elif mylist[high] >= pivot_val:
                high -= 1
            else:
                self.swap(low, high)
                low += 1
                high -= 1
            
        self.swap(pivot_id, low)

        return low



    def choose_pivot(self, low, high):
        """ 
        Using random python library to randomly select and return a pivot
        value from the input list.    
        """
        pivot_id = random.randint(low, high-1)

        return (pivot_id, self._sorted_list[pivot_id])

    def swap(self, id1, id2):
        """
        Simple function to swap between values in a list based on their ids
        """
        mylist = self._sorted_list # Create a pointer, just for a shorter
                                   # more elegant name

        mylist[id1], mylist[id2] = mylist[id2], mylist[id1]



nz = WordTracker(["hello", "helloworld", "hellojason", "hellojbson", "helloiason"])

n = WordTracker([82,4,5,7,1,5,1,2,3,5,7,9])
print(nz._sorted_list)
print(n._sorted_list)
#print("should be: ", nz._sorted_list.sort() )

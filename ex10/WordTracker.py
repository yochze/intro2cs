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
        self._word_list         = word_list
        self._sorted_list       = word_list[:]
        self._encountered_words = self._sorted_list[:]

        self._list_size = len(self._sorted_list)

        self.quicksort(0, self._list_size-1)

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
        return self.binary_search(self._sorted_list,word,0,self._list_size-1) 

    def encounter(self, word):
        """
        A "report" that the give word was encountered.
        The implementation changes the internal state of the object as
        to "remember" this encounter.
        :param word: The encountered word.
        :return: True if the given word is contained in the dictionary,
        False otherwise.
        """
        if word in self._sorted_list and word not in self._encountered_words:
            self._encountered_words.append(word)
            return True
        else:
            return False

    def encountered_all(self):
        """
        Checks whether all the words in the dictionary were
        already "encountered".
        :return: True if for each word in the dictionary,
        the encounter function was called with this word;
        False otherwise.
        """
        if len(self._encountered_words) == self._list_size:
            return True
        else:
            return False

    def reset(self):
        """
        Changes the internal representation of the instance such
        that it "forget" all past encounters. One implication of
        such forgetfulness is that for encountered_all function
        to return True, all the dictionaries' entries should be
        called with the encounter function (regardless of whether
        they were previously encountered ot not).
        """
        self._encountered_words = []

    def quicksort(self, low, high):
        """
        An implementation of the quicksort algorithm.
        It recursively split the list's items into pairs and sort them
        then, it combines them into a single list
        This algorithm worst-case complexity is O(nlogn)
        """

        if low < high:
            # Continue iterating until low == high which means
            # partitions number reached its limit

            pivot = self.partition(low, high)

            self.quicksort(low, pivot -1) # Recursively 
            self.quicksort(pivot + 1, high)


    def partition(self, low, high):
        """
        This function reorder the array so the all low values compared
        to pivot value will be in the left side of the pivot.
        for higher values than pivot, it will be in right side. 
        """
        mylist = self._sorted_list

        pivot_id, pivot_val = self.choose_pivot(low,high) # Select pivot point
        self.swap(pivot_id, high) # Swap the pivod id with high val
        pivot_id = high

        while low < high:
            # As long the bounds of the array are >1
            if mylist[low] < pivot_val:
                # the mylist[low] is located correctly, so increase lower bound
                low += 1
            elif mylist[high] >= pivot_val:
                # the mylist[high] is located correctly, so decrease high bound
                high -= 1
            else:
                # Otherwise, there's a mixup so a swap is required !
                self.swap(low, high)
                low += 1
                high -= 1
        
        # Finished partitioning, so swap between pivot_id and low bound
        self.swap(pivot_id, low) 

        return low 



    def choose_pivot(self, low, high):
        """ 
        Using random python library to randomly select and return a pivot
        value from the input list.    
        Returns a tuple of the random value from the list and its index.
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


    def binary_search(self,sorted_list,term, left, right):
        """
        Implementation of binary search O(logn) to search the term in
        self._sorted_list.
        """
        
        if left > right:
            # The left id has exceeded the right id so the term is not
            # in the list, hence return False.
            return False
        center = (right + left) // 2 # Create the new updated center

        if term > sorted_list[center]:
            # Term is in the right side, recursively call the binary search
            # with the modified list list[center:]
            return self.binary_search(sorted_list, term, center+1, right)

        elif term < sorted_list[center]:
            # Term is in the left side, recursively call the binary search
            # with the modified list list[center:]
            return self.binary_search(sorted_list, term, left, center-1)

        else:
            # Found a match (term == sorted_list[center]), 
            # Return true and end function
            return True




#nz = WordTracker(["hello", "helloworld", "hellojason", "hellojbson", "helloiason"])

#n = WordTracker([82,4,5,7,1,5,1,2,3,5,7,9])
#print(nz._sorted_list)
#print(n._sorted_list)
#print(nz.binary_search(nz._sorted_list, "hh", 0, len(nz._sorted_list)-1))
#print(nz.binary_search(nz._sorted_list, "hello",0, len(nz._sorted_list)-1))
#print(nz.__contains__("hellojason"))
#print(nz.__contains__("hasdfellojason"))
#print("should be: ", nz._sorted_list.sort() )

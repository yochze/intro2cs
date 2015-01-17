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
        self._encountered_words = [] 

        self._list_size = len(self._sorted_list)

        self.quicksort(self._sorted_list, 0, self._list_size-1)

    def sorted_list(self):
        return self._sorted_list

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
        if word in self._sorted_list:
            if word not in self._encountered_words:
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
        self._encountered_words[:] = []



    def partition(self, mylist, start, end):
        """ 
        Partition implementation as part of the full quicksort implementation
        """
        pivot = random.randint(start, end)   # Select a pivot idx randomly
        self.swap_helper(mylist, pivot, end) # trigger swap on pivot and end

        for i in range(start, end):
            # For each item in start,pivot (new end) do
            if mylist[i] <= mylist[end]:
                # re order element if it's smaller the end
                self.swap_helper(mylist, i, start)
                start += 1 # Increment start to smaller the range

        self.swap_helper(mylist, start, end) # Swap last elements

        return start 
        


    def quicksort(self, mylist, start, end):
        """
        The main function of quicksort. It works O(nlogn) in an average case
        and O(n^2) in worst case (which is rare !).
        """
        if start < end:                       
            # As long there are >2 items 
            pivot = self.partition(mylist,start,end) # Select a pivot point
            self.quicksort(mylist, start, pivot-1)   # Trigger on left range
            self.quicksort(mylist, pivot+1, end)     # Trigger on right range


    def swap_helper(self, mylist, x, y):
        mylist[x], mylist[y] = mylist[y], mylist[x]

    def binary_search(self, sorted_list, term, left, right):
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

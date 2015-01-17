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



    def partition(self, list, start, end):
        pivot = list[end]                       # Partition around the last value
        bottom = start-1                        # Start outside the area to be partitioned
        top = end                               # Ditto

        done = 0
        while not done:                         # Until all elements are partitioned...

            while not done:                     # Until we find an out of place element...
                bottom = bottom+1               # ... move the bottom up.

                if bottom == top:               # If we hit the top...
                    done = 1                    # ... we are done.
                    break

                if list[bottom] > pivot:        # Is the bottom out of place?
                    list[top] = list[bottom]    # Then put it at the top...
                    break                       # ... and start searching from the top.

            while not done:                     # Until we find an out of place element...
                top = top-1                     # ... move the top down.
                
                if top == bottom:               # If we hit the bottom...
                    done = 1                    # ... we are done.
                    break

                if list[top] < pivot:           # Is the top out of place?
                    list[bottom] = list[top]    # Then put it at the bottom...
                    break                       # ...and start searching from the bottom.

        list[top] = pivot                       # Put the pivot in its place.
        return top                              # Return the split point


    def quicksort(self, list, start, end):
        if start < end:                         # If there are two or more elements...
            split = self.partition(list, start, end) # ... partition the sublist...
            self.quicksort(list, start, split-1)     # ... and sort both halves.
            self.quicksort(list, split+1, end)
        else:
            return

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

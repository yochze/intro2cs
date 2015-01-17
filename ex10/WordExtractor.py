#!/usr/bin/env python3


class WordExtractor(object):
    """
    This class should be used to iterate over words contained in files.
     The class should maintain space complexity of O(1); i.e, regardless
     of the size of the iterated file, the memory requirements ofa class
     instance should be bounded by some constant.
     To comply with the space requirement, the implementation may assume
     that all words and lines in the iterated file are bounded by some
     constant, so it is allowed to read words or lines from the
     iterated file (but not all of them at once).
    """

    def __init__(self, filename):
        """
        Initiate a new WordExtractor instance whose *source file* is
        indicated by filename.
        :param filename: A string representing the path to the instance's
        *source file*
        """
        self._filepath = filename
        self._lines = self.get_lines_count()
        self._current_line = 0
        self._current_word_idx = 0

    def __iter__(self):
        """
        Returns an iterator which iterates over the words in the
        *source file* (i.e - self)
        :return: An iterator which iterates over the words in the
        *source file*
        """
        return self


    def get_lines_count(self):
        """
        Returns the number of lines in the file
        """
        return sum(1 for line in open(self._filepath))

    def read_line(self, n):
        """
        Reads the file and returns the n (input integer) line of the file
        
        Assuming (by the question data) that the line count is C (constant)
        so the complexity of worst case scenario will be O(C) == O(1).
        
        The function uses the "with open.. as" context to easily release
        resources.
        """
        i = 0 # Set index

        with open(self._filepath) as f:
            # Using with context to automatically close file and 
            # release resources when finish iterating

            for line in f:
                # For each line in the file, if the index equals the
                # input, return the line. Otherwise keep iterating

                if i == n:
                    # Return line if it's the requested index
                    return line

                i += 1 # Increment index otherwise

    def __next__(self):
        """
        Make a single word iteration over the source file.
        :return: A word from the file.
        """
        if self._current_line <= self._lines-1:
            # Run while current line doesn't reach the len of file lines.
            line = self.read_line(self._current_line) # Get the currentline
            words = line.split()

            if len(words) != 0:
                # The line contains words
                if self._current_word_idx == len(words)-1:
                    # If it's last word in line
                    self._current_word_idx = 0 # Reset word index
                    self._current_line += 1    # Increment current line
                else:
                    # Not last word in line
                    self._current_word_idx += 1 # Increment index

            else:
                # Line doesn't contain words,
                # reset index and move on to the next line. 
                # Recursively call __next__ function
                self._current_word_idx = 0
                self._current_line += 1

                return self.__next__()

            return words[self._current_word_idx-1]


        else:
            # Reached 1 line bigger than lines size, so EOF and stop
            # iterating.
            raise StopIteration()

## Test
#f = WordExtractor('text_file.txt')
#i = 0
#for w in f:
    #print(i, w)
#print(f._lines)

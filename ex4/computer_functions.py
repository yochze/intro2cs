'''Given a heap return a move for Nim game
'''
import copy
import time
import random
import argparse

SLEEP_DURATION = 0.5
MAX_TURN_TIME = 10
HEAPS = (7, 5, 3)

class Positives(object):
    def __iter__(self): #fake an iterator to play nice with argparse
        return iter(['positives only'])
    def __contains__(self,y):
        return y>0

positives = Positives()

#Argparse to set the seed
parser = argparse.ArgumentParser()
parser.add_argument('-s','--seed', type=int, default=None,
                    help="seed for computer's random choices")
parser.add_argument('--heaps', metavar = 'H', type=int, choices=positives, 
                    nargs='+', default = HEAPS,
                    help='heap sizes for alternate starting state')
args = parser.parse_args()

random.seed(args.seed)
HEAPS = tuple(args.heaps)

def nim_sum(heaps):
    nsum = 0
    for heap in heaps:
        nsum = nsum ^ heap
    return nsum

def get_computer_move(heaps):
    '''Given the heaps as a list of non-negative integers.
    Returns the move of the computer as a list with two elements:
    [heap_num, num_of_elements]
    Where heap_num is the index of the heap to be removed from
    and num_of_elements is the number of elements to be removed from this heap
    '''
    # (nim-sum <> 0) is a winning position
    # aim is to pass on a losing position (nim-sum = 0) to next player
    print("Computer is thinking ",)
    sleep_duration = min([SLEEP_DURATION,MAX_TURN_TIME/sum(heaps)])
    if nim_sum(heaps) == 0:
        # no winning move available, so pick the largest heap and take one from it
        for i in range(0, sum(heaps)):
            print (".", end='', flush=True)
            time.sleep(sleep_duration)
            heap_num = 0
        for i in range(len(heaps)):
            if heaps[i] > heaps[heap_num]:
                heap_num = i
            move = [heap_num, 1]
    else:
        # could just find first winning move, but game is more interesting if
        # we list all the winning moves and pick one at random
        winning_moves = []
        heap_num = 0
        while (heap_num < len(heaps)):
            num_remove = 1
            while num_remove <= heaps[heap_num]:
                trial_heaps = copy.copy(heaps)
                trial_heaps[heap_num] -= num_remove
                if nim_sum(trial_heaps) == 0:
                    winning_moves.append([heap_num, num_remove])
                print (".", end='', flush=True)
                time.sleep(sleep_duration)
                num_remove = num_remove + 1
            heap_num = heap_num + 1
        move = random.choice(winning_moves)
    return move

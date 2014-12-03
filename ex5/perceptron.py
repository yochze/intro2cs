#############################################################
# FILE : ex5.py
# WRITER : your_name , your_login ,
# EXERCISE : intro2cs ex5
# DESCRIPTION:
# Enter description.
#
#############################################################

def dot(A, B):
    """ 
    This function receives two vectors in size of N
    It calculates DOT product with this formula:
        \sum A_i * B_i
    """
    dot = 0.0
    for i in range(len(A)):
        dot += A[i] * B[i]

    return dot

def sign(x):
    """ 
    A simple sign implementation gets a number and return:
    -1.0 if x < 0
    1.0  if x >= 0 
    0    if x == 0
    """
    if x < 0:
        s = -1
    elif x > 0:
        s = 1
    else:
        s = 0

    return s

def perceptron(data, labels):
    """
    The perceptron algorithm

    An iteratoin that goes through the data input list and
    for each vector it runs a sign(dot(w,vector)-b) and compares it with the
    matching result from the labels list.
    If they're matching, it means that the current weights set are working
    for that vector. Otherwise, the weights aren't good and an update is 
    required.

    Updating the weights is simply by adding the current vector while 
    multiplying it with the matching labels scalar (-1|1)

    INPUT: 
        data   == list size M of lists size N
        labels == list size M of (-1|+1), 
        
        Note: labels[i] is the result of data[i] 
    
    OUTPUT: 
        A tuple of the calculated weights (list) and bias (integer).
    
    """

    DATA_SIZE    = len(data)    # Set the data size (size of list)
    VECTOR_SIZE  = len(data[0]) # Set the data's vector size 
                                # (list of list size)

    UPDATES_LIMIT = DATA_SIZE*10 # Set the run limit of the while loop (below)
                                # to 10 times the DATA_SIZE

    weights       = [0] * VECTOR_SIZE # Set the weights vector to the same size
                                     # as input data's vectors.

    bias           = 0 # Initialize bias variable
    total_updates  = 0 # Initialize updates/errors count variables
    no_errors = False  # Initialize no_errors with False
                       # so the loop will start
    
    while total_updates < UPDATES_LIMIT and not no_errors:
    # The main perceptron iteration.
        
        no_errors = True # Initializing 

        for i in range(DATA_SIZE):
            # Iterating through the input size (both labels and data)
            
            result = sign(dot(data[i], weights)-bias) # Calculate DOT of 
                                                      # data[i] AND weights 
                                                      # and get either -1 or 1
                                                      # based on sign func

            if result != labels[i]:
                # Compare the result with according labels[i]
                # if they are equal, means the current linear seperator works
                # for the couple. If they are different, the linear seperator 
                # doesn't work for data[i] and error needs to be counted.
                # Also, updating weights by adding the data[i][n] the
                # weights vector, and updating bias by substracting the 
                # matching label.
                total_updates    += 1 
                no_errors         = False 

                # Updating weights and bias
                for num in range(len(weights)):
                    weights[num] +=  (data[i][num] * labels[i])
                bias -= labels[i]
 
        if no_errors:
            return(weights, bias)

    else:
        return(None, None)

def generalization_error(data, labels, w, b):
    """ 
    A method to test the returned weights and bias with test data and labels.

    Iterating through the data size (labels and input) and check if the
    there's a good match of sign(dot(x,w)-b) with the calculated
    bias and weights from the perceptron algorithm.

    If there's a match, append 0 to the new list, otherwise append 1.

    INPUT: 
        data    - list size M of vectors (lists) size N
        labels  - list size M of (-1|1)
        w       - list (vector) size N
        b       - integer

    OUTPUT:
        result - list type variable, containing 1 or 0 according to the
        success of the weights, bias and perceptron algorithm.

    """
    results = []

    for i in range(len(data)):
        # Go through all the data size.
        if sign(dot(data[i], w)-b) == labels[i]:
            # function result for vector i and w,b are matching
            # for the label[i] in the list. Therefor append 0.
            results.append(0)
        else:
            # There's a no match. Append 1 to the list
            results.append(1)
        
    return (results) 



def vector_to_matrix(vec):
    """ Gets a vector in size of x^2 and returns x*x matrix """
    M_SIZE = int((len(vec))**0.5) # Get the square root of the vector
                                  # to calculate the future matrix size.
    matrix = [] # Initialize matrix
    
    while len(vec) != 0:
        # Iterating until vec (input) size is 0.
        # in each iteration, append 0 to M_SIZE list to matrix list
        # and remove 0 to M_SIZE from vec.
        # Thus, will have a list of lists (M_SIZE*M_SIZE) as matrix
        matrix.append(vec[:M_SIZE])
        vec = vec[M_SIZE:]
    
    return matrix

def classifier_4_7(data, labels):
    """ Simply call the perceptron function with the input
        data and labels. 
    """
    return perceptron(data, labels)


def test_4_7(train_data, train_labels, test_data, test_labels):
    """
        Testing the weights and bias generated from the perceptron
        algorithm with test data.
        First, we will generate w & b with train data.
        Then, if w & b were found (!= None) , then get the 
        generalization errors list output and return a tuple of 3
        ( weights, bias , errors )
    """
    w, b = classifier_4_7(train_data, train_labels)
    if (w,b) == (None, None):
        errors = None
    else:
        errors = generalization_error(test_data, test_labels, w, b) 

    return (w, b, errors)

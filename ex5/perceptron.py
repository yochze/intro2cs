#############################################################
# FILE : ex5.py
# WRITER : your_name , your_login ,
# EXERCISE : intro2cs ex5
# DESCRIPTION:
# Enter description.
#
#############################################################

# Import helpers
# import intro2cs_ex5

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
    """ A simple sign implementation gets a number and return:
        -1.0 if x < 0
        1.0  if x >= 0 
    """
    if x < 0:
        s = -1
    elif x > 0:
        x = 1
    else:
        x = 0

    return s

def perceptron(data, labels):
    """
    data == list size M of lists size N

    labels == list size M of (-1|+1), 

    labels[i] is the result of data[i] 
    
    OUTPUT: 
    list W with size N and bias variable

    pseudocode:

    for vector in data: 
        if vector*w == labels[vector]
            next
        else:
            w = w[x] + data[vector]*labels[vector]
            b -= b - labels[vector]
    
    """

    DATA_SIZE    = len(data)
    VECTOR_SIZE  = len(data[0])
    weights      = [0] * VECTOR_SIZE
    bias         = 0
    error_rate   = 0
    total_errors = 0
    
    while total_errors < DATA_SIZE*10:
        error_rate = 0
        for i in range(DATA_SIZE):
            
            result = sign(dot(data[i], weights)-bias)

            if result != labels[i]:
                # The linear seperator doesn't work for data[i] and error found.
                # Updating weights by adding the data[i][n] to each weight
                # Updating bias.
                error_rate += 1
                total_errors += 1
                for num in range(len(weights)):
                    weights[num] +=  (data[i][num] * labels[i])

                bias -= labels[i]
 
                # intro2cs_ex5.show_perceptron(data, labels, weights, bias)
        if error_rate == 0:
            break

    else:
       weights = None
       bias    = None

    # Returning the final weights and bias (mekadem)
    return (weights, bias)

def generalization_error(data, labels, w, b):
    """ Gets a list of M lists in the size of N
        and 
    """
    results = []

    for i in range(len(data)):
        if sign(dot(data[i], w)-b) == labels[i]:
            results.append(0)
        else:
            results.append(1)
        
    return (results) 



def vector_to_matrix(vec):
    """ Gets a vector in size of 784 and returns 28*28 matrix"""
    M_SIZE = int((len(vec))**0.5)
    matrix = []
    
    while len(vec) != 0:
        matrix.append(vec[:M_SIZE])
        vec = vec[M_SIZE:]
    
    return matrix

def classifier_4_7(data, labels):
    return perceptron(data, labels)


def test_4_7(train_data, train_labels, test_data, test_labels):
    w, b = classifier_4_7(train_data, train_labels)
    if (w,b) == (None, None)
        errors = None
    else:
        errors = generalization_error(test_data, test_labels, w, b) 

    return (w, b, errors)



# TASKS

# TASK 1:
# data   = intro2cs_ex5.loadtxt('helpers/data_2D.txt')
# labels = intro2cs_ex5.loadtxt('helpers/labels_2D_sep.txt')

# perceptron(data, labels)


# Task 4
# data_47   = intro2cs_ex5.loadtxt('helpers/data_47.txt')
# labels_47 = intro2cs_ex5.loadtxt('helpers/labels_47.txt')

# Test data
# test_data_47   = intro2cs_ex5.loadtxt('helpers/test_data_47.txt')
# test_labels_47 = intro2cs_ex5.loadtxt('helpers/test_labels_47.txt')


# w,b,errors = test_4_7(data_47, labels_47, test_data_47, test_labels_47)
# for i in range(len(errors)):
#    if errors[i] == 1:
#        print(i)
#        print("The label is:" + str(test_labels_47[i]) )

#        # matrix = vector_to_matrix(test_data_47[i])

#        intro2cs_ex5.show_number(matrix)

# m = vector_to_matrix(w)
# intro2cs_ex5.show_number(m)

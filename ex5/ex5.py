#############################################################
# FILE : ex5.py
# WRITER : your_name , your_login ,
# EXERCISE : intro2cs ex5
# DESCRIPTION:
# Enter description.
#
#############################################################

# Import helpers
import intro2cs_ex5


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
        1.0  if x > 0 
    """

    s = -1.0 if x < 0 else 1.0
    return s

def vector_addition(v1, v2):
    """
        A simple vector addition
    """
    for i in len(v1):
       v1[i] += v2[i]

    return v1

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
    error_rate = 0
    
    print(labels)
    print(weights)
    print(data)

    while error_rate < 10*DATA_SIZE:
        for i in range(len(data)):
            if sign(dot(data[i], weights)) == labels[i]:
                # The linear seperator works for data[i]
                next
            else:
                # The linear seperator doesn't work for data[i] and error found.
                # Updating weights by adding the dot_product to each weight
                # Updating bias.
                for num in range(len(data[i])):
                    weights[num] += data[i][num] * labels[i]

                bias -= labels[i]
                error_rate += 1

                intro2cs_ex5.show_perceptron(data,labels,weights,bias)

        # Returning the final weights and bias (mekadem)

        return (weights, bias)
    else:
        (None, None)


def generalization_error(data, labels, w, b):
    pass


def vector_to_matrix(vec):
    pass
 

def classifier_4_7(data, labels):
    pass


def test_4_7(train_data, train_labels, test_data, test_labels):
    pass

# TESTING

data   = intro2cs_ex5.loadtxt('helpers/data.txt')
# labels = intro2cs_ex5.loadtxt('helpers/labels_AND.txt')
labels = intro2cs_ex5.loadtxt('helpers/labels_XOR.txt')

perceptron(data, labels)



#############################################################
# FILE : ex7.py
# WRITER : Yochay Ettun , yochze
# EXERCISE : intro2cs ex6
# DESCRIPTION:
# Face morphing program
# The program gets 2 images of faces, and several parameters and form
# a new combined image of both of the faces.
#############################################################

from SolveLinear3 import solve_linear_3

def is_point_inside_triangle(point, v1, v2, v3):
    """
    This function check if a given point is in the area of the 
    triangle.

    point == tuple of 2 numbers, i.e (0,3)
    v1,v2,v3 are tuples of 2 numbers each (1,2) (3,4) (5,6)

    OUTPUT: 
    Depending if the equations have a solution return a matching boolean
    and the list of a,b,c.
    Example: (boolean, (1,2,3))
    """

    res = True # Set default value for final output

    xs = [v1[0], v2[0], v3[0]]
    ys = [v1[1], v2[1], v3[1]]
    zs = [1, 1, 1]

    coefficients_lists = [xs, ys, zs] # Collects lists into single list
    right_hand_lists   = [point[0], point[1], 1] # Equations answers list 

    # Call external method to solve linear equations 
    a, b, c = solve_linear_3(coefficients_lists, right_hand_lists)

    if a < 0 or b < 0 or c < 0:
        # If any of a,b,c is lower than 0, then the equation
        # doesn't have a solution. Therfore return False.
        res = False
    
    return (res, (a,b,c))



def create_triangles(list_of_points):
    """
    The function retrieves a list of points, and creates
    triangles out of it.
    Firstly, it creates triangles from the first 1..INITIAL_POINTS(=4)
    and then iterates through the rest of the points and creates
    a list of triangles.


    INPUT: list of x_i, y_i [(0,1),(2,0)...]
    
    OUTPUT: list of triangles:
            [((x,y),(x2,y2),(x3,y3)), ((x,y),(x2,y2),(x3,y3)), ..]

    """
    
    initial_points = 4 
    triangles = [] # Initialize the output list
    
    # Add the initial triangles (corners of the images)

    triangles.append((list_of_points[0],list_of_points[1],list_of_points[2])) 
    triangles.append((list_of_points[0],list_of_points[3],list_of_points[2])) 
    # Add triangles from id 4 to n

    for point_idx in range(initial_points, len(list_of_points)):
        # For every point in the INPUT list (points)
        # check if any of the triangles contain that point.
        # if it does, create a new triangles and delete the previous
        p = list_of_points[point_idx]

        for t in range(len(triangles)):
            # For every triangle in the assembeled list
            # there's a condition that if the given point (p)
            # is in the t triangle, then remove the triangle from
            # list and append 3 new ones .
            v1, v2, v3 = triangles[t] # vertex of the triangle T

            if is_point_inside_triangle(p, v1, v2, v3)[0]:
                # Found a Triangle containing point P
                # Create new triangles
                new_triangles = add_3_triangles(p, v1, v2, v3)
                triangles.pop(t) # Remove triangle[t]
                triangles.extend(new_triangles) # extend triangles
                                                # list with the assembeled
                                                # triangles
                break
                # Move on to the next P(x,y)

    return triangles # Return assemebeld triangles

def add_3_triangles(p, v1, v2, v3):
    """
    Helper function to add  3 triangles from 3 different points
    and one anchor point (p).
    """

    t1 = (v1, v2, p)
    t2 = (v2, v3, p)
    t3 = (v3, v1, p)

    return [t1, t2, t3]



def do_triangle_lists_match(list_of_points1, list_of_points2):
    """
    Testing if triangles list are match.
    Given 2 lists of points, the function create the triangles
    for each of the lists.
    Then it matches every point id with the parallel point id and 
    and if point is in a matching triangle (in the matching list)

    INPUT: 2 lists, same size.
    OUTPUT: True or False depending if tests was success.
    """
    
    triangles_list1 = create_triangles(list_of_points1) # Create triangles
    triangles_list2 = create_triangles(list_of_points2) 

    i, result = 0, True # Initialize variables index and result.
    
    for i in range(len(list_of_points1)):
        # Iterating through the list of points (assumint len(list1/list2)
        # is equal). And iterating until result is not True.

        point_i_1 = list_of_points1[i] # Refering to the current i point
        point_i_2 = list_of_points2[i] # in each list. 

        for j in range(len(triangles_list1)):
            # Iterating through the triangles list
            # to find if there's a match.
        
            tr1 = triangles_list1[j] # ((x,y),(x,y),(x,y))
            tr2 = triangles_list2[j] # Current triangles j.
            
            res1 = (is_point_inside_triangle(point_i_1, tr1[0], tr1[1],
                tr1[2])[0]) # Returns a bool if point in triangle.
            res2 = (is_point_inside_triangle(point_i_2, tr2[0], tr2[1],
                tr2[2])[0])
                
            if (res1 != res2):
                # There was no match.
                # Finish and return False.
                return False
    
    return True # Success! return True


def get_point_in_segment(p1, p2, alpha):
    """ Based on the equation, this function computes 
        the point in the segment.

        INPUT: 2 points and an alpha parameter
        OUTPUT: (x,y) coordinates
    """
    x = int((1-alpha)*p1[0] + alpha*p2[0])
    y = int((1-alpha)*p1[1] + alpha*p2[1])

    return (x,y)

def get_intermediate_triangles(source_triangles_list, target_triangles_list,
                                                                  alpha):
    """
    This functions finds an intermediate triangle for each pair of triangles
    in the two lists (images).
    
    INPUT:  source list size N, target list size N and an alpha parameter
    OUTPUT: a list size N containing all the intermediate triangles.
    """
    
    triangles = [] # Initialize output

    for i in range(len(source_triangles_list)):
        # For every source triangle list, 
        
        triangle_vertexs = [] # Single triangle init 
                              # to fill with points of the intermediate
                              # triangle.

        for j in range(len(source_triangles_list[i])):
            # For each point in pair of triangles 
            p1 = source_triangles_list[i][j] # Point of 1st triangle
            p2 = target_triangles_list[i][j] # Point of 2nd triangle
            
            # Append the intermediate point to the triangle
            triangle_vertexs.append(get_point_in_segment(p1, p2, alpha))

        triangles.append(tuple(triangle_vertexs)) # Append the entire points
                                                  # as a tuple to the 
                                                  # triangles list.

    return triangles # Return all triangles


# until here should be submitted by next week - 18.12.2014


def get_array_of_matching_points(size, triangles_list,
                                 intermediate_triangles_list):
    """ """
    max_x, max_y = size

    final_image = ([[0] * max_y]) * max_x

    for i in range(max_x):
        for j in range(max_y):

            for tr in intermediate_triangles_list:
                point = (i,j)
                p1, p2, p3 = tr 
                result     = is_point_inside_triangle(point, p1, p2, p3)

                if result[0]:
                    new_point = compute_new_point(tr, result[1])

                    final_image[i][j] = new_point
        
    return final_image

                




def compute_new_point(old_triangle, coefficients):
    xs = (old_triangle[0][0], old_triangle[1][0], old_triangle[2][0])
    ys = (old_triangle[0][1], old_triangle[0][1], old_triangle[0][1])
    

    x = (coefficients[0] * xs[0]) + (coefficients[1] * xs[1]) + \
    (coefficients[2] * xs[2])

    y = (coefficients[0] * ys[0]) + (coefficients[1] * ys[1]) + \
    (coefficients[2] * ys[2])

    return (x,y)


def create_intermediate_image(alpha, size, source_image, target_image,
                              source_triangles_list, target_triangles_list):
   # This function gets an alpha, size, source image and target image
   # and needs to return an intermediate image based on that data.


    # Source image - max_y * max_x size multiarray
    inter_tr = get_intermediate_triangles(source_triangles_list,
                                            target_triangles_list,
                                            alpha)

    source_matching_points = get_array_of_matching_points( 
                                            size,
                                            source_triangles_list,
                                            inter_tr)


    target_matching_points = get_array_of_matching_points( 
                                            size,
                                            target_triangles_list,
                                            inter_tr)

    max_x, max_y = size 
    
    final_image = ([[0] * max_y]) * max_x
    
    for row in range(max_y):
        for cell in range(max_x):

            source_RGB = source_image[cell,row]
            target_RGB = target_image[cell,row]            

            r = int((((1-alpha)*source_RGB[0]) + (alpha*target_RGB[0])))
            g = int((((1-alpha)*source_RGB[1]) + (alpha*target_RGB[1])))
            b = int((((1-alpha)*source_RGB[2]) + (alpha*target_RGB[2])))

            final_image[cell][row] = (r,g,b)

    return final_image



def create_sequence_of_images(size, source_image, target_image, 
                source_triangles_list, target_triangles_list, num_frames):

    num_frames = 2

    images = []

    for frame in range(num_frames):
        alpha = (frame / (num_frames - 1))
        current_frame = create_intermediate_image(alpha, size, source_image, target_image, source_triangles_list, target_triangles_list)
        images.append(current_frame)


    return images



# until here should be submitted by 25.12.2014

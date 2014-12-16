from SolveLinear3 import solve_linear_3


def is_point_inside_triangle(point, v1, v2, v3):
    """
    This function check if a given point is in the area of the 
    triangle.

    point == tuple of 2 numbers, i.e (0,3)
    v1,v2,v3 are tuples of 2 numbers each (1,2) (3,4) (5,6)

    OUTPUT: 
    (boolean, (1,2,3))
    """

    xs = [v1[0], v2[0], v3[0]]
    ys = [v1[1], v2[1], v3[1]]
    zs = [1, 1, 1]

    coefficients_lists = [xs, ys, zs]
    right_hand_lists = [point[0], point[1], 1]

    a, b, c = solve_linear_3(coefficients_lists, right_hand_lists)
    
    if a <= 0 or b <= 0 or c <= 0:
        return (False, (a,b,c))
    else:
        return (True, (a,b,c))



def create_triangles(list_of_points):
    """
    INPUT: list of x_i, y_i [(0,1),(2,0)...]
    
    OUTPUT: list of triangles:
            [((x,y),(x2,y2),(x3,y3)), ((x,y),(x2,y2),(x3,y3)), ..]


    """
    points = range(4, len(list_of_points))
    triangles = []
    
    # Add the initial triangles (corners of the images)

    triangles.append((list_of_points[0], list_of_points[1], list_of_points[2])) 
    triangles.append((list_of_points[0], list_of_points[2], list_of_points[3])) 

    for point_idx in range(4, len(list_of_points)):
        p = list_of_points[point_idx]

        for t in range(0, len(triangles)):
            v1, v2, v3 = triangles[t]
            if is_point_inside_triangle(p, v1, v2, v3)[0]:
                new_triangles = add_3_triangles(p, v1, v2, v3)
                triangles.pop(t)
                triangles.extend(new_triangles)

    return triangles

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
    return True


def get_point_in_segment(p1, p2, alpha):
    pass


def get_intermediate_triangles(source_triangles_list, target_triangles_list,
                                                                  alpha):
    pass

# until here should be submitted by next week - 18.12.2014


def get_array_of_matching_points(size,triangles_list ,
                                 intermediate_triangles_list):
    pass


def create_intermediate_image(alpha, size, source_image, target_image,
                              source_triangles_list, target_triangles_list):
    pass


def create_sequence_of_images(size, source_image, target_image, 
                source_triangles_list, target_triangles_list, num_frames):
    pass


# until here should be submitted by 25.12.2014

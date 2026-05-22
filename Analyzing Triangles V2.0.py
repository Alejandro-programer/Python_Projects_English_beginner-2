# Read the three segments.
segment_1 = int(input('First segment: '))
segment_2 = int(input('Second segment: '))
segment_3 = int(input('Third segment: '))

# First, check whether the segments can form a triangle.
if segment_1 + segment_2 > segment_3 and segment_1 + segment_3 > segment_2 and segment_2 + segment_3 > segment_1:
    # After confirming the triangle, classify it by its sides.
    if segment_1 == segment_2 == segment_3:
        print('The segments above CAN FORM an EQUILATERAL triangle!')
    elif segment_1 == segment_2 or segment_1 == segment_3 or segment_2 == segment_3:
        print('The segments above CAN FORM an ISOSCELES triangle!')
    else:
        print('The segments above CAN FORM a SCALENE triangle!')
else:
    print('The segments above CANNOT FORM a triangle!')
import math


def plot_sub_sections(point, section_type):

    ## Tan(9degrees)
    # clock of degrees

    if section_type is 'NorthEast':
        degree = 9
    elif section_type is 'SouthEast':
        degree = 99
    elif section_type is 'SouthWest':
        degree = 189
    else: degree = 279


    sect = ['one','two','three','four','five','six','seven','eight','nine','ten']
    sub_sections = {}
    ## ploty = mx - b
    #degree = 9
    for s in sect:
        slope = (math.tan(math.radians(degree)))
        mx = (slope * point[0])
        b = point[1] - mx
        sub_sections[s] = [slope, b]
        degree +=9


    return sub_sections

def split_section(section_type, point, section_points):


    sub_sections = plot_sub_sections(point,section_type)

    return sub_sections



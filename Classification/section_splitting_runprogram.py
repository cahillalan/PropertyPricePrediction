import csv
import compassSplitter
import sectionStepper

def run_section_splitter(newhouses,point,price,label,gate,borderpoints):

    ##send in all border points
    #borderpoints is done...

    ##send to a border points function
    ##return each compass of border points.
    ##send with 'SouthEast' etc.
    north_eastb,north_westb,south_eastb,south_westb,northb,southb,eastb,westb,the_centreb = compassSplitter.splitter(borderpoints,point)
    north_east,north_west,south_east,south_west,north,south,east,west,the_centre = compassSplitter.splitter(newhouses,point)
    ## split the houses into nsew etc

    # send each set of properties into the classifier with the relevant string
    south_east_endpoints,south_east_points = sectionStepper.step_Section('SouthEast',point,south_east,price,label,gate,south_eastb)
    north_east_endpoints, north_east_points= sectionStepper.step_Section('NorthEast',point,north_east,price,label,gate,north_eastb)
    north_west_endpoints,north_west_points = sectionStepper.step_Section('NorthWest', point, north_west, price, label,gate,north_westb)
    south_west_endpoints,south_west_points = sectionStepper.step_Section('SouthWest', point, south_west, price, label,gate,south_westb)
    north_endpoints,north_points = sectionStepper.step_nsew(point,north,price,label,gate,'north',northb)
    south_endpoints, south_points = sectionStepper.step_nsew(point, south, price, label, gate, 'south',southb)
    east_endpoints, east_points = sectionStepper.step_nsew(point, east, price, label, gate, 'east',eastb)
    west_endpoints, west_points = sectionStepper.step_nsew(point, west, price, label, gate, 'west',westb)

    # if the point has a distance add it to the section points

    section_points = []
    for pt in south_east_endpoints:
        if pt['Distance']:
            section_points.append(pt)
    for pt in north_east_endpoints:
        if pt['Distance']:
            section_points.append(pt)
    for pt in north_west_endpoints:
        if pt['Distance']:
            section_points.append(pt)
    for pt in south_west_endpoints:
        if pt['Distance']:
            section_points.append(pt)
    for pt in south_endpoints:
        if pt['Distance']:
            section_points.append(pt)
    for pt in north_endpoints:
        if pt['Distance']:
            section_points.append(pt)
    for pt in east_endpoints:
        if pt['Distance']:
            section_points.append(pt)
    for pt in west_endpoints:
        if pt['Distance']:
            section_points.append(pt)


   # print(section_points)
    #append all the houses from the subsections to the full list.
    all_houses = []
    for house in south_east_points:
        all_houses.append(house)
    for house in south_west_points:
        all_houses.append(house)
    for house in north_east_points:
        all_houses.append(house)
    for house in north_west_points:
        all_houses.append(house)
    for house in north_points:
        all_houses.append(house)
    for house in west_points:
        all_houses.append(house)
    for house in east_points:
        all_houses.append(house)
    for house in south_points:
        all_houses.append(house)
    for house in the_centre:
        all_houses.append(house)

    count = 0
    # remove compas section and distance to prevent crossover issues
    for house in all_houses:
        try:
            del house['Compass']
        except:
            a=1
        try:
            del house['Section']
        except:
            a = 2
        try:
            del house['Distance']
        except:
            a=3
        if house['label']:
            count+= 1

    ###returns wrong amount of houses
    return section_points,all_houses


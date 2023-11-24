import sectionSplitter
import math
import operator

def order_points(point,points):



    for p in points:
        p['Distance'] = 0
    # calculate the distance using sqrt(x-x^2 + y-y^2)

    x = point[0]
    y = point[1]

    for p in points:
        x2 = p['LatLng'][0]
        y2 = p['LatLng'][1]
        mx = ((x2) - (x))
        my = ((y2) - (y))
        add = ((mx) + (my))
        sq = ((add) * (add))
        distance = math.sqrt(sq)
        p['Distance'] = distance



    return points

def claasify_points_section(points, sub_sections,section_type) :

    for p in points:
        p['Section'] = ''

    # plot point into y = mx + b

    for key, section in sub_sections.items():
        for point in points:

            x = point['LatLng'][0]
            y = point['LatLng'][1]
            m = sub_sections[str(key)][0]
            b = sub_sections[str(key)][1]
            # use y = mx+b formula
            mx = m*x
            test = (mx + b) - (y)

            if point['Section'] == '':
                if section_type is 'SouthEast' or 'NorthEast':
                    # if the section is southeast or northeast then the point is in this section
                    # if it is on the line-test is 0
                    # or
                    # if test is greater than zero
                    # the point is on the right of the line
                    # meaning it is in this section.
                    if test is 0:
                        point['Section'] = key

                    elif test > 0:
                        point['Section'] = key

                else:
                    # otherwise it is the opposite
                    if test is 0:
                        point['Section'] = key
                    elif test < 0:
                        point['Section'] = key

    for p in points:
        if p['Section'] == '':
            p['Section'] = 'Unknown'

    return points


def step_through_nsew_points(points, price, label, gate, point, compass, borders):
    # step through points and assign lable where necessary:
    point_dict = {}
    point_dict[compass] = []
    # use the gate to assign a small and big point for reference
    small = price - gate
    big = price + gate
    # sort the points and borders by their distance
    points.sort(key=operator.itemgetter('Distance'))
    borders.sort(key=operator.itemgetter('Distance'))
    endpointa = ''
    if borders:
        endpointa = borders[0]
    # the closest border point for this section is used as an end point reference

    end_points =[]
    end_points.append({'Label': label, 'Compass': compass, 'Section': compass, 'Distance': 0})

    counter = 0
    endpoint = ''

    for p in points:
        # for all points
        if endpointa:
            # if the endpoint a was set continue
            # IF A
            if p['Distance'] < endpointa['Distance']:
                # IF B
                # if the distance of the point is less than the distance of endpoint a continue.
                # distance is saved as avalue and represents the distance between p and endpointa

                if float(p['price']) > small and float(p['price']) < big:
                    # if the price is within the gate
                    if p['label'] == '':
                        # if the point has no label set
                        p['label'] = label
                        # assign a label
                        counter = 0

                        # put counter as 0
                else:
                    # if the counter is already one then the border has been found so set the p as the endpoint
                    if counter == 1:
                        endpoint = p
                    else:
                        # otherwise set the tempoint and increment counter
                        temppoint = p
                        # temp point is unused and only declared as a demonstration
                        # this point gets missed here but is assigned later in another function
                        counter += 1
                # if endpoint the set enpoints lat and lang
                if endpoint:
                    end_points[0]['LatLng'] = endpoint['LatLng']
                    end_points[0]['Distance'] = endpoint['Distance']
                    break
            else:
                #If B
                if endpoint:
                    # if endpoint the set enpoints lat and lang
                    end_points[0]['LatLng'] = endpoint['LatLng']
                    end_points[0]['Distance'] = endpoint['Distance']
                    break
                else:
                    endpoint = endpointa
                    # otherwise set the enpoints 0 to endpointa
                    end_points[0]['LatLng'] = endpointa['LatLng']
                    end_points[0]['LatLng'] = endpointa['LatLng']
                    break
                # then break as all further points are outside the borderpoint

        else:
            # If A
            # otherwise if there is no border do the following
            # repeat of the above loops
            if float(p['price']) > small and float(p['price']) < big:
                if p['label'] == '':
                    p['label'] = label
                    counter = 0


            else:
                if counter == 1:
                    endpoint = p
                else:
                    temppoint = p
                    counter += 1

            if endpoint:
                end_points[0]['LatLng'] = endpoint['LatLng']
                end_points[0]['Distance'] = endpoint['Distance']
                break
    return end_points


def step_through_points(points, price, label, gate, point, compass, borders):
    # step through points and assign lable where necessary:
    point_dict = {}
    #print('@STEPPING POINTS')
    ###new dict of lists
    #################needs reviewing
    ####Possibly setting the wrong distances
    for p in points:
        point_dict[str(p['Section'])]=[]
    for p in points:
        point_dict[p['Section']].append(p)
    for keys,vale in point_dict.items():
        point_dict[keys].sort(key=operator.itemgetter('Distance'))
    the_border_points = {}
    # sort by distance
    big = price + gate
    small = price - gate
    # set the gate
    sect = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten','Unknown']
    for s in sect:
        the_border_points[s] = []
    for b in borders:
        the_border_points[b['Section']].append(b)
    ###put the other borderpoints into a list for each section to make it easier to eliminate ones too far away.
    for s in sect:
        for key,value in the_border_points.items():
            from operator import itemgetter
            the_border_points[key] = sorted(value, key=itemgetter('Distance'))
            # sort each dictionary of points based off of distance
            if len(the_border_points[key]) > 0:
                the_border_points[key] = the_border_points[key][0:1]
            # set the border points list is longer than 0 then slice off the positions above 0.


    end_points =[]
    ###set a distance for each endpoint
    for i in sect:
        # create reference variables for later!
        end_points.append({'Label':label,'Compass':compass,'Section':i,'Distance':0,'Point':point})
    # iter through the dictionary
    for key, value in point_dict.items():

        # BIGGEST DIFFERENCE HERE
        # iterate through the the point-dict
        # This repeats the previous functions transactions on each section instead of just nsew
        counter = 0
        endpoint = ''
        # iter through the list at dict point
        if the_border_points[key]:

            for p in point_dict[key]:
                # check to see if this point fits the criteria
                if p['Distance'] < the_border_points[key][0]['Distance']:

                    if float(p['price']) >small and float(p['price']) < big:

                        if p['label'] == '':
                            p['label'] = label
                            ##assign a label
                            counter = 0

                    else:
                        if counter == 1:
                            endpoint = p
                        else:
                            temppoint = p
                            counter+=1


                    if endpoint:
                        for pt in end_points:
                            if pt['Section'] == key:
                                pt['LatLng'] = endpoint['LatLng']
                                pt['Distance'] = endpoint['Distance']
                        break
                else:
                    if endpoint:
                        break
                    else:
                        endpoint = the_border_points[key][0]
                        for pt in end_points:
                            if pt['Section'] == key:
                                pt['LatLng'] = endpoint['LatLng']
                                pt['Distance'] = endpoint['Distance']
                        break

        else:

            for p in point_dict[key]:
                # check to see if this point fits the criteria
                if float(p['price']) > small and float(p['price']) < big:

                    if p['label'] == '':
                        p['label'] = label
                        ##assign a label
                        counter = 0

                else:
                    if counter == 1:
                        endpoint = p
                    else:
                        temppoint = p
                        counter += 1

                if endpoint:
                    for pt in end_points:
                        if pt['Section'] == key:
                            pt['LatLng'] = endpoint['LatLng']
                            pt['Distance'] = endpoint['Distance']
                    break

    #ordered_end_points = order_points(point,end_points)

    return end_points


def checkpoints(orderedpoints,endpoints,label):
# thi sets the missed point tempoint
    for point in orderedpoints:
        ####here is wherer i had new label setting
        try:
            if point['Distance'] < endpoints[point['Section']]['Distance']:
                if point['label'] == '':
                    point['label'] = label
        except:
            #print(point['Distance'])
            #print(endpoints[point['Section']])
            a = 1

    return orderedpoints

def get_all_borders(section_points):

    all_borders=[]
    for house in section_points:
        if house['label']:
            all_borders.append(house)

    return all_borders

def step_Section(section_type,point,section_points,price,label,gate,borders ):

    ## recieve borderpoints
    all_borders = get_all_borders(section_points)

    ##split into sections
    ##get the closest for each section.


    sub_sections = sectionSplitter.split_section(section_type,point,section_points)
    if all_borders:
        all_borders = claasify_points_section(all_borders,sub_sections,section_type)
        all_borders = order_points(point,all_borders)

    section_points = claasify_points_section(section_points,sub_sections,section_type)

    ordered_points = order_points(point,section_points)

    #Actually Step through the points!!!!!
    ###needs new input
    ####pass the borderpoints to the function
    ##use the border points to ensure that the function does not pass over the points of another area
    endpoints = step_through_points(ordered_points,price,label,gate,point,section_type,all_borders)
    ##endpoints is a list only
    section_points = checkpoints(ordered_points, endpoints,label)

    #border_equations = plot_border(point,endpoints,section_type)


    return endpoints,section_points

def step_nsew(point,section_points,price,label,gate,compass,borders):
    if borders:
        borders = order_points(point, borders)

    ordered_points = order_points(point,section_points)
    endpoints = step_through_nsew_points(ordered_points, price, label, gate, point,compass,borders)
    section_points = checkpoints(ordered_points, endpoints, label)

    return endpoints,section_points
    ###order the points
    # root[(x2-x1)sq + (y2-y1)sq]
    # step each section

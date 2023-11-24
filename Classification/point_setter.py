import section_splitting_runprogram


def check_coverage(coverage_houses):
    # checks how many houses have a label and returns percentage
    count = 0
    for house in coverage_houses:
        if house['label']:
            #print(house)
            count +=1
    amount = len(coverage_houses)

    percent = count/amount
    print('MY NEW %%%%%%%%%%%%%%%% COVERAGE')
    print(percent)
    return percent



def set_point(set_point_houses,lowprice):
    price = 99999999999
    point = []
    ##initialise point to [] and price to 999999999999999999999

    myhouse = ''
    ###loop through the houses
    for house in set_point_houses:
        #if a house has a label it is excluded
        if house['label']: n = 'no'
        else:
            #otherwise it is tested to see if it fits between the prices
            if float(house['price']) < float(price) and float(house['price']) > float(lowprice):
                #price is set to the first house that is lower than 999999999 and greater than the lowprice
                price = float(house['price'])
                #point is also set to this house's point
                point = house['LatLng']
                myhouse = house
    ###if a house has been choosen as a viable house then its price is set to lowprice.
    ###this stops the program lloking for previous low priced houses!!!!
    if myhouse:
        lowprice = myhouse['price']
    ###returns both variabnles.
    return point,lowprice
def test_area(test_allhouses,area,length):
    ####testing area to ensure it has a length over 8% of the total houses
    count = 0
    amount = length *.08

    for h in test_allhouses:
        if h['label'] == str(area):
            count +=1
    if count < amount:
        check = False


    else:
        check = True
    ### if check is false reset all values the same as the area sent in as that area is invalid
    # other previous areas are valid so dont reset all values!!!
    if check == False:
        for h in test_allhouses:
            if h['label'] == str(area):
                h['label'] = ''
    ##return all houses and check
    return check,test_allhouses


def nintey_percent_runner(nhouses,gate,price,lowprice,borderpoints,length):
    ### run the splitter untill 90% coverage
    # check coverage
    points = []
    perc = check_coverage(nhouses)
    area = 1

    #set area and border and test
    areatest = False
    percentage = []
    # while the percentage coverage is less than 85%
    while perc < .85:
        number = 0
        #while area test is False ***** this should stop areas with 0 from escaping!!!!!
        while areatest == False:
            print(number)
            # set point and the lowprice
            point,lowprice = set_point(nhouses,lowprice)
            # makesure there is a point to use as reference
            if point:

                #lowprice = float(point['price'])
                ##if there is a point of reference then run the section splitter running program.
                ##return borders and nhouses
                newgate = gate
                gatetest = False
                ########################################################################################################
                while newgate < 2500000 and gatetest == False:

                    newborderpoints, nhouses = section_splitting_runprogram.run_section_splitter(nhouses, point,
                                                                                            price, str(area),
                                                                                                 newgate,borderpoints)
                    gatetest,ngate = test_area(nhouses,area,length)
                    newgate+= 5000
                ##test the area
                for pt in newborderpoints:
                    borderpoints.append(pt)

                areatest, nhouses = test_area(nhouses, area,length)
            #otherwise escape the entire loop as no points are left
            else:
                print('AREA IS 12')
                # not ideal but effective way of escaping the while areatest loop
                area = 12
                areatest = True
            number+=1
            #number is the label and is incremented after each new label is set


        areatest = False
        lowprice = 0



        percentage.append(check_coverage(nhouses))
        perc = check_coverage((nhouses))
        my_dict = {}
        #set my dict params for future use
        my_dict['point'] = point
        my_dict['label'] = area
        points.append(my_dict)
        area += 1

        if area > 10:
            perc = 1.1
        #escape the loop as 10 areas is too big
    if not percentage:
        percentage.append(check_coverage(nhouses))
    print(percentage)
    return area,borderpoints,nhouses,percentage[0],points


def checknumber(area):
    if area < 11 and area >3:
        check = True
    else: check = False
    # check if area numbers is acceptable

    return check

def opening_gate(gate,houses,lowprice,price,borderpoints,length):
    # set the opening gate
    newgate = gate
    area = 1
    gatetest = False
    point, lowprice = set_point(houses, lowprice)
    # run the loop through the classifier untill the classifier returns a viable gate
    while newgate < 700000 and gatetest == False:
        newborderpoints, nhouses = section_splitting_runprogram.run_section_splitter(houses, point,
                                                                                     price, str(area), newgate,
                                                                                     borderpoints)
        gatetest, ngate = test_area(nhouses, area,length)
        newgate += 5000
    return newgate

def new_gate(gate,houses,lowprice,price,borderpoints,length,oldcoverage):
    newgate = gate
    area = 1
    gatetest = False
    coverage = 0
    # ad .001 to ensure an increase in the coverage
    oldcoverage = oldcoverage + .001
    print(oldcoverage)
    print('Outside')
    point, lowprice = set_point(houses, lowprice)
    while gatetest == False or coverage <= oldcoverage :
        # run through classier in loops untill a new larger coverage is found in comparison to the last one

        for h in houses:
            h['label'] = ''
        newborderpoints, nhouses = section_splitting_runprogram.run_section_splitter(houses, point,
                                                                                     price, str(area), newgate,
                                                                                     borderpoints)
        gatetest, ngate = test_area(nhouses, area,length)
        newgate += 5000
        coverage = check_coverage(nhouses)
        print('HERE')
        print(newgate)
        print(coverage)
        # problem with recurring rerunning of the loop had to be stopped by using this coverage > .9
        if coverage > .9:
            break
    return newgate,coverage

def number_of_areas(newhouses,price,length):
    print(length)
    gate = opening_gate(0,newhouses,0,price,[],length)
    #assign the gate
    percentage = 0
    check = False
    while check == False:
        # loop while the check for the area numbers is false
        lowprice = 0
        for h in newhouses:
            h['label'] = ''
        #assign/reset label to null
        borders =[]
        gate,p = new_gate(0, newhouses, 0, price, [], length, percentage)
        if p > .9:
            break
        # second break for over 90% as a safety. Will return no borders so no values are saved
        area,borders,mynewhouses,percentage,points = nintey_percent_runner(newhouses, gate, price,lowprice,borders,length)
        check = checknumber(area)
        print('PERCENTAGE',percentage)
        print('a')
        print(gate)



    print('FFFFFFFFFFFFFFFFFIIIIIIIIIIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNNNNNAAAAAAAAAAAAAAAAAAAAAAAALLLLLLLLLLLLLLLLLLLLLL')

    return borders,mynewhouses,gate,area,points



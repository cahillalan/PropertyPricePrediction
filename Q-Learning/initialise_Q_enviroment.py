import csv


def createDict():
    financial_list = []
    value = 100000
    for lp in range(99):
        financial_list.append({'Value':value})
        value+= 100000

# initialise a 2d array of increments of 5000 on the x and 100,000 on the y
    for dic in financial_list:
        dic['5KStep']={}
        val = dic['Value']
        actions = []
        for lp in range(20):
            plus5 =val + 5000
            minus5 = val - 5000
            plus100 = val +100000
            minus100 = val - 100000
            if plus5 > 9995000 or plus5 < 100000:
                plus5 = val
            if minus5 > 9995000 or minus5 < 100000:
                minus5 = val
            if plus100 > 9995000 or plus100 < 100000:
                plus100 = val
            if minus100 > 9995000 or minus100 < 100000:
                minus100 = val

            # each has an up a down a left and a right
            #up = -100k
            # down = +100k
            # left = minus 5k
            # right = plus 5k
            # if at an edge the choice rebounds
            # hence the if statement

            dic['5KStep'][val] = {}
            dic['5KStep'][val]['Actions']={'Minus5k':{'Q':0,'ActionVal':minus5,'Exit':False},'Plus5k':{'Q':0,'ActionVal':plus5,'Exit':False},
                                                'Minus100k':{'Q':0,'ActionVal':minus100,'Exit':False},
                                                'Plus100k':{'Q':0,'ActionVal':plus100,'Exit':False}}

            val+= 5000

    return financial_list


def set_exit_points(exits):
    environment = createDict()
    position = 100000
    # get the details from a house entery method.
    #####all next steps containing the action val ex
    for env in environment:
        # loop down te list and check if the list contains a dict with the exit number

        for ex in exits:
            ex = int(ex)
            if ex in env['5KStep'].keys():
                print('INENV')
                env['5KStep'][ex]['Exit'] = True
            steps = env['5KStep'].keys()
            for step in steps:
                # if it dows then set all steps towards that exit number as exits
                # and the Q value to 1
                if ex == env['5KStep'][step]['Actions']['Minus5k']['ActionVal']:
                    env['5KStep'][step]['Actions']['Minus5k']['Q'] = 1
                    env['5KStep'][step]['Actions']['Minus5k']['Exit'] = True
                if ex == env['5KStep'][step]['Actions']['Plus5k']['ActionVal']:
                    env['5KStep'][step]['Actions']['Plus5k']['Q'] = 1
                    env['5KStep'][step]['Actions']['Plus5k']['Exit'] = True
                if ex == env['5KStep'][step]['Actions']['Minus100k']['ActionVal']:
                    env['5KStep'][step]['Actions']['Minus100k']['Q'] = 1
                    env['5KStep'][step]['Actions']['Minus100k']['Exit'] = True
                if ex == env['5KStep'][step]['Actions']['Plus100k']['ActionVal']:
                    env['5KStep'][step]['Actions']['Plus100k']['Q'] = 1
                    env['5KStep'][step]['Actions']['Plus100k']['Exit'] = True


    return environment


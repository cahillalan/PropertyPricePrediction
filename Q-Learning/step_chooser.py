import operator
import random

def choose_next_step(position,env):
    my_list = []
    position = int(position)
    for e in env:
        if position in e['5KStep'].keys():
            plus5k = [e['5KStep'][position]['Actions']['Plus5k']['Q'],'Plus5k',e['5KStep'][position]['Actions']['Plus5k']['ActionVal'],e['5KStep'][position]['Actions']['Plus5k']['Exit']]
            minus5k = [e['5KStep'][position]['Actions']['Minus5k']['Q'],'Minus5k',e['5KStep'][position]['Actions']['Minus5k']['ActionVal'],e['5KStep'][position]['Actions']['Minus5k']['Exit']]
            minus100k = [e['5KStep'][position]['Actions']['Minus100k']['Q'], 'Minus100k',e['5KStep'][position]['Actions']['Minus100k']['ActionVal'],e['5KStep'][position]['Actions']['Minus100k']['Exit']]
            plus100k = [e['5KStep'][position]['Actions']['Plus100k']['Q'], 'Plus100k',e['5KStep'][position]['Actions']['Plus100k']['ActionVal'],e['5KStep'][position]['Actions']['Plus100k']['Exit']]
            my_list.append(plus5k)
            my_list.append(minus5k)
            my_list.append(minus100k)
            my_list.append(plus100k)
    # enters the env and supplies the possible choices to the list
    # the list is sorted in descendiing order
    my_list = sorted(my_list, key = operator.itemgetter(0), reverse=True)
    maximumq = my_list[0][0]
    # the first is set as the highest and then a random choice is enforced
    # if there is a match of two choices
    final_list = []
    for i in my_list:
        if i[0] == maximumq:
            final_list.append(i)

    nextstep = random.choice(final_list)

    return nextstep

def get_max(position,env):
    my_list = []
    for e in env:
    # enters the environment and finds the mas then returns the relevant data
        if position in e['5KStep'].keys():
            plus5k = [e['5KStep'][position]['Actions']['Plus5k']['Q'], 'Plus5k',
                      e['5KStep'][position]['Actions']['Plus5k']['ActionVal']]
            minus5k = [e['5KStep'][position]['Actions']['Minus5k']['Q'], 'Minus5k',
                       e['5KStep'][position]['Actions']['Minus5k']['ActionVal']]
            minus100k = [e['5KStep'][position]['Actions']['Minus100k']['Q'], 'Minus100k',
                         e['5KStep'][position]['Actions']['Minus100k']['ActionVal']]
            plus100k = [e['5KStep'][position]['Actions']['Plus100k']['Q'], 'Plus100k',
                        e['5KStep'][position]['Actions']['Plus100k']['ActionVal']]
            my_list.append(plus5k)
            my_list.append(minus5k)
            my_list.append(minus100k)
            my_list.append(plus100k)

    my_list = sorted(my_list, key=operator.itemgetter(0), reverse=True)
    maximumq = my_list[0][0]

    return maximumq



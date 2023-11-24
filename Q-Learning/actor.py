import initialise_Q_enviroment as envinit
import step_chooser
import q_value_handler
import time

def get_predictions(environment,oldposition):
    old_pos = 0
    position = oldposition
    loopexit = False
    x = 0
    while not loopexit:
    # while the loopexit is not true the loop keeps chhoosing a new step
        new_pos = step_chooser.choose_next_step(position,environment)

        # if ever the loop rebounds it is then stuck and must be exited imediatley
        if new_pos[2] == old_pos:
            loopexit = True
            position = 0
        else:
            old_pos = position
            loopexit = new_pos[3]
            position = new_pos[2]
        x+=1
    # if the loop goes above 2000 it is likley to be caught in a constant and must be exited
        if x > 2000:
            loopexit=True
            position = 0
    return position





def update_all_qvalues(environment,oldposition):
    #env = envinit.set_exit_points()
    totaltest = True
    needstraining = True
    while needstraining:
        position = oldposition
        loopexit = False
        trainingcheck = True
        x = 0
        while not loopexit:
            x+=1
            new_pos = step_chooser.choose_next_step(position,environment)
            newmax = step_chooser.get_max(new_pos[2],environment)
            Q = new_pos[0]
            if Q > 10:
                needstraining = False
            loopexit = new_pos[3]

            for e in environment:
                if position in e['5KStep'].keys():
                    if loopexit == False:
                        # fixing a bug for long floats
                        newq = float("{0:.5f}".format(q_value_handler.calculate_new_Q(Q,newmax)))
                        if Q == newq:
                            a=1
                        if str(Q) != str(newq):

                            trainingcheck = False
                            totaltest = False
                        e['5KStep'][position]['Actions'][new_pos[1]]['Q'] = newq
            if x > 5000:
                loopexit = True

            position = new_pos[2]
        if trainingcheck:
            needstraining = False

    return environment,totaltest

def enter_environment(exit_points ):


    environment = envinit.set_exit_points(exit_points)
    # set the exit points

    totaltest = False
    while not totaltest:
        # total test is designed to keep the loop continuing
        # only a complete run with no updates will make it return true
        position = 100000
        position2 = 195000
        for lp in range(99):
            environment,totaltest = update_all_qvalues(environment, position)
            if totaltest:
                # if true it will be retested
                environment, totaltest = update_all_qvalues(environment, position2)
            else:
                # if false a seperate value will be used as a false on the first
                # means the loop should not break
                environment, totaltest2 = update_all_qvalues(environment, position2)
            position += 100000
            position2 += 100000

    return environment





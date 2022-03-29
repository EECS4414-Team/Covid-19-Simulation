from glob import glob
import simulation.global_state as global_state
import matplotlib.pyplot as plt


def build_graph(tuple_list):
    healthy = [x[0] for x in tuple_list]
    infected = [x[1] for x in tuple_list]
    dead = [x[2] for x in tuple_list]
    immune = [x[3] for x in tuple_list]

    x_axis = list(range(global_state.cycle_number))

    _, ax1 = plt.subplots()
    line1, = ax1.plot(x_axis, healthy, color='red', label='healthy')
    line2, = ax1.plot(x_axis, infected, color='blue', label='infected')
    line3, = ax1.plot(x_axis, dead, color='black', label='dead')
    line4, = ax1.plot(x_axis, immune, color='green', label='immune')
    ax1.set_ylabel('count')
    ax1.set_xlabel('cycle')
    plt.xticks(list(range(1, global_state.cycle_number, global_state.cycle_number//10)))
    plt.legend(handles=[line1,line2,line3,line4])
    plt.title('count of states each person is in')
    plt.savefig('graphs/main_graph.png')
    plt.clf()

def build_early_infection_graph(tuple_list):
    healthy = [x[0] for x in tuple_list][:global_state.cycle_number//10]
    infected = [x[1] for x in tuple_list][:global_state.cycle_number//10]
    dead = [x[2] for x in tuple_list][:global_state.cycle_number//10]
    immune = [x[3] for x in tuple_list][:global_state.cycle_number//10]

    x_axis = list(range(global_state.cycle_number//10))

    _, ax1 = plt.subplots()
    line1, = ax1.plot(x_axis, healthy, color='red', label='healthy')
    line2, = ax1.plot(x_axis, infected, color='blue', label='infected')
    line3, = ax1.plot(x_axis, dead, color='black', label='dead')
    line4, = ax1.plot(x_axis, immune, color='green', label='immune')
    ax1.set_ylabel('count')
    ax1.set_xlabel('cycle')
    plt.xticks(list(range(1, global_state.cycle_number//10, global_state.cycle_number//100)))
    plt.legend(handles=[line1,line2,line3,line4])
    plt.title('count of states each person is in')
    plt.savefig('graphs/early_infection_graph.png')
    plt.clf()


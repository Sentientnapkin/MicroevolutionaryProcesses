import MicroevolutionaryProcesses as mp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plot_dynamic(y_list1, y_list2, title):

    fig, ax = plt.subplots()

    x,y1,y2 = [],[],[]
    def animate(i):
        ax.clear()
        ax.set_xlabel("Generation")
        ax.set_ylabel("Allele Frequency")
        ax.set_title(title)
        x.append(i)
        y1.append(y_list1[i])
        y2.append(y_list2[i])
        ax.plot(x, y1, color="red", label="Dominant Allele")
        ax.plot(x, y2, color="yellow", label="Recessive Allele")
        ax.legend(loc="upper left")

    anim = FuncAnimation(fig=fig, func=animate, frames=20, repeat=False)

    plt.show()

    return fig, ax


gen_list, dom_list, res_list = mp.natural_selection(['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
                                                     'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 20)

fig, ax = plot_dynamic(dom_list, res_list, "Natural Selection")

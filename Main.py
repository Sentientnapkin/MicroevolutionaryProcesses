import sys

import MicroevolutionaryProcesses as mp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pygame

def plot_dynamic_two_alleles(y_list1, y_list2, title):

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
        ax.legend(loc="upper center", bbox_to_anchor=(0.5,1.15),
                  fancybox=True, shadow=True)

    anim = FuncAnimation(fig=fig, func=animate, frames=20, repeat=False)

    plt.show()

    return fig, ax


def plot_dynamic_three_alleles(y_list1, y_list2, y_list3, title):

    fig, ax = plt.subplots()

    x,y1,y2,y3 = [],[],[],[]
    def animate(i):
        ax.clear()
        ax.set_xlabel("Generation")
        ax.set_ylabel("Allele Frequency")
        ax.set_title(title)
        x.append(i)
        y1.append(y_list1[i])
        y2.append(y_list2[i])
        y3.append(y_list3[i])
        ax.plot(x, y1, color="red", label="Dominant Allele")
        ax.plot(x, y2, color="yellow", label="Recessive Allele")
        ax.plot(x, y3, color="blue", label="New Allele")
        ax.legend(loc="upper center", bbox_to_anchor=(0.5,1.15),
                  fancybox=True, shadow=True)

    anim = FuncAnimation(fig=fig, func=animate, frames=20, repeat=False)

    plt.show()

    return fig, ax


gen_list, dom_list, res_list = mp.natural_selection(['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
                                                    'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 20)

# gen_list, dom_list, res_list = mp.artificial_selection(['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
#                                                         'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 20)

#gen_list, dom_list, res_list = mp.sexual_selection(['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
#                                                    'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 20)

# gen_list, dom_list, res_list = mp.bottleneck_effect(['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
#                                                      'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 20)

# gen_list, dom_list, res_list = mp.founder_effect(['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
#                                                   'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 20)

# gen_list, dom_list, res_list, new_list = mp.gene_flow(['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
#                                                        'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 20)

# gen_list, dom_list, res_list, new_list = mp.mutation(['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
#                                                       'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 20)

fig, ax = plot_dynamic_two_alleles(dom_list, res_list, "")
# fig, ax = plot_dynamic_three_alleles(dom_list, res_list, new_list, "")

# Convert the Matplotlib figure to a Pygame surface.
surface = pygame.surfarray.make_surface(fig.canvas.tostring_rgb())

# Blit the Pygame surface to the Pygame window.
pygame.display.blit(surface, (0, 0))

# Update the Pygame window.
pygame.display.update()

# Keep the Pygame window open until the user closes it.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

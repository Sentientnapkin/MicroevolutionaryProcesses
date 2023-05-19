import MicroevolutionaryProcesses as mp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pygame
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import time

class InputBox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ''
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    output = self.text
                    self.text = ''
                    return output
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self):
        color = active_color if self.active else inactive_color
        pygame.draw.rect(screen, color, self.rect, 2)
        text_surface = font.render(self.text, True, text_color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

class Button:
    def __init__(self, x, y, width, height, text, font, click_handler):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.click_handler = click_handler
        self.hovered = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered and self.click_handler:
                self.click_handler()

    def draw(self, screen):
        color = button_hover_color if self.hovered else button_color
        t_color = text_hover_color if self.hovered else text_color
        pygame.draw.rect(screen, color, self.rect)
        text_surface = self.font.render(self.text, True, t_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


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
        ax.legend(loc="upper center", bbox_to_anchor=(0.1,1.15),
                  fancybox=True, shadow=True)

    anim = FuncAnimation(fig=fig, func=animate, frames=20, repeat=False)
    anim.save('dynamic_two_alleles.gif')

    # plt.show()

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
        ax.legend(loc="upper center", bbox_to_anchor=(0.1,1.15),
                  fancybox=True, shadow=True)

    anim = FuncAnimation(fig=fig, func=animate, frames=20, repeat=False)

    plt.show()

    return fig, ax


index = 0
x,y1,y2 = [],[],[]
def update_graph_two_alleles(title):
    ax.clear()
    ax.set_xlabel("Generation")
    ax.set_ylabel("Allele Frequency")
    ax.set_title(title)
    x.append(index)
    y1.append(dom_list[index])
    y2.append(res_list[index])
    ax.plot(x, y1, color="red", label="Dominant Allele")
    ax.plot(x, y2, color="yellow", label="Recessive Allele")
    ax.legend(loc="upper center", bbox_to_anchor=(0.1,1.15),
                fancybox=True, shadow=True)

    return ax

selection_types = {
    "Natural Selection": mp.natural_selection,
    "Artificial Selection": mp.artificial_selection,
    "Sexual Selection": mp.sexual_selection,
    "Bottleneck Effect": mp.bottleneck_effect,
    "Founder Effect": mp.founder_effect,
    "Gene Flow": mp.gene_flow,
    "Mutation": mp.mutation
}    

def selection_handler(button_selection_type):
    global selection_type
    if button_selection_type == "Natural Selection":
        selection_type = "Natural Selection"
    elif button_selection_type == "Artificial Selection":
        selection_type = "Artificial Selection"
    elif button_selection_type == "Sexual Selection":
        selection_type = "Sexual Selection"
    elif button_selection_type == "Bottleneck Effect":
        selection_type = "Bottleneck Effect"
    elif button_selection_type == "Founder Effect":
        selection_type = "Founder Effect"
    elif button_selection_type == "Gene Flow":
        selection_type = "Gene Flow"
    elif button_selection_type == "Mutation":
        selection_type = "Mutation"

def on_button_click():
    global dom_allele_count
    global res_allele_count
    global ready_to_run
    dom_allele_count = int(dom_allele_input.text)
    res_allele_count = int(res_allele_input.text)
    dom_allele_input.text = ''
    res_allele_input.text = ''
    ready_to_run = True
    start_simulation(dom_allele_count, res_allele_count)


def start_simulation(dom_allele_count, res_allele_count):
    global index
    global dom_list
    global res_list
    global gen_list
    global new_list
    global selection_type
    global ready_to_run
    index = 0
    initial_pop = []
    for i in range(dom_allele_count):
        initial_pop.append('A')
    for i in range(res_allele_count):
        initial_pop.append('a')    
    if selection_type == "Mutation" or selection_type == "Gene Flow":  
        gen_list, dom_list, res_list, new_list = selection_types[selection_type](initial_pop, 20)    
    else:
        gen_list, dom_list, res_list = selection_types[selection_type](initial_pop, 20)
    fig, ax = plot_dynamic_two_alleles(dom_list, res_list, "")
    ready_to_run = True


pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# Font settings
font = pygame.font.Font(None, 20)
text_color = pygame.Color('black')
text_hover_color = (255, 255, 0)
active_color = pygame.Color('dodgerblue1')
inactive_color = pygame.Color('gray70')
background_color = (255, 255, 255)
button_color = (0, 128, 255)
button_hover_color = (0, 0, 255)

dom_allele_input = InputBox(10, 10, 300, 32)
res_allele_input = InputBox(10, 50, 300, 32)

enter_button = Button(10, 300, 200, 50, "Click Me", font, on_button_click)
ns_button = Button(10, 100, 175, 60, "Natural Selection", font, lambda: selection_handler("Natural Selection"))
as_button = Button(195, 100, 175, 60, "Artificial Selection", font, lambda: selection_handler("Artificial Selection"))
ss_button = Button(380, 100, 175, 60, "Sexual Selection", font, lambda: selection_handler("Sexual Selection"))
be_button = Button(10, 175, 125, 60, "Bottleneck Effect", font, lambda: selection_handler("Bottleneck Effect"))
fe_button = Button(145, 175, 125, 60, "Founder Effect", font, lambda: selection_handler("Founder Effect"))
gf_button = Button(280, 175, 125, 60, "Gene Flow", font, lambda: selection_handler("Gene Flow"))
mu_button = Button(415, 175, 125, 60, "Mutation", font, lambda: selection_handler("Mutation"))

dom_allele_count = 0
res_allele_count = 0
selection_type = ""

dom_list = []
res_list = []
gen_list = []
new_list = []
fig = None
ax = None

ready_to_run = False
running = True
while running:
    if not ready_to_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            dom_allele_input.handle_event(event)
            res_allele_input.handle_event(event)
            enter_button.handle_event(event)
            ns_button.handle_event(event)
            as_button.handle_event(event)
            ss_button.handle_event(event)
            be_button.handle_event(event)
            fe_button.handle_event(event)
            gf_button.handle_event(event)
            mu_button.handle_event(event)
            

        screen.fill((255, 255, 255))
        dom_allele_input.draw()
        res_allele_input.draw()
        ns_button.draw(screen)
        as_button.draw(screen)
        ss_button.draw(screen)
        be_button.draw(screen)
        fe_button.draw(screen)
        gf_button.draw(screen)
        mu_button.draw(screen)
        enter_button.draw(screen)

    else:    
        if index < len(dom_list)-1:
            index += 1
        # Update the graph and get the updated graph object
        graph = update_graph_two_alleles(selection_type)

        # Convert the Matplotlib figure to a Pygame surface
        canvas = FigureCanvas(graph.figure)
        canvas.draw()

        # Convert the canvas to a Pygame surface
        graph_array = np.frombuffer(canvas.renderer.tostring_rgb(), dtype=np.uint8)
        graph_array = graph_array.reshape((1280,960)[::-1] + (3,))

        # Create a Pygame surface from the array
        graph_surface = pygame.surfarray.make_surface(graph_array)

        graph_surface = pygame.transform.flip(graph_surface, False, True)
        graph_surface = pygame.transform.rotate(graph_surface, 270)

        resized_graph_surface = pygame.transform.scale(graph_surface, (640, 480))

        # Blit the graph surface onto the Pygame window
        screen.blit(resized_graph_surface, (0, 0))

        time.sleep(0.5)

    pygame.display.update()

    clock.tick(60)  # Limit the frame rate to 60 FPS    

pygame.quit()


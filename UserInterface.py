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

x,y1,y2, y3 = [],[],[], []
def update_graph_two_alleles(title):
    ax.clear()
    ax.set_xlabel("Generation")
    ax.set_ylabel("Allele Frequency")
    ax.set_title(title)
    x.append(index+1)
    y1.append(dom_list[index])
    y2.append(res_list[index])
    ax.plot(x, y1, color="red", label="Dominant Allele")
    ax.plot(x, y2, color="yellow", label="Recessive Allele")
    ax.legend(loc="upper center", bbox_to_anchor=(0.1,1.15),
                fancybox=True, shadow=True)

    return ax

def update_graph_three_alleles(title):
    ax.clear()
    ax.set_xlabel("Generation")
    ax.set_ylabel("Allele Frequency")
    ax.set_title(title)
    x.append(index+1)
    y1.append(dom_list[index])
    y2.append(res_list[index])
    y3.append(new_list[index])
    ax.plot(x, y1, color="red", label="Dominant Allele")
    ax.plot(x, y2, color="yellow", label="Recessive Allele")
    ax.plot(x, y3, color="blue", label="New Allele")
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

def start_handler():
    global dom_allele_count
    global res_allele_count
    global ready_to_run
    dom_allele_count = int(dom_allele_input.text)
    res_allele_count = int(res_allele_input.text)
    gen_count = int(generations_input.text)
    dom_allele_input.text = ''
    res_allele_input.text = ''
    generations_input.text = ''
    ready_to_run = True
    start_simulation(dom_allele_count, res_allele_count, gen_count)


def start_simulation(dom_allele_count, res_allele_count, gen_count):
    global index, dom_list, res_list, gen_list, new_list, selection_type, ready_to_run
    global fig, ax
    global y1, y2, y3, x
    index = -1
    initial_pop = []
    for i in range(dom_allele_count):
        initial_pop.append('A')
    for i in range(res_allele_count):
        initial_pop.append('a')    
    if selection_type == "Mutation" or selection_type == "Gene Flow":  
        gen_list, dom_list, res_list, new_list = selection_types[selection_type](initial_pop, gen_count)    
    else:
        gen_list, dom_list, res_list = selection_types[selection_type](initial_pop, gen_count)
    x, y1, y2, y3 = [],[],[], []
    ready_to_run = True

def toggle_ready_to_run():
    global ready_to_run
    ready_to_run = not ready_to_run


pygame.init()
screen = pygame.display.set_mode((940, 480))
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont('Helvetica', 15)

# Color Scheme
text_color = pygame.Color(0, 0, 0)  # Black
text_hover_color = pygame.Color(255, 255, 255)  # White3
active_color = pygame.Color(102, 204, 204)  # Aqua
inactive_color = pygame.Color(200, 200, 200)  # Light Gray
background_color = pygame.Color(245, 245, 245)  # Off-White
button_color = pygame.Color(0, 153, 255)  # Sky Blue
button_hover_color = pygame.Color(0, 102, 204)  # Deep Blue

dom_text, res_text, new_text, gen_text = None, None, None, None

dom_allele_count = 0
res_allele_count = 0
selection_type = ""

dom_list, res_list, new_list, gen_list = [], [], [], []
fig, ax = plt.subplots()
resized_graph_surface = None

ready_to_run = False
running = True

dom_allele_input = InputBox(175, 10, 300, 32)
res_allele_input = InputBox(175, 50, 300, 32)
generations_input = InputBox(175, 90, 300, 32)

dom_allele_input_text = font.render("Dominant Allele Count", True, (0, 0, 0))
res_allele_input_text = font.render("Recessive Allele Count", True, (0, 0, 0))
generations_input_text = font.render("Generations", True, (0, 0, 0))

start_button = Button(10, 300, 200, 50, "Start Simulation", font, start_handler)
ns_button = Button(10, 140, 175, 60, "Natural Selection", font, lambda: selection_handler("Natural Selection"))
as_button = Button(195, 140, 175, 60, "Artificial Selection", font, lambda: selection_handler("Artificial Selection"))
be_button = Button(10, 215, 125, 60, "Bottleneck Effect", font, lambda: selection_handler("Bottleneck Effect"))
fe_button = Button(145, 215, 125, 60, "Founder Effect", font, lambda: selection_handler("Founder Effect"))
gf_button = Button(280, 215, 125, 60, "Gene Flow", font, lambda: selection_handler("Gene Flow"))
mu_button = Button(415, 215, 125, 60, "Mutation", font, lambda: selection_handler("Mutation"))

restart_button = Button(10, 300, 200, 50, "Go Back", font, toggle_ready_to_run)
end_button = Button(10, 375, 200, 50, "End", font, lambda: pygame.quit())

while running:
    if not ready_to_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            dom_allele_input.handle_event(event)
            res_allele_input.handle_event(event)
            generations_input.handle_event(event)
            start_button.handle_event(event)
            ns_button.handle_event(event)
            as_button.handle_event(event)
            be_button.handle_event(event)
            fe_button.handle_event(event)
            gf_button.handle_event(event)
            mu_button.handle_event(event)
            end_button.handle_event(event)
            
        screen.fill(background_color)
        dom_allele_input.draw()
        res_allele_input.draw()
        generations_input.draw()
        ns_button.draw(screen)
        as_button.draw(screen)
        be_button.draw(screen)
        fe_button.draw(screen)
        gf_button.draw(screen)
        mu_button.draw(screen)
        end_button.draw(screen)
        if selection_type != "" and dom_allele_input.text != "" and res_allele_input.text != "" and generations_input.text != "":
            start_button.draw(screen)
        selection_type_text = font.render("Microevolutionary Process: " + selection_type, True, (0, 0, 0))
        screen.blit(selection_type_text, (10, 300))
        screen.blit(dom_allele_input_text, (10, 20))
        screen.blit(res_allele_input_text, (10, 60))
        screen.blit(generations_input_text, (10, 100))

    else:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            restart_button.handle_event(event)
            end_button.handle_event(event)

        font = pygame.font.Font(None, 30)
        screen.fill(background_color)   
        if index < len(dom_list)-1:
            index += 1
        else:
            restart_button.draw(screen)

        end_button.draw(screen)

        #3 alleles
        if selection_type == "Mutation" or selection_type == "Gene Flow":
            if index <= len(dom_list)-1:
                # Update the graph and get the updated graph object
                graph = update_graph_three_alleles(selection_type)

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
            screen.blit(resized_graph_surface, (300, 0))

            d_count = 0
            r_count = 0
            n_count = 0
            for allele in gen_list[index]:
                if allele == 'A':
                    d_count += 1
                elif allele == 'a':
                    r_count += 1
                elif allele == 'M':
                    n_count += 1
            dom_text = font.render("Dominant Allele Count: " + str(d_count), True, (0, 0, 0))
            res_text = font.render("Recessive Allele Count: " + str(r_count), True, (0, 0, 0))
            new_text = font.render("New Allele Count: " + str(n_count), True, (0, 0, 0))
            gen_text = font.render("Generation: " + str(index+1), True, (0, 0, 0))
            screen.blit(dom_text, (10, 10))
            screen.blit(res_text, (10, 30))
            screen.blit(new_text, (10, 50))
            screen.blit(gen_text, (10, 70))

        #2 alleles
        else:
            if index <= len(dom_list)-1:
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
            screen.blit(resized_graph_surface, (300, 0))


            d_count = 0
            r_count = 0
            for allele in gen_list[index]:
                if allele == 'A':
                    d_count += 1
                else:
                    r_count += 1
            dom_text = font.render("Dominant Allele Count: " + str(d_count), True, (0, 0, 0))
            res_text = font.render("Recessive Allele Count: " + str(r_count), True, (0, 0, 0))
            gen_text = font.render("Generation: " + str(index+1), True, (0, 0, 0))
            screen.blit(dom_text, (10, 10))
            screen.blit(res_text, (10, 30))
            screen.blit(gen_text, (10, 70))   


        time.sleep(1)

    pygame.display.update()

    clock.tick(60)  # Limit the frame rate to 60 FPS    

pygame.quit()


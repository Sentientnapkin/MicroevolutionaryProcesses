import sys

import numpy as np
import matplotlib.pyplot as plt
import pygame
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import time
import random
import copy

def natural_selection(alleles, generations):
    dom_list = []
    res_list = []
    new_list = []
    gen_list = []
    for gen in range(generations):
        pairs = []
        allele_dom_count = 0
        allele_res_count = 0
        allele_new_count = 0
        gen_list.append(copy.deepcopy(alleles))
        while len(alleles) > 0:
            allele1 = random.choice(alleles)
            if allele1 == 'A':
                allele_dom_count += 1
            elif allele1 == 'a':
                allele_res_count += 1
            else:
                allele_new_count += 1
            alleles.remove(allele1)

            if len(alleles) == 0:
                break

            allele2 = random.choice(alleles)
            if allele2 == 'A':
                allele_dom_count += 1
            elif allele2 == 'a':
                allele_res_count += 1
            else:
                allele_new_count += 1
            alleles.remove(allele2)

            pairs.append([allele1, allele2])

        allele_dom_freq = allele_dom_count / (allele_dom_count + allele_res_count + allele_new_count)
        dom_list.append(allele_dom_freq)
        allele_res_freq = allele_res_count / (allele_dom_count + allele_res_count + allele_new_count)
        res_list.append(allele_res_freq)
        allele_new_freq = allele_new_count / (allele_dom_count + allele_res_count + allele_new_count)
        new_list.append(allele_new_freq)

        next_generation = []
        for pair in pairs:
            if pair[0] == 'A' and pair[1] == 'A':
                for i in range(3):
                    next_generation.append('A')
            elif pair[0] != pair[1]:
                next_generation.append(pair[0])
                next_generation.append(pair[1])
                rand = np.random.randint(0, 2)
                next_generation.append(pair[rand])

        alleles = next_generation

    return gen_list, dom_list, res_list, new_list


def artificial_selection(alleles, generations):
    dom_list = []
    res_list = []
    new_list = []
    gen_list = []
    for gen in range(generations):
        pairs = []
        allele_dom_count = 0
        allele_res_count = 0
        allele_new_count = 0
        gen_list.append(copy.deepcopy(alleles))
        while len(alleles) > 0:
            allele1 = random.choice(alleles)
            if allele1 == 'A':
                allele_dom_count += 1
            elif allele1 == 'a':
                allele_res_count += 1
            else:
                allele_new_count += 1
            alleles.remove(allele1)

            if len(alleles) == 0:
                break

            allele2 = random.choice(alleles)
            if allele2 == 'A':
                allele_dom_count += 1
            elif allele2 == 'a':
                allele_res_count += 1
            else:
                allele_new_count += 1
            alleles.remove(allele2)

            pairs.append([allele1, allele2])

        allele_dom_freq = allele_dom_count / (allele_dom_count + allele_res_count + allele_new_count)
        dom_list.append(allele_dom_freq)
        allele_res_freq = allele_res_count / (allele_dom_count + allele_res_count + allele_new_count)
        res_list.append(allele_res_freq)
        allele_new_freq = allele_new_count / (allele_dom_count + allele_res_count + allele_new_count)
        new_list.append(allele_new_freq)

        next_generation = []
        for pair in pairs:
            if pair[0] == 'a' and pair[1] == 'a':
                for i in range(3):
                    next_generation.append('a')
            else:
                next_generation.append(pair[0])
                next_generation.append(pair[1])

        alleles = next_generation

    return gen_list, dom_list, res_list, new_list


def founder_effect(alleles, generations):
    return genetic_drift(alleles, generations, np.random.randint(3, 5))


def bottleneck_effect(alleles, generations):
    return genetic_drift(alleles, generations, 4)


def genetic_drift(alleles, generations, survivor_count):
    dom_list = []
    res_list = []
    new_list = []
    gen_list = []

    survivors = []
    for i in range(survivor_count):
        survivors.append(alleles[np.random.randint(0, len(alleles))])

    alleles = survivors
    gen_list.append(copy.deepcopy(alleles))

    allele_dom_count = 0
    allele_res_count = 0
    allele_new_count = 0
    pairs = []
    for i in range(10):
        allele1 = random.choice(alleles)
        if allele1 == 'A':
            allele_dom_count += 1
        elif allele1 == 'a':
            allele_res_count += 1
        else:
            allele_new_count += 1

        allele2 = random.choice(alleles)
        if allele2 == 'A':
            allele_dom_count += 1
        elif allele2 == 'a':
            allele_res_count += 1
        else:
            allele_new_count += 1

        pairs.append([allele1, allele2])

    allele_dom_freq = allele_dom_count / (allele_dom_count + allele_res_count + allele_new_count)
    dom_list.append(allele_dom_freq)
    allele_res_freq = allele_res_count / (allele_dom_count + allele_res_count + allele_new_count)
    res_list.append(allele_res_freq)
    allele_new_freq = allele_new_count / (allele_dom_count + allele_res_count + allele_new_count)
    new_list.append(allele_new_freq)

    next_generation = []
    for pair in pairs:
        if pair[0] == pair[1]:
            for i in range(3):
                next_generation.append(pair[0])
        else:
            next_generation.append(pair[0])
            next_generation.append(pair[1])
            rand = np.random.randint(0, 2)
            next_generation.append(pair[rand])

    alleles = next_generation
    gen_list.append(copy.deepcopy(alleles))

    for gen in range(generations - 1):
        alleles, dom_freq, res_freq, new_freq = standard_reproduction(alleles)
        dom_list.append(dom_freq)
        res_list.append(res_freq)
        new_list.append(new_freq)
        gen_list.append(copy.deepcopy(alleles))

    gen_list.pop()     

    return gen_list, dom_list, res_list, new_list


def gene_flow(alleles, generations):
    gen_list = []
    dom_list = []
    res_list = []
    new_list = []
    for i in range(6):
        alleles.append('B')

    gen_list.append(copy.deepcopy(alleles))
    for gen in range(generations):
        alleles, dom_freq, res_freq, new_freq = gene_flow_wrapper(alleles)
        dom_list.append(dom_freq)
        res_list.append(res_freq)
        new_list.append(new_freq)
        gen_list.append(copy.deepcopy(alleles))

    gen_list.pop()
    return gen_list, dom_list, res_list, new_list    


def gene_flow_wrapper(alleles):
    pairs = []
    allele_dom_count = 0
    allele_res_count = 0
    allele_new_count = 0
    while len(alleles) > 0:
        allele1 = random.choice(alleles)
        if allele1 == 'A':
            allele_dom_count += 1
        elif allele1 == 'a':
            allele_res_count += 1
        else:
            allele_new_count += 1
        alleles.remove(allele1)

        if len(alleles) == 0:
            break

        allele2 = random.choice(alleles)
        if allele2 == 'A':
            allele_dom_count += 1
        elif allele2 == 'a':
            allele_res_count += 1
        else:
            allele_new_count += 1
        alleles.remove(allele2)

        pairs.append([allele1, allele2])

    allele_dom_freq = allele_dom_count / (allele_dom_count + allele_res_count + allele_new_count)
    allele_res_freq = allele_res_count / (allele_dom_count + allele_res_count + allele_new_count)
    allele_new_freq = allele_new_count / (allele_dom_count + allele_res_count + allele_new_count)

    next_generation = []
    for pair in pairs:
        if pair[0] == pair[1]:
            for i in range(3):
                next_generation.append(pair[0])
        else:
            next_generation.append(pair[0])
            next_generation.append(pair[1])
            rand = np.random.randint(0, 2)
            next_generation.append(pair[rand])

    alleles = next_generation
    return alleles, allele_dom_freq, allele_res_freq, allele_new_freq


def mutation(alleles, generations):
    gen_list = []
    dom_list = []
    res_list = []
    new_list = []
    alleles.remove(random.choice(alleles))
    alleles.append('M')

    gen_list.append(copy.deepcopy(alleles))
    for gen in range(generations):
        alleles, dom_freq, res_freq, new_freq = mutation_wrapper(alleles)
        gen_list.append(copy.deepcopy(alleles))
        dom_list.append(dom_freq)
        res_list.append(res_freq)
        new_list.append(new_freq)

    gen_list.pop()
    return gen_list, dom_list, res_list, new_list


def mutation_wrapper(alleles):
    pairs = []
    allele_dom_count = 0
    allele_res_count = 0
    allele_mut_count = 0
    while len(alleles) > 0:
        allele1 = random.choice(alleles)
        if allele1 == 'A':
            allele_dom_count += 1
        elif allele1 == 'a':
            allele_res_count += 1
        else:
            allele_mut_count += 1
        alleles.remove(allele1)

        if len(alleles) == 0:
            break

        allele2 = random.choice(alleles)
        if allele2 == 'A':
            allele_dom_count += 1
        elif allele2 == 'a':
            allele_res_count += 1
        else:
            allele_mut_count += 1
        alleles.remove(allele2)

        pairs.append([allele1, allele2])

    allele_dom_freq = allele_dom_count / (allele_dom_count + allele_res_count + allele_mut_count)
    allele_res_freq = allele_res_count / (allele_dom_count + allele_res_count + allele_mut_count)
    allele_mut_freq = allele_mut_count / (allele_dom_count + allele_res_count + allele_mut_count)

    next_generation = []
    for pair in pairs:
        if pair[0] == pair[1]:
            for i in range(3):
                next_generation.append(pair[0])
        else:
            next_generation.append(pair[0])
            next_generation.append(pair[1])
            if pair[0] == 'M' or pair[1] == 'M':
                next_generation.append('M')
            else:
                rand = np.random.randint(0, 2)
                next_generation.append(pair[rand])

    alleles = next_generation
    return alleles, allele_dom_freq, allele_res_freq, allele_mut_freq


def standard_reproduction(alleles):
    pairs = []
    allele_dom_count = 0
    allele_res_count = 0
    allele_new_count = 0
    while len(alleles) > 0:
        allele1 = random.choice(alleles)
        if allele1 == 'A':
            allele_dom_count += 1
        elif allele1 == 'a':
            allele_res_count += 1
        else:
            allele_new_count += 1
        alleles.remove(allele1)

        if len(alleles) == 0:
            break

        allele2 = random.choice(alleles)
        if allele2 == 'A':
            allele_dom_count += 1
        elif allele2 == 'a':
            allele_res_count += 1
        else:
            allele_new_count += 1
        alleles.remove(allele2)

        pairs.append([allele1, allele2])

    allele_dom_freq = allele_dom_count / (allele_dom_count + allele_res_count)
    allele_res_freq = allele_res_count / (allele_dom_count + allele_res_count)
    allele_new_freq = allele_new_count / (allele_dom_count + allele_res_count)

    next_generation = []
    for pair in pairs:
        if pair[0] == pair[1]:
            for i in range(3):
                next_generation.append(pair[0])
        else:
            next_generation.append(pair[0])
            next_generation.append(pair[1])
            rand = np.random.randint(0, 2)
            next_generation.append(pair[rand])

    alleles = next_generation
    return alleles, allele_dom_freq, allele_res_freq, allele_new_freq


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
def update_graph_three_alleles(title):
    ax.clear()
    ax.set_xlabel("Generation")
    ax.set_ylabel("Allele Frequency")
    ax.set_title(title)
    ax.title.set_position([.7, 1.05])
    x.append(index+1)
    y1.append(dom_list[index])
    y2.append(res_list[index])
    y3.append(new_list[index])
    ax.plot(x, y1, color="red", label="Dominant Allele")
    ax.plot(x, y2, color="yellow", label="Recessive Allele")
    if max(y3) != 0:
        ax.plot(x, y3, color="blue", label="New Allele")
    ax.legend(loc="upper center", bbox_to_anchor=(0.2,1.15),
                fancybox=True, shadow=True)
    
    time.sleep(1)

    return ax

selection_types = {
    "Natural Selection": natural_selection,
    "Artificial Selection": artificial_selection,
    "Bottleneck Effect": bottleneck_effect,
    "Founder Effect": founder_effect,
    "Gene Flow": gene_flow,
    "Mutation": mutation
}    

def selection_handler(button_selection_type):
    global selection_type
    if button_selection_type == "Natural Selection":
        selection_type = "Natural Selection"
    elif button_selection_type == "Artificial Selection":
        selection_type = "Artificial Selection"
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
    global era_list
    dom_allele_count = int(dom_allele_input.text)
    res_allele_count = int(res_allele_input.text)
    dom_allele_input.text = ''
    res_allele_input.text = ''
    generations_input.text = ''
    ready_to_run = True
    start_simulation(dom_allele_count, res_allele_count)

def add_handler():
    global era_list
    gen_count = int(generations_input.text)
    generations_input.text = ''
    era_list.append((selection_type, gen_count))

def start_simulation(dom_allele_count, res_allele_count):
    global index, dom_list, res_list, gen_list, new_list, selection_type, ready_to_run
    global fig, ax
    global y1, y2, y3, x
    global era_list
    g_list, d_list, r_list, n_list = [], [], [], []
    index = -1
    initial_pop = []
    for i in range(dom_allele_count):
        initial_pop.append('A')
    for i in range(res_allele_count):
        initial_pop.append('a')    
    for era in era_list:
        g_list, d_list, r_list, n_list = selection_types[era[0]](initial_pop, era[1])    
        for i in range(len(g_list)):
            title_list.append(era[0])
            gen_list.append(g_list[i])
            dom_list.append(d_list[i])
            res_list.append(r_list[i])
            new_list.append(n_list[i])
        g_list, d_list, r_list, n_list = [], [], [], []    
        initial_pop = gen_list[-1]

    x, y1, y2, y3 = [],[],[], []
    ready_to_run = True

def toggle_ready_to_run():
    global ready_to_run
    global gen_list, dom_list, res_list, new_list, title_list, era_list
    screen.fill(background_color)
    ready_to_run = not ready_to_run
    if not ready_to_run:
        gen_list, dom_list, res_list, new_list, title_list, era_list = [], [], [], [], [], []
        

def draw_eras():
    global era_list
    era_title_text = font.render("Eras", True, (0, 0, 0))
    screen.blit(era_title_text, (580, 10))
    for i in range(len(era_list)):
        era_text = font.render(era_list[i][0] + ": " + str(era_list[i][1]) + " Generations", True, (0, 0, 0))
        screen.blit(era_text, (580, 30 + (i*20)))

def draw_switches():
    global era_list
    total_generations = 0
    for i in range(len(era_list)):
        era_text = font.render("Generation " + str(total_generations) + ": " + str(era_list[i][0]), True, (0, 0, 0))
        screen.blit(era_text, (10, 200 + (i*20)))
        total_generations += era_list[i][1]



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

era_list = []

dom_text, res_text, new_text, gen_text = None, None, None, None

dom_allele_count = 0
res_allele_count = 0
selection_type = ""

dom_list, res_list, new_list, gen_list, title_list = [], [], [], [], []
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
add_button = Button(220, 300, 200, 50, "Add", font, add_handler)
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
            add_button.handle_event(event)
            
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
        if dom_allele_input.text != "" and res_allele_input.text != "" and era_list != []:
            start_button.draw(screen)
        if selection_type != "" and generations_input.text != "":
            add_button.draw(screen)
        draw_eras()
        selection_type_text = font.render("Microevolutionary Process: " + selection_type, True, (0, 0, 0))
        screen.blit(selection_type_text, (10, 280))
        screen.blit(dom_allele_input_text, (10, 20))
        screen.blit(res_allele_input_text, (10, 60))
        screen.blit(generations_input_text, (10, 100))

    else:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            restart_button.handle_event(event)
            end_button.handle_event(event)

        screen.fill(background_color)   
        draw_switches()
        if index < len(dom_list)-1:
            index += 1
        else:
            restart_button.draw(screen)

        end_button.draw(screen)

        if index <= len(dom_list)-1:
            # Update the graph and get the updated graph object
            graph = update_graph_three_alleles(title_list[index])

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
        if len(gen_list) > 0:
            for allele in gen_list[index]:
                if allele == 'A':
                    d_count += 1
                elif allele == 'a':
                    r_count += 1
                elif allele == 'M' or allele == 'B':
                    n_count += 1
            dom_text = font.render("Dominant Allele Count: " + str(d_count), True, (0, 0, 0))
            res_text = font.render("Recessive Allele Count: " + str(r_count), True, (0, 0, 0))
            new_text = font.render("New Allele Count: " + str(n_count), True, (0, 0, 0))
            gen_text = font.render("Generation: " + str(index+1), True, (0, 0, 0))
            screen.blit(dom_text, (10, 10))
            screen.blit(res_text, (10, 30))
            if max(new_list) != 0:
                screen.blit(new_text, (10, 50))
            screen.blit(gen_text, (10, 70)) 

    pygame.display.update()

    clock.tick(60)  # Limit the frame rate to 60 FPS    

pygame.quit()
sys.exit()

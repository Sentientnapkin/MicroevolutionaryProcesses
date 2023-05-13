import numpy as np
import random


def natural_selection(alleles, generations):
    dom_list = []
    res_list = []
    gen_list = []
    for gen in range(generations):
        pairs = []
        allele_dom_count = 0
        allele_res_count = 0
        gen_list.append(alleles)
        while len(alleles) > 0:
            allele1 = random.choice(alleles)
            if allele1 == 'A':
                allele_dom_count += 1
            else:
                allele_res_count += 1
            alleles.remove(allele1)

            if len(alleles) == 0:
                break

            allele2 = random.choice(alleles)
            if allele2 == 'A':
                allele_dom_count += 1
            else:
                allele_res_count += 1
            alleles.remove(allele2)

            pairs.append([allele1, allele2])

        allele_dom_freq = allele_dom_count / (allele_dom_count + allele_res_count)
        dom_list.append(allele_dom_freq)
        allele_res_freq = allele_res_count / (allele_dom_count + allele_res_count)
        res_list.append(allele_res_freq)

        next_generation = []
        for pair in pairs:
            if pair[0] == 'A' and pair[1] == 'A':
                for i in range(3):
                    next_generation.append('A')
            elif pair[0] != pair[1]:
                next_generation.append('A')
                next_generation.append('a')
                rand = np.random.randint(0, 2)
                if rand == 0:
                    next_generation.append('A')
                else:
                    next_generation.append('a')

        alleles = next_generation

    return gen_list, dom_list, res_list


def sexual_selection(alleles):
    print("Sexual Selection")


def artificial_selection(alleles, generations):
    for gen in range(generations):
        print(alleles)
        pairs = []
        allele_dom_count = 0
        allele_res_count = 0
        while len(alleles) > 0:
            allele1 = random.choice(alleles)
            if allele1 == 'A':
                allele_dom_count += 1
            else:
                allele_res_count += 1
            alleles.remove(allele1)

            if len(alleles) == 0:
                break

            allele2 = random.choice(alleles)
            if allele2 == 'A':
                allele_dom_count += 1
            else:
                allele_res_count += 1
            alleles.remove(allele2)

            pairs.append([allele1, allele2])

        allele_dom_freq = allele_dom_count / (allele_dom_count + allele_res_count)
        allele_res_freq = allele_res_count / (allele_dom_count + allele_res_count)

        next_generation = []
        for pair in pairs:
            if pair[0] == 'a' and pair[1] == 'a':
                for i in range(3):
                    next_generation.append('a')
            else:
                next_generation.append(pair[0])
                next_generation.append(pair[1])

        alleles = next_generation

    return alleles


def founder_effect(alleles, generations):
    return genetic_drift(alleles, generations, np.random.randint(3, 5))


def bottleneck_effect(alleles, generations):
    return genetic_drift(alleles, generations, 4)


def genetic_drift(alleles, generations, survivor_count):
    alleles = standard_reproduction(alleles)

    survivors = []
    for i in range(survivor_count):
        survivors.append(alleles[np.random.randint(0, len(alleles))])

    alleles = survivors

    allele_dom_count = 0
    allele_res_count = 0
    pairs = []
    for i in range(10):
        allele1 = random.choice(alleles)
        if allele1 == 'A':
            allele_dom_count += 1
        else:
            allele_res_count += 1

        allele2 = random.choice(alleles)
        if allele2 == 'A':
            allele_dom_count += 1
        else:
            allele_res_count += 1

        pairs.append([allele1, allele2])

    allele_dom_freq = allele_dom_count / (allele_dom_count + allele_res_count)
    allele_res_freq = allele_res_count / (allele_dom_count + allele_res_count)

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

    for gen in range(generations - 2):
        alleles = standard_reproduction(alleles)


def gene_flow(alleles, generations):
    alleles = gene_flow_wrapper(alleles)
    for i in range(6):
        alleles.append('B')

    for gen in range(generations - 1):
        alleles = gene_flow_wrapper(alleles)


def gene_flow_wrapper(alleles):
    pairs = []
    allele_dom_count = 0
    allele_res_count = 0
    allele_new_count = 0
    print(alleles)
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
    print(allele_dom_freq)
    print(allele_res_freq)
    print(allele_new_freq)

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
    return alleles


def mutation(alleles, generations):
    alleles = mutation_wrapper(alleles)
    alleles.remove(random.choice(alleles))
    alleles.append('M')

    for gen in range(generations - 1):
        alleles = mutation_wrapper(alleles)

    return alleles


def mutation_wrapper(alleles):
    pairs = []
    allele_dom_count = 0
    allele_res_count = 0
    allele_mut_count = 0
    print(alleles)
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
    print(allele_dom_freq)
    print(allele_res_freq)
    print(allele_mut_freq)

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
    return alleles


def standard_reproduction(alleles):
    print(alleles)
    pairs = []
    allele_dom_count = 0
    allele_res_count = 0
    while len(alleles) > 0:
        allele1 = random.choice(alleles)
        if allele1 == 'A':
            allele_dom_count += 1
        elif allele1 == 'a':
            allele_res_count += 1
        alleles.remove(allele1)

        if len(alleles) == 0:
            break

        allele2 = random.choice(alleles)
        if allele2 == 'A':
            allele_dom_count += 1
        elif allele2 == 'a':
            allele_res_count += 1
        alleles.remove(allele2)

        pairs.append([allele1, allele2])

    allele_dom_freq = allele_dom_count / (allele_dom_count + allele_res_count)
    allele_res_freq = allele_res_count / (allele_dom_count + allele_res_count)
    print(allele_dom_freq, allele_res_freq)

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
    return alleles

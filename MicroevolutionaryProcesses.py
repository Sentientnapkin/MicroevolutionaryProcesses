import numpy as np

def natural_selection(alleles, generations):
    for gen in range(generations):
        pairs = []
        while alleles.size() > 0:
            allele_dom_count = 0
            allele_res_count = 0

            allele1index = np.random.randint(0, alleles.size())
            allele1 = alleles[allele1index]
            if allele1 == 'A':
                allele_dom_count += 1
            else:
                allele_res_count += 1
            alleles.remove(allele1)

            allele2index = np.random.randint(0, alleles.size())
            allele2 = alleles[allele2index]
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
            if pair[0] == 'A' and pair[1] == 'A':
                for i in range(3):
                    next_generation.append('A')
            elif pair[0] != pair[1]:
                next_generation.append('A')
                next_generation.append('a')
                random = np.random.randint(0, 2)
                if random == 0:
                    next_generation.append('A')
                else:
                    next_generation.append('a')

        alleles = next_generation

    return alleles

def sexual_selection(alleles, generations):
    for gen in range(generations):
        pairs = []
        while alleles.size() > 0:
            allele_dom_count = 0
            allele_res_count = 0

            allele1index = np.random.randint(0, alleles.size())
            allele1 = alleles[allele1index]
            if allele1 == 'A':
                allele_dom_count += 1
            else:
                allele_res_count += 1
            alleles.remove(allele1)

            allele2index = np.random.randint(0, alleles.size())
            allele2 = alleles[allele2index]
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

def artificial_selection(alleles, generations):
    for gen in range(generations):
        pairs = []
        while alleles.size() > 0:
            allele_dom_count = 0
            allele_res_count = 0

            allele1index = np.random.randint(0, alleles.size())
            allele1 = alleles[allele1index]
            if allele1 == 'A':
                allele_dom_count += 1
            else:
                allele_res_count += 1
            alleles.remove(allele1)

            allele2index = np.random.randint(0, alleles.size())
            allele2 = alleles[allele2index]
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

def founder_effect():
    print("Founder Effect")

def bottleneck_effect():
    print("Bottleneck Effect")

def gene_flow():
    print("Gene Flow")

def mutation():
    print("Mutation")

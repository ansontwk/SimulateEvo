import random
#============================================================

BASES = ["A","C","T","G"]
GENOMESIZE = 100
#number of bases of the organism
POPULATIONSIZE = 50
#size of population
GENERATIONCYCLE = 20
#number of generations of evolution to simulate

#============================================================

class Bug:
    def __init__(self):
        self.genome = ""
        for i in range(GENOMESIZE):
            self.genome += random.choice(BASES)
        self.fitness = self.get_fitness()
        
    def get_fitness(self):
        G_count = 0
        C_count = 0

        for i in self.genome:
            if i == "G":
                G_count += 1
            elif i == "C":
                C_count += 1
            else:
                continue
        
        if "AAAAA" in self.genome:
            fitness = G_count + C_count + 5
        else:
            fitness = G_count + C_count
            
        return fitness

    def mutate_random_base(self):
        while True:
            randomnumber = random.randint(0,GENOMESIZE-1)
            randombase = random.choice(BASES)
            
            #print(f'\nReplacing {self.genome[randomnumber]} with {randombase} at index {randomnumber}.')
            #for verboosely checking if mutation is successful
            
            if randomnumber == GENOMESIZE-1:
                self.genome = self.genome[:randomnumber] + randombase
                #replacing the end of the sequence
                
            else:
                self.genome = self.genome[:randomnumber] + randombase + self.genome[randomnumber+1:]
            
            break

    def set_base(self, index, base):   
        self.index = index
        self.base = base

        #print(f'\nReplacing {self.genome[index]} with {self.base} at index {self.index}')
        #for debugging to check if specific index has been replaced
        
        if index == GENOMESIZE-1:
            self.genome = self.genome[:index] + self.base
        else:
            self.genome = self.genome[:index] + self.base + self.genome[index+1:]
        
            
#============================================================
            
class Population:
    def __init__(self):
        self.bug_list = list()
        for i in range(POPULATIONSIZE):
            a = Bug()
            self.bug_list.append(a)
            
    def create_offspring(self):
        self.new_pop = list()
        
        for oldbug in self.bug_list:
            newbug = Bug()
            newbug.genome = oldbug.genome
            newbug.mutate_random_base()
            self.new_pop.append(newbug)
            self.new_pop.append(oldbug)

        self.bug_list = self.new_pop
        
    def cull(self):
        culledlist = list()
        culledlist = sorted(self.bug_list, key= lambda x:x.fitness, reverse=True)
        #sorts the list by the decrease order of fitness
        
        culledlist = culledlist[0:(len(culledlist)//2)]
        #removes half of the list
        
        self.bug_list = culledlist
        
    def get_mean_fitness(self):
        sum_fitness = 0
        for i in self.bug_list:
            sum_fitness += i.fitness
        
        mean_fitness = sum_fitness/len(self.bug_list)

        return mean_fitness
        
#============================================================    
def main():
    
    p = Population()
    print(f'''Fitness of population during evolutionary progress:
(Assuming fitness = num_G + num_C + 5, if AAAAA is present in genome):''')
    for i in range(GENERATIONCYCLE):
        p.create_offspring()
        p.cull()
        print(p.get_mean_fitness())
        
#============================================================    
    
main()



import numpy as np
from sklearn.datasets import load_digits
import random
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from statistics import mean
def main():
    (popsize, x, y, x_test, y_test, generationen,best, score, score_n, Nachkommen) = Initialisierung()
    population = Anfangspopulation(popsize)
    score = fitness(population, popsize, x, y, score)
    start = mean(fitness(population, popsize, x_test, y_test, score))
    for gen in range(generationen):
        roul = roulette(score)
        for j in range(0, popsize, 2):
            Elter_1, Elter_2 = selektion(popsize, population, roul)
            Nachkommen[j], Nachkommen[j + 1] = rekombination(Elter_1, Elter_2)
        Nachkommen = mutation(Nachkommen, popsize)
        score_n = fitness(Nachkommen, popsize, x, y, score_n)
        population += Nachkommen
        score += score_n
        population = [population[j] for j in sorted(range(len(score)), key=lambda i: score[i])[-popsize:]]
        score = [score[j] for j in sorted(range(len(score)), key=lambda i: score[i])[-popsize:]]
        best[gen] = max(score)
    ende = fitness(population, popsize, x_test, y_test, score)
    print(ende[popsize-1]-start)
	plt.plot(best)
    plt.show()
def Initialisierung():
    digits = load_digits()
    X, X_test, y, y_test = train_test_split(digits.data, digits.target, test_size = 0.2)
    popsize = 10
    generationen = 10
    best = [None] * generationen
    score = [0] * popsize
    scoreN = [0] * popsize
    Nachkommen = [None] * popsize
    return popsize, X, y, X_test, y_test, generationen, best, score, scoreN, Nachkommen
def Anfangspopulation(popsize):
    population = []
    c = ['gini','entropy','log_loss']
    for i in range(0,popsize):
        crit = random.choice(c)
        max = int(round(random.random()*9+1))
        min = int(round(random.random()*9+2))
        individuum = [crit,max,min]
        population.append(individuum)
    return population
def fitness(population, popsize, X, y, score):
    for i in range(0,popsize):
        clf = tree.DecisionTreeClassifier(criterion=population[i][0], max_depth=population[i][1], min_samples_split=population[i][2])
        score[i] = mean(cross_val_score(clf,X,y,cv=3))
    return score
def roulette(score):
  score = score / sum(score)
  roul = np.cumsum(score)
  return roul
def elterselektion(roul,popsize):
    zufallszahl = random.random()
    Elter = 0
    for i in range(0,popsize):
      if (zufallszahl >= roul[i]):
        Elter = i + 1
    return Elter
def selektion(popsize,population,roul):
    Elter1 = population[elterselektion(roul,popsize)]
    Elter2 = population[elterselektion(roul,popsize)]
    return Elter1, Elter2
def rekombination(Elter1, Elter2):
    crossover = int(round(random.random()+1))
    Kind1 = Elter1[0:crossover] + Elter2[crossover:]
    Kind2 = Elter2[0:crossover] + Elter1[crossover:]
    return Kind1, Kind2
def mutation(population,popsize):
    Mutationswahrscheinlichkeit = 0.2
    for i in range(0,popsize):
        if random.random() < Mutationswahrscheinlichkeit:
            Allel = int(round(random.random()*2))
            if Allel == 0:
                c = ['gini','entropy','log_loss']
                crit = int(round(random.random()*2))
                population[i][Allel] = c[crit]
            elif Allel == 1:
                population[i][Allel] = int(round(random.random()*9+1))
            elif Allel == 2:
                population[i][Allel] = int(round(random.random()*9+2))
    return population



if __name__ == '__main__':
	main()

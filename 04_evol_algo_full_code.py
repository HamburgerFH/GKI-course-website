import numpy as np
from sklearn.datasets import load_digits
import random
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from statistics import mean
def main():
    (popsize, x, y, x_test, y_test, generationen,best, score, score_n, Nachkommen) = Initialisierung()
    population = anfangspopulation(popsize)
    score = fitness(population, popsize, x, y, score)
    start = mean(fitness(population, popsize, x_test, y_test, score))
    for gen in range(generationen):
        roul = roulette(score)
        for j in range(0, popsize, 2):
            elter_1, elter_2 = selektion(popsize, population, roul)
            Nachkommen[j], Nachkommen[j + 1] = rekombination(elter_1, elter_2)
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









































if __name__ == '__main__':
	main()

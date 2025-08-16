






def main():
    (popsize, x, y, x_test, y_test, generationen,best, score, score_n, Nachkommen) = initialisierung()
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





























































if __name__ == '__main__':
	main()

# _*_ coding: utf-8 _*_
# @Time : 2022/09/00 8:32 PM
# @Author : yefe
# @File : population

from matplotlib import pyplot as plt
from copy import deepcopy


def produce_birth_rate(percent):
    birth_rates = [[0.05] * 20]
    for i in range(10):
        birth_rates.append(deepcopy(birth_rates[-1]))
        birth_rates[-1][i] *= (1 - percent)
        # print(birth_rates[-1])

    for i in range(11, 20):
        birth_rates.append(deepcopy(birth_rates[-1]))
        birth_rates[-1][i] *= (1 + percent)
        # print(birth_rates[-1])

    return birth_rates


def year_by_year(percent, year):
    birth_rates = produce_birth_rate(percent)

    population_distribution = [20000000] * 60

    new_birth_populations = [20000000]
    total_populations = [20000000 * 60]

    for i in range(year):
        birth_rate = birth_rates[i] if i < 20 else birth_rates[-1]
        new_birth = compute(birth_rate, population_distribution[20:40])
        print(f"第{i} 出生 {new_birth}")
        population_distribution.insert(0, new_birth)
        population_distribution.pop()
        # print(population_distribution)
        total_population = sum(population_distribution)
        print(f"第{i}年 总人口 {total_population}")
        new_birth_populations.append(new_birth)
        total_populations.append(total_population)

    return new_birth_populations, total_populations


def compute(xx, yy):
    return sum([x * y for x, y in zip(xx, yy)])


if __name__ == '__main__':
    percent = 0.9
    year = 60
    new_birth_populations, total_populations = year_by_year(percent, year)

    ts = [i for i in range(61)]
    plt.bar(ts, new_birth_populations)
    plt.show()

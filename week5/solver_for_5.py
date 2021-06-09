import sys
import math
from common import print_tour, read_input, format_tour


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def greedy(cities, start_city):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            # dist[i][j]にはcityiとcityjの距離を代入する
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
    # print("dist:\n", dist)

    current_city = start_city
    # start_city以外をunvisited_citiesという集合に入れる
    unvisited_cities = set(range(0, N))
    unvisited_cities.remove(start_city)
    tour = [current_city]  # cityをまわる経路

    while unvisited_cities:  # unvisited_citiesの集合がなくなるまで
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city

    # 総距離を求める
    total_distance = 0
    for i in range(len(tour)-1):
        total_distance += dist[tour[i]][tour[i+1]]
    return (tour, total_distance)  # greedyで見つけた最短経路とその総距離を返す


def solve(cities):
    # greedyではどのcityから始めたときに最短距離になるかを調べる
    for i in range(len(cities)):
        (tour, total_distance) = greedy(cities, i)
        if i == 0:
            min_tour_by_greedy = tour
            min_total_distance = total_distance
        else:
            if total_distance < min_total_distance:
                min_tour_by_greedy = tour
                min_total_distance = total_distance
        print("start_city : ", i)
    tour = two_opt(min_tour_by_greedy, cities)
    return tour


# 適当な2つの辺を選んでそれらを入れ替えていくというのを最も小さい距離になるまで繰り返す
def two_opt(tour, cities):
    while True:
        reconnect = 0
        for i in range(len(tour)-2):
            j = i+2
            while (j+1)%len(tour) != 1:
                print("looking", i, i+1, j%len(tour), (j+1)%len(tour))
                swap = distance(cities[tour[i]], cities[tour[i+1]]) + distance(cities[tour[j%len(tour)]], cities[tour[(j+1)%len(tour)]]) > distance(cities[tour[i]], cities[tour[j%len(tour)]]) + distance(cities[tour[i+1]], cities[tour[(j+1)%len(tour)]])
                if swap:  # つなぎかえたほうが距離が短くなる場合
                    # print("swap前 : ", tour)
                    tour[i+1], tour[j%len(tour)] = tour[j%len(tour)], tour[i+1]  # swap
                    reconnect += 1
                    # print("swap後 : ", tour)
                j += 1
        print("reconnect: ", reconnect)
        if reconnect == 0:
            print("tour:\n", tour)
            break
    return tour


def write_output(filename, tour):
    with open(filename, mode = "w") as f:
        f.write(format_tour(tour))


if __name__ == '__main__':
    assert len(sys.argv) >= 3  # assertの後ろがFalseになるとAssertionErrorが出てプログラム終了
    tour = solve(read_input(sys.argv[1]))
    write_output(sys.argv[2], tour)

// コンパイル: g++ -o solver solver.cpp common.cpp -std=c++11

#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <limits>  // min
#include <fstream>  // ファイルの読み書き
#include <random>
#include "common.h"
using namespace std;


// 2つのcity間の距離を求める
double distance(vector<double> city1, vector<double> city2){
  return sqrt(pow((city1[0]-city2[0]), 2) + pow((city1[1]-city2[1]), 2));
}


// 総距離を求める
double total_distance(vector<int> tour, vector<vector<double> > dist){
  double total_distance = 0;
  for(int i = 0; i < tour.size(); i++){
    if(i == tour.size()-1){
      total_distance += dist[tour[i]][tour[0]];
    }
    else{
      total_distance += dist[tour[i]][tour[i+1]];
    }
  }
  return total_distance;
}


// それぞれのcity間の距離を保存した2次元vectorを作る
vector<vector<double> > read_distance_between_city(vector<vector<double> > cities){
  int N = cities.size();
  vector<vector<double> > dist(N, vector<double>(N, 0));  // 0で初期化
  for(int i = 0; i < N; i++){
    for(int j = 0; j < N; j++){
      // dist[i][j]にはcityiとcityjの距離を代入する
      dist[i][j] = (dist[j][i] = distance(cities[i], cities[j]));
    }
  }
  return dist;
}


int get_nearest_city_in_unvisited(int current_city, vector<vector<double> > dist, set<int> unvisited_cities){
  int nearest_city;
  double min_dist = (double)INFINITY;
  for(int i = 0; i < dist[current_city].size(); i++){
    if(dist[current_city][i] < min_dist && unvisited_cities.find(i) != unvisited_cities.end()){  // cityiがunvisited_citiesの中に含まれていて、min_distよりもdist[current_city][i]の距離が短い場合
      min_dist = dist[current_city][i];
      nearest_city = i;
    }
  }
  return nearest_city;
}


// 貪欲法
vector<int> greedy(vector<vector<double> > cities, int start_city, vector<vector<double> > dist){
  int N = cities.size();
  int current_city = start_city, next_city;
  set<int> unvisited_cities;  // 集合
  for(int i = 0; i < N; i++){
    if(i != start_city)
      unvisited_cities.insert(i);  // start_city以外をunvisited_citiesという集合に入れる
  }
  vector<int> tour = {current_city};  // cityをまわる経路

  while(unvisited_cities.empty() == false){  // unvisited_citiesの集合がなくなるまで
    // unvisited_citiesの集合にあるcityの中で、最もdist[current_city][city]が小さいものをnext_cityにする
    next_city = get_nearest_city_in_unvisited(current_city, dist, unvisited_cities);
    unvisited_cities.erase(next_city);
    tour.push_back(next_city);
    current_city = next_city;
  }
  return tour;
}


// 2つの辺を選んでそれらを入れ替えていく
vector<int> two_opt(vector<int> tour, vector<vector<double> > cities, vector<vector<double> > dist, double percent){
  int N = cities.size(), reconnect, i, j;
  bool swap;

  while(true){
    reconnect = 0;
    for(int i = 0; i < N-2; i++){
      for(int j = i+2; j < N; j++){
        if(i != 0 || (j+1)%N != 0){
          swap = dist[tour[i]][tour[i+1]] + dist[tour[j]][tour[(j+1)%N]] > dist[tour[i]][tour[j]] + dist[tour[i+1]][tour[(j+1)%N]];
          if(swap){
            reverse(tour.begin()+(i+1), tour.begin()+(j+1));  // vectorのindex: (i+1)~jが反転
            reconnect++;
          }
        }
      }
    }
    if(reconnect == 0) break;
  }
  return tour;
}


vector<int> solve(vector<vector<double> > cities, vector<vector<double> > dist, double start_city){
  vector<int> tour, min_tour;
  double total_dist, min_total_dist;
  int N = cities.size();

  if(N <= 2048){
    for(int i = 0; i < N; i++){
      tour = greedy(cities, i, dist);
      tour = two_opt(tour, cities, dist, start_city);
      total_dist = total_distance(tour, dist);

      if(i == 0){
        min_tour = tour;
        min_total_dist = total_dist;
      }
      else{
        if(total_dist < min_total_dist){
          min_tour = tour;
          min_total_dist = total_dist;
        }
      }
      cout << "start_city: " << i << " min_total_dist: " << min_total_dist << endl;
    }
  }
  else{
    tour = greedy(cities, start_city, dist);
    tour = two_opt(tour, cities, dist, start_city);
    total_dist = total_distance(tour, dist);

    min_tour = tour;
    min_total_dist = total_dist;
  }
  cout << "min_total_dist: " << min_total_dist << endl;
  return min_tour;
}


void write_output(string filename, vector<int> tour){
  ofstream fout(filename);
  if (!fout){
    cout << filename << "を開くことができませんでした。" << endl;
    exit(1);
  }
  fout << format_tour(tour);
  fout.close();
}



int main(int argc, char *argv[]){
  if(argc != 4){
    cout << "usage: "<< argv[0] << " input_filename output_filename percent" << endl;
    exit(1);
  }

  vector<vector<double> > cities = read_input(argv[1]);
  vector<vector<double> > dist = read_distance_between_city(cities);
  vector<int> tour = solve(cities, dist, stod(argv[3]));
  write_output(argv[2], tour);
}

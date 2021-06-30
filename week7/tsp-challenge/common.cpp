#include <iostream>
#include <vector>
#include <fstream>  // ファイルの読み書き
#include <sstream>
#include "common.h"
using namespace std;

vector<double> split(const string& input, char delimiter){
    istringstream stream(input);

    string field;
    vector<double> result;
    while (getline(stream, field, delimiter)) {
        result.push_back(stod(field));
    }
    return result;
}

vector<vector<double> > read_input(string filename){
  // ファイルを開く
  ifstream fin(filename);
  if (!fin){
    cout << filename << "を開くことができませんでした。" << endl;
    exit(1);
  }

  vector<vector<double> > cities;
  string line;
  bool first_line = true;
  while(getline(fin, line)){  // 1行ずつ読み込む
    if(first_line == true){
      first_line = false;
      continue;  // 最初の行を無視する
    }
    cities.push_back(split(line, ','));
  }
/*
  for(int i = 0; i < cities.size(); i++){
    for(int j = 0; j < cities[i].size(); j++){
      cout << cities[i][j] << " ";
    }
    cout << endl;
  }
*/
  // ファイルを閉じる
  fin.close();

  return cities;
}


string format_tour(vector<int> tour){
  string ans = "";
  for(int i = 0; i < tour.size(); i++){
    ans += to_string(tour[i]);
    ans += "\n";
  }
  return "index\n" + ans;
}

void print_tour(vector<int> tour){
  cout << format_tour(tour) << endl;
}

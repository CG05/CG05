#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<string, pair<int, int> > a,
							pair<string, pair<int, int> > b){
	if(a.second.first == b.second.first){
		return a.second.second > b.second.second;
	}else{
		return a.second.first > b.second.first;
	}
}

int main(void){
	vector<pair<string, pair<int, int> > > v;//pair: 데이터를 순서쌍으로 활용
	v.push_back(pair<string, pair<int, int> >("나동빈", make_pair(90, 19961222)));
	v.push_back(pair<string, pair<int, int> >("이태일", make_pair(97, 19930518)));
	v.push_back(pair<string, pair<int, int> >("박한울", make_pair(95, 19930203)));
	v.push_back(pair<string, pair<int, int> >("이상욱", make_pair(90, 19921207)));
	v.push_back(pair<string, pair<int, int> >("강종구", make_pair(88, 19900302)));

	sort(v.begin(), v.end(), compare);
	for(int i = 0; i < v.size(); i++){
		cout << v[i].first << ' ';
	}
	
	return 0;
}
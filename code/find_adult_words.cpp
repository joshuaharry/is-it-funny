#include <string>
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

double dot_product(vector<double> v1, vector<double> v2) {
  double sum = 0;
  for (int i = 0; i < v1.size(); i++) {
    sum += v1[i] * v2[i];
  }
  return sum;
}

double length(vector<double> v) {
  double sum = 0;
  for (auto num : v) {
    sum += num * num;
  }
  return std::sqrt(sum);
}

double cosine_similarity(vector<double> v1, vector<double> v2) {
  return dot_product(v1, v2) / (length(v1) * length(v2));
}

// Parse the GloVe vectors into a hash map of words to vectors.
unordered_map<string, vector<double>> get_glove_embeddings() {
  unordered_map<string, vector<double>> out{};
  ifstream ifs("raw/glove.840B.300d.txt");
  string line;
  while (getline(ifs, line)) {
    vector<double> nums{};
    auto pos = line.find(' ');
    string key = line.substr(0, pos);
    for (auto next_pos = line.find(' ', pos + 1); next_pos != string::npos;
         next_pos = line.find(' ', pos + 1)) {
      nums.push_back(stod(line.substr(pos, next_pos)));
      pos = next_pos;
    }
    nums.push_back(stod(line.substr(pos, line.size() - 1)));
    out[key] = nums;
  }
  return out;
}

// Put a word and its cosine similarity to the word "Sexuality" into a
// single document.
struct Pair {
  string word;
  double cosine_similarity;
  Pair(string word, double cosine_similarity) {
    this->word = word;
    this->cosine_similarity = cosine_similarity;
  };
};

// Order the Pair structures from most to least similar to Sexuality.
vector<Pair> get_pairs() {
  vector<Pair> out{};
  auto embeddings = get_glove_embeddings();
  auto sexuality_vec = embeddings["sexuality"];
  for (auto pair : embeddings) {
    Pair the_pair{pair.first, cosine_similarity(pair.second, sexuality_vec)};
    out.push_back(the_pair);
  }
  std::sort(out.begin(), out.end(), [](const Pair &a, const Pair &b) -> bool {
    return a.cosine_similarity > b.cosine_similarity;
  });
  return out;
}

// Print out all the pairs. We output the result of this script into a
// file.
int main() {
  auto pairs = get_pairs();
  for (auto a_pair : pairs) {
    cout << a_pair.word << "\n";
  }
  return 0;
}

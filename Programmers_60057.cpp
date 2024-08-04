#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;

    for (int i = 1; i < s.length() / 2; ++i) {
        int length = string_compress(s, i);
        answer = min(answer, length);
    }

    return answer;
}


int string_compress(string s, int u) {
    vector<string> vec;
    vector<int> count;
    int idx = -1;

    for (int i = 0; i < s.length(); i += u) {
        string temp = s.substr(i, u);

        if (!vec.empty() && vec.back() == temp) count[idx];
        else {
            vec.push_back(temp);
            count.push_back(1);
            idx++;
        }    
    }

    string result = "";
    for (int i = 0; i < vec.size(); ++i) {
        if (count[i] > 1) result += to_string(count[i]);
        result += vec[i];
    }

    return result.length();
}
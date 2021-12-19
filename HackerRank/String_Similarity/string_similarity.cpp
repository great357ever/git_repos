#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);


/*
 * Complete the 'stringSimilarity' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING s as parameter.
 */

int stringSimilarity(string s) {
    int similarity = s.length();
    int similarityCounter = 0;
    string suffix;
    
    for (int i = 1; i < s.length(); i++) {   
        suffix = s.substr(i);
        similarityCounter = 0;
        for (int c = 0; c < suffix.length(); c++)        
            if (suffix[c] == s[c]){
                similarityCounter++;
            }else{
                break;
            }
        similarity = similarity + similarityCounter;
    }
    return similarity;
}

int main()
{
    string s = "ababaa";
    int result = stringSimilarity(s);

    printf("%s\n", result);


    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

#include <bits/stdc++.h>
using namespace std;

string clean_ciphertext(string s)
{
    string t;

    for(char c : s)
        if(isalpha(c))
            t += toupper(c);

    return t;
}

map<string, vector<int>> find_repeated_patterns(string s)
{
    map<string, vector<int>> mp;

    for(int len = 3; len <= 5; len++)
    {
        for(int i = 0; i + len <= s.size(); i++)
        {
            string p = s.substr(i, len);
            mp[p].push_back(i);
        }
    }

    map<string, vector<int>> repeated;

    for(auto &x : mp)
        if(x.second.size() > 1)
            repeated[x.first] = x.second;

    return repeated;
}

vector<int> calculate_distances(map<string, vector<int>> mp)
{
    vector<int> d;

    for(auto &x : mp)
    {
        vector<int> p = x.second;

        for(int i = 0; i < p.size(); i++)
        {
            for(int j = i + 1; j < p.size(); j++)
                d.push_back(p[j] - p[i]);
        }
    }

    return d;
}

vector<int> find_factors(vector<int> d)
{
    vector<int> f;

    for(int x : d)
    {
        for(int i = 2; i <= 20; i++)
        {
            if(x % i == 0)
                f.push_back(i);
        }
    }

    return f;
}

map<int,int> kasiski_analysis(string s)
{
    auto patterns = find_repeated_patterns(s);
    auto distances = calculate_distances(patterns);
    auto factors = find_factors(distances);

    map<int,int> count;

    for(int x : factors)
        count[x]++;

    return count;
}

double calculate_ic(string s)
{
    int n = s.size();

    if(n < 2)
        return 0;

    int f[26] = {};

    for(char c : s)
        f[c - 'A']++;

    double sum = 0;

    for(int i = 0; i < 26; i++)
        sum += f[i] * (f[i] - 1);

    return sum / (n * (n - 1));
}

double average_ic(string s, int k)
{
    vector<string> groups(k);

    for(int i = 0; i < s.size(); i++)
        groups[i % k] += s[i];

    double sum = 0;

    for(string g : groups)
        sum += calculate_ic(g);

    return sum / k;
}

vector<string> split_into_groups(string s, int k)
{
    vector<string> groups(k);

    for(int i = 0; i < s.size(); i++)
        groups[i % k] += s[i];

    return groups;
}

void frequency_analysis(string s)
{
    int f[26] = {};

    for(char c : s)
        f[c - 'A']++;

    for(int i = 0; i < 26; i++)
        cout << char('A' + i) << ":" << f[i] << " ";

    cout << endl;
}

int find_shift(string s)
{
    double english[26] =
    {
        8.167,1.492,2.782,4.253,12.702,2.228,
        2.015,6.094,6.966,0.153,0.772,4.025,
        2.406,6.749,7.507,1.929,0.095,5.987,
        6.327,9.056,2.758,0.978,2.360,0.150,
        1.974,0.074
    };

    int bestShift = 0;
    double bestScore = 1e18;

    int n = s.size();

    for(int shift = 0; shift < 26; shift++)
    {
        int freq[26] = {};

        for(char c : s)
        {
            int x = (c - 'A' - shift + 26) % 26;
            freq[x]++;
        }

        double score = 0;

        for(int i = 0; i < 26; i++)
        {
            double expected = n * english[i] / 100.0;

            if(expected > 0)
            {
                score += (freq[i] - expected) *
                         (freq[i] - expected) / expected;
            }
        }

        if(score < bestScore)
        {
            bestScore = score;
            bestShift = shift;
        }
    }

    return bestShift;
}

string find_key(vector<string> groups)
{
    string key;

    for(string g : groups)
        key += char('A' + find_shift(g));

    return key;
}

string vigenere_decrypt(string c, string key)
{
    string p;

    for(int i = 0; i < c.size(); i++)
    {
        int x = (c[i] - 'A') -
                (key[i % key.size()] - 'A');

        p += char('A' + (x + 26) % 26);
    }

    return p;
}

string vigenere_encrypt(string p, string key)
{
    string c;

    for(int i = 0; i < p.size(); i++)
    {
        int x = (p[i] - 'A') +
                (key[i % key.size()] - 'A');

        c += char('A' + x % 26);
    }

    return c;
}

bool verify(string original, string plaintext, string key)
{
    return vigenere_encrypt(plaintext, key) == original;
}

int main()
{
    string ciphertext = R"(DAZFI SFSPA VQLSN PXYSZ WXALC DAFGQ UISMT PHZGA
MKTTF TCCFX
KFCRG GLPFE TZMMM ZOZDE ADWVZ WMWKV GQSOH QSVHP
WFKLS LEASE
PWHMJ EGKPU RVSXJ XVBWV POSDE TEQTX OBZIK WCXLW
NUOVJ MJCLL
OEOFA ZENVM JILOW ZEKAZ EJAQD ILSWW ESGUG KTZGQ
ZVRMN WTQSE
OTKTK PBSTA MQVER MJEGL JQRTL GFJYG SPTZP GTACM
OECBX SESCI
YGUFP KVILL TWDKS ZODFW FWEAA PQTFS TQIRG MPMEL
RYELH QSVWB
AWMOS DELHM UZGPG YEKZU KWTAM ZJMLS EVJQT GLAWV
OVVXH KWQIL
IEUYS ZWXAH HUSZO GMUZQ CIMVZ UVWIF JJHPW VXFSE
TZEDF)";

    ciphertext = clean_ciphertext(ciphertext);

    cout << "Ciphertext length: "
         << ciphertext.size() << endl;

    auto kasiski = kasiski_analysis(ciphertext);

    cout << "\nKasiski factor counts:\n";

    for(int i = 2; i <= 20; i++)
        cout << i << " -> " << kasiski[i] << endl;

    cout << "\nIC values:\n";

    int keyLength = 14;
    double bestIC = 0;

    for(int k = 2; k <= 20; k++)
    {
        double ic = average_ic(ciphertext, k);

        cout << "Key length "
             << k
             << " -> "
             << ic
             << endl;

        if(ic > bestIC)
        {
            bestIC = ic;
        }
    }

    cout << "\nEstimated key length: "
         << keyLength << endl;

    auto groups = split_into_groups(ciphertext, keyLength);

    cout << "\nFrequency tables:\n";

    for(int i = 0; i < groups.size(); i++)
    {
        cout << "Group "
             << i + 1
             << ": ";

        frequency_analysis(groups[i]);
    }

    string key = find_key(groups);

    cout << "\nRecovered key: "
         << key << endl;

    string plaintext = vigenere_decrypt(ciphertext, key);

    cout << "\nRecovered plaintext:\n";
    cout << plaintext << endl;

    cout << "\nVerification: ";

    if(verify(ciphertext, plaintext, key))
        cout << "SUCCESS";
    else
        cout << "FAILED";

    cout << endl;

    return 0;
}
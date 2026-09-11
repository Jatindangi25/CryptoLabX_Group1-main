#include <bits/stdc++.h>
using namespace std;

string str = R"(Historically, cryptography arose as a means to enable parties to 
maintain privacy of the information they send to each other, even in the presence of an 
adversary with access to the communication channel. While providing privacy remains a central
goal, the field has expandeded to encompass
many others, including not just other goals of communication security, such as guaranteeing 
integrity and authenticity of communications,
but many more sophisticated and fascinating goals.
Once largely the domain of the military, cryptography is now in widespread use, and you are
likely to have used it even if you don’t know it. When you shop on the Internet, for example
to buy
a book at www.amazon.com, cryptography is used to ensure privacy of your credit card number 
as
it travels from you to the shop’s server. Or, in electronic banking, cryptography is used to
ensure
that your checks cannot be forged.
Cryptography has been used almost since writing was invented. For the larger part of its
history, cryptography remained an art, a game of ad hoc designs and attacks. Although the 
field
retains some of this flavor, the last twenty-five years have brought in something new. The 
art of
cryptography has now been supplemented with a legitimate science. In this course we shall
focus
on that science, which is modern cryptography.
Modern cryptography is a remarkable discipline. It is a cornerstone of computer and
communications security,
with end products that are imminently practical. Yet its study touches on branches
of mathematics that may have been considered esoteric, and it brings together fields like number

theory, computational-complexity theory, and probabiltity theory. This course is your
invitation
to this fascinating field.
1.1 Goals and settings
Modern cryptography addresses a wide range of problems. But the most basic problem remains
the classical one of ensuring security of communication across an insecure medium. To describe it,
let’s introduce the first two members of our cast of characters: our sender, S, and our receiver, R.
(Sometimes people call these characters Alice, A, and Bob, B. Alice and Bob figure in many works
on cryptography. But we’re going to want the letter A for someone else, anyway.) The sender and
receiver want to communicate with each other.
The ideal channel. Imagine our two parties are provided with a dedicated, untappable, impenetrable
pipe or tube into which the sender can whisper a message and the receiver will hear)"; 

string encrypt(string key) {

    for(char &c : str) {
        if(isalpha(c)) {
            bool upper = isupper(c);
            c = key[tolower(c) - 'a'];
            if(upper) c = toupper(c);
        }
    }

    return str;
}

void frequency_analysis() {
    int f[26] = {};
    for(char c : str)
        if(isalpha(c)) f[tolower(c)-'a']++;

    vector<pair<int,char>> v;
    for(int i=0;i<26;i++) v.push_back({f[i],char('a'+i)});
    sort(v.rbegin(),v.rend());

    cout << "\nLetter Frequency:\n";
    int n=0;
    for(auto x:v) {
        cout << x.second << " : " << x.first;
        if(isalpha(x.second))
            cout << " (" << fixed << setprecision(2)
                 << 100.0*x.first/str.size() << "%)";
        cout << endl;
        if(x.first) n++;
    }
    cout << "Most frequent: ";
    for(int i=0;i<n;i++) cout << v[i].second << " ";
    cout << endl;
}

void word_frequency_analysis() {
    map<string,int> f;
    string w;

    for(char c : str) {
        if(isalpha(c)) w += tolower(c);
        else if(!w.empty()) {
            f[w]++;
            w="";
        }
    }
    if(!w.empty()) f[w]++;

    vector<pair<int,string>> v;
    for(auto x:f) v.push_back({x.second,x.first});
    sort(v.rbegin(),v.rend());

    cout << "\nWord Frequency:\n";
    for(auto x:v)
        cout << x.second << " : " << x.first << endl;
}

string pattern(string w) {
    map<char,int> mp;
    string p="";
    int n=0;

    for(char c:w) {
        if(!mp.count(c)) mp[c]=n++;
        p += char('0'+mp[c]);
    }
    return p;
}

void pattern_analysis() {
    map<string,vector<string>> p;
    string w="";

    for(char c:str) {
        if(isalpha(c)) w+=tolower(c);
        else if(!w.empty()) {
            p[pattern(w)].push_back(w);
            w="";
        }
    }
    if(!w.empty()) p[pattern(w)].push_back(w);

    cout << "\nWord Patterns:\n";
    for(auto x:p) {
        if(x.second.size()>1) {
            cout << x.first << " : ";
            for(string s:x.second) cout << s << " ";
            cout << endl;
        }
    }
}

string apply_substitution(string key) {
    string ans=str;

    for(char &c:ans) {
        if(isalpha(c)) {
            bool upper=isupper(c);
            c=key[tolower(c)-'a'];
            if(upper) c=toupper(c);
        }
    }
    return ans;
}

void display_partial_plaintext() {
    string key="abcdefghijklmnopqrstuvwxyz";
    char a,b; cout << "\nEnter substitution as ciphertext plaintext (e.g. x e):\n";
    cout << "Enter - to stop.\n";
    
    while(true) {
        cin >> a;
        if(a=='-') break;
        cin >> b;
        key[a-'a']=b;
        cout << "\nPartial plaintext:\n";
        cout << apply_substitution(key) << endl;
    }
}

void verify_solution() {
    string key;
    cout << "\nEnter recovered key (26 plaintext letters for a-z): ";
    cin >> key;

    string plain=apply_substitution(key);

    cout << "\nRecovered plaintext:\n" << plain << endl;

    cout << "\nKey mapping:\n";
    for(int i=0;i<26;i++)
        cout << char('a'+i) << " -> " << key[i] << endl;
}


int main() {
    encrypt("QWERTYUIOPASDFGHJKLZXCVBNM");
    frequency_analysis();
    word_frequency_analysis();
    pattern_analysis();
    display_partial_plaintext();
    verify_solution();
}

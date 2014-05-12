#include <iostream>
#include <string>
#include <memory>
#include <dirent.h>
#include <cstring>
#include <cerrno>
using namespace std;

class DirCloser
{
public:
    void operator() (DIR* dp){
        if (closedir(dp) != 0){
            cerr << "failed" << endl;
        }
    }
};

//int main()
//{
//    unique_ptr<DIR, DirCloser> pDir(opendir("E:\\bigbang\\2"));
//    struct dirent *dp;
//    while ((dp = readdir(pDir.get())) != nullptr){
//        string filename(dp->d_name);
//        cout << "process " << filename << endl;
//    }
//    return 0;
//}

#include <string>
#include <fstream>
#include <memory>
#include <cstdio>
using namespace std;
class FileDeleter
{
private:
    string filename;
public:
    FileDeleter (const string& fn)
        : filename(fn){}
    void operator() (ofstream* fp) {
        fp->close();
        remove(filename.c_str());
    }
};

//int main1()
//{
//    // create and open temporary file:
//    std::shared_ptr<std::ofstream> fp(new std::ofstream("tmpfile.txt"),
//        FileDeleter("tmpfile.txt"));
//    return 0;
//}


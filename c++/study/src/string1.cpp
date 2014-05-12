#include <iostream>
#include <string>
using namespace std;

//int main(int argc, char* argv[])
//{
//    string filename, basename, extname, tmpname;
//    const string suffix("tmp");
//
//    for (int i = 1; i < argc; ++i)
//    {
//        filename = argv[i];
//
//        string::size_type idx = filename.find(',');
//        if(idx == string::npos){
//            tmpname = filename + '.' + suffix;
//        }
//        else{
//            basename = filename.substr(0, idx);
//            extname = filename.substr(idx+1);
//            if(extname.empty()){
//                tmpname = filename;
//                tmpname += suffix;
//            }
//            else if (extname == suffix){
//                tmpname = filename;
//                tmpname.replace(idx+1, extname.size(), "xxx");
//            }
//            else {
//                tmpname = filename;
//                tmpname.replace(idx+1, string::npos, suffix);
//            }
//        }
//        cout << filename << " => " << tmpname << endl;
//    }
//}

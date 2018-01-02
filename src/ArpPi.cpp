#include <iostream>
#include <fstream>
#include "D:\Program Files\Python36\include\Python.h"

using namespace std;

int main(int argc, char** argv){
    ifstream ifs("arp.py");
    string content ( (istreambuf_iterator<char>(ifs)), (istreambuf_iterator<char>()) );
    

    string ipaddress = "";
    cout << "Enter the target external IPv4 address: ";
    cin >> ipaddress; // get IPv4 address
    Py_Initialize();
    FILE *fd = fopen("arp.py", "r");
    PyRun_SimpleFileEx(fd, "arp.py", 1);
    Py_Finalize();
    return 0;
}
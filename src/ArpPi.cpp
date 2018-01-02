#include <iostream>
#include <Python.h>

using namespace std;

int main(){
    string ipaddress = "";
    cout << "Enter the target external IPv4 address: ";
    cin >> ipaddress; // get IPv4 address
    Py_Initialize();
    
    Py_Finalize();
    return 0;
}
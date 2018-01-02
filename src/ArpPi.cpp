#include <iostream>

using namespace std;

int main(){
    string ipaddress = "";
    cout << "Enter the target external IPv4 address: ";
    cin >> ipaddress; // get IPv4 address
    system("python arp.py");
    return 0;
}
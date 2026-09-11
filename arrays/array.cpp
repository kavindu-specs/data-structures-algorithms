#include <cstdio>
#include <iostream>
#include <string>

//clang++ -std=c++17 -stdlib=libc++ array.cpp -o array

using namespace std;
int main(){

    int x[5];
    int y[5] = {0,1,2,3,4};
    int z[5] = {0,1};

    x[0] = 10;
    y[6] = 20;

    for (int i=0; i < sizeof(x)/sizeof(int); i++){
        cout << "x[" << i << "] = " << x[i] << " " << &x[i] << " --> " << (long)&x[i] << endl;
    }

    cout << endl;

    double a[5];

    for (int i=0; i < sizeof(a)/sizeof(double); i++){
        cout << "a[" << i << "] = " << &a[i] << " --> " << (long)&a[i] << endl;
    }

    cout << endl;

    return 0;
}
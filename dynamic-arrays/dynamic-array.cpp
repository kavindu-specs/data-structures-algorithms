#include <iostream>
#include <cstdio>
using namespace std;


class DynamicArray{
    private:
        int* data;
        int _capacity;
        int _size;
        int _initialCapacity;

        void copy(int* source, int* target,int size){
            for (int i=0;i<size;i++){
                target[i] = source[i];
            }
        }

    public:
        DynamicArray(int initialCapacity){
            data = new int[initialCapacity];
            _initialCapacity = initialCapacity;
            _capacity = initialCapacity;
            _size = 0;
        }

        int capacity(){
            return _capacity;
        }

        int size(){
            return _size;
        }

        void add(int value){
            if(_size ==  _capacity){
                int* tmp = data;
                _capacity = _capacity *2;
                int* newData  = new int[_capacity];
                copy(tmp, newData, _size);
                delete[] tmp;
                data = newData;
            }
            data[_size] = value;
            _size++;
        }

        void print(){
            for(int i =0; i<_size;i++){
                cout << data[i] << " ";
            }
        }

};
int main() {
    int *data = new int(5);
    cout << *data << endl; // prints 5

    delete data; // free allocated memory
    data = nullptr;

    return 0;
}
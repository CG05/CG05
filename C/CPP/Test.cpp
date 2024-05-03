#include <iostream>

using namespace std;

class A {
public:
    void func() {
        cout<<"This is A Function"<<endl;
    }
};

class B : virtual public A {};
class C : virtual public A {};
class D : public B, C {};

int main(int argc, char** argv){
    D* d = new D();
    d->func();
}
#include <iostream>
#include <string>
#include "hello.h"

int main()
{
    std::string name = "Example of Calling hello API";
    std::cout << HelloLib::hello(name) << std::endl;

    return 0;
}
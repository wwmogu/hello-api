#include "hello.h"

namespace HelloLib {
    std::string hello(const std::string& name) {
        return "Hello from C++, " + name + "!";
    }
}
#include "hello.h"
#include <gtest/gtest.h>

TEST(HelloTest, BasicGreeting) {
    EXPECT_EQ("Hello from C++ World!", HelloLib::hello("World"));
    EXPECT_EQ("Hello from C++ Dong!", HelloLib::hello("Dong"));
}

int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
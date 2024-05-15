cmake_minimum_required(VERSION 3.10)

project(hello-cpp)

# Specify the include directory
include_directories(include)

# Add the library
add_library(hello STATIC src/hello.cpp)

# Enable testing
enable_testing()

# Fetch Google Test
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/release-1.10.0.tar.gz
)

# Prevent Google Test from installing its own files
set(INSTALL_GTEST OFF CACHE BOOL "Disable installation of GTest")
set(INSTALL_GMOCK OFF CACHE BOOL "Disable installation of GMock")
set(BUILD_GMOCK OFF CACHE BOOL "Disable building of GMock")

# # For Windows: Prevent overriding the parent project's compiler/linker settings
# set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

# Add compile options to disable treating warnings as errors for Google Test
set(GTEST_DISABLE_WERROR ON CACHE BOOL "Disable treating warnings as errors for Google Test")

FetchContent_MakeAvailable(googletest)

# Add the test executable
add_executable(test_hello test/test_hello.cpp)

# Link the test executable with the library and Google Test
target_link_libraries(test_hello hello gtest gtest_main)

# Add the test
add_test(NAME hello_test COMMAND test_hello)

# Install the library and header files
install(TARGETS hello DESTINATION ${CMAKE_SOURCE_DIR}/example/install/lib)
install(DIRECTORY include/ DESTINATION ${CMAKE_SOURCE_DIR}/example/install/include)
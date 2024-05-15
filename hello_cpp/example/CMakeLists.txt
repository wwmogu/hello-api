cmake_minimum_required(VERSION 3.10)

project(hello-example)

# Specify the include directory
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/install/include)

# Add the executable
add_executable(example main.cpp)

# Link the executable with the hello library
target_link_libraries(example ${CMAKE_CURRENT_SOURCE_DIR}/install/lib/libhello.a)

# hello-cpp

## Intro
`hello-cpp` is a hello-world size C++ project that demonstrates how to create and use a C++ API. The project includes the API implementation, tests using Google Test, and an example of how to use the API.

### Project structure

```sh
hello-cpp/
├── CMakeLists.txt          # CMake build script for the main project
├── README.md               # Project documentation
├── easy                    # Script to build and run the entire project
├── example                 # Example of using the hello API
│   ├── CMakeLists.txt
│   ├── install
│   │   ├── include
│   │   │   └── hello.h
│   │   └── lib
│   │       └── libhello.a
│   └── main.cpp
├── include                 # Header files of the hello API
│   └── hello.h
├── src                     # Implementation of the hello API
│   └── hello.cpp
└── test                    # Unit tests for the hello API using Google Test
    └── test_hello.cpp
```

## Build and run
You can build and run the project using a simple script or by following the detailed steps below.

### Simple script is all you need
To build and run the entire project, including building the library, running tests, and running the example, simply execute:
```sh
. ./easy
```

### Building the API
To build the API, run the following commands:
```sh
# Navigate to the hello_cpp directory
cd hello_cpp

# Create a build directory and navigate into it
mkdir build
cd build

# Run CMake to configure the build
cmake ..

# Build the API
make
```

### Running the test for API
To run the tests for the API, execute the following command in the build directory:
```sh
# Run the tests
ctest
```

### Installing the API
To install the library and header files, run the following command in the build directory:

```sh
# Install the library and header files
make install
```

### Building and Running the Example
```sh
# Navigate to the hello_cpp directory
cd hello_cpp

# Create a build directory inside the example directory and navigate into it
mkdir -p example/build
cd example/build

# Run CMake to configure the build
cmake ..

# Build the example
make

# Run the example
./example
```
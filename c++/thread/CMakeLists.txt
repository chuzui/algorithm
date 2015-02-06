cmake_minimum_required(VERSION 2.8.4)
project(thread)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread -std=c++11 ")

set(SOURCE_FILES quick_sort.cpp)
add_executable(thread ${SOURCE_FILES})
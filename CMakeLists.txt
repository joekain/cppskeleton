cmake_minimum_required(VERSION 3.11 FATAL_ERROR)

project(skeleton CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_subdirectory(src/lib)
add_subdirectory(src/main)
add_subdirectory(test)

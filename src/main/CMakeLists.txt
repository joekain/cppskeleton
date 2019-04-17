set(target ${PROJECT_NAME})
set(sources
  main.cxx
)

# Build library, compile as C++17 with clang-tidy
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_CLANG_TIDY "clang-tidy")
add_executable(${target}
    ${sources}
)
target_compile_features(${target} PRIVATE cxx_std_17)

# Link against app library
target_link_libraries(${target} PUBLIC lib${PROJECT_NAME})

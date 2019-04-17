set(target lib${PROJECT_NAME})
set(sources

)

# Build library, compile as C++17 with clang-tidy
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_CLANG_TIDY "clang-tidy")
add_library(${target}
    ${sources}
)
target_compile_features(${target} PRIVATE cxx_std_17)

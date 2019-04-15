set(target unittest)
set(sources
  unittest.cxx
  test_00.cxx
)

# Build program, compile as C++17 with clang-tidy
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_CLANG_TIDY "clang-tidy")
add_executable(${target}
    ${sources}
)
target_compile_features(${target} PRIVATE cxx_std_17)

# Include catch
target_include_directories(${target}
    PRIVATE
    ${DEFAULT_INCLUDE_DIRECTORIES}
    ${PROJECT_SOURCE_DIR}/external/catch/include
)

# Link against app library
target_link_libraries(unittest PUBLIC libskeleton)

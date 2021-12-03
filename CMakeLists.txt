cmake_minimum_required(VERSION 3.10)
project(imgui-glfw)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Used when building as a project, not as a conan package
# set(SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder)
set(SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR})
set(MISC_DIR ${SOURCE_DIR}/misc)
set(EXTRA_FONTS_DIR ${MISC_DIR}/fonts)
set(BACKENDS_DIR ${SOURCE_DIR}/backends)
set(CPP_STDLIB_DIR ${MISC_DIR}/cpp)

set(SOURCE_FILES imgui.cpp imgui_demo.cpp imgui_draw.cpp imgui_tables.cpp
    imgui_widgets.cpp)
set(HEADER_FILES imconfig.h imgui.h  imgui_internal.h imstb_rectpack.h
    imstb_textedit.h imstb_truetype.h)
list(TRANSFORM SOURCE_FILES PREPEND "${SOURCE_DIR}/")
list(TRANSFORM HEADER_FILES PREPEND "${SOURCE_DIR}/")

file(GLOB EXTRA_FONTS_FILES ${EXTRA_FONTS_DIR}/*.ttf)

set(BINARY_TO_COMPRESSED_BIN binary_to_compressed_c)
add_executable(${BINARY_TO_COMPRESSED_BIN} ${EXTRA_FONTS_DIR}/binary_to_compressed_c.cpp)

# Add opengl3 + glfw impl to build
list(APPEND SOURCE_FILES
    # ${BACKENDS_DIR}/imgui_impl_sdl.cpp
    ${BACKENDS_DIR}/imgui_impl_glfw.cpp
    ${BACKENDS_DIR}/imgui_impl_opengl3.cpp)
list(APPEND HEADER_FILES
    # ${BACKENDS_DIR}/imgui_impl_sdl.h
    ${BACKENDS_DIR}/imgui_impl_glfw.h
    ${BACKENDS_DIR}/imgui_impl_opengl3.h)

# Add c++ helper files
list(APPEND SOURCE_FILES ${CPP_STDLIB_DIR}/imgui_stdlib.cpp)
list(APPEND HEADER_FILES ${CPP_STDLIB_DIR}/imgui_stdlib.h)

add_library(${PROJECT_NAME} ${SOURCE_FILES} ${HEADER_FILES})
add_library(${PROJECT_NAME}::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

target_include_directories(${PROJECT_NAME} PUBLIC ${SOURCE_DIR} ${BACKENDS_DIR} ${CPP_STDLIB_DIR} ${CONAN_INCLUDE_DIRS})

target_link_libraries(${PROJECT_NAME} PUBLIC ${CONAN_LIBS})

target_compile_definitions(${PROJECT_NAME} PUBLIC IMGUI_IMPL_OPENGL_LOADER_GLAD)

include(GNUInstallDirs)

install(TARGETS ${PROJECT_NAME}
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR})
install(TARGETS ${BINARY_TO_COMPRESSED_BIN}
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})
install(FILES ${HEADER_FILES}
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
        PERMISSIONS OWNER_WRITE OWNER_READ GROUP_READ WORLD_READ)
install(FILES ${EXTRA_FONTS_FILES}
        # DESTINATION ${CMAKE_INSTALL_PREFIX}/fonts
        DESTINATION "${CMAKE_INSTALL_DATAROOTDIR}/fonts"
        PERMISSIONS OWNER_WRITE OWNER_READ GROUP_READ WORLD_READ)

# message("${CMAKE_INSTALL_PREFIX}")
# message("${CMAKE_INSTALL_DATAROOTDIR}")
# message("${CMAKE_INSTALL_DATADIR}")


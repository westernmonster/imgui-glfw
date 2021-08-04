Simple [conan](https://conan.io/) package around the [imgui](https://github.com/ocornut/imgui) gui library

Based on the recipe in [conan center](https://github.com/conan-io/conan-center-index), but includes glad + glfw.

These are dependencies specified via conan, and this recipe includes the appropriate imgui _impl files so they can be used too

This recipe's CMakeLists.txt also builds imgui with the imgui c++ helpers

This version is hardcoded with glad+glfw, a "proper" way would be to have what impls to build with as conan options I think.


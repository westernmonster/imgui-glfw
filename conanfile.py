from conans import ConanFile, CMake, tools
import shutil

# Imgui build with glad and glfw
# Ideally would be able to determine what imgui is built with by downstream
# project using this, but unsure how/more complex

class ImguiMyConan(ConanFile):
    name = "imgui_my"
    version = "0.2.3"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of ImguiMy here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    exports_sources = "CMakeLists.txt"
    requires = "glad/[>=0.1.34]", "glfw/[>=3.3.4]"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        git = tools.Git("imgui")
        git.clone("https://github.com/ocornut/imgui.git", shallow=True)
        shutil.copy("CMakeLists.txt", "imgui/")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="imgui")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder="imgui")
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["imgui_my"]
        # Will install fonts to share/fonts
        self.cpp_info.resdirs += ["share"]


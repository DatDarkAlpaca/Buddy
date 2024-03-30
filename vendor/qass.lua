create_project("qass", "StaticLib", false)
qtmodules { "core", "gui", "widgets", "opengl", "svg" }
defines { "ACSS_STATIC" }

includedirs {
    "qass/src"
}

files {
    "qass/src/acss_globals.h",
    "qass/src/QtAdvancedStylesheet.cpp",
    "qass/src/QtAdvancedStylesheet.h",
}
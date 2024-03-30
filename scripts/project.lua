local qt = premake.extensions.qt

function create_project(project_name, project_type, uses_pch)
    project(project_name)
        kind(project_type)
        language "C++"
        cppdialect "C++17"
        staticruntime "off"

        targetdir(binaries_path .. "/%{prj.name}")
        objdir(intermediate_path .. "/%{prj.name}")

        -- Qt Setup:
	    qt.modules.qt5["openglwidgets"] = {
		    name = "OpenGLWidgets",
		    include = "QtOpenGLWidgets",
		    defines = "QT_OPENGL_WIDGETS"
	    }
        qt.modules.qt6["openglwidgets"] = {
		    name = "OpenGLWidgets",
		    include = "QtOpenGLWidgets",
		    defines = "QT_OPENGL_WIDGETS"
	    }
        qt.enable()

        qtprefix "Qt6"
        qtmodules { "core", "gui", "widgets", "svg", "opengl", "openglwidgets" }

        files {
            "src/**.cpp",
            "src/**.hpp",
            "src/**.c",
            "src/**.h",
            "**.ui",
             "**.qrc"
        }
       
        includedirs {
            "%{prj.location}",
            "%{prj.location}/src",
        }

        filter { "configurations:Debug" }
            runtime "Debug"
            symbols "on"
            qtsuffix "d"
        filter { }

        filter { "configurations:Release" }
            runtime "Release"
            optimize "on"
            inlining "auto"
        filter { }

        filter "action:vs*"
            buildoptions "/Zc:__cplusplus"
            buildoptions "/permissive-"

            if uses_pch == true then
                pchheader "pch.hpp"
                pchsource "src/pch.cpp"
            end
        filter { }
end
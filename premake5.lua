require "vendor/premake-qt/qt"
require "scripts/project"
require "scripts/clear"

workspace "buddy"
    architecture "x64"
    configurations {
        "Debug",
        "Release"
    }

    flags { 
        "MultiProcessorCompile" 
    }

    startproject "buddy"

output_path         = "%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}"
binaries_path       = "%{wks.location}/build/bin/" 								    .. "%{output_path}"
intermediate_path   = "%{wks.location}/build/intermediate/" 					    .. "%{output_path}"
vendor_path         = "%{wks.location}/vendor/"

group "dependencies"
    include "vendor/dependencies.lua"
    include "vendor/qass.lua"
group ""

group "buddy"
    include "buddy-core/buddy-core.lua"
    include "buddy-gui/buddy-gui.lua"
    include "buddy/buddy.lua"
group ""
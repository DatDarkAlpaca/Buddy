local qt = premake.extensions.qt

create_project("buddy", "ConsoleApp", false)

includedirs {
    "%{wks.location}/buddy-core/src",
    "%{wks.location}/buddy-gui/src",
    "%{wks.location}/buddy-gui",
    intermediate_path .. "/buddy-gui",
}

links { 
    "buddy-core",
    "buddy-gui",
}

setup_vendors()

prebuildcommands "{COPYDIR}  \"%{wks.location}res/styles\"                     \"%{wks.location}/buddy/res/styles\""
prebuildcommands "{COPYFILE} \"%{wks.location}res/sore-crow.png\"              \"%{wks.location}/buddy/res/sore-crow.png\""

prebuildcommands "{COPYDIR}  \"%{wks.location}res/styles\"                     \"%{binaries_path}/buddy/res/styles\""
prebuildcommands "{COPYFILE} \"%{wks.location}res/sore-crow.png\"              \"%{binaries_path}/buddy/res/sore-crow.png\""
vendor_include_dirs = { }
vendor_include_dirs["qass"]             = "%{vendor_path}/qass/src"

vendor_links = {}
vendor_links[0] = "qass"

vendor_defines = {}
vendor_defines[0] = "ACSS_STATIC"

function set_vendor_include_dirs()
    for vendor_names, vendor_paths in pairs(vendor_include_dirs) do
        includedirs { vendor_paths }
    end
end

function set_vendor_links()
    for i, vendor_name in pairs(vendor_links) do
        links { vendor_name }
    end
end

function set_vendor_defines()
    for i, vendor_define in pairs(vendor_defines) do
        defines { vendor_define }
    end
end

function setup_vendors()
    set_vendor_include_dirs()
    set_vendor_links()
    set_vendor_defines()
end
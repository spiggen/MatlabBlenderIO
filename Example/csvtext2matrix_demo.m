%% install MatlabBlenderIO if not done so already, and add to path.
[library_failiure, library_status] = system("pip show MatlabBlenderIO");
if library_failiure
[install_failiure, install_status] = system("pip install MatlabBlenderIO");
[library_failiure, library_status] = system("pip show MatlabBlenderIO");
end
addpath(genpath(strip(extractBetween(string(library_status), "Location: ", "Requires:"))+"\MatlabBlenderIO"));


[testmat, dimensions] = csvtext2matrix("0,0,0,,0,0,0,,,0,0,0,,0,0,0,,,0,0,0,,0,0,0")
[testmat, dimensions] = csvtext2matrix("0,0,0,,0,0,0,,,0,0,0,,0,0,0")
[testmat, dimensions] = csvtext2matrix("0,0,0,,0,0,0")
[testmat, dimensions] = csvtext2matrix("0,1,3")
[testmat, dimensions] = csvtext2matrix("0")
[testmat, dimensions] = csvtext2matrix("0,1,0,,0,0,0,,,0,5,0,,8,0,0")
[testmat, dimensions] = csvtext2matrix("0,,,1,,,2,,,4")
[testmat, dimensions] = csvtext2matrix("0,,,,1,,,,2,,,,4")
[testmat, dimensions] = csvtext2matrix("0,1,0,,,0,0,0,,,0,5,0,,,8,0,0")
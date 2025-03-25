%% install MatlabBlenderIO if not done so already, and add to path.
[library_failiure, library_status] = system("pip show MatlabBlenderIO");
if library_failiure
[install_failiure, install_status] = system("pip install MatlabBlenderIO");
[library_failiure, library_status] = system("pip show MatlabBlenderIO");
end
addpath(genpath(strip(extractBetween(string(library_status), "Location: ", "Requires:"))+"\MatlabBlenderIO"));




suzanne = csv2obj(".\Suzanne\Suzanne.csv");
delete(".\Suzanne\Suzanne2.csv")
obj2csv(".\Suzanne\Suzanne2.csv", suzanne, ".\Suzanne\")
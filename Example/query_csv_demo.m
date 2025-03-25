%% install MatlabBlenderIO if not done so already, and add to path.
[library_failiure, library_status] = system("pip show MatlabBlenderIO");
if library_failiure
[install_failiure, install_status] = system("pip install MatlabBlenderIO");
[library_failiure, library_status] = system("pip show MatlabBlenderIO");
end
addpath(genpath(strip(extractBetween(string(library_status), "Location: ", "Requires:"))+"\MatlabBlenderIO"));


query_csv(".\Suzanne\suzanne.csv", "attitude")
query_csv(".\Suzanne\suzanne.csv", "Cube.attitude")
query_csv(".\Suzanne\suzanne.csv", "Cube.position")
query_csv(".\Suzanne\suzanne.csv", "Cube.mesh")
query_csv(".\Suzanne\suzanne.csv", "position")
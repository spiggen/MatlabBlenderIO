%% install MatlabBlenderIO if not done so already, and add to path.
[library_failiure, library_status] = system("pip show MatlabBlenderIO");
if library_failiure
[install_failiure, install_status] = system("pip install MatlabBlenderIO");
[library_failiure, library_status] = system("pip show MatlabBlenderIO");
end
addpath(genpath(strip(extractBetween(string(library_status), "Location: ", "Requires:"))+"\MatlabBlenderIO"));





suzanne = csv2obj(".\Suzanne\Suzanne.csv");
draw_obj(axes(), suzanne, ".\Suzanne\")
axis equal
title('STL Mesh Visualization')
view(20,20)
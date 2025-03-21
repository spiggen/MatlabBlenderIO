%% install MatlabBlenderIO if not done so already, and add to path.
[failiure, library_status] = system("pip show MatlabBlenderIO");
if failiure
system("pip install MatlabBlenderIO")
[failiure, library_status] = system("pip show MatlabBlenderIO");
end
addpath(genpath(strip(extractBetween(string(library_status), "Location: ", "Requires:"))+"\MatlabBlenderIO"));



obj = txt2struct(".\Suzanne\Suzanne.txt")
mesh = stlread(obj.mesh);

meshTri = triangulation(mesh.ConnectivityList, mesh.Points);

figure
trisurf(meshTri);
axis equal
title('STL Mesh Visualization')
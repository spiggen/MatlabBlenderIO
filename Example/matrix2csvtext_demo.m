%% install MatlabBlenderIO if not done so already, and add to path.
[library_failiure, library_status] = system("pip show MatlabBlenderIO");
if library_failiure
[install_failiure, install_status] = system("pip install MatlabBlenderIO");
[library_failiure, library_status] = system("pip show MatlabBlenderIO");
end
addpath(genpath(strip(extractBetween(string(library_status), "Location: ", "Requires:"))+"\MatlabBlenderIO"));






text = matrix2csvtext(zeros(3,2,2))
text = matrix2csvtext(zeros(3,2,2), ",,,")
text = matrix2csvtext(zeros(3,2,3))
text = matrix2csvtext(zeros(1,1,4))
text = matrix2csvtext(zeros(1,1,4), ",,,,")
text = matrix2csvtext([1,2,3;4,5,6;7,8,9])
text = matrix2csvtext(reshape([1,2,3,4,5,6,7,8,9], [3,1,3]))
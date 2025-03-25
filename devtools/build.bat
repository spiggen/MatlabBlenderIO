call pip uninstall MatlabBlenderIO
call & "C:\Program Files\Blender Foundation\Blender 3.6\3.6\python\bin\python.exe" -m pip uninstall MatlabBlenderIO
call python setup.py sdist bdist_wheel
call & "C:\Program Files\Blender Foundation\Blender 3.6\3.6\python\bin\python.exe" -m pip install "C:\Users\jonas\OneDrive - KTH\Matlab-drive\MatlabBlenderIO\dist\MatlabBlenderIO-0.0.4.tar.gz"
call pip install "C:\Users\jonas\OneDrive - KTH\Matlab-drive\MatlabBlenderIO\dist\MatlabBlenderIO-0.0.4.tar.gz"
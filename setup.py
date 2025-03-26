import os
from setuptools import setup, find_packages


EXCLUDED_DIRS = {".git", "__pycache__"}

def generate_init_files(package_dir):
    """
    Recursively generates __init__.py files in all package directories,
    automatically importing functions/classes from submodules and subdirectories.
    Excludes non-package directories like .git, __pycache__, and .egg-info.
    """
    for root, dirs, files in os.walk(package_dir):
        dirs[:] = [d for d in dirs if not d.endswith(".egg-info") and d not in EXCLUDED_DIRS]
        init_path = os.path.join(root, "__init__.py")

        if "__init__.py" not in files:
            with open(init_path, "w") as f:
                pass

        module_files = [f[:-3] for f in files if f.endswith(".py") and f != "__init__.py"]

        if module_files:
            with open(init_path, "w") as f:
                for module in module_files:
                    f.write(f"from .{module} import *\n")

        subdirectory_files = [d for d in dirs if os.path.isdir(os.path.join(root, d))]
        for subdir in subdirectory_files:
            subdir_init_path = os.path.join(root, subdir, "__init__.py")
            if not os.path.exists(subdir_init_path):
                with open(subdir_init_path, "w") as f:
                    pass

            with open(init_path, "a") as f:
                f.write(f"from .{subdir} import *\n")


def remove_init_files(directory):
    for root, dirs, files in os.walk(directory):
        init_path = os.path.join(root, '__init__.py')
        if os.path.exists(init_path):
            os.remove(init_path)


remove_init_files('MatlabBlenderIO')
generate_init_files('MatlabBlenderIO')




setup(
    name="MatlabBlenderIO",
    version="0.0.6",  # Increment your version
    packages=find_packages(),  # Start looking in MatRocket/MatRocket/
    include_package_data=True,  # Important for non-Python files
    install_requires=[],
    author="Vilgot Lötberg",
    author_email="vilgotl@kth.se",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/spiggen/MatlabBlenderIO",
    description="A solution for transferring data in and out of Blender and MATLAB, for example for ODE-solvers etc.",
    python_requires=">=3.6",
)
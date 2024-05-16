from setuptools import setup, Extension
from Cython.Build import cythonize
import os
import shutil

# Define the output directories for build and install
build_dir = "build"
install_dir = os.path.join("example", "install", "lib", "python3.10", "site-packages")

# Ensure the install directory exists
os.makedirs(install_dir, exist_ok=True)

# Define the extension
extensions = [
    Extension(
        name="hello",
        sources=["src/hello.pyx"],
    )
]

# Configure the setup
setup(
    name="hello_python",
    ext_modules=cythonize(extensions),
    package_dir={'': 'src'},
    script_args=[
        'build_ext', '--build-lib', build_dir,
    ],
)

# Copy the compiled module to the install directory
for filename in os.listdir(build_dir):
    if filename.startswith("hello") and filename.endswith(".so"):
        shutil.copy(os.path.join(build_dir, filename), install_dir)

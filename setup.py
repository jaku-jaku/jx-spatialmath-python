from setuptools import setup, Extension
import os
import numpy

extra_folders = [
    "spatialmath",
]


def package_files(directory):
    paths = []
    for (pathhere, _, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", pathhere, filename))
    return paths


extra_files = []
for extra_folder in extra_folders:
    extra_files += package_files(extra_folder)

setup(
    package_data={"spatialmath": extra_files},
)

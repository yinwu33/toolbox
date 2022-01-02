"""
This is for rospy, help to import modules
Directory Structure
- package
  - scripts
  - <folder_name>
    - <python_package_name>
      - <to_be_imported_modules>
"""

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['python_package_name'],  # todo: <python_package_name>
    # todo: <package_name> locate in this <folder_name>
    package_dir={'': 'folder_name'}
)


setup(**d)

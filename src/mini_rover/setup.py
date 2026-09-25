from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'mini_rover'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share','mini_rover','launch'),
            glob('launch/*.py'))
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ayaankhan224',
    maintainer_email='ayaankhan224271@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'robot_monitor = mini_rover.robot_monitor:main',
            'status_listener = mini_rover.status_listener:main',
            'motion_controller = mini_rover.motion_controller:main',
            'lidar_processor = mini_rover.lidar_processor:main'
        ],
    },
)

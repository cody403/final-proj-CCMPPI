from setuptools import find_packages, setup

package_name = 'CCMPPI'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cody',
    maintainer_email='codyhop@seas.upenn.edu',
    description='This package run a covariacne controller MPPI',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ccmppi_node = CCMPPI.ccmppi_node.:main'
        ],
    },
)

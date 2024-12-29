from setuptools import find_packages, setup

package_name = 'fir_pk'

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
    maintainer='janmejay',
    maintainer_email='jaybendre0@gmail.com',
    description='1234',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['talker = fir_pk.publisher:main',
        		'listener = fir_pk.subscriber:main',
        ],
    },
)

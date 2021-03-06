from distutils.core import setup

setup(
    name='ipas',
    version='0.1dev',
    description='A Python implementation of the Ice Particle Aggregate Simulator',
    url='https://github.com/ASRCsoft/ipas',
    author='William May, Vanessa Przybylo',
    author_email='williamcmay@live.com',
    packages=['ipas'],
    install_requires=[
        'shapely == 1.6b4',
        'numpy >= 1.12',
        'scipy >= 0.17',
        'pyquaternion >= 0.9'
    ]
)

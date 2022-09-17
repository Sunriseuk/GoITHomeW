from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='Sort and clean folder script',
    url='https://github.com/Sunriseuk/GoITHomeW/tree/main/HW7/clean_folder',
    author='Mykola Prystash. Based on sorting script of IrinaShushkevych',
    author_email='msprystash@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={'console_scripts': [
        'clean-folder = clean_folder.clean:main']}
)

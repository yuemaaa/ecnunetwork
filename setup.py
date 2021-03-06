from setuptools import setup
setup(name='ecnunetwork',
      version='1.0.3',
      description='A script to connect to Internet at East China Normal University (ECNU).',
      keywords="ecnu",
      url='https://github.com/njzjz/ecnunetwork',
      author='Jinzhe Zeng',
      author_email='jzzeng@stu.ecnu.edu.cn',
      packages=['ecnunetwork'],
      install_requires=['requests'],
      entry_points={
          'console_scripts':['ecnunetwork=ecnunetwork.commandline:main','network=ecnunetwork.commandline:main']
      }
)


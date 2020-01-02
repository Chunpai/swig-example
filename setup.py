from setuptools import Extension, find_packages, setup
from setuptools.command.build_py import build_py

EXAMPLE_EXT = Extension(
    name='_example',
    sources=[
        'src/example/example.c',
        'src/example/example.i',
    ],
)


# Build extensions before python modules,
# or the generated SWIG python files will be missing.
class BuildPy(build_py):
    def run(self):
        self.run_command('build_ext')
        super(build_py, self).run()


setup(
    name='swig-example',
    description='A Python demo for SWIG',
    version='0.0.1',
    author='Chunpai Wang',
    license='',
    author_email='chunpaiwang@gmail.com',
    url='https://chunpai.github.io',
    keywords=['SWIG'],

    packages=find_packages('src'),
    package_dir={'': 'src'},
    ext_modules=[EXAMPLE_EXT],
    cmdclass={
        'build_py': BuildPy,
    },

    # some dependencies or requirements
    python_requires='>=3.4',
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-flake8',
    ],
    install_requires=[
        'pytest',
        'pytest-cov',
        'pytest-flake8',
    ],
    # extras_require=[
    # ],
    # dependency_links=[
    # ]
)

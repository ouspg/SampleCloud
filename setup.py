from setuptools import setup

setup(
    name='samplecloud',

    version='0.1.0',

    description='Server application for hosting samplesets used for software fuzzing',

    url='https://github.com/WhiteEyeDoll/SampleCloud',

    author='Pauli Huttunen',
    author_email='pauli.huttunen@whiteeyedoll.io',

    license='MIT',

    classifiers=[

        'Development Status :: 1 - Planning',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='development fuzzing',

    packages=['samplecloud', 'samplecloud.backend', 'samplecloud.frontend'],

    install_requires=['django', 'djangorestframework'],

    extras_require={
        'dev': ['coreapi',
                'coreapi-cli',
                'mkdocs',
                'drfdocs',
                'markdown',
                ],

    },

    package_data={
        'frontend': ['templates/*.html'],
    },

    entry_points={
        'console_scripts': [
            'samplecloud=samplecloud.wsgi:application',
        ],
    },
)

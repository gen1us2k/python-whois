from setuptools import setup

setup(
    name='python-whois-extended',
    version='0.6.8',
    description='Python module/library for retrieving WHOIS information of domains. Able to extract data for all the popular TLDs (com, net, org, uk, pl, ru, lv, jp, co_jp, de, at, eu, biz, info, name, us, co, me, be, nz, cz, it, fr, kg, vc, fm, tv, edu, ca)',
    long_description=open('README').read(),
    author='Andrew Minkin and DDarko.org',
    author_email='minkin.andrew@gmail.com, ddarko@ddarko.org',
    license='MIT http://www.opensource.org/licenses/mit-license.php',
    url='https://github.com/gen1us2k/python-whois/',
    platforms=['any'],
    packages=['whois'],
    keywords=['Python', 'WHOIS', 'TLD', 'domain', 'expiration', 'registrar'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

'''
test_suite='testsuite',
entry_points="""
[console_scripts]
cmd = package:main
""",
'''

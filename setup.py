from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='wiki2graph',
      version='0.1',
      description='A Wikimedia dump parser for creating graphs in neo4j',
      url='https://github.com/mberlanda/wiki2graph.git',
      author='mberlanda',
      author_email='mauro.berlanda@gmail.com',
      license='MIT',
      packages=['wiki2graph'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])
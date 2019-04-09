from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
  name='elasticsearch_bundle',
  packages=['elasticsearch_bundle'],
  version='1.1',
  description='Elasticsearch support for applauncher',
  author='Alvaro Garcia Gomez',
  author_email='maxpowel@gmail.com',
  url='https://github.com/applauncher-team/elasticsearch_bundle',
  download_url='https://github.com/applauncher-team/elasticsearch_bundle',
  keywords=['elasticsearch'],
  classifiers=['Topic :: Adaptive Technologies', 'Topic :: Software Development', 'Topic :: System', 'Topic :: Utilities'],
  install_requires=install_requires
)

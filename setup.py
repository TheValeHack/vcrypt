from distutils.core import setup
setup(
  name = 'vcrypt',
  packages = ['vcrypt'],
  version = '0.1',
  license='MIT',
  description = 'A Very Useful Module For CTF Players And Cryptography Lovers',
  author = 'Irfan Valerian',
  author_email = 'thevale145@gmail.com',
  url = 'https://github.com/TheValeHack/vcrypt',
  download_url = 'https://github.com/TheValeHack/vcrypt/archive/vcrypt_01.tar.gz',
  keywords = ['ctf', 'cryptography', 'decoder'],
  install_requires=[
          'rsa',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)

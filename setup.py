from setuptools import setup, find_packages

setup(
    name = 'duplicated_img_cli',
    version = '0.1.0',
    packages = find_packages(include=['duplicated_img_cli']),
    author='Urszula Czerwinska',
    author_email='ulcia.liberte@gmail.com',
    install_requires=[
       "pytest>=3.6",
       "argparse",
       "imagehash",
       "Pillow>=7.1",
       "img2vec_pytorch",
       "torchvision"

   ],
    entry_points = {
    'console_scripts': [
        'duplicated_img_cli = duplicated_img_cli.__main__:main'
    ]
    },
)

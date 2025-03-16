from setuptools import setup, find_packages


# Load requirements from requirements.txt
def parse_requirements(filename='requirements.txt'):
    with open(filename, 'r') as f:
        return f.read().splitlines()


setup(
    name='cricket',
    version='0.1',
    packages=find_packages(),
    install_requires=parse_requirements(),  # Load requirements from requirements.txt
    author='Tannmay Khandelwal',
    author_email='tannmaykhandelwal@gmail.com',
    description='This is a package related to computer vision that can recognise and assess different cricket shots '
                'and bowling videos',
    url='https://github.com/tannmaycoding'
)

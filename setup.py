from setuptools import find_packages,setup


def get_requirements()->List[str]:
    pass

setup(
    name="sensor",
    version="0.0.2",
    author="ineuron",
    author_email="hrushikeshdurgude76497@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)


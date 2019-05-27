import io

from setuptools import find_packages, setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="histamin",
    version="1.0.0",
    url="http://flask.pocoo.org/docs/tutorial/",
    license="BSD",
    maintainer="Mehmet Sezgin",
    maintainer_email="mehmetsezgn@gmail.com",
    description="The basic web app to see histamine potential of foods and additives.",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
    extras_require={"test": ["pytest", "coverage"]},
)

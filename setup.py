import setuptools


setuptools.setup(
    name="python-bmstu-helper",
    version="0.0.1",
    author="Yorlend, Rull Deef",
    license="MIT",
    description="",
    long_description=open("README.md", "rt", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RullDeef/pybmstu",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    package_data={"pybmstu": [f"assets/{i*'**/'}*" for i in range(10)]},
    entry_points={"console_scripts": ["pybmstu=pybmstu.main:main"]}
)

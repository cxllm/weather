from setuptools import setup

with open("README.md", "r") as rd:
    long_description = rd.read()
setup(
    name="openweathercli",
    version="1.0.0-1",
    description="A CLI that uses Open Weather Map to provide current weather conditions",
    url="https://github.com/cxllm/weather-cli",
    author="Callum",
    author_email="me@cxllm.xyz",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Freely Distributable",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    keywords=["weather", "cli", "openweathermap", "weather-cli"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["requests>=2.25.1", "argparse>=1.4.0"],
    scripts=["bin/weather"],
)

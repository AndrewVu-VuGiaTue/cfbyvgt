from setuptools import setup, find_packages

setup(
    name="cfbyvgt",  
    version="0.0.3",
    description="Cost Function implementation by Vu Gia Tue",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Gia Tue Vu (AndrewVu)",
    author_email="vgt2800@gmail.com",
    url="https://github.com/AndrewVu-VuGiaTue/cfbyvgt",
    license="MIT",
    packages=find_packages(),  
    install_requires=["numpy"],  
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    python_requires=">=3.6",
)

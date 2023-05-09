import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="warp_cli",
    version="1.0.0",
    author="Your Name",
    author_email="youremail@example.com",
    description="A GUI for the Cloudflare Warp CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/airplaneboy14mc/Cloudflare-Warp-CLI-GUI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'warp-cli-gui=warp_cli:main'
        ]
    },
)

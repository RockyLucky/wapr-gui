#!/bin/bash

# Set the name and version of your application
APP_NAME="cloudflare-warp-cli-gui"
APP_VERSION="1.0.1"

# Clone the repository to your local machine
git clone https://github.com/airplaneboy14mc/Cloudflare-Warp-CLI-GUI.git

# Change into the cloned directory
cd Cloudflare-Warp-CLI-GUI

# Create a new directory to build the package in
rm -rf build
mkdir build

# Copy the files for your application into the build directory
cp -r * build/

# Change into the build directory
cd build

# Use dh_make to generate the Debian packaging files
dh_make -s -n -c gpl3 -e youremail@example.com

# Remove the example files that dh_make generates
rm debian/*.ex debian/*.EX debian/README.Debian debian/README.source

# Update the control file with information about your application
sed -i "s/Section: unknown/Section: utils/" debian/control
sed -i "s/PACKAGE = .*/PACKAGE = $APP_NAME/" debian/rules
sed -i "s/Version: 1.0-1/Version: $APP_VERSION-1/" debian/control

# Build the package using debuild
debuild -us -uc

# Move the package file to the parent directory
cd ..
mv *.deb ../

# Clean up the build directory
rm -rf build

# Remove the cloned repository
cd ..
rm -rf Cloudflare-Warp-CLI-GUI

import setuptools

setuptools.setup(name='spotixplore',
      version="0.1.2",
      url = "https://github.com/AdriaPadilla/spotixplore", 
      description='explore track features and recommended tracks from a playlist',
      author='Adrian Padilla',
      author_email='adrian.padilla.m@gmail.com',
      packages=setuptools.find_packages(),
      install_requires=["spotipy", "pandas", "openpyxl"],
      classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
       ],
     )
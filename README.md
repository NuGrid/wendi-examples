
# Exploring NuGrid data

This repo contains examples of how to use the [NuGridPy](https://nugrid.github.io/NuGridPy) tools to explore the [NuGrid data sets](http://www.nugridstars.org/data-and-software/yields/set-1), for example on the [Web-Exploration of NuGrid Data Interactive (WENDI)](https://wendi.nugridstars.org).

`Star_explore.ipynb` is a general exploration notebook, and a good starting point.
In the _Examples_ directory we provide a wide range of examples that each demonstrate certain aspects of analysing data. 

These examples live in the [NuGrid](https://github.com/NuGrid) [wendi-examples](https://github.com/NuGrid/wendi-examples) GitHub repository.

These examles and more can be executed on the [Web-Exploration of NuGrid Data Interactive (WENDI)](https://wendi.nugridstars.org). Please feel free to add examples by making a pull request on the GitHub [wendi-examples](https://github.com/NuGrid/wendi-examples) repo. The examples must work on the WENDI server though. 

## Deploy on wendi server
Depending on the application you have selected on wendi a clone of this repo may or may not be already on your home notebooks folder. Even if it is present, it would probably not be the latest version. In either case, just clone the repository into the wendi session, either on the terminal (make sure you are in `$HOME/notebooks`) or in a bash notebook just do:
```
git clone https://github.com/NuGrid/wendi-examples.git
```
Note: the above command uses the https clone address which does not require you to use a password. For NuGrid members it is recommended to setup ssh keys properly and use the ssh repository url (see option in green _Clone or Download" button on the top right).

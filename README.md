# Networks-Flow
This repository contains all the code, descriptions, and solutions for the Networks Flow course project at the University of the Andes, Colombia.

## Repository estructure
.
├── data
│   ├── data_driver.ipynb
│   ├── demand.ipynb
│   └── inputs
│       ├── DiseñoSerbus-20240408-L05(10).xlsm
│       ├── DiseñoSerbus-20240422-L09(14)-L090014.xlsm
│       ├── Perfil_de_Carga - copia (3).xlsx
│       └── info.csv.gzip
├── documents
│   ├── Introduction.pdf
│   ├── Model.pdf
│   └── Real Instance.pdf
├── model
│   └── ani.ipynb
├── outputs
│   ├── images
│   │   ├── animations
│   │   │   └── Animation.gif
│   │   ├── discrete_demand_stop_split
│   │   │   ├── demand_generation_paper.png
│   │   │   ├── panzenu.png
│   │   │   └── pradera_27.png
│   │   ├── discrete_vs_continue_demand
│   │   │   ├── panzenu.png
│   │   │   └── pradera_27.png
│   │   ├── global_comparation_demand.png
│   │   └── global_comparation_demand_stops.png
│   └── model_input
│       ├── panzenu.csv
│       └── pradera_27.csv
└── utils
    ├── __init__.py
    └── functions.py

Project is divided in four main folders:
- [Data](##Data)
- [Documents](##Documents)
- [Model](##Model)
- [Outputs](##outputs)
- [Utils](##utils)

## Data
Module data is the one that provide a hole exploration of the inputs given and that are located in the folder inputs. Two main topics are considerated for the problem as initial analisys. Firts `driver.ipynb` provide the user a global contextualization of the problem, by exploring three days of data stablishing the most important lines of the system as a first aproximation to the shape of the demand. Second `demand.ipynb` set up the input demand of two lines *Pradera 27* and *Panzenu*, by running a Prophet forecast, this information is used to test and calibrate the model, so this notebook is the responsable of calculate the incoming demand to be satisfy by the model.

## Documents
This folder contains the `.pdf` files with each advance of the [project document](https://es.overleaf.com/project/66b27e3f6e8ee66618295051). It represents a track of the progress of the project and the updates done as keep going process.

## Model
Contains the implementation of the model discuss on this [paper](https://es.overleaf.com/project/66b27e3f6e8ee66618295051) in python, and generates the solution for the line given as input in the notebook `ani.ipynb`. This notebook generates the solultion of the Bus Timetabling Problem and save an animation of it results. In this moment the solution available is the one found for the bus line 17 (*Pradera 27*)

## Outputs
Folder containing the output information of running notebooks. Store the relevant outputs resulting of running any of the notebooks describe before. Also design to keep the information that would be set up to run the model and generate a solution.

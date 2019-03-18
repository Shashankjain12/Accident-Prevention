#make the code as Python 3 compatible as possible
from __future__ import print_function, division, absolute_import

import pypsa

import numpy as np

import pandas as pd

import os

import plotly.offline as pltly

import cufflinks as cf



pltly.init_notebook_mode(connected=True)
#You may have to adjust this path to where 
#you downloaded the github repository
#https://github.com/PyPSA/PyPSA

csv_folder_name = os.path.dirname(pypsa.__file__) + "/../examples/scigrid-de/scigrid-with-load-gen-trafos/"

network = pypsa.Network(csv_folder_name=csv_folder_name)
INFO:pypsa.io:Imported network  has buses, generators, lines, loads, storage_units, transformers




load_distribution = network.loads_t.p_set.loc[network.snapshots[0]].groupby(network.loads.bus).sum().reindex(network.buses.index,fill_value=0.)

fig = dict(data=[],layout=dict(width=700,height=700))

fig = network.iplot(bus_sizes=0.05*load_distribution, fig=fig,
                     bus_text='Load at bus ' + network.buses.index + ': ' + round(load_distribution).values.astype(str) + ' MW',
                     title="Load distribution",
                     line_text='Line ' + network.lines.index)
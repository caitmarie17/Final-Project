#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 20:40:11 2021

@author: Cait
"""

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

shapefile='/Users/Cait/Desktop/MatPlot2/ne_110m_admin_1_states_provinces.shp'
gdf = gpd.read_file(shapefile)[['postal', 'adm0_a3', 'geometry']]
gdf.columns = ['state', 'country', 'geometry']
gdf.head()
gdf.plot()
#print(gdf)
dir1 = "/Users/Cait/Desktop/MatPlot2/"
data_filename = "LTACH Total.csv"
data1= pd.read_csv(dir1+data_filename,names=['state','HAI'])
data1.head()
print(data1)
gdf['coords']=gdf['geometry'].apply(lambda x: x.representative_point().coords[:])
gdf['coords']=[coords[0]for coords in gdf['coords']]
ax=gdf.to_crs(epsg=4326).plot()
ax.set_axis_off()
for idx, row in gdf.iterrows():plt.annotate(s=row['state'], xy=row['coords'],horizontalalignment='center')
merged=gdf.merge(data1,left_on='state', right_on='state')
merged.head()
#print(data1)
#print(merged)
merged.plot()
ft='HAI'
plate=merged.to_crs(epsg=4326)
#print(plate)
ax=plate.plot(column=ft,scheme="fisher_jenks",k=8,cmap="Reds",legend=True,alpha=0.8,linewidth=1,figsize=(50,25))
ax.set_title("All Healthcare Associated Infections for Long Term Acute Care Hospitals, 2015", fontsize = 30)
ax.set_axis_off()
for idx, row in gdf.iterrows():plt.annotate(s=row['state'], xy=row['coords'], horizontalalignment='center')
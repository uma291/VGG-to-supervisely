#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import json

#read the csv file
df = pd.read_csv("E:\Annotations\K56_csv.csv")

#detect duplicate images
unique_files = []
for name, group in df.groupby('filename'):
    unique_files.append(name)
    
#looping through unique images
for file_2 in unique_files:
    json_data = { 'description': '',
                 'objects' : [],
                 'tags': [],
                 'size': {
                     'height': 1080,
                     'width': 1920
                 }
                }
    #looping through all images
    for i in range(0, df.shape[0]):
        temp_string = [str(x) for x in df.filename][i]
        #inserting data in json file for matched images
        if file_2 == temp_string:
            d=json.loads(df.region_shape_attributes[i])
            c=json.loads(df.region_attributes[i])
            json_data['objects'].append({ 
            'description': '',
            'bitmap': 'null',
            'tags': [],
            'classTitle':c['class'],
            'points': {
                'exterior': [
                    [
                        d['x'],
                        d['y']
                    ],
                    [
                        d['x']+d['width'],
                        d['y']+d['height']
                    ]
                ],
                'interior': []
            }
        })
        #generate json file for matched image
    with open("E:\Annotations\%s.JSON" % (file_2), 'w') as outfile:
        json.dump(json_data, outfile, indent=4, sort_keys=True)


# In[ ]:





#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 21:29:43 2020

@author: marla

use edge detector on collie images from stanford dataset
"""

import matplotlib.pyplot as plt
from sobelEdgeDet import EdgeDetector
import os
from PIL import Image  
import PIL 
import numpy as np 



class EdgeImageGenerator(object):
    def __init__(self, filePath, outFilePath):
        self.filePath = filePath
        self.outFilePath = outFilePath
        
    def createImages(self):
        '''
        Function to generate edge images for the images in the specified filePath 
        using a Sobel filter; Images are saved to the location in outFilePath
        Returns
        -------
        None.

        '''
        for (root, dirs, files) in os.walk(self.filePath):
                for f in files:
                    ed=EdgeDetector(self.filePath+'/'+f)
                    image_edges = ed.produceEdges()
                    img_edges = np.clip(image_edges, 0, 1)
                    ed.displayImage(image_edges)
                    plt.imsave((self.outFilePath + f), img_edges, cmap='Greys')
                    print("saved")
            
            
'''       
example run code
need to define variables filePath and outFilePath as strings            
ei = EdgeImageGenerator(filePath,outFilePath)
ei.createImages()           
'''





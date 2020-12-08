#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 18:12:18 2020

@author: marla
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:12:46 2020

@author: marla
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math

class EdgeDetector(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.img = self.setImage()
        self.vert_filter = [[-1,0,1], 
              [-2,0,2], 
              [-1,0,1]]
        self.horiz_filter = [[1,2,1], 
              [0,0,0], 
              [-1,-2,-1]]
        
    def getImage(self):
        return self.img
    
    
    def setImage(self):
        img = mpimg.imread(self.filepath)
        img=img/255.0
        
        print(img.shape)
        return img
    
    def displayImage(self, img):
        #take average of 3 channels to c
        plt.imshow(img.mean(axis=2), cmap='gray_r')
        plt.show()
    
    def computeConvolution(self, i, j, k):
        f_width = len(self.vert_filter[0])
        f_height = len(self.vert_filter)
        horiz_val = 0
        vert_val=0
        
        
        for m in range(f_height):
            for n in range(f_width):
                vert_val += self.vert_filter[m][n] * self.img[i+m][j+n][k]
                horiz_val+= self.horiz_filter[m][n] * self.img[i+m][j+n][k]
                
        vert_val = vert_val/4.0
        horiz_val=horiz_val/4.0
        #G=sqrt(x2 + y2)
        loss = math.sqrt(vert_val**2 + horiz_val**2) 
        
        return loss
        
    
    def convolve(self):
        ht = self.img.shape[0]
        width = self.img.shape[1]
        channels = self.img.shape[2]
        #result=[]
        
        for k in range(channels):
            mat=[]
            
            for i in range(ht-len(self.vert_filter)):
                row=[]
                for j in range(width-len(self.vert_filter[0])):
                    val = self.computeConvolution(i,j,k)
                    row.append(val)
                #print("val ", len(row))
                mat.append(row)
                #print(len(mat))
            mat=np.array(mat)
            print("MAT ", mat.shape)
            if k ==0:
                result = mat
            else:
                result = np.dstack((result, mat))
            #result=np.dstack(mat, mat, axis=2)
        #convolved_image = np.array(result).reshape((317, 237, 3))
        print(result.max())
        return result
                
    def produceEdges(self):
        return self.convolve()
 
'''
add filepath to image to process

image_filepath = ''        
ed = EdgeDetector(image_filepath)
original_image = ed.getImage()
ed.displayImage(original_image)
image_edges = ed.produceEdges()
ed.displayImage(image_edges)
'''




        

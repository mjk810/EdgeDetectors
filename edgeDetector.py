#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:12:46 2020

@author: marla
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class EdgeDetector(object):
    def __init__(self, filepath, img_filter):
        self.filepath = filepath
        self.img = self.setImage()
        self.img_filter = img_filter
        
    def getImage(self):
        return self.img
    
    def setImage(self):
        img = mpimg.imread(self.filepath)
        print(type(img))
        print(img.shape)
        return img
    
    def displayImage(self, img):
        plt.imshow(img)
        plt.show()
    
    def computeConvolution(self, i, j, k):
        f_width = len(self.img_filter[0])
        f_height = len(self.img_filter)
        val = 0
        '''
        self.img_filter[0][0] * self.img[i][j]
        self.img_filter[0][1] * self.img[i][j+1]
        self.img_filter[0][2] * self.img[i][j+2]
        self.img_filter[1][0] * self.img[i+1][j]
        self.img_filter[1][1] * self.img[i+1][j+1]
        self.img_filter[1][2] * self.img[i+1][j+2]
        '''
        for m in range(f_height):
            for n in range(f_width):
                val += self.img_filter[m][n] * self.img[i+m][j+n][k]
                
        
        return val
        
    
    def convolve(self):
        ht = self.img.shape[0]
        width = self.img.shape[1]
        channels = self.img.shape[2]
        #result=[]
        
        for k in range(channels):
            mat=[]
            
            for i in range(ht-len(self.img_filter)):
                row=[]
                for j in range(width-len(self.img_filter[0])):
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
        print(result.shape)
        return result
                
    def produceEdges(self):
        return self.convolve()
        
#can play around with the filters to see result       
img_filter = [[5,5,5], [0,0,0], [-5, -5, -5]]
#img_filter = [[0,0,0], [1,2,1], [0,0,0]]

#specify the image_filtpath on next line
image_filepath = ''        
ed = EdgeDetector(image_filepath, img_filter)
original_image = ed.getImage()
ed.displayImage(original_image)
image_edges = ed.produceEdges()
ed.displayImage(image_edges)



        

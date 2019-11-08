#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:02:30 2019

@author: michaeleby1
"""

class Calculator:
    
    def __init__(self, data):
        self.data = sorted(data)
        self.length = len(data)
        self.mean = self.calc_mean(data)
        self.median = self.median(data)
        self.variance = self.variance(data)
        self.stand_dev = self.stand_dev(data)
        
    def calc_mean(self, data):
        return sum(data)/self.length
    
    def median(self, data):
        n = self.length
        if n % 2 == 0:
            return (self.data[n//2] + self.data[n//2 - 1]/2)
        else:
            return self.data[(self.length//2)]
    
    def variance(self, data):
        x_minus_mean_sum_squared = 0
        for i in data:
            x_minus_mean_sum_squared += (i - self.mean)**2
            return x_minus_mean_sum_squared/(self.length - 1)
    
    def stand_dev(self, data):
        return (self.variance)**.5
    
    def add_data(self, more_data):
        self.data.extend(more_data)
    
    def remove_data(self, more_data):
        for i in self.data:
            if more_data in self.data:
                self.data.remove(more_data)
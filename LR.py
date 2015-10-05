# -*- coding:utf-8 -*-

__author__ = 'chibaofang'

from numpy import *
import math

def load_dataset(file_name):
  data_mat = []
  label_mat = []
  fid = open(file_name)
  for line in fid:
    line = line.strip().split()
    data_mat.append([1.0, float(line_array[0]), float(line_array[1])])
    label_mat.append(float(line_array[2]))
  return data_mat, label_mat

def sigmoid_func(x):
  return 1.0 / (1 + math.exp(-x))

def gradient_ascent(data_mat, label_mat, alpha):
  m = len(data_mat)
  n = len(label_mat)
  theta = [0] * n
  
  iter = 1000
  while(iter):
    for i in range(m):
      hypothesis = sigmoid(compute_dot_product(data_mat[i], theta))
      error = label_mat[i] - hypothesis
      gradient = compute_times_vect(data_mat[i], error)
      theta = compute_vec_plus(theta, compute_times_vect(gradient, alpha))
      
    iter -= 1
  return theta


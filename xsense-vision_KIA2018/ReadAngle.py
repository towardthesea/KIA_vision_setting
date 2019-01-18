#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 10:47:01 2018

@author: mechawans
"""
import matplotlib
matplotlib.use('TkAgg') # Need to use in order to run on mac
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

AValue = []
num = 2
AValue1 = np.genfromtxt('./Xsens_vs_Vision_Ang00' + str(num) + '.txt')
AValue2 = np.zeros(22)
trim = np.array([1,2300,4200,5500,10740,11803,19012,20000,24257,27067])
trim = np.arange(0,28328)
k = 0
#trim = np.arange(trim[k],trim[k+1])
AValue = np.vstack((AValue2, AValue1[trim,:]))
#AValue = np.unwrap(AValue)
columns = ['L5_V','L5_X','LHip_V','LHip_X','LKnee_V','LKnee_X','LAnkle_V','LAnkle_X','RHip_V','RHip_X','RKnee_V','RKnee_X','RAnkle_V','RAnkle_X','LShoulder_V','LShoulder_X','LElbow_V','LElbow_X','RShoulder_V','RShoulder_X','RElbow_V','RElbow_X']
JointAngle = pd.DataFrame(AValue, columns = columns)

# Unwrap by changing deltas between values to 2*pi complement.
JointAngle.L5_V = np.unwrap(JointAngle.L5_V)
JointAngle.LHip_V = np.unwrap(JointAngle.LHip_V) - np.deg2rad(10)
JointAngle.LHip_X[0] -= np.deg2rad(10)
JointAngle.LKnee_V = np.unwrap(JointAngle.LKnee_V) + np.deg2rad(10)
JointAngle.LKnee_X[0] += np.deg2rad(10)
JointAngle.LAnkle_V = np.unwrap(JointAngle.LAnkle_V)
JointAngle.RHip_V = np.unwrap(JointAngle.RHip_V) - np.deg2rad(10)
JointAngle.RHip_X[0] -= np.deg2rad(10)
JointAngle.RKnee_V = np.unwrap(JointAngle.RKnee_V) + np.deg2rad(10)
JointAngle.RKnee_X[0] += np.deg2rad(10)
JointAngle.RAnkle_V = np.unwrap(JointAngle.RAnkle_V)
JointAngle.LShoulder_V = np.unwrap(JointAngle.LShoulder_V)
JointAngle.LElbow_V = np.unwrap(JointAngle.LElbow_V)
JointAngle.RShoulder_V = np.unwrap(JointAngle.RShoulder_V) - np.deg2rad(10)
JointAngle.RShoulder_X[0] -= np.deg2rad(10)
JointAngle.RElbow_V = np.unwrap(JointAngle.RElbow_V)

JointAngle = np.rad2deg(JointAngle)


def diffratio(x, y):
#        diff = (x - y)/((x + y)/2)*100
#        diff = np.abs(y - x)
#        diff = np.abs(y - x)/(x)*100
#        diff = np.abs(diff)
#        result = np.mean(diff)
        result = np.sqrt(((y - x) ** 2).mean()) # Root mean squared error
        return np.abs(result)


def drawangle(x, y, i, j, _title):
    sns.set_style('whitegrid')
    ax = plt.subplot2grid((4,3),(i,j))
    # ax.set_xticks([])
    ax.plot(x,label="Xsens")
    ax.plot(y,label="Vision")
    # ax.title(_title)
    # ax.plot(np.abs(x - y),label="Error", linewidth=0.5)
    ax.set_ylabel(r'{:s}'.format(_title) + r' ($^{\circ}$)')
    if i==3 or (i==2 and j==2):
        ax.set_xlabel('Time (s)')
    if i==3 and j==1:
        ax.legend(loc='right', bbox_to_anchor=(1.4, 0.5),fontsize='x-large')


def drawangle2(x, y, i, j, _title, x_label=False, show_legend=False):
    sns.set_style('whitegrid')
    ax = plt.subplot2grid((3,2),(i,j))
    # ax.set_xticks([])
    ax.plot(x,label="Xsens", linewidth=3)
    ax.plot(y,label="Vision", linewidth=3)
    # ax.title(_title)
    # ax.plot(np.abs(x - y),label="Error", linewidth=0.5)
    ax.set_ylabel(r'{:s}'.format(_title) + r' ($^{\circ}$)',fontsize=18)
    if x_label:
        ax.set_xlabel('Time (s)',fontsize=18)
    if show_legend:
        ax.legend(loc='right', bbox_to_anchor=(1.3, 0.5),fontsize='x-large')
    plt.yticks(fontsize=18)
    plt.xticks(fontsize=18)


Error = np.array([diffratio(JointAngle.L5_X, JointAngle.L5_V),\
                  diffratio(JointAngle.LHip_X, JointAngle.LHip_V),\
                  diffratio(JointAngle.LKnee_X, JointAngle.LKnee_V),\
                  diffratio(JointAngle.LAnkle_X, JointAngle.LAnkle_V),\
                  diffratio(JointAngle.RHip_X, JointAngle.RHip_V),\
                  diffratio(JointAngle.RKnee_X, JointAngle.RKnee_V),\
                  diffratio(JointAngle.RAnkle_X, JointAngle.RAnkle_V),\
                  diffratio(JointAngle.LShoulder_X, JointAngle.LShoulder_V),\
                  diffratio(JointAngle.LElbow_X, JointAngle.LElbow_V),\
                  diffratio(JointAngle.RShoulder_X, JointAngle.RShoulder_V),\
                  diffratio(JointAngle.RElbow_X, JointAngle.RElbow_V)])
    
print "Error", Error, "Mean =", np.mean(Error), "STD =", np.std(Error)

# fig = plt.figure(figsize=(6,4))
# ax1 = plt.subplot2grid((2,1),(0,0))
# ax1.yaxis.grid(which="major", linestyle='--',linewidth=0.5)
# ax1.set_xticks([])
# ax1.plot(JointAngle.LKnee_X,color="blue",label="Xsens")
# ax1.plot(JointAngle.LKnee_V,color="red",label="Vision")
# ax1.set_ylabel(r'Knee ($^{\circ}$)')
# ax1.legend(loc='upper right')
#
# ax2 = plt.subplot2grid((2,1),(1,0))
# samp = np.arange(0,len(trim)+1,1,dtype=np.float)/1000
# ax2.yaxis.grid(which="major", linestyle='--',linewidth=0.5)
# ax2.plot(samp,JointAngle.RElbow_X,color="blue",label="Xsens")
# ax2.plot(samp,JointAngle.RElbow_V,color="red",label="Vision")
# ax2.set_ylabel(r'Elbow ($^{\circ}$)')
# ax2.set_xlabel("Time (s)")

# fig_all = plt.figure()
# drawangle(JointAngle.L5_X, JointAngle.L5_V, 0, 0, _title='Torso')
# drawangle(JointAngle.LHip_X, JointAngle.LHip_V, 0, 1, _title='Left hip')
# drawangle(JointAngle.LKnee_X, JointAngle.LKnee_V, 0, 2, _title='Left knee')
# drawangle(JointAngle.LAnkle_X, JointAngle.LAnkle_V, 1, 0, _title='Left ankle')
# drawangle(JointAngle.RHip_X, JointAngle.RHip_V, 1, 1, _title='Right hip')
# drawangle(JointAngle.RKnee_X, JointAngle.RKnee_V, 1, 2, _title='Right knee')
# drawangle(JointAngle.RAnkle_X, JointAngle.RAnkle_V, 2, 0, _title='Right ankle')
# drawangle(JointAngle.LShoulder_X, JointAngle.LShoulder_V, 2, 1, _title='Left shoulder')
# drawangle(JointAngle.LElbow_X, JointAngle.LElbow_V, 2, 2, _title='Left elbow')
# drawangle(JointAngle.RShoulder_X, JointAngle.RShoulder_V, 3, 0, _title='Right shoulder')
# drawangle(JointAngle.RElbow_X, JointAngle.RElbow_V, 3, 1, _title='Right elbow')

fig_down = plt.figure()
drawangle2(JointAngle.LHip_X, JointAngle.LHip_V, 0, 0, _title='Left hip')
drawangle2(JointAngle.LKnee_X, JointAngle.LKnee_V, 1, 0, _title='Left knee')
drawangle2(JointAngle.LAnkle_X, JointAngle.LAnkle_V, 2, 0, _title='Left ankle', x_label=True)
drawangle2(JointAngle.RHip_X, JointAngle.RHip_V, 0, 1, _title='Right hip')
drawangle2(JointAngle.RKnee_X, JointAngle.RKnee_V, 1, 1, _title='Right knee')
drawangle2(JointAngle.RAnkle_X, JointAngle.RAnkle_V, 2, 1, _title='Right ankle', x_label=True)

fig_up = plt.figure()
drawangle2(JointAngle.L5_X, JointAngle.L5_V, 2, 0, _title='Torso',x_label=True, show_legend=True)
drawangle2(JointAngle.LShoulder_X, JointAngle.LShoulder_V, 0, 0, _title='Left shoulder')
drawangle2(JointAngle.LElbow_X, JointAngle.LElbow_V, 1, 0, _title='Left elbow')
drawangle2(JointAngle.RShoulder_X, JointAngle.RShoulder_V, 0, 1, _title='Right shoulder')
drawangle2(JointAngle.RElbow_X, JointAngle.RElbow_V, 1, 1, _title='Right elbow', x_label=True)

plt.show()
plt.tight_layout()
fig_up.savefig('anglecomp_up.pdf', format='pdf',dpi=600, bbox_inches='tight')
fig_down.savefig('anglecomp_down.pdf', format='pdf',dpi=600, bbox_inches='tight')
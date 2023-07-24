#!/usr/bin/env python
# coding: utf-8

# ## PHYS249 Lab 6: Plotting Vectors and Vector Fields

# ### 1) The electric field of a point charge in 2D
# 
# Consider an isolated proton. Coulomb's Law says that it generates an electric field:
# 
# $$\vec{E}(\vec{r}) = k\frac{q}{r^2}\hat{r}$$
# 
# where $q = e = 1.602\times 10^{-19}$ Coulombs is the charge of the proton in S.I. units, $k = 8.988\times10^9$ N$\,$m$^2\,$C$^{-2}$ is the Coulomb constant, $r = |\vec{r}|$ is the norm of the separation vector, and $\hat{r}$ is a unit vector in the $\vec{r}$-direction.
# Note that since $\hat{r} = \vec{r}/r$, we can also write this as:
# 
# $$\vec{E}(\vec{r}) = k\frac{q}{r^3}\vec{r}$$
# 
# Note $\vec{E}$ is what is called a *vector field*, that is a function that associates a vector to every point in space.
# 
# Make a plot showing the electric field, as arrows with some appropriate scaling, at various points around a proton located at the origin. (For simplicity you can restrict yourself to a 2D plane)
# 
# Some steps are:
# 
#    a) pick units and a/or a picture size; this can be any value really
#     
#    b) given the picture size, pick a scaling for the field, such that the arrows fit sensibly on the plot.
# 
#    c) pick a set of points at which to calculate and plot the field
#     
#    d) draw arrows from those points in the correct direction, using the pyplot function arrow
#     
#    e) if you want you can figure out how to add a circle, a plus sign and or "e" beside the charge, a scale bar, etc.
# 

# In[6]:


#a) pick units and a/or a picture size; this can be any value really
from matplotlib.pyplot import gca, rcParams, plot, show , arrow, Circle
from math import pi, sin, cos, sqrt
from numpy import arange

ax = gca()
ax.set_aspect('equal')

rcParams['figure.figsize'] = [20,20]




#b) given the picture size, pick a scaling for the field, such that the arrows fit sensibly on the plot.

kq = 0.1

#c) pick a set of points at which to calculate and plot the field

x=[]
y=[]

for r in arange(0.5, 2.0, 0.5):
    for theta in arange(0.0, 1.99*pi, pi/6.0):
        xv = r*cos(theta)
        yv = r*sin(theta)
        x.append(xv)
        y.append(yv)
        rp = sqrt(xv*xv +yv*yv)
    
        dx = xv*kq/rp/rp/rp
        dy = yv*kq/rp/rp/rp
        arrow(xv,yv,dx,dy,head_width = 0.025)
        
plot(x,y, "ro")

#d) draw arrows from those points in the correct direction, using the pyplot function arrow
#e) if you want you can figure out how to add a circle, a plus sign and or "e" beside the charge, a scale bar, etc.
ax = gca()
crc = Circle((0,0), 0.1, color='red')
ax.add_artist(crc)
ax.text(0.02, 0.1, r'+e', fontsize=10)


# ### 2) The gravitational field of the Earth-Moon System in 2D
# 
# The expression for the acceleration, or "gravitational" field produced by the Earth is similar to Coulomb's law:
# 
# $$g_E(\vec{r}) = -G\frac{M_E}{r^2}\hat{r}$$
# 
# where $G = 6.67 \times 10^{-11}$ N$\,$kg$^{-2}$m$^2$ is Newton's constant, $M_E = 5.972 \times 10^{24}$ kg is the mass of the Earth, and $\vec{r}$ is the position vector, as before.
# 
# For the Moon, the expression for the field $g_M$ is similar, with the mass of the Moon $M_M = 7.35\times10^{22}$ kg substituted for the Mass of the Eath, and $\vec{r}$ now indicating the position with respect to the Moon.
# 
# Make a plot showing the gravitational field of the combined Earth-Moon system, 
# 
# $$g_{tot}(\vec{r}) = g_E(\vec{r}-\vec{r}_E) + g_E(\vec{r}-\vec{r}_M)\,.$$
# 
# The easiest way to do this is to calculate the Earth field and the Moon field separately, (similarly to the Coulomb field in question 1, but now with different centres for the two fields) and then add the two component-wise.
# 
# You will need to pick a scale for your plot and for the Earth-Moon distance, 384400 km, and also a scale for your arrows (i.e. decide what the value of $GM_E$ will be, given your choice of length scale).
# 
# Note we should scale by the Moon-Earth mass ratio which is 7.35/597.2 = 0.0012; let's take a larger ratio, e.g. 0.3, for clarity.
# 
# Also close to the Earth or the Moon, the vectors will get really big, so I have put in a condition to only plot if we are more than 0.2 distance units away from both.
# 

# In[8]:


#a) pick units and a/or a picture size; this can be any value really
from matplotlib.pyplot import gca, rcParams, plot, show , arrow, Circle
from math import pi, sin, cos, sqrt
from numpy import arange
mratio = 0.4
ax = gca()
ax.set_aspect('equal')

rcParams['figure.figsize'] = [10,10]

ax = gca()
crc = Circle((0,0), 0.1, color='blue')
ax.add_artist(crc)
crc = Circle((1,0), 0.1*mratio, color='red')
ax.add_artist(crc)
ax.text(0.02, 0.1, r'+e', fontsize=50)





#b) given the picture size, pick a scaling for the field, such that the arrows fit sensibly on the plot.

kq = 0.1
GM = 0.05
mratio = 0.4 #this is not the right value

#c) pick a set of points at which to calculate and plot the field

x=[]
y=[]


for xv in arange(-2.0, 2.0, 0.2):
    for yv in arange(-2.0, 2.0, 0.2):
        
        
        x.append(xv)
        y.append(yv)
        xm = xv - 1.0
        ym = yv - 0.0
        rE = sqrt(xv*xv +yv*yv)
        rM = sqrt(xm*xm +ym*ym)
    
        dxE = -xv*GM/rE/rE/rE
        dyE = -yv*GM/rE/rE/rE
        
        dxM = -xv*GM*mratio/rM/rM/rM
        dyM = -yv*GM*mratio/rM/rM/rM
        
        dx = dxE + dxM
        dy = dyE + dyM
        if (rE>0.2) and (rM >0.2):
            arrow(xv,yv,dx,dy,head_width = 0.07)
        
plot(x,y, "bo")
show()

#d) draw arrows from those points in the correct direction, using the pyplot function arrow
#e) if you want you can figure out how to add a circle, a plus sign and or "e" beside the charge, a scale bar, etc.


# ### 3) The gravitational field of the Earth-Moon system in 3D
# 
# Now let's try the same calculation in 3D. We will need some modifications:
# 
# - reduce the number of points for visibility
# 
# - add z to the sample point coordinates; also use meshgrid to create a 3D array for each of the x, y andz coordinates of the sample points
# 
# - calculate arrays of distances to the Earth and distances to the Moon for each sample point
# 
# - use the 3D methods/projections Axes3D from mplot3d, gca
# 
# The result doesn't look great because of the sample points close to the Earth and Moon; it would take some work to fix this...

# In[14]:


#a) pick units and a/or a picture size; this can be any value really
from matplotlib.pyplot import gca, rcParams, plot, show , arrow, Circle
from math import pi, sin, cos, sqrt
from numpy import arange
mratio = 0.4
ax = gca()
ax.set_aspect('equal')

rcParams['figure.figsize'] = [210,210]

ax = gca()
crc = Circle((0,0,0), 0.1, color='blue')
ax.add_artist(crc)
crc = Circle((1,0,0), 0.1*mratio, color='red')
ax.add_artist(crc)
ax.text(0.02, 0.1, r'+e', fontsize=100)





#b) given the picture size, pick a scaling for the field, such that the arrows fit sensibly on the plot.

kq = 0.1
GM = 0.05
mratio = 0.4 #this is not the right value

#c) pick a set of points at which to calculate and plot the field

x=[]
y=[]
#z=[0]


for xv in arange(-2.0, 2.0, 0.4):
    for yv in arange(-2.0, 2.0, 0.4):
        
        
        x.append(xv)
        y.append(yv)
        xm = xv - 1.0
        ym = yv - 0.0
        rE = sqrt(xv*xv +yv*yv)
        rM = sqrt(xm*xm +ym*ym)
    
        dxE = -xv*GM/rE/rE/rE
        dyE = -yv*GM/rE/rE/rE
        
        dxM = -xv*GM*mratio/rM/rM/rM
        dyM = -yv*GM*mratio/rM/rM/rM
        
        dx = dxE + dxM
        dy = dyE + dyM
        if (rE>0.2) and (rM >0.2):
            arrow(xv,yv,dx,dy,head_width = 0.07)
        
plot(x,y, "bo")
show()


# In[8]:


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import gca, rcParams, plot, show , arrow, Circle
from math import pi, sin, cos, sqrt
from numpy import arange



ax = plt.figure().add_subplot(projection='3d')

# Make the grid
x, y, z = np.meshgrid(np.arange(-2.0, 2.0, 0.5),
                      np.arange(-2.0, 2.0, 0.5),
                      np.arange(-2.0, 2.0, 0.5))

# Make the direction data for the arrows
dz = 0

ax.quiver(x, y, z, dx, dy,dz, length=0.1, normalize=True)

plt.show()


# ### 4) The tidal field of the Moon near the Earth
# 
# Finally, we can try to plot the *tidal* field of the Moon. This is the gravitational field of the Moon on Earth, *relative* to its mean value. 
# 
# Specifically, we can calculate this as:
# $$g_{tid}(\vec{r}) = g_M(\vec{r}-\vec{r}_M) + g_M(\vec{r_E}-\vec{r}_M)\,.$$
# 
# Where $\vec{r}_E$ is the location of the centre of the Earth, as before.
# 
# In this case, the tidal field varies strongly around the location of the Earth, so it makes sense to zoom in on the regionaround the Earth; you might use the radius of the Earth, $r_E = 6371$ km, as a reference scale for the plot, plotting out to a few $r_E$.
# 
# 

# In[ ]:


#No, could barely even do Q3


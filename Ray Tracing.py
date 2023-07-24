#!/usr/bin/env python
# coding: utf-8

# ## PHYS249 Lab 7: Ray Tracing

# ### 1) Modelling Reflection off a Spherical Mirror
# 
# In your 1st-year Physics lab, to understand the properties of optical systems, you probably drew rays through them. This technique is actually a real industrial one for studying the properties of real or proposed optical systems such as cameras, spectrographs, etc.
# 
# As a simple example, we will model the reflection of rays off a spherical mirror.
# 
# a) Start by defining the limits ot the system you will plot. We can take it to be a 2D cross-section through an optical system, extending from -5 to +5 on the x-axis and 0 to 10 on the y axis. Set the limits of the plot accordingly.
# 
# b) Then draw the mirror surface. We can take this to be an arc of the circle with centre (x, y) = (0,7), and radius 6, extending from -5 to 5 in x. You can either draw this parametrically or by calculating $y = f(x)$; you may want the latter form for subsequent calculations. I will call $y = f(x)$ the `equation of the surface'.
# 
# c) Then start a ray at the position (-4,10), and have it travel downwards vertically until it hits the mirror. At what coordinates does this happen? (Note "draw a ray" here really just means draw a line segment from the starting point to the ending point. If you wanted to get really fancy, you could animate the ray as it travels through the system, but we won't bother here. You might want to write a user-defined function that given a starting point, a direction, and a length, draws the required line segment.)
# 
# d) Once the ray hits the mirror, it should be reflected. The law of (specular) reflection says that the ray will be reflected *around* the normal to the mirror's surface at the reflection point. This means that the component parallel to the normal will be reversed, while the component perpendicular to the normal will remain unchanged. To perform this operation and get the reflected direction vector, you will first need to calculate the *normal vector* to the surface; this is the unit vector perpendicular to the *tangent* vector, which we saw can be calculated as a unit vector with a slope equal to the derivative of the function describing the surface.
# 
# e) Once you have the reflected vector, draw the reflected ray for some distance throught the system, say until it intersects the y axis or goes just past it.
# 
# f) Then repreat this operation for more downward-going rays, starting from points (-3,10), (-2,10), etc., across to (4,10).
# 
# g) Looking at the resulting system, what do you conclude about the abiltiy of spherical mirrors to focus light from infinity?

# In[67]:


# a) set limits
from matplotlib.pyplot import xlim, ylim, show, plot, gca, rcParams
from numpy import linspace, sqrt

xlim(-5,5)
ylim(0,10)

ax = gca()
ax.set_aspect('equal')
rcParams['figure.figsize'] = [10,10]

#*show()

# b) derive equation for surface and plot it

#x*x + (y-7)*(y-7) = 6*6
#(y-7)*(y-7) = 6*6 - x*x
#abs(y-7) = sqrt(6*6 -x*x)

#(y-7) = sqrt(6*6 -x*x)
#want the half below
#(y-7) = -sqrt(6*6 -x*x)

#define function 
def f(x):
    return(7 -sqrt(6*6 -x*x))

#defining coordinates of the function to plot
N = 200
x = linspace(-5,5,N)
y = f(x)
#plot(x,y)
#show()




# c) draw incident ray

def drawseg_pts(x0,y0,x1,y1):
    xp = []
    yp = []
    
    xp.append(x0)
    xp.append(x1)
    yp.append(y0)
    yp.append(y1)
    plot(xp,yp)

def drawseg_vec(x0,y0,dx,dy,mult):
    xp = []
    yp = []
    
    xp.append(x0)
    xp.append(x0+mult*dx)
    yp.append(y0)
    yp.append(y0+mult*dy)
    plot(xp,yp)

xv = -4
drawseg_pts(xv,10,xv,f(-4))
plot(x,y)
    
# d) calculate and draw tangent, then normal

def dfdx(x):
    return(x/sqrt(6*6 -x*x))

slope = dfdx(xv)
xp = xv
yp = f(xv)
dx = 0.1
dy = slope*dx
mult = 10.0
drawseg_vec(xp,yp,dx,dy,mult)

#note if [x0,y0] and [x1,y1] are orthogonal, x0x1 + y0y1 = 0
#so y1 = -(x0/y0) x1
#taking x1 = -y0, we get y1 = x0

drawseg_vec(xp,yp,-dy,dx,mult)

show()

# e) calculate and draw refelcted ray 

# (all this component-wise)
# form a unit vector in the normal direction
# form a direction vector for the incoming ray (-1,0)
# then project the direction vector onto the normal
# remeber this is (dv.en)en
# get the transverse component tv = dv - pv
# flip the project bit: ov = tv - pv
# draw a segment in this direction



# f) repeat


# In[69]:


xv = -4

def drawray_refl(xv):
    drawseg_pts(xv,10,xv,f(xv))
    
    slope = dfdx(xv)
  
    xp = xv
    yp = f(xv)
    dx = 0.1
    dy = slope*dx
    mult = 10.0
    drawseg_vec(xp,yp,dx,dy,mult)
    drawseg_vec(xp,yp,-dy,dx,mult)

plot(x,y)
drawray_refl(-4) 
drawray_refl(-4)
drawray_refl(-3)
drawray_refl(-2)
drawray_refl(-1)
drawray_refl(0)
drawray_refl(1)
drawray_refl(2)
drawray_refl(3)
drawray_refl(4)
drawray_refl(4)


# Spherical mirrors reflects rays from inifinity to the centre point of the spherical surface.   All the reflected rays converge at the focal point created.

# ### 2) Modelling Reflection off a Flat Mirror
# 
# Now try the same thing, with a flat mirror, i.e. one where the equation describing the surface is a linear equation. Assume a non-zero slope (i.e. a tilted mirror) for clarity. What do you find?

# In[51]:


#model of the reflection of the rays from infinity off a the surface of a tilted mirror
#slope (mirror) is linear 
from matplotlib.pyplot import xlim, ylim, show, plot, gca, rcParams
from numpy import linspace, sqrt

xlim(-10,10)
ylim(-10,10)

ax = gca()
ax.set_aspect('equal')
rcParams['figure.figsize'] = [10,10]
#define function 
def f(x):
    return(x)

#defining coordinates of the function to plot
N = 200
x = linspace(-5,5,N)
y = f(x)

#plot(x,y)

def drawray_refl(xv):
    drawseg_pts(xv,100,xv,f(xv))
    
    #slope = dfdx(xv)
  
    xp = xv
    yp = f(xv)
    dx = 0.1
    dy = dx
    #dy = slope*dx
    mult = 50.0
    drawseg_vec(xp,yp,dx,dy,mult)
    drawseg_vec(xp,yp,-dy,dx,mult)

plot(x,y)
drawray_refl(-4) 
#drawray_refl(-3)
drawray_refl(-2)
#drawray_refl(-1)
drawray_refl(0)
#drawray_refl(1)
drawray_refl(2)
#drawray_refl(3)
drawray_refl(4)


# ### 3) Modelling Reflection off a Parabolic Mirror
# 
# Finally, try the same thing, with a *parabolic* mirror, i.e. one where the equation describing the surface is a quadratic equation of the form $y = ax^2,\ \ a > 0$. Compare the results to question 1.

# In[75]:


from matplotlib.pyplot import xlim, ylim, show, plot, gca, rcParams
from numpy import linspace, sqrt

xlim(-30,30)
ylim(-5,30)

ax = gca()
ax.set_aspect('equal')
rcParams['figure.figsize'] = [10,10]
#define function 
def g(x):
    return(0.025*x**2)

#defining coordinates of the function to plot
N = 200
x = linspace(-30,30,N)
y = g(x)

plot(x,y)

def dgdx(x):
    return(0.05*x)

def drawray_refl(xv):
    drawseg_pts(xv,100,xv,g(xv))
    
    slope = dgdx(xv)
  
    xp = xv
    yp = g(xv)
    dx = 0.1
    dy = slope*dx
    mult = 100.0
    drawseg_vec(xp,yp,dx,dy,mult)
    drawseg_vec(xp,yp,-dy,dx,mult)

plot(x,y)
drawray_refl(-20) 
drawray_refl(-15)
drawray_refl(-10)
drawray_refl(-5)
drawray_refl(0)
drawray_refl(5)
drawray_refl(10)
drawray_refl(15)
drawray_refl(20)


# The results for a parabolic mirror is very similar to a spherical mirror, but if you extend the reflected lines
# for the parabolic surface the rays do not all converge at a point, but at various points with respect to each other.

import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

def Lorenz(xyz=[0, 1, 1.05], s=10, r=28, b=2.667, time=0.01):
    """
    Parameters
    ----------
    xyz : array-like, shape (3,)
       Intial point
    s, r, b : float
       Parameters defining the Lorenz attractor.
    time: float
        The 'time' step between each point
    Returns
    -------
    3 lists containing the x-coordinates, y-coordinates and z-coordinates
    respectively.
    """
    #Intializing the list of points
    x, y, z = [xyz[0]], [xyz[1]], [xyz[2]]
    for i in range(1, 10000):
        #setting the current x,y,z cooridnate.
        current_x, current_y, current_z = x[-1], y[-1], z[-1]

        #Updating the list of points with the next value
        x.append(current_x + time * (s * (current_y - current_x)))
        y.append(current_y + time * (r * current_x - current_y - current_x * current_z))
        z.append(current_z + time * (current_x * current_y - b * current_z))
    return x, y, z

def init():
    return ln,

def animate(i):
    ln.set_data([ x_values[:i], y_values[:i]])
    ln.set_3d_properties( z_values[:i] )
    return ln,

fig = plt.figure(facecolor="black")
ax = fig.add_subplot(projection='3d')

x_values, y_values, z_values = Lorenz()
ln, = ax.plot(x_values, y_values, z_values)

animation = FuncAnimation(fig, 
                    animate,
                    frames=len(x_values), 
                    init_func=init,
                    interval=.01,
                    )
plt.show()

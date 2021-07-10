import numpy as np
import math
import matplotlib.pyplot
from noise import snoise3
import time

def mandelbrot(canvas, x_win, y_win):
    print('run')
    #scale for perlin time
    scale = 9
    #seed for perlin noise
    seed = [0.49233038 , 0.5709, 0.651]
    #max iteration for mandelbrot convergence
    maxIter = 20
    
    x_scale = np.linspace(x_win[0], x_win[1], width, dtype='float32')
    y_scale = np.linspace(y_win[0], y_win[1], height, dtype='float32')
    
    x_time = x_scale * scale
    y_time = x_scale * scale
    # y_signal = scaleInput(y_scale,y_win[0],y_win[1],-height/2,height/2)
    for y, row in enumerate(canvas[:,:,0]):
        if not y %50:
            print(f'{y}/{height}')
        for x, _ in enumerate(row):
            z = complex(0,0)
            c = complex(x_scale[x],y_scale[y])
                
            for _ in range(maxIter):
                z = poly(z,c)
                zAbs = abs(z)
                if zAbs > 50:
                    break
                
            if zAbs > 30:
                #sand waves
                particleWave = math.sin(zAbs/32)
                canvas[y,x,0] = 0.92 + particleWave/8
                canvas[y,x,1] = 0.82 + particleWave/88
                canvas[y,x,2] = 0.70 + particleWave/8
            else:
                #water
                canvas[y,x, 1] = (snoise3(x_time[x], y_time[y], seed[1], 5) + 1)/2.5
                canvas[y,x, 2] = (snoise3(x_time[x], y_time[y], seed[2], 5) + 1)/2
                
                
#second order polynomial
def poly(z, c):
    return z*z + c
    
if __name__ == "__main__":
    height = 180*100
    width = 190*100
    canvas = np.zeros((height, width,3), dtype = np.float32)
    
    #full mandelbrot set
    # [minX, maxX],[minY, maxY]= [1-(2*width/height), 1], [-1, 1] 
    [minX, maxX],[minY, maxY]= [-2.1855746760144465+0.1, -0.8258975993201616+0.1] ,[0.3975462077756533, -0.39727214786488205]
    x_win = [minX, maxX]
    y_win = [minY, maxY]
              
    t = time.time()
    mandelbrot(canvas, x_win, y_win)
    print('Time elapsed:', time.time()-t)
    canvas = np.transpose(canvas,(1,0,9))
    
    matplotlib.pyplot.imsave('.//canvas.jpg', canvas)
    print('saved')
    # matplotlib.pyplot.imshow(canvas)






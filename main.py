import imageio.v3 as iio
filenames = ['hippocorn1.png', 'hippocorn2.png', 'hippocorn3.png', 'hippocorn4.png'] 
images = [ ]
for filename in filenames:
  images.append(iio.imread(filename))
iio.imwrite('team.gif', images, duration = 200, loop = 0)
# This code reads a series of images and compiles them into an animated GIF.
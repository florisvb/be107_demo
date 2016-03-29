import multi_tracker_analysis as mta
import matplotlib.pyplot as plt

# define the directory, and find the h5 file
filename = 'data/XXXXXX.hdf5'

# get the background image filename
bgimg_filename = 'data/XXXXXXXX.png'

# load the h5 file as a pandas dataframe
pd = mta.read_hdf5_file_to_pandas.load_data_as_pandas_dataframe_from_hdf5_file(filename)

# get the size of the image
binsx, binsy = mta.plot.get_bins_from_backgroundimage(bgimg_filename)

# set up a figure
fig = plt.figure()
ax = fig.add_subplot(111)

# plot the trajectories, save the figure
mta.plot.plot_trajectories(pd, binsx, binsy, ax=ax)
fig.savefig('trajectories.pdf', format='pdf')

# put in the background image
bgimg = plt.imread(bgimg_filename)
ax.imshow(bgimg, cmap='gray', zorder=-100)
fig.savefig('trajectories_with_bgimg.pdf', format='pdf')


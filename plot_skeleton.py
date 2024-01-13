import numpy as np
import matplotlib.pyplot as plt

# Change Font Size 
# plt.rcParams.update({'font.size': 10})

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# load skeleton 
raw_data = np.loadtxt("Skeletons\s02_a08\_raw_data.txt")


# remove first column (frame number) # load data with frame number
data= np.delete(raw_data,0,1) 
print(raw_data.shape, data.shape)


def get_activity_start_end(subject =  1, activity = 1):	
	activity_range = labels[subject, activity-1:activity+1]
	print(activity_range)
	return activity_range[0], activity_range[1]


# get the hip_centre from the first frame on the activity sequence
raw_frame_1 = data[0].reshape(20,3)
hip_center_first = raw_frame_1[0]

# define set of joints
bones = [[0, 1],[1, 2], [2,3], #Spine 
[2,4], [4, 5], [5, 6], [6,7], # left hand
[2,8], [8,9], [9,10], [10,11],# right hand 
[0,12], [12,13], [13,14], [14,15], #left leg
[0,16], [16,17], [17,18], [18,19] # right leg 
]

def showAllFrames(frame_start,frame_end):
	for i in range(frame_start,frame_end): # show all frames data.shape[0]
		raw_frame = data[i].reshape(20,3)
		next_frame = data[i+1].reshape(20,3)

		if i==1:			
			frame = raw_frame - raw_frame[0]
		else:		
			frame = raw_frame - raw_frame[0] + (next_frame - raw_frame)
			# frame = raw_frame - raw_frame[0]

		# print(frame.shape) # 75,3 

		x = frame[:,0]
		y = frame[:,1]
		z = frame[:,2]

		ax.scatter(x, y, z,c='b', marker='o')
		# ax.scatter(x[:,0], y[:,1], z[:,2], c='r', marker='o') 

		for bone in bones:
			start = bone[0]
			end = bone[1]
			# ax.plot([x[start+i], x[end+i]], [y[start+i], y[end+i]], [z[start+i], z[end+i]], color='red')
			ax.plot([x[start], x[end]], [y[start], y[end]], [z[start], z[end]], color='red')

		ax.set_xlim(-1, 1)
		ax.set_ylim(-1, 1)
		ax.set_zlim(-1, 1)

		# Set plot title 
		ax.set_title(i, y=-0.01)

		ax.view_init(elev=90, azim=-90)# front view
		# ax.view_init(elev=110, azim=-90)

		# set labels
		ax.set_xlabel('X Label')
		ax.set_ylabel('Y Label')
		ax.set_zlabel('Z Label')

		plt.draw()
		plt.pause(0.1)
		plt.cla()

# showAllFrames()

# get x,y,z coordinates of each joints from a frame. 
def get_xyz_coordinates(frame):	
	x = frame[:,0]
	y = frame[:,1]
	z = frame[:,2]

	return x,y,z

# plot bones
def plot_bones(bones,x,y,z):
	for bone in bones:
		start = bone[0]
		end = bone[1]
		# ax.plot([x[start+i], x[end+i]], [y[start+i], y[end+i]], [z[start+i], z[end+i]], color='red')
		ax.plot([x[start], x[end]], [y[start], y[end]], [z[start], z[end]], color='red')

		# Configure x,y,z range 
		ax.set_xlim(-1, 1)
		ax.set_ylim(-1, 1)
		ax.set_zlim(-1, 1)	

		# Change the viewing angle 
		ax.view_init(elev=90, azim=-90)# front view
		# ax.view_init(elev=110, azim=-90)

		# set labels
		ax.set_xlabel('X')
		ax.set_ylabel('Y')
		ax.set_zlabel('Z')
	return ax

# plot a 
def showSingleFrame(frame_no, translation=True, single_frame=False):

	"""
	Display a single frame from a sequence.

	Parameters:
	- frame_no (int): The frame number to display.
	- translation (bool, optional): Whether to translate the frame. Default is True.
	- single_frame (bool, optional): used for clearing the display when used to display frames in the sequence. 
	Set single_frame=True when displaying a single frame

	Returns:	
	Displays a visualization of the specified frame
	"""

	raw_frame = data[frame_no].reshape(20,3)
	x,y,z = get_xyz_coordinates(raw_frame)

	# translate the frame
	if translation:		
		translated_frame = raw_frame - hip_center_first # Relative translation
		x,y,z = get_xyz_coordinates(translated_frame)

	# Scatter the joints 
	ax.scatter(x, y, z,c='b', marker='o')	

	# plot the bones 
	plot_bones(bones,x,y,z)

	# Set plot title 
	# ax.set_title("Skeleton", y=-0.01)

	ax.view_init(elev=114, azim=-90,roll=0)

	# #Enable to save the figure
	# plt.savefig('skeleton_frame_'+str(frame_no) + '_s2_a08.svg')

	if single_frame:
		plt.show()

	# clear previos drawing for multiple frames 
	# plt.cla()


# #Show frames in ranges with an interval 
# frames = [x for x in range(0,40,5)]
# print(frames)
# for frame in frames:
# 	showSingleFrame(frame)



def showFrameRange(frame_start,frame_end, translation=True):
	"""
	Display a range of frames from a sequence.

	Parameters:
	- frame_start (int): The starting frame number of the range to display.
	- frame_end (int): The ending frame number of the range to display.
	- translation (bool, optional): Whether to translate the frames. Default is True.

	Displays a visualization of the frames within the specified range, optionally including translation information.
	"""

	for i in range(frame_start,frame_end): 	
		raw_frame = data[i].reshape(20,3)
				
		# frame = raw_frame - raw_frame[0] # frame by frame translation 
		frame = raw_frame - hip_center_first # Relative translation

		x,y,z = get_xyz_coordinates(frame)

		ax.scatter(x, y, z,c='b', marker='o')
		# ax.scatter(x[:,0], y[:,1], z[:,2], c='r', marker='o')

		plot_bones(bones,x,y,z)

		# Set plot title 
		ax.set_title(i, y=-0.01)

		plt.draw()
		plt.pause(0.1)
		plt.cla()

# A shorter version to display frame range
def showFrameRangeV2(frame_start,frame_end):
	for frame_no in range(frame_start,frame_end):
		showSingleFrame(frame_no)

		ax.set_title("Frame #{} ".format(frame_no), y=-0.01)
		plt.pause(0.1)
		# Clear the current plot 
		plt.cla()

# showSingleFrame(120, single_frame=True)
showFrameRange(20, 50)
# showFrameRangeV2(20, 50)


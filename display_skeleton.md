### Showing a Single Frame

1. **Function Call:**
   - Call the `showSingleFrame` function with the desired frame number.

   ```python
   showSingleFrame(frame_no)
   ```

2. **Optional Parameters:**
   - Optionally, you can customize the display:
      - Set `translation` to `False` to disable joint translation.
      - Set `single_frame` to `True` if you want to display only the specified frame.

   ```python
   showSingleFrame(frame_no, translation=False, single_frame=True)
   ```

3. **Visualization:**
   - The function will visualize the specified frame in a 3D plot, highlighting joint positions and bone connections.

4. **Interactivity:**
   - Interact with the plot to explore the 3D representation of the skeleton.
   - Close the plot window to proceed with further analysis or visualization.

**Example:**
```python
# Display single frame number 120 without translation
showSingleFrame(120, translation=False, single_frame=True)
```


### Displaying a Range of Frames

To visualize a range of frames using the `showFrameRange` function:

1. **Function Call:**
   - Call the `showFrameRange` function with the starting and ending frame numbers.

   ```python
   showFrameRange(frame_start, frame_end)
   ```

2. **Optional Parameters:**
   - Optionally, you can customize the display:
      - Set `translation` to `False` to disable joint translation.

   ```python
   showFrameRange(frame_start, frame_end, translation=False)
   ```

3. **Visualization:**
   - The function will iterate through the specified frame range, displaying each frame's 3D representation.
   - Observe joint movements and connections throughout the specified range.

4. **Interactivity:**
   - Interact with the plots to explore the evolving skeleton positions.
   - Close the plot window to proceed with further analysis or visualization.

**Example:**
```python
# Display frames from 20 to 50 with joint translation enabled
showFrameRange(20, 50, translation=True)
```

This function provides an interactive way to observe the sequence of frames and analyze the dynamics of the skeleton movements within the specified range.
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
# Physical-Activity-Tracker-App

&ensp;&ensp;Our software provides sensor data from a physical device that tracks a user’s physical activity. Raw sensor data does not have much value to an unsophisticated user, our application is designed to interpret that data visually in a way that is not only more appealing but also more informative.

![image](https://user-images.githubusercontent.com/59776018/206876225-3573ff34-e326-4ce5-84a9-45f6f297e61e.png)

---

# How To Run?

# File Structure As Follows:

- `README.md` - This file
- `LICENSE` - The license file for this project **(MIT)** Coming Soon
- `src` - The source code for this project, including the `main` method, gui, and data processing.
- `tests` - The test code for this project. i.e:
  - `tests/test_main.py` - The test code for the `main` method
  - `tests/test_gui.py` - The test code for the `gui` method
  - `tests/test_data_processing.py` - The test code for the `data_processing` method
- `build` - The build files for this project.
  - `build/Physical-Activity-Tracker-App.exe` - The executable file for this project.
- `bin` - The binary files for this project or scripts to run the project
  - `bin/run.bat` - The batch file to run the project // If needed
  - `bin/run.sh` - The shell script to run the project // If needed
- `docs` - The documentation for this project.
- `data` - The data files for this project.

---

# Installation

### 1. Clone the repository:

   - Select a directory to clone the repository into. Make sure you have git installed.
   - Run Command: `git clone https://github.com/ReaVNaiL/Physical-Activity-Tracker-App.git` in the directory you want to clone the repository into or a CLI.
     - ***Note**: If you prefer to use SSH, use the SSH link instead of the HTTPS link; as well as if you prefer to use GitHub Desktop, use the GitHub Desktop link instead of the HTTPS link.*

### 2. Install the requirements:
   - Run Command: `pip install -r requirements.txt` in the directory you cloned the repository into or a CLI.

### 3. Run the program:
   - Run Command: `python app.py` or `py app.py` in the directory you cloned the repository into or a CLI.

# How To Contribute

### 1. Creating your own branch:
   - In github.com, create a branch for the project. This will be your own branch to work on.
   - The branch name should be in this format: `user/username` where `username` is your github username or your name.
   
### 2. When you are ready to commit your changes, make sure you are on your branch and run the following commands:
   - `git add .` - This will add all the files you have changed to the staging area.
   - `git commit -m "message"` - This will commit your changes to your branch. The message should be a short description of what you have changed.
   - `git push` - This will push your changes to your branch on github.com.

   >>**Or Github.com/DesktopApp**:

   - Create a pull request to merge your branch into the master branch. The pull request should be reviewed by another team member before it is merged into the master branch.

---

### *If you have any questions, please reach out in Teams. If having issues with git, please reach out to merge the files manually.*

# User Manual:
## Main Window:
### 1. Import Data
Click on Import Data to choose a `data` source.
### 2. Clear Data
Click on Clear Data to remove imported `data` from memory.
### 3. Index
Click on this dropdown menu to choose whether to load `data` from the `metadata.csv` or `summary.csv` file.
### 4. Subject
Click on this dropdown menu to select which user’s `data` to load, or choose “All Subjects” to load everyone’s data.
### 5. Device
Click on this dropdown menu to specify `Android` or `iOS`, or choose All Devices.
### 6. Date Range
The Physical Activity Tracker Application will only display `data` within the chosen `date range`. To change values, you can click on a number in the date picker window and then type, or click the up and down arrows, or use the up and down arrows on your keyboard.
### 7. Standard Time
By default this checkbox is clicked, but unclicked, the time will be converted to `UTC` instead. 
### 8. Save
Click this button to `save` your changes and the second window will appear which contains your data’s headers. From here, choose which `headers` you will like to be plotted by moving them to the second column as seen below.

## Data Display:
### 1. Legend
The `legend` in the upper-right corner of the graph will show you what each color in the `graph` refers to. You can also click each member on the `legend` to hide or reshow the relevant data.
### 2. Title
The `title` will display above each `graph` to identify what kind of data is being displayed.
### 3. Right Click Menu
`Right` clicking on a `graph` brings up a menu that allows you to manipulate the graph in various ways:
- `View All`: Clicking this resets the graph back to its original state of viewing the entire graph
- `X-Axis`: This opens a menu that allows the user to manipulate the X axis in various ways. These include being able to select for manual or automatic scaling of the X axis, being able to invert the X axis, being able to enable mouse controls for the X axis, and being able to like the X axis to another axis.
- `Y-Axis`:  This opens a menu that allows the user to manipulate the Y axis in various ways, similar to the X axis.
- `Mouse Mode`: This allows you to switch between 3 Button mode and 1 Button mode. 1 Button mode allows the user to click and drag a rectangle over the graph to zoom into the selected area.
### 4. Plot Options
In the right click menu, there exists another menu that allows you to further manipulate the data the graph is depicting:
- `Transforms`: This section allows the user to apply various transforms to the data. These transforms include: Power Spectrum, Log(X), Log(Y), dy/dx, and Y vs. Y’.
- `Downsample`: This allows the user to downsample the data.
- `Average`: When selected, displays the average of the graphs.
- `Alpha`: Change the alpha (transparency) value of the graph.
- `Grid`: This section allows the user to modify the visibility of the X lines on the grid, the Y lines on the grid, and the opacity of the grid lines.
- `Points`: Allows the user to toggle the display of points on the graph.
### 5. Export
- This allows the user to export the current graph as an image file, SVG file, Matplotlib window, or CSV from plot data. It also allows the user to select which parameters are carried through the export.




Virtual Drawing with Hand Tracking

This project uses hand tracking to create a virtual drawing application where you can draw and erase on a canvas using hand gestures. The application uses OpenCV and a custom HandTrackingModule to detect hand gestures and control the drawing process.

Features:
- Drawing Mode: Draw on the canvas using the index finger.
- Erase Mode: Erase the drawing by making a fist.
- Clear Canvas: Clear all drawings with a button click.
- Real-Time Hand Detection: Uses a webcam to detect hand positions and gestures.

Requirements:
- Visual Studio (or any .NET compatible IDE)
- OpenCV (with EmguCV wrapper for .NET)
- HandTrackingModule (custom module for hand gesture detection)

Installing Dependencies:
You can install the required libraries using NuGet:
- Install EmguCV for OpenCV support.
- Make sure to include your custom HandTrackingModule in the project.

How to Use:
1. Run the Program:
   - Simply run the VB.NET program to start the virtual drawing application.
   - The webcam will open, and you'll see the virtual canvas.

2. Modes:
   - Draw Mode: Raise your index finger to draw on the canvas.
   - Erase Mode: Close your fist to erase the drawing.
   - Clear All: Press the "Clear All" button to reset the canvas.

3. Exit: Press the "q" key to close the application.

Code Overview:
- The program captures video from your webcam.
- Hand tracking is done using the HandTrackingModule to detect the position of your hands and fingers.
- You can draw with the index finger or erase with a fist.
- On-screen buttons allow switching between draw and erase modes and clearing the canvas.

License:
This project is open-source and available under the MIT License.

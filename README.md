# GIF_Creator

# Python GIF Creator

Python GIF Creator is a simple program that creates a GIF from a sequence of images. It uses the Pillow library for image processing and combines the images into an animated GIF with customizable frame durations and loop count.

## Getting Started

These instructions will help you run the GIF Creator program on your local machine.

### Prerequisites

- Python 3.x
- Pillow library

You can install the required library using pip:

pip install Pillow


### Usage

1. Clone this repository or download the `gif_creator.py` file.

2. Prepare the images you want to include in the GIF. Place them in a folder and make note of their file paths.

3. Open the `gif_creator.py` file in a text editor.

4. Replace the `image_list` variable with a list of image paths you want to include in the GIF. For example:

image_list = ["path/to/image1.png", "path/to/image2.png", "path/to/image3.png"]


5. Set the output GIF file path using the `gif_path` variable:

gif_path = "output.gif"


6. (Optional) Customize the duration of each frame in milliseconds using the `duration` parameter:

duration = 100 # 100 ms


7. (Optional) Set the number of loops for the GIF using the `loop` parameter. Use 0 for an infinite loop:

loop = 0 # Infinite loop


8. Save the changes to the `gif_creator.py` file.

9. Open a terminal or command prompt.

10. Navigate to the directory containing the `gif_creator.py` file.

11. Run the program by executing the following command:

python gif_creator.py

12. The program will create the GIF using the specified images, duration, and loop count and save it as `output.gif` in the same directory.

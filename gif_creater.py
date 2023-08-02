from PIL import Image

def create_gif(image_list, gif_path, duration=100, loop=0):
    """
    Create a GIF from a list of images.

    Parameters:
    image_list (list): List of image paths.
    gif_path (str): Output GIF file path.
    duration (int, optional): Duration of each frame in milliseconds. Default is 100 ms.
    loop (int, optional): Number of loops. Set 0 for infinite loop. Default is 0 (infinite).

    Returns:
    None
    """
    images = []
    for image_path in image_list:
        images.append(Image.open(image_path))

    images[0].save(gif_path, save_all=True, append_images=images[1:], duration=duration, loop=loop)

if __name__ == "__main__":
    # List of image paths to include in the GIF
    image_list = ["image1.png", "image2.png", "image3.png"]

    # Output GIF file path
    gif_path = "output.gif"

    # Create the GIF with default duration and infinite loop
    create_gif(image_list, gif_path)

We need to replace "image1.png", "image2.png", etc., with the paths of the images you want to include in the GIF. You can adjust the duration (in milliseconds) 
of each frame and the number of loops.

Make sure you have the Pillow library installed before running the program:
Pip install Pillow

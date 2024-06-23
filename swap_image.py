from PIL import Image

def swap_pixels(image_path):
    # Open the image file
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure the image is in RGB mode
    width, height = img.size

    # Create a new image to store the swapped pixels
    swapped_img = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width // 2):
            # Get pixels from left and right halves
            pixel1 = img.getpixel((x, y))
            pixel2 = img.getpixel((width - 1 - x, y))

            # Swap the pixels
            swapped_img.putpixel((x, y), pixel2)
            swapped_img.putpixel((width - 1 - x, y), pixel1)

    # Save the new image
    swapped_img.save("swapped_image.png")

def main():
    image_path = input("Enter the path to the image: ")
    swap_pixels(image_path)

if __name__ == "__main__":
    main()

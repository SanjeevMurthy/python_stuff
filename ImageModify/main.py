from PIL import Image, ImageDraw, ImageFont


def create_image(name):
    # Open the image
    image_path = "invite.jpg"  # Replace with your image file path
    image = Image.open(image_path)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Define the text to be added
    text = f"{name}"
    font = ImageFont.truetype("italic.ttf", 50)  # Replace with your desired font and size

    # Calculate the position to place the text (e.g., top center)
    text_width, text_height = draw.textsize(text, font)
    image_width, image_height = image.size
    # text_x = (image_width - text_width) / 2
    # text_y = 0

    text_x = 695  # Replace with your desired x-coordinate
    text_y = 170  # Replace with your desired y-coordinate

    # Add the text to the image
    draw.text((text_x, text_y), text, fill="black", font=font)

    # Save the modified image
    output_path = f"./invites/{name}.jpg"  # Replace with your desired output file path
    image.save(output_path)

    print("Text added to the image successfully!")


def getNames():
    file_path = 'txt/contact_names.txt'  # Replace with your input file path

    # Open the text file in read mode
    with open(file_path, 'r') as file:
        # Read all lines from the file into a list
        lines = file.readlines()

    # Remove newline characters from each line in the list
    lines = [line.strip() for line in lines]

    # Print the list of lines from the text file
    print("List of lines from the text file:")
    return lines


NAMES = getNames()
for name in NAMES:
    create_image(name)

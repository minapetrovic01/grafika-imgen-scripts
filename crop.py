from PIL import Image
import os

def split_image(image_path, output_dir):
    original_image = Image.open(image_path)

    width, height = original_image.size

    new_width = width // 2
    new_height = height // 2

    for i in range(2):
        for j in range(2):
            left = j * new_width
            top = i * new_height
            right = left + new_width
            bottom = top + new_height
            cropped_image = original_image.crop((left, top, right, bottom))

            filename = f"resized_{i}_{j}.jpg"
            output_path = os.path.join(output_dir, filename)

            cropped_image.save(output_path)
            print(f"Saved {output_path}")

if __name__ == "__main__":
    image_path = "resized_image.jpg"

    output_directory = "C:\\Users\\minap\\ELFAK\\vid\\za_grafiku\\"

    split_image(image_path, output_directory)

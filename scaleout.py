from PIL import Image

def resize_image(input_path, output_path):
    original_image = Image.open(input_path)

    width, height = original_image.size

    new_width = width // 2
    new_height = height // 2

    resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)

    resized_image.save(output_path)
    print(f"Resized image saved at {output_path}")

if __name__ == "__main__":
    input_image_path = "C:\\Users\\minap\\ELFAK\\vid\\za_grafiku\\resized_image.jpg"

    output_image_path = "C:\\Users\\minap\\ELFAK\\vid\\za_grafiku\\resized_image.jpg"

    resize_image(input_image_path, output_image_path)

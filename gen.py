import os
import json

# folder z obrazkami (relatywnie do skryptu)
images_folder = "images"

# rozszerzenia plików, które chcemy uwzględnić
valid_extensions = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

# lista plików
image_files = []

if os.path.exists(images_folder):
    for filename in os.listdir(images_folder):
        if os.path.splitext(filename)[1].lower() in valid_extensions:
            image_files.append(filename)
else:
    print(f"Folder '{images_folder}' nie istnieje!")

# zapis do images.json
with open("images.json", "w", encoding="utf-8") as f:
    json.dump(image_files, f, indent=4, ensure_ascii=False)

print(f"Wygenerowano 'images.json' z {len(image_files)} plikami.")

import os
import yaml


def generate_photo_of_the_day_metadata():
    photo_metadata = {}
    photo_directory = "website/assets/photo-of-the-day"

    for root, dirs, files in os.walk(photo_directory):
        for filename in files:
            if filename.endswith(".jpg") or filename.endswith(".jpeg"):
                file_path = os.path.join(root, filename)
                # Extract date from the file path
                parts = file_path.split("/")
                date = parts[-2]  # Assumes date is in second last part of path
                image_name = filename

                if date in photo_metadata:
                    raise ValueError(f"Duplicate date found for {date}.")

                # Assign to dictionary using date as key
                photo_metadata[date] = {"display_image": image_name}

    # Write metadata to YAML file
    metadata_file = "website/_data/photo-of-the-day-metadata.yml"
    
    with open(metadata_file, "w") as file:
        yaml.dump(photo_metadata, file, default_flow_style=False)

    print(f"Generated metadata file: {metadata_file}")


if __name__ == "__main__":
    generate_photo_of_the_day_metadata()

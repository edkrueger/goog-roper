"""
Creates the .env file with the service account jsons as strings.
"""

import json
import os


def load_json_file_as_str(filepath):
    """Read in a file as a string."""
    with open(filepath, "r") as in_file:
        # load as dict and write as string to remove spacing
        json_as_dict = json.loads(in_file.read())
        json_as_str = json.dumps(json_as_dict)
        return json_as_str


if __name__ == "__main__":
    BQ_FILEPATH = "gcp-bq.json"
    STORAGE_FILEPATH = "gcp-storage.json"
    with open(".env", "w+") as out_file:
        for json_filepath in [BQ_FILEPATH, STORAGE_FILEPATH]:
            root, ext = os.path.splitext(json_filepath)
            json_file_as_str = load_json_file_as_str(json_filepath)
            line = f"{root.upper().replace('-','_')}='{json_file_as_str}'\n"
            out_file.write(line)

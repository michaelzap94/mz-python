import os
import shutil
from os import path
import tempfile
from csv import DictWriter
import gzip

consolidated_file_name = 'consolidated.csv.gz'

with tempfile.NamedTemporaryFile(mode="w") as feed_resultant_file:
    headers = ["name", "age"]
    csvwriter = DictWriter(feed_resultant_file, fieldnames=headers, delimiter="\t")
    csvwriter.writeheader()
    csvwriter.writerow({'name': 'mike', 'age': 23})

    with open(feed_resultant_file.name, 'rb') as f_in, gzip.open(consolidated_file_name, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    # copy file and rename it to 'consolidated.csv.gz' -> THIS DOES NOT COMPRESS IT
    # shutil.copy(feed_resultant_file.name, consolidated_file_name)

    # remove the file created
    os.remove(consolidated_file_name)

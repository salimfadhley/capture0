import copy
import json
import logging
import os
import uuid
from typing import Mapping

from capture0.config import CONFIG

log = logging.getLogger(__name__)

def store_data(dataset: str, record: Mapping):
    record = copy.copy(record)
    id = str(uuid.uuid1())
    dataset_dir = os.path.join(CONFIG["SAVE_DIR"], dataset)
    record["uuid"] = id

    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)

    file_path = os.path.join(dataset_dir, "%s.json" % id)

    with open(file_path, "w") as output_file:
        output_file.write(json.dumps(record))
        log.info("Saved %s" % file_path)

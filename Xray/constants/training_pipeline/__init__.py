from datetime import datetime

from typing import List

import torch

TIMESTAMP: datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

# Data Ingestion Constants
ARTIFACT_DIR: str = "artifacts"
BUCKET_NAME: str = "LungsXrayImgs"
S3_DATA_FOLDER: str = "data"

CLASS_LABEL_1: str = "NORMAL"
CLASS_LABEL_2: str = "PNEUMONIA"
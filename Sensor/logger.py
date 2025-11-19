import os
import logging
from datetime import datetime

# here in this file we are just creating the log file in the particular folder('log')


# Step 1: Generate file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 2: Create logs folder path
LOGS_FOLDER = os.path.join(os.getcwd(), "logs")  # os.getcwd() this is folder path or project path in which we are creating folder logs

# Step 3: Create folder if not exists
os.makedirs(LOGS_FOLDER, exist_ok=True)

# Step 4: Create final file path
LOG_FILE_PATH = os.path.join(LOGS_FOLDER, LOG_FILE)

logging.basicConfig(filename=LOG_FILE_PATH,
                    format='[%(asctime)s]-%(lineno)d - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,

                    )



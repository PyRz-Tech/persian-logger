import sys
from pathlib import Path
from persian_logger import get_fa_logger


sys.path.append(str(Path(__file__).resolve().parents[1]))
logger = get_fa_logger()
logger.debug("این DEBUG است")
logger.info("این INFO است")
logger.warning("این WARNING است")

import os

THIS_DIR, _ = os.path.split(os.path.abspath(os.path.expanduser(__file__)))

CONFIG = {
    "STATIC": os.path.join(THIS_DIR, "static"),
    "SAVE_DIR": os.path.join(os.path.expanduser("~"), "capture0")
}

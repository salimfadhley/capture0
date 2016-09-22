import os
import pkg_resources
import static

THIS_DIR, _ = os.path.split(os.path.abspath(os.path.expanduser(__file__)))

CONFIG = {
    "STATIC": pkg_resources.resource_filename("capture0_static", "dist"),
    "SAVE_DIR": os.path.join(os.path.expanduser("~"), "capture0")
}

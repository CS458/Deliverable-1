import sys
import os


ROOT_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))

TEMPLATE_DIR = os.path.join(ROOT_DIR, "views")
STATIC_DIR = os.path.join(ROOT_DIR, "static")
DATABASE_DIR = os.path.join(ROOT_DIR, "database")

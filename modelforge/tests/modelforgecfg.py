import os
import shutil
import tempfile

tmpdir = os.path.join(tempfile.gettempdir(), "modelforge-tests")
shutil.rmtree(tmpdir, ignore_errors=True)
VENDOR = os.path.relpath(tmpdir, os.getcwd())
BACKEND = "gcs"
BACKEND_ARGS = "bucket=models.cdn.srcd.run,credentials="
ALWAYS_SIGNOFF = True

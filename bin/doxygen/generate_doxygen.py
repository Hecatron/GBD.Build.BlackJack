"""
Script to generate doxygen docs
"""

import shutil, subprocess, os

doxygen_exe = "C:\\Program Files\\doxygen\\bin\\doxygen.exe"
doxygen_config = "doxygen_config.dox"
doxygen_dir = "../../docs/doxygen"

# Run a command
def run_cmd(cmdarray, workingdir):
    proc = subprocess.Popen(cmdarray, cwd=workingdir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    proc_out, proc_err = proc.communicate()
    print(proc_out)
    print(proc_err)
    if proc.returncode != 0:
        raise RuntimeError("Failure to run command")
    return

# Remove the old doxygen directory
doxygen_dir = os.path.abspath(doxygen_dir)
print(doxygen_dir)
shutil.rmtree(doxygen_dir)

# Generate the doxygen files
run_cmd([doxygen_exe, doxygen_config], ".")

import marvmiloTools as mmt

output = mmt.Output("SCRIPT", logfile = "output.log")
#cleanup from last time
output.cleanup_logfile()
output.log("logging output")

print = output.print
print("logging prints")

def main():
    1 / 0

output.log_python_error(main)
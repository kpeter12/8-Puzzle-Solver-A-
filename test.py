# Used only for testing of the main program.
import subprocess


num_shuffles = 100
num_runs = 10

time_sum = 0
for i in range(0, num_runs):
    print("running program ", i)
    output = subprocess.check_output('python3 Main.py ' + str(num_shuffles), shell=True)
    last_line = output.splitlines()[-1]
    time_sum += float(last_line)

print("AVG: ", time_sum / num_runs)

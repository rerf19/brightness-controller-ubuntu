import os
import subprocess


print("What monitor do you wanna modify? (1,2,3,...)")

##GET MONITORS
# Run the command and capture the output
output = subprocess.check_output('xrandr | grep " connected" | cut -f1 -d " "', shell=True)
# Decode the output and split it into lines
output = output.decode('utf-8')
monitorName = output.split('\n')

print(monitorName)
monitorNumber = input()

print("What brighgtness do you want put?(0-1)")
monitorBrightness = input()

command = f'xrandr --output {monitorName[int(monitorNumber) - 1]} --brightness {monitorBrightness}'
os.system(command)

print("Succefully Completed")


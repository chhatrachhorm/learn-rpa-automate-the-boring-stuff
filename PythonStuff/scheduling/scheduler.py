import subprocess


# running python script
subprocess.Popen(['C:\ProgramData\Anaconda3\python.exe', 'openingExe.py'])

# opening file with default app

subprocess.Popen(['start', 'files/account.csv'], shell=True)

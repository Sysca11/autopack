import os,subprocess,sys
def runldd(exe):
	a=subprocess.Popen(("ldd",exe),stdout=subprocess.PIPE)
	a.wait()
	return a.stdout.read().decode("utf-8")


def cookldd(exe):
	raw=runldd(exe)
	raw=raw.split('\n')
	for i in raw:
		i=i.strip()
		if i.find('=> ')!=-1:
			lpath=i.split('=> ')[1].split(' ')[0]
			print(lpath)
			os.system("cp %s packed"%lpath)
os.system("mkdir packed")
cookldd(sys.argv[-1])
os.system("cp %s packed"%sys.argv[-1])


import sys
import os
import pefile


def ReadFile(folder, file):
	lines = []
	d = os.getcwd() #current dir

	return pefile.PE(d + '\\' + folder + '\\' + file)

#simplesmente retorna os arquivos na pasta informada
def FindFiles(folder):
	return os.listdir(folder)

def IsExecutable(sec):
	att = getattr(sec, 'Characteristics')

	if att & 0x00000020 > 0 or att & 0x20000000 > 0:
		return True
	return False

def CheckBin(pe):

	exectbl = []

	for sec in pe.sections:
		if IsExecutable(sec):
			exectbl.append(sec.Name.decode('utf-8').strip())
	return exectbl


def ListExec(results):
	for i in range(0, len(results)):
		print(str(results[i][0]) + ': [', end='')
		for j in range(1, len(results[i])):
			print(str(results[i][j])+', ', end='')
		print(']')


if __name__ == "__main__":
	arq_dir = sys.argv[1]
	lines, results = [], []


	if arq_dir == 'a':
		file = sys.argv[2]

		pe = pefile.PE(os.getcwd() + '\\' + file)
		exec_sec = CheckBin(pe)
		results.append([file]+exec_sec)

	elif(arq_dir == 'd'):
		diret = sys.argv[2]

		files = FindFiles(diret)

		for file in files:
			pe = ReadFile(diret, file) # -> lemos o arquivo
			#print(pe.sections[1][0])
			exec_sec = CheckBin(pe)
			results.append([file]+exec_sec)

	ListExec(results)

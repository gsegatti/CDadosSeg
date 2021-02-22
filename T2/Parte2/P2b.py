import sys
import os
import pefile


def FillDic(pe):
	d = {}
	for sec in pe.sections:
		sec_name = sec.Name.decode('utf-8').strip()
		#print(sec_name)
		if sec_name not in d:
			d[sec_name] = 1

	return d


def Find_Common_Unique(d1,d2):
	common, unique = [], []
	for key, val in d1.items():
		if key in d2:
			common.append(key)
		else:
			unique.append(key)

	return common, unique

def PrintRes(common, unique):
	print('------------\n\n' + 'Seções Únicas:')

	print(unique)

	print()
	print('------------\n\n' + 'Seções Comuns:')
	print(common)
	print()

if __name__ == "__main__":
	f1, f2 = sys.argv[1], sys.argv[2]

	p1 = pefile.PE(f1)
	p2 = pefile.PE(f2)

	d1 = FillDic(p1)
	d2 = FillDic(p2)

	common, unique = Find_Common_Unique(d1, d2)
	PrintRes(common, unique)
	

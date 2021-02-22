import sys
import os

#lê o AndroidManifesto, encontrando o caminho ate o diretorio atual (d), a pasta em q se encontram (folder) e o nome do arquivo achado
# em FindFiles()
def ReadFile(folder, file):
	lines = []
	d = os.getcwd() #current dir

	with open(d + '\\' + folder + '\\' + file) as f:
		for line in f:
			lines.append(line)
	return lines

#simplesmente retorna os arquivos na pasta informada
def FindFiles(folder):
	return os.listdir(folder)


'''
aqui queremos pegar as linhas no seguinte formato:
        android:name="android.permission.ACCESS_WIFI_STATE" />

para isso, jogamos fora linhas como
<uses-permission

ou qualquer outra linha sem a ocorrencia da palavra permission
'''
def FilterLines(lines):
	newLines = []

	for line in lines:
		if '=' in line and "permission" in line:
			newLines.append(line)

	return newLines


'''
os splits a seguir fazem
android:name="android.permission.ACCESS_WIFI_STATE" />
virar -> android.permission.ACCESS_WIFI_STATE" />
virar -> ACCESS_WIFI_STATE"
virar -> ACCESS_WIFI_STATE


Salvamos as permissoes em um dicionario, evitando repetições, e retornamos como uma lista
'''
def GetPermissions(lines):
	dic = {}

	for line in lines:
		perm = line.split('.')[-1]#ACCESS_WIFI_STATE" />
		perm = perm.split()[0] #ACCESS_WIFI_STATE"
		perm = perm[:-1] #ACCESS_WIFI_STATE
		if perm not in dic:
			dic[perm] = 1

	return list(dic.keys())



def ListPermissions(results):
	for i in range(0, len(results)):
		print(results[i][0] + ': [', end='')
		for j in range(1, len(results[i])-1):
			print(results[i][j]+', ', end='')
		print(results[i][-1] + ']', end='\n\n')

def Get_Unique_Common(results):
	print('------------\n\n' + 'Permissões Únicas:\n\n' + '------------\n')

	dic = {}

	for i in range(0, len(results)):
		for j in range(1, len(results[i])):
			perm = results[i][j]
			if results[i][j] not in dic:
				dic[perm] = 1
			else:
				dic[perm] += 1

	#uniques
	for i in range(0, len(results)):
		print(results[i][0] + ': [', end='')
		for j in range(1, len(results[i])):
			perm = results[i][j]

			if(dic[perm] == 1):
				print(perm +', ', end='')

		print(']', end='\n')

	print()


	print('------------\n\n' + 'Permissões Comuns a Todos:\n\n' + '------------\n')

	for key, val in dic.items():
		if dic[key] == len(results):
			print('[' + key + ']')

	print()

if __name__ == "__main__":
	files, lines = [], []
	results = []


	files = FindFiles(sys.argv[1])
	
	for file in files:
		lines = ReadFile(sys.argv[1], file) # -> lemos o arquivo
		lines = FilterLines(lines) #-> salvamos so as linhas com "permission"
		results.append([file]+GetPermissions(lines)) #salvamos somente as chaves sem repetição
	

	if(int(sys.argv[2]) == 1):
		ListPermissions(results)
	else:
		Get_Unique_Common(results)

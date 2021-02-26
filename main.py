import os
import shutil

pasta_principal = r'D:\Python\Copiar arquivos'
pasta_saida = r'D:\Python\Copiar arquivos\resultado'
arquivos = open(r'D:\Python\Copiar arquivos\arquivos.txt', 'r')

try:
    os.mkdir(pasta_saida)
except FileExistsError as e:
    print(f'Pasta {pasta_saida} ja existe.')


for arquivo in arquivos.readlines():
    nome_xml = arquivo[1:-1]

    

    for root, dirs, files in os.walk(pasta_principal):
        for file in files:
            pasta_arquivo_original = os.path.join(root, file)
            pasta_arquivo_saida = os.path.join(pasta_saida, file)




            if nome_xml in file:
                shutil.copy(pasta_arquivo_original, pasta_arquivo_saida)
                print(nome_xml + ' copiado')


arquivos.close()
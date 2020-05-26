from sklearn import tree;

skin=1;
nonSkin=2;

# Lendo o Dataset
# link do dataset: https://archive.ics.uci.edu/ml/datasets/Skin+Segmentation#
arquivo = open('Skin_NonSkin.txt', 'r');

entradas_test=[]
resultado=[]


for line in arquivo:
    lineSplited = line.split()
    # Entradas de treinamento:
    B = int(lineSplited[0]);
    G = int(lineSplited[1]);
    R = int(lineSplited[2]);
    entradas_test.append([R,G,B]);
    # Saídas de treinamento:
    skin_nonSkin = int(lineSplited[3]);
    resultado.append(skin_nonSkin);

# Fechando o arquivo de leitura
arquivo.close();

# print(entradas_test)

# Padrões de classificação
clf=tree.DecisionTreeClassifier();
clf=clf.fit(entradas_test, resultado);

# Input dos dados para predição
R_input = input("Entre o valor (R)ed: ");
G_input = input("Entre o valor (G)ren: ");
B_input = input("Entre o valor (B)lue: ");

# Resultado da predução da entrada do usuário
resultadoUsuario = clf.predict([[R_input, G_input, B_input]])

#Resultado
if resultadoUsuario == skin:
    print("É uma tonalidade de cor de pele real")
else:
    print("Não é uma tonalidade de cor de pele real")
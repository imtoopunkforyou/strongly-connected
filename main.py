# -*- coding: utf-8 -*-
import networkx as nx #библиотека для посторения графа, а так же для использования алгоритма Косараджу
import matplotlib.pyplot as plt # библиотека, позволяющая отрисовать графы


def create_graph(): #функция для считывания графа с текстового файла
    result = [] # массив, который вернёт функция
    graph_text = open("graph_text.txt", "r") #открываем файл на чтение как graph_text
    while True: # цикл для построчного перебора файла
        temp = [] #временный массив, в нём храним текущую строчку
        line = graph_text.readline() #считываем строку, заносим в переменную line
        if not line: #если line нет, прекращаем считывание
            break
        for letter in line: #для каждой буквы в строчке
            temp.append(letter) # добавить в массив temp
        temp.pop() #убрать последний элемент (перенос строки)
        temp.append(1) #добавляем вес ребра, без указания веса алгоритм Косарджу не работает
        result.append(tuple(temp)) #Добавляем в конечный массив кортеж вида (вершина, вершина, вес ребра между ними). Например (A,B,1).
    graph_text.close() # закрываем файл graph_text.txt
    return result 


Graph = nx.MultiDiGraph() #создаём экземпляр класса MultiDiGraph. если буквально, то создаём пустой граф без вершин и без ребер
Graph.add_weighted_edges_from(create_graph()) #вводим полученные нами данные из текстрового файла в наш граф
nx.draw(Graph, with_labels=True, font_weight='bold') #рисуем граф
plt.savefig('graph_pic.png') #сохраняем граф
strongly_connected_component = sorted(nx.kosaraju_strongly_connected_components(Graph), key=len) #Разложение графа на максимально сильно связные подграфы при помощи алгоритма Косараджу


print("В вашем графе " + str(len(strongly_connected_component)) + " максимально сильно связных подграфа. \n\nСвязи: ")
print(strongly_connected_component)

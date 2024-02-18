# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 5 - Zadatak 2

Napišite program u kojem se za usmjereni graf ispituje broj komponenti u grafu, te
veličina najveće komponente. Za testiranje za vrijeme izrade programa možete k
oristiti datoteku football .net, koji možete slobodno modificirati, ili neku manju 
koji sami napravite.

Nakon toga testirajte program za dataset EVA. Dataset EVA je velika mreža telekom i
medijskih kompanija ekstrahirana iz godišnjeg izvještaja U.S. Securities and Exchange
Commission (SEC) u kojoj čvorovi predstavljaju kompanije, a veze vlasništvo jedne
kompanije nad drugom. Mreža ima 8343 čvorova i 6726 veza.
Ispišite prvih deset kompanija i za svaku broj kompanija koje posjeduje.

@author: Anamarija Papic
"""

from papic_anamarija_05_00 import read_parse_pajek

def dfs(graph, start, visited):
    component = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            component.append(node)
            stack.extend(graph.vertices.get(node, []))
    
    return component

def find_components(graph):
    visited = set()
    components = []
    
    for node in graph.vertices:
        if node not in visited:
            component = dfs(graph, node, visited)
            components.append(component)
    
    return components

def largest_component_size(graph):
    components = find_components(graph)
    
    if not components:
        return 0
    
    return max(len(component) for component in components)

def main():
    # g1 = read_parse_pajek('resources/football.net')
    
    # components = find_components(g1)
    # largest_component_size_value = largest_component_size(g1)
    
    # print(f"Number of components: {len(components)}")
    # print(f"Size of the largest component: {largest_component_size_value}")
    
    g2 = read_parse_pajek('resources/eva.net')
    
    components = find_components(g2)
    largest_component_size_value = largest_component_size(g2)
    
    print(f'Number of components: {len(components)}')
    print(f'Size of the largest component: {largest_component_size_value}')
    
    print('First 10 companies:')
    for node in list(g2.vertices.keys())[:10]:
        neighbors = g2.vertices.get(node, [])
        print(f'Company {node} - {g2.vertices[node]}: Number of companies it owns - {len(neighbors)}')

if __name__ == '__main__':
    main()

# Grafo representando o mapa da Romênia
mapa_romenia = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

heuristica_bucareste = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
    'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
    'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
    'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

def busca_a_estrela(inicio, objetivo, grafo, heuristica):
    g_inicial = 0
    f_inicial = g_inicial + heuristica[inicio]
    
    fronteira = [(f_inicial, g_inicial, inicio, [inicio])]
    visitados = set()
    passo = 1
    
    print(f" INICIANDO BUSCA A* (A-Star Search)")
    print(f" Origem: {inicio} -> Destino: {objetivo}\n")
    
    while fronteira:
        fronteira.sort(key=lambda x: x[0])
        
        print(f"--- PASSO {passo} ---")
        print("Estado da Fronteira (Ordenada por menor f(n) = g + h):")
        for f, g, cid, cam in fronteira:
            print(f"  > {cid} [f = {f} | g = {g}, h = {f-g}] | Caminho: {' -> '.join(cam)}")
        
        f_atual, g_atual, cidade_atual, caminho = fronteira.pop(0)
        
        print(f"\n[ESCOLHA] Selecionada para expansão: {cidade_atual} (f = {f_atual})")
        
        if cidade_atual == objetivo:
            print(f"\n✓ OBJETIVO ENCONTRADO! Chegamos a {objetivo}.")
            return caminho
            
        if cidade_atual not in visitados:
            visitados.add(cidade_atual)
            
            for vizinho, custo_estrada in grafo.get(cidade_atual, []):
                if vizinho not in visitados:
                    novo_g = g_atual + custo_estrada
                    novo_f = novo_g + heuristica[vizinho]
                    
                    novo_caminho = caminho + [vizinho]
                    fronteira.append((novo_f, novo_g, vizinho, novo_caminho))
                    
        print("-" * 60 + "\n")
        passo += 1
                    
    return None

caminho_final = busca_a_estrela('Arad', 'Bucharest', mapa_romenia, heuristica_bucareste)

print(" RESULTADO FINAL")
if caminho_final:
    print(f"Caminho ideal pela Busca A*:\n{' -> '.join(caminho_final)}")
else:
    print("Não foi possível encontrar um caminho.")

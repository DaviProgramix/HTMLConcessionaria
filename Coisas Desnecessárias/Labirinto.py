from pyamaze import maze, agent, textLabel

labirinto = maze(10, 10)

labirinto.CreateMaze(loadMaze="lab.csv")

#celulas = labirinto.grid
#print(celulas)

#mapa = labirinto.maze_map
#print(mapa)

#caminho = labirinto.path
#print(caminho)

agente = agent(labirinto, footprints=True, filled=True)
caminho = ""
labirinto.tracePath({agente: caminho}, delay=200)
#posicao = agente.position

texto = textLabel(labirinto, title="Nº Passos", value=len(caminho))

labirinto.run()
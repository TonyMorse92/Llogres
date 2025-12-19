class Graph:
	def __init__(self, edges=[], verticies=[]):
		if len(edges) == 0:
			pass
		else:
			verticies = [edge[0] for edge in edges]
		verticies = set(verticies)
		

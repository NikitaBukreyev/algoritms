import beehive
import generator


workerBees = 60
scoutBees = 5
task = 300
maxConnections = 50

adjMatrix = generator.generate(task, maxConnections)


	


beehive = beehive.beehive(adjMatrix, workerBees, scoutBees)
coloredVertices = beehive.paint()

with open("result.txt", "w") as file:
	for i in range(len(coloredVertices)):
		file.write(f"Vertice {i} -> color #{coloredVertices[i]}\n")
	file.write(f"\nTotal colores used: {max(coloredVertices)}")

print(f"Total colores used: {max(coloredVertices)}")
print("Task completed! Check the result.txt file")
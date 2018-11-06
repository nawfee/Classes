
import matplotlib.pyplot
import agentframework

a = agentframework.Agent(1,2)
print(a)
print(a.y)
print(a.x)
a.x = 4
print(a.x)
a.hi()


def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(1,2))

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        agents[i].move()
            


matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

max_distance = 0
for i in range(0, num_of_agents):
    for j in range(i, num_of_agents):
        distance = distance_between(agents[i], agents[j])
        if (distance > max_distance):
            max_distance = distance
print("max_distance", max_distance)


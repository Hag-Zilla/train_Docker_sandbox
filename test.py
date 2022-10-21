from docker import DockerClient

client = DockerClient()
print("coucou")
client.containers.run(image='datascientest/neo4j:latest',
                      name='my_neo4j',
                      detach=True,
                      auto_remove=True,
                      ports={
                          '7474/tcp': 7474,
                           '7687/tcp':7687},
                      network='bridge'
                    )

# printing names of active containers
for c in client.containers.list():
    print(c.name, c.image)

print(len(client.containers.list()))
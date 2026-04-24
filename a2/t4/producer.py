import pulsar

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('input-topic')

INPUT_STRING = "I want to be capatilized"
words = INPUT_STRING.split()

for word in words:
    producer.send(word.encode('utf-8'))
    print(f"Sent: {word}")

client.close()
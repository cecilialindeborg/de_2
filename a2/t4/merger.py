import pulsar

client = pulsar.Client('pulsar://localhost:6650')

consumer = client.subscribe(
    'output-topic',
    subscription_name='agg-sub'
)

results = []


expected_words = 5

while len(results) < expected_words:
    message = consumer.receive()
    word = message.data().decode('utf-8')

    results.append(word)
    print(f"Received: {word}")

    consumer.acknowledge(message)

final_string = " ".join(results)
print("\nFinal result:", final_string)

client.close()
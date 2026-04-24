import pulsar

client = pulsar.Client('pulsar://localhost:6650')

consumer = client.subscribe(
    'output-topic',
    subscription_name='agg-sub'
)

results = []

while True:
    message = consumer.receive()
    word = message.data()

    if word == "__END__":
        consumer.acknowledge(message)
        break

    results.append(word)
    print(f"Received: {word}")

    consumer.acknowledge(message)

final_string = " ".join(results)
print("\nFinal merged string:", final_string)

client.close()
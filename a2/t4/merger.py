import pulsar

client = pulsar.Client('pulsar://localhost:6650')

consumer = client.subscribe(
    'output-topic',
    subscription_name='agg-sub'
)

results = []

while True:
    msg = consumer.receive()
    word = msg.data().decode('utf-8')

    if word == "__END__":
        consumer.acknowledge(msg)
        break

    results.append(word)
    print(f"Received: {word}")

    consumer.acknowledge(msg)

final_string = " ".join(results)
print("\nFinal merged string:", final_string)

client.close()
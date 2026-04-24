import pulsar

client = pulsar.Client('pulsar://localhost:6650')

consumer = client.subscribe(
    'input-topic', subscription_name='worker-sub', consumer_type=pulsar.ConsumerType.Shared)
producer = client.create_producer('output-topic')

print("Worker running...")

while True:

    message = consumer.receive()
    word = message.data()

    if word == "__END__":
        producer.send(message.data())
        consumer.acknowledge(message)
        continue

    processed = word.upper()

    producer.send(processed)
    print(f"Processed: {word} -> {processed}")

    consumer.acknowledge(message)
import pulsar

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('input-topic')

# INPUT_STRING = "I want to be capatilized"
INPUT_STRING = "Curabitur tempus lorem sed ipsum tempus pretium. Morbi at nulla scelerisque, lobortis velit id, vehicula augue. Duis pellentesque, lacus sed tincidunt ullamcorper, dui lectus facilisis magna, at porttitor ex nunc nec elit. Sed nunc enim, elementum vel viverra in, eleifend a enim. Nulla vitae felis vitae nisl blandit blandit. Nunc facilisis felis ut volutpat feugiat. Sed non pharetra arcu. Donec sed quam ante. Maecenas leo magna, posuere a velit sed, congue lacinia massa. Donec sed lobortis libero, non gravida quam. Curabitur elementum ante et ante vestibulum, ut euismod quam lacinia. Sed sagittis, erat non vehicula posuere, ipsum arcu rhoncus massa, eget egestas justo ipsum cursus tortor. Fusce viverra scelerisque orci, in pretium lorem convallis quis. In sed risus eget odio placerat viverra ac non ex. Curabitur suscipit tellus purus, a faucibus est mollis vitae. Vestibulum magna nisi, efficitur vel nibh sed, tincidunt pretium lacus."
words = INPUT_STRING.split()

for word in words:
    producer.send(word.encode('utf-8'))
    print(f"Sent: {word}")

client.close()
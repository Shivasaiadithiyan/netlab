class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Observer:
    def update(self, subject):
        pass


class StarTopology(Subject):
    def __init__(self):
        super().__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()

class NodeA(Observer):
    def update(self, subject):
        if isinstance(subject, StarTopology):
            print("Node A received state:", subject.state)

class NodeB(Observer):
    def update(self, subject):
        if isinstance(subject, StarTopology):
            print("Node B received state:", subject.state)

class NodeC(Observer):
    def update(self, subject):
        if isinstance(subject, StarTopology):
            print("Node C received state:", subject.state)


if __name__ == '__main__':
    star_topology = StarTopology()

    node_a = NodeA()
    node_b = NodeB()
    node_c = NodeC()

    star_topology.attach(node_a)
    star_topology.attach(node_b)
    star_topology.attach(node_c)

    star_topology.state = "ON"
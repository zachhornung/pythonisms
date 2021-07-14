from pythonisms.pythonisms import LinkedList

def test_imports():
    assert LinkedList
    
def test_linked_iterable():
    ll = LinkedList()
    animals = ['goats', 'babies', 'unicorns']
    [ll.insert(animal) for animal in animals]
    actual = [animal for animal in ll]
    assert actual == list(reversed(animals))
    


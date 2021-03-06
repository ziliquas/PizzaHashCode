from typing import List

class Cell:
    def __init__(self, character):
        self.type = character
        self.explored = False

    def explore(self):
        self.explored = True

class PizzaMatrix:
    def __init__(self, matrix):
        self.matrix = list(map(lambda pizzaRow : list(map(lambda pizzaCell: Cell(pizzaCell), pizzaRow)), matrix))

    def __getitem__(self, index):
        return self.matrix[index]

    def areAllExplored(self):
        for pizzaRow in self.matrix:
            for cell in pizzaRow:
                if cell.explored == False:
                    return False
        return True

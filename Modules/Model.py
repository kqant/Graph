
"""
Описание:
        Модуль модели (Model) предоставляет данные и реагирует
        на команды контроллера (Controller), изменяя своё состояние
Классы:
        GraphModel              класс модели (Model)
            Поля:
                graph: Graph    экземпляр класса Graph
                functions: dict словарь функций из модуля Render структуры:
                                funName: fun где
                                funName - название функции 'str'
                                fun - функция 'function'
            Методы:
                __init__        инициализация класса
"""



from .Graph import Graph
from .Render import *


class GraphModel():
    def __init__(self):
        self.graph = Graph()
        self.functions = {
            drawDefault.__name__: drawDefault,
            drawColoring.__name__: drawColoring,
            drawMinPath.__name__: drawMinPath
        }


# pdf, txt, excel

from abc import ABC, abstractmethod

class Document(ABC):

  @abstractmethod
  def load(self): pass

  @abstractmethod
  def view(self): pass

  @abstractmethod
  def format(self): pass

  @abstractmethod
  def calculate(self): pass

class PDF(Document):
  def load(self):
    print('load in pdf')

  def view(self):
    print('view informations')

  def calculate(self):
    print('No use')

  def format(self):
    print('No use')

document1 = PDF()
'''
Problem Statement: Cross-Platform UI Toolkit
You are building a UI toolkit that supports multiple platforms — say Windows, MacOS, and Linux.

Each platform supports the following UI elements:

Button

Checkbox

The client code should be able to render buttons and checkboxes without hardcoding platform-specific implementations
'''
from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):pass

class CheckBox(ABC):
    @abstractmethod
    def render(self):pass

class WindowsButton(Button):
    def render(self):
        print("Windows Button")

class MacButton(Button):
    def render(self):
        print("Mac Button")

class WindowsCheckBox(CheckBox):
    def render(self):
        print("Windows Checkbox")

class MacCheckBox(CheckBox):
    def render(self):
        print("Mac Checkbox")


class AbstractFactory(ABC):
    def create_Button(self)->Button:
        pass
    def create_Checkbox(self)->CheckBox:
        pass

class WindowsElementFactory(AbstractFactory):
    def create_Button(self):
        return WindowsButton()
    def create_Checkbox(self):
        return WindowsCheckBox()
    
class MacElementFactory(AbstractFactory):
    def create_Button(self):
        return MacButton()
    def create_Checkbox(self):
        return MacCheckBox()
    
class Client:
    @staticmethod
    def create_elements(factory:AbstractFactory):
        button = factory.create_Button()
        checkbox = factory.create_Checkbox()
        button.render()
        checkbox.render()

factory = WindowsElementFactory()
Client.create_elements(factory)


from abc import ABC, abstractmethod

class IBatchJob(ABC):
    @abstractmethod
    def Handle(self):
        pass
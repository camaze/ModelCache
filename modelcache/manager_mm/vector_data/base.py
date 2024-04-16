# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import numpy as np
from typing import List
from dataclasses import dataclass


@dataclass
class VectorData:
    id: int
    data: np.ndarray


class VectorBase(ABC):
    """VectorBase: base vector store interface"""

    @abstractmethod
    def mul_add(self, datas: List[VectorData], model=None):
        pass

    @abstractmethod
    def search(self, data: np.ndarray, top_k: int, model):
        pass

    @abstractmethod
    def rebuild(self, ids=None) -> bool:
        pass

    @abstractmethod
    def delete(self, ids) -> bool:
        pass

    @abstractmethod
    def rebuild_col(self, model):
        pass

    def flush(self):
        pass

    def close(self):
        pass

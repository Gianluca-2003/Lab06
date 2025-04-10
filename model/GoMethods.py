from dataclasses import dataclass


@dataclass
class GoMethods:
    order_method_code: int
    order_method_type: str

    def __eq__(self, other):
        return self.order_method_code == other.order_method_code


    def __hash__(self):
        return hash(self.order_method_code)


    def __str__(self):
        return f"{self.order_method_type}-{self.order_method_code}"
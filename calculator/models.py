class Model:
    # initially input_str variable will have "" value
    def __init__(self):
        self.input_str: str = ""

    # when the method data will be called like => Model.data or print(Model.data) => it will actaully call this method
    @property
    def data(self) -> str:
        return self.input_str

    # when the method data will be called like => Model.data = "some value assignment" => it will actaully call this setter method
    @data.setter
    def data(self, value) -> None:
        self.input_str = value
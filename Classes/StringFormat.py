class StringFormat:
    def __init__(self, input_str):
        self.in_str = input_str

    def number_format(self):
        return "".join(self.in_str.replace(',', '.').split()).replace('%','')
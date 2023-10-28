class StringFormat:
    """Класс для введенной строки
    Атрибуты класса:
    in_str - строка, которую необходимо отформатировать
    """
    def __init__(self, input_str):
        self.in_str = input_str

    def number_format(self):
        """
        Строку необходимо отформатировать следующим образом: Убрать все пробелы, заменить , на ., уюрать %
        :return: Отформатированная строка
        """
        return "".join(self.in_str.replace(',', '.').split()).replace('%','')
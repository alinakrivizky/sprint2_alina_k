
import task1.Case as case_module
Case = case_module.Case

class ExtendedClass(Case):
    def __init__(self, test_case_id, name, step_description, expected_result, precondition, environment):
        self.precondition = precondition
        self.environment = environment
        super().__init__(test_case_id, name, step_description, expected_result)
    def print_test_case_info(self):
        super().print_test_case_info()
        print(f"\nПредусловиe: {self.precondition}")
        print(f"\nОкружение: {self.environment}")

case = ExtendedClass(
    '1',
    'Наличие кнопки Принять',
    '1. Открыть вкладку приёма документов 2. Проверить наличие кнопки ',
    'Кнопка доступна',
    'Открыть сервис',
    'Яндекс Браузер'
)
case.print_test_case_info()
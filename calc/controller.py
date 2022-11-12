# контроллер работает с моделью, поэтому импортируем model и view, обеспечивая связь
import model_sub as model
import view

# кнопка

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)    # инициализация начальных значений, которые приходят из view
    result = model.do_it()
    view.view_data(result, "result")
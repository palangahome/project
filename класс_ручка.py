class Pencil:

    def __init__(self, color="серый"):
        self.color = color

    def draw_picture(self):
        return f"Нарисован рисунок цветом '{self.color}'."


class Pen(Pencil):

    def __init__(self, color, pen_type):
        super().__init__(color=color)
        self.pen_type = pen_type

    def sign_document(self):
        if self.color not in ("синий", "чёрный", "фиолетовый"):
            return f"Ручкой цвета '{self.color}' нельзя подписать документ."
        elif self.pen_type == "гелевая":
            return f"Ручкой типа '{self.pen_type}' нельзя подписать документ."
        return f"Подписан документ."


blue_ball_pen = Pen(color="синий", pen_type="шариковая")
print(blue_ball_pen.draw_picture())
print(blue_ball_pen.sign_document())
blue_gel_pen = Pen(color="синий", pen_type="гелевая")
print(blue_gel_pen.draw_picture())
print(blue_gel_pen.sign_document())
import tkinter as tk
import random

class CatchBallGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Поймай шарик")
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.score = 0
        self.speed = 3
        self.ball_radius = 20

        self.ball = self.canvas.create_oval(0, 0, self.ball_radius*2, self.ball_radius*2, fill="red")
        self.ball_dx = random.choice([-1, 1]) * self.speed
        self.ball_dy = random.choice([-1, 1]) * self.speed

        self.score_text = self.canvas.create_text(10, 10, anchor="nw", font=("Arial", 16), text=f"Очки: {self.score}")

        self.canvas.bind("<Button-1>", self.check_click)
        self.move_ball()

    def move_ball(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        x1, y1, x2, y2 = self.canvas.coords(self.ball)

        # Отскок от краёв
        if x1 <= 0 or x2 >= 600:
            self.ball_dx = -self.ball_dx
        if y1 <= 0 or y2 >= 400:
            self.ball_dy = -self.ball_dy

        self.root.after(20, self.move_ball)

    def check_click(self, event):
        x, y = event.x, event.y
        ball_coords = self.canvas.coords(self.ball)
        bx1, by1, bx2, by2 = ball_coords

        # Проверка попадания по шарику
        if bx1 <= x <= bx2 and by1 <= y <= by2:
            self.score += 1
            self.canvas.itemconfig(self.score_text, text=f"Очки: {self.score}")
            self.increase_speed()
            self.move_ball_to_random_position()

    def move_ball_to_random_position(self):
        x = random.randint(0, 600 - self.ball_radius*2)
        y = random.randint(0, 400 - self.ball_radius*2)
        self.canvas.coords(self.ball, x, y, x + self.ball_radius*2, y + self.ball_radius*2)

    def increase_speed(self):
        # Увеличиваем скорость каждые 5 очков
        if self.score % 5 == 0:
            self.speed += 1
            self.ball_dx = random.choice([-1, 1]) * self.speed
            self.ball_dy = random.choice([-1, 1]) * self.speed

if __name__ == "__main__":
    root = tk.Tk()
    game = CatchBallGame(root)
    root.mainloop()

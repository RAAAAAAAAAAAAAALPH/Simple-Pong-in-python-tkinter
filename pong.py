import tkinter as tk
import random

class Pong:
    def __init__(self, master):
        self.master = master
        self.master.title("Pong")
        self.canvas = tk.Canvas(master, width=500, height=300, bg="black")
        self.canvas.pack()
        self.ball = self.canvas.create_oval(245, 145, 255, 155, fill="white")
        self.paddle1 = self.canvas.create_rectangle(20, 125, 30, 175, fill="white")
        self.paddle2 = self.canvas.create_rectangle(470, 125, 480, 175, fill="white")
        self.score1 = 0
        self.score2 = 0
        self.label = self.canvas.create_text(250, 30, text=f"{self.score1} - {self.score2}", fill="white", font=("Arial", 20))
        self.canvas.bind("<KeyPress>", self.key_press)
        self.canvas.focus_set()
        self.ball_speed_x = random.choice([-2, 2])
        self.ball_speed_y = random.choice([-2, 2])
        self.move()

    def move(self):
        self.canvas.move(self.ball, self.ball_speed_x, self.ball_speed_y)
        ball_pos = self.canvas.coords(self.ball)
        paddle1_pos = self.canvas.coords(self.paddle1)
        paddle2_pos = self.canvas.coords(self.paddle2)
        
        if ball_pos[1] <= 0 or ball_pos[3] >= 300:
            self.ball_speed_y *= -1

        if ball_pos[0] <= 0:
            self.score2 += 1
            self.canvas.itemconfig(self.label, text=f"{self.score1} - {self.score2}")
            self.reset_ball()

        if ball_pos[2] >= 500:
            self.score1 += 1
            self.canvas.itemconfig(self.label, text=f"{self.score1} - {self.score2}")
            self.reset_ball()

        if ball_pos[0] <= paddle1_pos[2] and ball_pos[1] >= paddle1_pos[1] and ball_pos[3] <= paddle1_pos[3]:
            self.ball_speed_x *= -1

        if ball_pos[2] >= paddle2_pos[0] and ball_pos[1] >= paddle2_pos[1] and ball_pos[3] <= paddle2_pos[3]:
            self.ball_speed_x *= -1

        self.master.after(10, self.move)

    def key_press(self, event):
        if event.char == "s":
            self.canvas.move(self.paddle1, 0, -20)
        elif event.char == "w":
            self.canvas.move(self.paddle1, 0, 20)
        elif event.char == "i":
            self.canvas.move(self.paddle2, 0, -20)
        elif event.char == "k":
            self.canvas.move(self.paddle2, 0, 20)

    def reset_ball(self):
        self.canvas.coords(self.ball, 245, 145, 255, 155)
        self.ball_speed_x = random.choice([-2, 2])
        self.ball_speed_y = random.choice([-2, 2])


root = tk.Tk()
pong_game = Pong(root)
root.mainloop()

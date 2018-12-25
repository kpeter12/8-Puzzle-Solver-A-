import tkinter
from Board import Board


class Gui:
    def __init__(self):
        self.board = Board([0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.text_font = "Laksaman 18"
        self.background_color = "#FEFCFB"
        self.rectangle_color = "#FEFCFB"
        self.line_color = "#0A1128"
        self.text_color = "0A1128"
        self.window = tkinter.Tk()
        self.window.title("Specify Board Settings")
        self.window.configure(background=self.background_color)
        self.shuffles = 100
        self.start_board = [tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar(),
                            tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar(),
                            tkinter.StringVar()]
        self.int_start_board = []

        # beginning label
        tkinter.Label(self.window, text="8 BOARD", font=self.text_font, bg=self.rectangle_color, borderwidth=2, relief="groove").grid(row=0, columnspan=3, pady=5)  # this is placed in 1 0
        # the 9 text fields for the board
        tkinter.Entry(self.window, textvariable=self.start_board[0], justify=tkinter.CENTER, bg=self.rectangle_color).grid(row=1, column=0, pady=5)
        tkinter.Entry(self.window, textvariable=self.start_board[1], justify=tkinter.CENTER, bg=self.rectangle_color).grid(row=1, column=1, pady=5)
        tkinter.Entry(self.window, textvariable=self.start_board[2], justify=tkinter.CENTER, bg=self.rectangle_color).grid(row=1, column=2, pady=5)

        tkinter.Entry(self.window, textvariable=self.start_board[3], justify=tkinter.CENTER, bg=self.rectangle_color).grid(row=2, column=0, pady=5)
        tkinter.Entry(self.window, textvariable=self.start_board[4], justify=tkinter.CENTER, bg=self.rectangle_color).grid(row=2, column=1, pady=5)
        tkinter.Entry(self.window, textvariable=self.start_board[5], justify=tkinter.CENTER, bg=self.rectangle_color).grid(row=2, column=2, pady=5)

        tkinter.Entry(self.window, textvariable=self.start_board[6], justify=tkinter.CENTER, bg=self.rectangle_color).grid(row=3, column=0, pady=5)
        tkinter.Entry(self.window, textvariable=self.start_board[7], justify=tkinter.CENTER, bg=self.rectangle_color).grid(row=3, column=1, pady=5)
        tkinter.Entry(self.window, textvariable=self.start_board[8], justify=tkinter.CENTER, bg=self.rectangle_color).grid(row=3, column=2, pady=5)

        # shuffle and submit buttons
        tkinter.Button(self.window, text="SHUFFLE", command=self.shuffle_board, bg=self.background_color,
                       font=self.text_font, width=15, pady=10, borderwidth=2, relief="groove").grid(row=4, columnspan=3, pady=5)
        tkinter.Button(self.window, text="SOLVE", command=self.set_board, bg=self.background_color,
                       font=self.text_font, width=15, pady=10, borderwidth=2, relief="groove").grid(row=5, columnspan=3, pady=5)
        self.window.mainloop()

    def shuffle_board(self):
        Board.shuffle_board(self.board, self.shuffles)
        print(self.board)
        for i in range(0, 9):
            self.start_board[i].set(self.board.board_list[i])

    def set_board(self):
        board = []
        for item in self.start_board:
            board.append(int(item.get()))
        self.int_start_board = board.copy()
        self.window.destroy()

    def get_board(self):
        return self.int_start_board

import tkinter


class Graphics2:
    def __init__(self, start_board_list):
        self.board_list = start_board_list.copy()
        # make 0 be a blank string
        for i in range(0, len(self.board_list)):
            if self.board_list[i] == 0:
                self.board_list[i] = ""

        # set variables
        self.text_font = "Laksaman 18"
        self.background_color = "#FEFCFB"
        self.rectangle_color = "#FEFCFB"
        self.line_color = "#0A1128"
        self.text_color = "#0A1128"

        self.total_width = 600
        self.total_height = 600
        self.board_width = 500
        self.board_height = 500

        # initialize canvas
        self.window = tkinter.Tk()
        self.window.configure(background=self.background_color)
        self.canvas = tkinter.Canvas(self.window, width=self.total_width, height=self.total_height, bg=self.background_color)
        self.canvas.pack()
        self.draw_board(self.board_list, 10, 10, self.board_width, self.board_height)

    def draw_board(self, board_list, x, y, width, height):
        self.canvas.create_rectangle(x, y, x + width, y + height, fill=self.rectangle_color)
        self.canvas.create_line(x + (width / 3), y, x + (width / 3), y + height, fill=self.line_color)
        self.canvas.create_line(x + (width / 3 * 2), y, x + (width / 3 * 2), y + height, fill=self.line_color)
        self.canvas.create_line(x, y + (height / 3), x + width, y + (height / 3), fill=self.line_color)
        self.canvas.create_line(x, y + (height / 3 * 2), x + width, y + (height / 3 * 2), fill=self.line_color)
        self.canvas.create_text(x + (width / 6), y + (width / 6), text=board_list[0], font=self.text_font, fill=self.text_color)
        self.canvas.create_text(x + (width / 2), y + (width / 6), text=board_list[1], font=self.text_font, fill=self.text_color)
        self.canvas.create_text(x + (width / 6 * 5), y + (width / 6), text=board_list[2], font=self.text_font, fill=self.text_color)
        self.canvas.create_text(x + (width / 6), y + (width / 2), text=board_list[3], font=self.text_font,fill=self.text_color)
        self.canvas.create_text(x + (width / 2), y + (width / 2), text=board_list[4], font=self.text_font,fill=self.text_color)
        self.canvas.create_text(x + (width / 6 * 5), y + (width / 2), text=board_list[5], font=self.text_font,fill=self.text_color)
        self.canvas.create_text(x + (width / 6), y + (width / 6 * 5), text=board_list[6], font=self.text_font,fill=self.text_color)
        self.canvas.create_text(x + (width / 2), y + (width / 6 * 5), text=board_list[7], font=self.text_font,fill=self.text_color)
        self.canvas.create_text(x + (width / 6 * 5), y + (width / 6 * 5), text=board_list[8], font=self.text_font,fill=self.text_color)

    def update_main_board(self, board_list):
        self.canvas.delete("all")
        self.board_list = board_list.copy()
        # make 0 be a blank string
        for i in range(0, len(self.board_list)):
            if self.board_list[i] == 0:
                self.board_list[i] = ""
        self.draw_board(self.board_list, 50, 50, 500, 500)
        self.window.update()

    def show_solution(self, path_to_solution):
        boxes_per_row = 7
        padding = 10
        w = self.total_width / boxes_per_row - padding
        h = self.total_height / boxes_per_row - padding
        padding = 10
        self.canvas.delete("all")
        print("length", len(path_to_solution))
        rows = 0
        count = 0

        for item, i in zip(path_to_solution, range(0, len(path_to_solution))):
            for j in range(0, len(self.board_list)):
                if item.board.board_list[j] == 0:
                    item.board.board_list[j] = ""
            self.draw_board(item.board.board_list, (count * padding + padding) + (count * w), (rows * padding + padding) + (rows * h), w, h)
            count += 1
            if count > boxes_per_row - 1:
                rows += 1
                count = 0

        self.window.mainloop()

from game import Game
from snake import Snake
from game_display import GameDisplay


def __draw_object(object_location, color, gd):
    """
    this function draws a single object on the board in the specified color
    :param object_location: a list containg all of the cells the object is in
    :param color: a string that specifies the cells the object is to be drawn in
    :param gd: a GameDisplay object for the game_display class
    :return: None
    """
    for i in range(len(object_location)):
        gd.draw_cell(*object_location[i], color)


def draw_game(game, gd, last_round=False):
    """
    this functions draws all of objects of the game on the board
    :param game: a game object containing the game that is to be drawn on the board
    :param gd: a GameDisplay object for the game_display class
    :return: None
    """
    __draw_object(game.snake_location(), "black", gd)
    bomb_color = "red"
    if game.bomb.time == 0:
        bomb_color = "orange"
    __draw_object(game.bomb_location(), bomb_color, gd)
    __draw_object(game.apples_location(), "green", gd)



def main_loop(gd: GameDisplay) -> None:
    """
    this function manages the snake game object
    :param gd: a GameDisplay type object
    :return: None
    """
    game_over = False
    cur_rounds_to_grow = 0
    x, y = 10, 10
    showed_score = 0
    gd.show_score(showed_score)
    game = Game(Snake(3, (x, y), "Up"))
    draw_game(game, gd)
    gd.end_round()
    while not game_over:
        does_grow = False
        if cur_rounds_to_grow > 0:
            does_grow = True
            cur_rounds_to_grow -= 1
        key_clicked = gd.get_key_clicked()
        game_over = game.single_round(key_clicked, does_grow)
        gd.show_score(game.current_score())
        if game.current_score() > showed_score:
            cur_rounds_to_grow += 3
        showed_score = game.current_score()
        draw_game(game, gd)
        gd.end_round()


if __name__ == "__main__":
    gd = GameDisplay()
    main_loop(gd)

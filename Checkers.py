# importing
import sys
import CheckersPieces
import CheckersBoard
import pygame
import Gameplay


# 2 Player Checkers
# Jason Lin, 2023

def main():
    """
    Main function that handles game process
    """

    # initialize pygame
    pygame.init()

    # renaming the window/icon
    pygame.display.set_caption("2-Player Checkers")
    icon = pygame.image.load('elements/checkers_icon.png')
    pygame.display.set_icon(icon)

    # responsible for game load-up and gameplay
    CheckersBoard.main()
    CheckersPieces.main()
    Gameplay.main()

    # quit
    pygame.quit()
    sys.exit()


main()

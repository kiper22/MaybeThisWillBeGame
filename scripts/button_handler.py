from constants import *


class ButtonHandler:
    @staticmethod
    def generate_frame(screen, text, font, pos, is_button=False):
        '''Used to generate buttons with frame in game menu'''
        text = font.render(text, True, MENU_TITLE_FONT_COLOR)
        text_width, text_height = text.get_size()
        frame_width = text_width * 0.9
        frame_height = text_height * 1.5
        
        frame_middle = pygame.image.load("assets/buttons/Frame_Middle.png").convert_alpha()
        frame_middle = pygame.transform.scale(frame_middle, (int(frame_width), int(frame_height)))
        frame_left = pygame.image.load("assets/buttons/Frame_Left.png").convert_alpha()
        frame_left = pygame.transform.scale(frame_left, (int(frame_height), int(frame_height)))
        frame_right = pygame.image.load("assets/buttons/Frame_Right.png").convert_alpha()
        frame_right = pygame.transform.scale(frame_right, (int(frame_height), int(frame_height)))
        
        frame_middle_rect = frame_middle.get_rect(center=pos)
        text_rect = text.get_rect(center=frame_middle_rect.center)
        frame_left_rect = frame_left.get_rect(center=(frame_middle_rect.left - frame_left.get_width()//2, pos[1])) 
        frame_right_rect = frame_right.get_rect(center=(frame_middle_rect.right + frame_right.get_width()//2, pos[1]))
        
        screen.blit(frame_middle, frame_middle_rect)
        screen.blit(frame_left, frame_left_rect)
        screen.blit(frame_right, frame_right_rect)
        screen.blit(text, text_rect)
        
        if is_button:
            return pygame.Rect(frame_left_rect.x, frame_left_rect.y, frame_left_rect.width+frame_middle_rect.width+frame_right_rect.width, frame_left_rect.height)
    
    @staticmethod
    def bar_button(screen, text, pos, icon=''):
        font = pygame.font.SysFont(MENU_FONT, BAR_FONT_SIZE)
        text_surface = font.render(text, True, MENU_TITLE_FONT_COLOR)
        text_width, text_height = text_surface.get_size()
        
        # Obliczanie szerokości ikony (jeśli istnieje)
        icon_width = 0
        if icon:
            icon_surface = pygame.image.load(icon).convert_alpha()
            icon_width = text_width  # Przeskalowanie ikony do szerokości tekstu
            icon_height = int(icon_surface.get_height() * (icon_width / icon_surface.get_width()))
            icon_surface = pygame.transform.scale(icon_surface, (icon_width, icon_height))

        frame_width = text_width + icon_width  # Szerokość przycisku = szerokość tekstu + szerokość ikony
        frame_height = text_height * 1.2  # Wysokość ramki - zakładam, że wysokość ramki jest równa wysokości tekstu

        frame_middle_image = pygame.image.load("assets/buttons/Bar_Button_Frame_Middle.png").convert_alpha()
        frame_middle = pygame.transform.scale(frame_middle_image, (int(frame_width), int(frame_height)))
        frame_left_image = pygame.image.load("assets/buttons/Bar_Button_Frame_Left.png").convert_alpha()
        frame_left = pygame.transform.scale(frame_left_image, (int(frame_height) * 0.6, int(frame_height)))
        frame_right_image = pygame.image.load("assets/buttons/Bar_Button_Frame_Right.png").convert_alpha()
        frame_right = pygame.transform.scale(frame_right_image, (int(frame_height) * 0.6, int(frame_height)))

        icon_offset_x = 0
        if icon:
            icon_offset_x = icon_width // 2

        frame_middle_rect = frame_middle.get_rect(center=pos)
        text_rect = text_surface.get_rect(center=(frame_middle_rect.centerx - icon_offset_x, frame_middle_rect.centery))  # Wyśrodkowanie tekstu
        frame_left_rect = frame_left.get_rect(center=(frame_middle_rect.left - frame_left.get_width()//2, pos[1]))
        frame_right_rect = frame_right.get_rect(center=(frame_middle_rect.right + frame_right.get_width()//2, pos[1]))

        screen.blit(frame_middle, frame_middle_rect)
        screen.blit(frame_left, frame_left_rect)
        screen.blit(frame_right, frame_right_rect)
        screen.blit(text_surface, text_rect)

        # Rysowanie ikony, jeśli istnieje
        if icon:
            screen.blit(icon_surface, (frame_middle_rect.centerx + text_width // 2, frame_middle_rect.centery - icon_height // 2))

        return pygame.Rect(frame_left_rect.x, frame_left_rect.y, frame_left_rect.width+frame_middle_rect.width+frame_right_rect.width, frame_left_rect.height)
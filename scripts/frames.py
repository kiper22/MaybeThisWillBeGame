from constants import *

class Frames:
    @staticmethod
    def big_frame(screen, image, image_pos_x, image_pos_y, frame_return=False):
        '''Display big frame'''
        background = pygame.image.load("assets/village/Frame_Background.png").convert_alpha()
        background = pygame.transform.scale(background, (image.get_width() + 2 * FRAME_WIDTH, image.get_height() + 2 * FRAME_WIDTH))

        frame_border_inner = pygame.Rect(image_pos_x - FRAME_BORDER_THICKNESS,
            image_pos_y - FRAME_BORDER_THICKNESS,
            image.get_width() + 2 * FRAME_BORDER_THICKNESS,
            image.get_height() + 2 * FRAME_BORDER_THICKNESS)
        
        frame_border_outer = pygame.Rect(image_pos_x - FRAME_BORDER_THICKNESS - FRAME_WIDTH,
            image_pos_y - FRAME_BORDER_THICKNESS - FRAME_WIDTH,
            image.get_width() + 2 * (FRAME_BORDER_THICKNESS + FRAME_WIDTH),
            image.get_height() + 2 * (FRAME_BORDER_THICKNESS + FRAME_WIDTH))

        if frame_return:
            frame_image = pygame.Surface((background.get_width(), background.get_height())).convert_alpha()
            frame_image.fill((0, 0, 0, 0))
            pygame.draw.rect(frame_image, FRAME_BORDER_COLOR, frame_border_inner, FRAME_BORDER_THICKNESS)
            pygame.draw.rect(frame_image, FRAME_BORDER_COLOR, frame_border_outer, FRAME_BORDER_THICKNESS)
            
            frame_image.blit(image, (0, 0))
            return frame_image
            
        else:
            screen.blit(background, (image_pos_x - FRAME_WIDTH, image_pos_y - FRAME_WIDTH))
            pygame.draw.rect(screen, FRAME_BORDER_COLOR, frame_border_inner, FRAME_BORDER_THICKNESS)
            pygame.draw.rect(screen, FRAME_BORDER_COLOR, frame_border_outer, FRAME_BORDER_THICKNESS)
    
    @staticmethod
    def frame_border(image):
        '''Return border rectangle'''
        frame = pygame.Surface((image.get_width() + 2 * FRAME_BORDER_THICKNESS, image.get_height() + + 2 * FRAME_BORDER_THICKNESS)).convert_alpha()
        frame.fill((0, 0, 0, 0))
        pygame.draw.rect(frame, FRAME_BORDER_COLOR, (0, 
                                                     0, 
                                                     image.get_width() + 2 * FRAME_BORDER_THICKNESS, 
                                                     image.get_height() + 2 * FRAME_BORDER_THICKNESS), 
                         FRAME_BORDER_THICKNESS)
        return frame
    
    @staticmethod
    def in_frame_options(options, font, frame_x=0, frame_y=0):
        '''Return options with rectangles'''
        options_text_list = []
        rectangles_list = []
        y = 0
        
        for index, option in enumerate(options):
            # text_color = MENU_HIGHLIGHT_COLOR if highlight_states[option] else MENU_BASE_COLOR
            text = font.render(option, True, COLOR_BLACK)
            rect = text.get_rect(topleft=(frame_x + text.get_height(), frame_y + text.get_height()/2 + y))
            options_text_list.append((option, text))
            rectangles_list.append(rect)
            y += text.get_height() * 1.5
                
        return options_text_list, rectangles_list
    
        # get big frame needs to return image of frame - goal is to remove displaying from function
    # @staticmethod
    # def get_big_frame(image, image_pos_x, image_pos_y):
    #     '''Display big frame'''
    #     background = pygame.image.load("assets/village/Frame_Background.png").convert_alpha()
    #     background = pygame.transform.scale(background, (image.get_width() + 2 * FRAME_WIDTH, image.get_height() + 2 * FRAME_WIDTH))

    #     frame_border_inner = pygame.Rect(image_pos_x - FRAME_BORDER_THICKNESS,
    #         image_pos_y - FRAME_BORDER_THICKNESS,
    #         image.get_width() + 2 * FRAME_BORDER_THICKNESS,
    #         image.get_height() + 2 * FRAME_BORDER_THICKNESS)
        
    #     frame_border_outer = pygame.Rect(image_pos_x - FRAME_BORDER_THICKNESS - FRAME_WIDTH,
    #         image_pos_y - FRAME_BORDER_THICKNESS - FRAME_WIDTH,
    #         image.get_width() + 2 * (FRAME_BORDER_THICKNESS + FRAME_WIDTH),
    #         image.get_height() + 2 * (FRAME_BORDER_THICKNESS + FRAME_WIDTH))

    #     frame_image = pygame.Surface((background.get_width(), background.get_height())).convert_alpha()
    #     frame_image.fill((0, 0, 0, 0))
    #     pygame.draw.rect(frame_image, FRAME_BORDER_COLOR, frame_border_inner, FRAME_BORDER_THICKNESS)
    #     pygame.draw.rect(frame_image, FRAME_BORDER_COLOR, frame_border_outer, FRAME_BORDER_THICKNESS)
        
    #     frame_image.blit(image, (0, 0))
    #     return frame_image
            
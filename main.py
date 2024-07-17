import pygame
import sys

class LLM2Novel:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("LLM2Novel")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 32)
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((255, 255, 255))

        self.character_image = None
        self.current_text = ""
        self.text_position = (50, 400)

    def set_character_image(self, image_path):
        self.character_image = pygame.image.load(image_path)

    def set_text(self, text):
        self.current_text = text

    def render_text(self):
        words = self.current_text.split()
        lines = []
        current_line = []
        for word in words:
            current_line.append(word)
            if self.font.size(' '.join(current_line))[0] > 700:
                current_line.pop()
                lines.append(' '.join(current_line))
                current_line = [word]
        lines.append(' '.join(current_line))

        y_offset = 0
        for line in lines:
            text_surface = self.font.render(line, True, (0, 0, 0))
            self.screen.blit(text_surface, (self.text_position[0], self.text_position[1] + y_offset))
            y_offset += 40

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.background, (0, 0))

            if self.character_image:
                self.screen.blit(self.character_image, (300, 50))

            self.render_text()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

# 使用例
if __name__ == "__main__":
    novel = LLM2Novel()
    novel.set_character_image("character.png")  # 立ち絵の画像ファイルを指定
    novel.set_text("これはLLMからの回答テキストです。長い文章の場合は自動的に改行されます。")
    novel.run()
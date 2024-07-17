import pygame
import sys

class LLM2Novel:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("LLM2Novel")
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height

        # デフォルトフォントを使用
        self.font = pygame.font.Font(None, 24)

        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((255, 255, 255))

        self.character_image = None
        self.current_text = ""
        self.name = ""
        self.text_box = pygame.Surface((width - 40, 150))
        self.text_box.set_alpha(200)
        self.text_box.fill((0, 0, 0))

    def set_character_image(self, image_path):
        self.character_image = pygame.image.load(image_path)
        self.character_image = pygame.transform.scale(self.character_image, (400, 500))

    def set_text(self, text):
        self.current_text = text

    def set_name(self, name):
        self.name = name

    def render_text(self):
        name_surface = self.font.render(self.name, True, (255, 255, 255))
        self.screen.blit(name_surface, (50, self.height - 180))

        words = self.current_text.split()
        lines = []
        current_line = []
        for word in words:
            current_line.append(word)
            if self.font.size(' '.join(current_line))[0] > self.width - 80:
                current_line.pop()
                lines.append(' '.join(current_line))
                current_line = [word]
        lines.append(' '.join(current_line))

        y_offset = 0
        for line in lines:
            text_surface = self.font.render(line, True, (255, 255, 255))
            self.screen.blit(text_surface, (50, self.height - 150 + y_offset))
            y_offset += 30

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.background, (0, 0))

            if self.character_image:
                self.screen.blit(self.character_image, (200, 50))

            self.screen.blit(self.text_box, (20, self.height - 170))
            self.render_text()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

# 使用例
if __name__ == "__main__":
    novel = LLM2Novel()
    novel.set_character_image("character.jpg")  # 立ち絵の画像ファイルを指定
    novel.set_name("Sumibito")
    novel.set_text("Suiei ni wa mottekoi no hiyori da na")
    novel.run()
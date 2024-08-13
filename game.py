
import pygame
import sys
import os
from moviepy.editor import VideoFileClip

DARK_RED = (175, 75, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Oregon Trail")

# Load background image
background = pygame.image.load("oregon_trail_bg.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Load sounds
try:
    pygame.mixer.music.load("OT OST.mp3")
except pygame.error as e:
    print(f"Error loading sound file: {e}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Files in current directory: {os.listdir()}")
    sys.exit()  # Exit if sound files can't be loaded

# Play background music
pygame.mixer.music.play(-1)  # -1 means loop indefinitely

# Define button class
class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, surface):
        pygame.draw.rect(surface, DARK_RED, self.rect, 2)
        font = pygame.font.Font(None, 18)
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Define the padding between buttons
padding = 50

# Define the initial y-coordinates
initial_y_group1 = 70  # For the first three buttons
initial_y_group2 = initial_y_group1 + 2 * (30 + padding)  # For the remaining buttons

# Create buttons
main_buttons = [
    Button(20, initial_y_group2, 150, 30, "GAME HISTORY"),
    Button(20, initial_y_group2 + 30 + padding, 150, 30, "TUTORIAL"),
    Button(20, initial_y_group2 + 2 * (30 + padding), 150, 30, "SETTINGS"),
    Button(WIDTH - 170, initial_y_group1, 150, 30, "TRAVEL THE TRAIL"),
    Button(WIDTH - 170, initial_y_group1 + 50 + padding, 150, 30, "LEARN ABOUT US"),
    Button(WIDTH - 170, initial_y_group1 + 2 * (50 + padding), 150, 30, "OREGON TOP-10"),
    Button(WIDTH - 170, initial_y_group1 + 3 * (50 + padding), 150, 30, "TURN SOUND OFF"),
    Button(WIDTH - 170, initial_y_group1 + 4 * (50 + padding), 150, 30, "CREDITS")
]

# Create PLAY button
play_button = Button(WIDTH // 2 - 50, HEIGHT // 3 + 50, 100, 40, "PLAY")

# Create back button
back_button = Button(10, HEIGHT - 40, 100, 30, "BACK")

# Define page content
pages = {
    "GAME HISTORY": "The Courage and Determination of America's Pioneers\n"
            "The Oregon Trail: An Epic Journey Westward\n"
            "Learn more about history of the Oregon Trail. The Oregon Trail, an emblem of\n"
            "American westward expansion, is a legendary path etched into the nation’s\n"
            "history.\n"
            "\n"
            "It’s a saga of pioneers, courage, and the relentless pursuit of new horizons.\n"
            "\n"
            "History of the Oregon Trail – The Trail Begins\n"
            "In the early 1800s, a significant wave of settlers was drawn to the West Coast’s\n"
            "Oregon Country. Lured by the promise of fertile lands, abundant game, and a\n"
            "chance for a better life, they set out on the Oregon Trail.\n"
            "\n"
            "The journey to a better future began in Independence, Missouri, and stretched\n"
            "over vast plains, arid deserts, and rugged mountain passes, covering a distance\n"
            "well exceeding 2,000 miles.\n"
            "\n"
            "The pioneers had their eyes on the rich Willamette Valley in Oregon, where\n"
            "dreams of prosperity awaited.\n"
            "\n"
            "Challenges and Perseverance\n"
            "The journey was far from a leisurely stroll. Pioneers encountered a barrage of\n"
            "challenges, from treacherous river crossings to extreme weather conditions.\n"
            "Disease and accidents were constant threats.\n"
            "\n"
            "Many travelers were forced to lighten their loads, leaving behind precious\n"
            "belongings to make it through. Native American tribes, often portrayed as\n"
            "adversaries in popular culture, were more likely to be allies and guides.\n"
            "\n"
            "The true enemy was disease, with cholera and other illnesses claiming many lives\n"
            "along the trail.\n"
            "\n"
            "The Great Migration\n"
            "In 1843, the famous “Great Migration” marked a turning point. Around 1,000\n"
            "pioneers formed the first major wagon train, setting off on a journey that would\n"
            "be remembered for generations to come.\n"
            "\n"
            "Over the next few years, the numbers swelled, with upwards of 50,000 people\n"
            "using the trail each year.\n"
            "\n"
            "The Oregon Trail created one of the largest mass migrations in human history.\n"
            "\n"
            "The Oregon Trail became a symbol of Manifest Destiny, the belief in the\n"
            "expansion of the United States.\n"
            "\n"
            "Settlement and Legacy\n"
            "Only around 80,000 of the estimated 400,000 Oregon Trail emigrants actually\n"
            "reached Oregon. The majority splintered off in Wyoming or Idaho, seeking their\n"
            "fortunes in California’s goldfields or the Mormon settlements in Utah.\n"
            "\n"
            "Despite the adversity they faced on the trail, these pioneers helped shape the\n"
            "American frontier and contribute to the westward expansion of the nation.\n"
            "\n"
            "History of the Oregon Trail – Conclusion\n"
            "The Oregon Trail is more than just a historical route, it’s a testament to human\n"
            "spirit and determination.\n"
            "\n"
            "It’s a narrative of dreams, hardships, and the unyielding pursuit of a brighter\n"
            "future.\n"
            "\n"
            "The legacy of those who embarked on this epic journey lives on, forever etched\n"
            "into the annals of American history. The History of the Oregon Trail is a\n"
            "captivating chapter in American history, and it holds valuable lessons for\n"
            "students of all ages.",
            "TUTORIAL": "The year is 1848, and you will assume the role of a wagon leader \n"
        "guiding a group of settlers from Independence, Missouri, to Oregon’s \n"
        "Willamette Valley via a covered wagon. \n"
        "You will make pivotal decisions on supplies, resource management, and the \n"
        "route you take while navigating treacherous rivers and facing unpredictable \n"
        "events such as storms and disease. \n",
            "SETTINGS": "Settings content...",
            "TRAVEL THE TRAIL": "As you embark on your journey to Oregon, you’ll face a \n"
        "series of challenging decisions. You start by selecting your \n"
        "character’s profession: banker, carpenter, or farmer. \n"
        "Each choice comes with its own difficulty level and an initial sum \n"
        "of money to begin your journey. Then, you’ll name your character \n"
        "and the four members of your party. \n"
        "You’ll need to purchase essential supplies like oxen, food, \n"
        "clothing, ammunition, and spare wagon parts from Matt’s General Store. \n"
        "The journey is divided into sixteen segments, each concluding at a \n"
        "landmark, such as a river crossing or a fort. These landmarks \n"
        "offer various choices, like acquiring supplies, conversing with \n"
        "fellow travelers, or deciding how to cross a river. \n"
        "You’ll need to make critical choices when navigating rivers, \n"
        "including fording, caulking, or paying for a ferry. The state of \n"
        "the river and weather conditions affect your chances of crossing \n"
        "without any hiccups. \n"
        "Along the way, the prices for supplies rise, and you’ll need to make \n"
        "the right decisions to ensure your party’s survival.",
            "LEARN ABOUT THE TRAIL": "The journey between landmarks involves traveling for days over hundreds of miles. \n"
        "You’ll receive updates on the date, weather conditions, the health of your party, \n"
        "available food supplies, distances to the next landmark, and the distance covered. \n"
        "Embrace the spirit of the pioneers on a treacherous journey to the Wild West. \n"
        "Random events can occur, like storms causing delays or party members falling ill. \n"
        "The player can control the pace of travel, the amount of daily food rations, rest periods,\n"
        "trade with other parties, and even hunt for food. \n"
        "The hunting component is presented as a mini-game where you control a character \n"
        "who shoots animals for food. \n"
        "Careful resource management and strategic choices are key to success on the trail. \n"
        "The game concludes when your party either reaches Willamette Valley or .\n"
        "when all members succumb to illness or injury. \n"
        "Your performance is scored based on several factors,.\n"
        "creating a sense of competition and replayability.",
        "OREGON TOP-10": "1. PaulPowers\n"
        "2. Alejo\n"
        "3. Tino\n"
        "4. Kwam\n"
        "5. Erisa\n"
        "6. Jade\n"
        "7. Alex\n"
        "8. Maria\n"
        "9. John\n"
        "10. Sarah\n",
        "CREDITS": "Credits content...",
        "PLAY": "Welcome to The Oregon Trail! Your journey begins here. Choose your party, stock up on supplies, and prepare for an adventure across the American frontier, lets play."
    }



# Scrollbar class
class Scrollbar:
    def __init__(self, x, y, width, height, content_height):
        self.rect = pygame.Rect(x, y, width, height)
        self.content_height = content_height
        self.scroll_position = 0
        self.scroll_ratio = min(1, height / content_height)
        self.thumb_height = max(20, int(height * self.scroll_ratio))
        self.thumb_rect = pygame.Rect(x, y, width, self.thumb_height) 

    def draw(self, surface):
        pygame.draw.rect(surface, GRAY, self.rect)
        pygame.draw.rect(surface, WHITE, self.thumb_rect)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                self.scroll_position = max(0, self.scroll_position - 20)
            elif event.button == 5:  # Scroll down
                self.scroll_position = min(self.content_height - self.rect.height, self.scroll_position + 20)
            self.update_thumb_position()

    def update_thumb_position(self):
        self.thumb_rect.y = self.rect.y + int(self.scroll_position * self.scroll_ratio)

# Initialize scrollbar
scrollbar = Scrollbar(WIDTH - 20, 0, 20, HEIGHT, 2000)



# Function to toggle music
def toggle_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    else:
        pygame.mixer.music.play(-1)

# Load video
video = VideoFileClip('Mix1.mp4')

def play_video():
    video_width, video_height = video.size
    scale_factor = min(WIDTH / video_width, HEIGHT / video_height)
    new_width = int(video_width * scale_factor)
    new_height = int(video_height * scale_factor)
    
    for frame in video.iter_frames(fps=24, dtype='uint8'):
        # Resize the frame
        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        frame_surface = pygame.transform.scale(frame_surface, (new_width, new_height))
        
        # Center the video
        frame_rect = frame_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        
        screen.fill(BLACK)
        screen.blit(frame_surface, frame_rect)
        back_button.draw(screen)  # Draw the back button on top of the video
        pygame.display.flip()
        pygame.time.delay(int(1000 / 24))  # Adjust delay for frame rate

# Main loop
running = True
current_page = "HOME"
video_playing = False

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if video_playing and back_button.is_clicked(pos):
                video_playing = False
                current_page = "HOME"
                pygame.mixer.music.play(-1)  # Resume background music
            elif current_page == "HOME":
                for button in main_buttons:
                    if button.is_clicked(pos):
                        if button.text == "TURN SOUND OFF":
                            toggle_music()
                            button.text = "TURN SOUND ON" if button.text == "TURN SOUND OFF" else "TURN SOUND OFF"
                        else:
                            current_page = button.text
                        break
                if play_button.is_clicked(pos):
                    current_page = "PLAY"
                    video_playing = True
                    # Start video playback
                    play_video()
                    video_playing = False  # After playback ends, return to home
            elif current_page != "HOME" and back_button.is_clicked(pos):
                current_page = "HOME"
                pygame.mixer.music.play(-1)  # Resume background music
            scrollbar.update(event)

    if current_page == "HOME":
        screen.blit(background, (0, 0))
        for button in main_buttons:
            button.draw(screen)
        play_button.draw(screen)
    else:
        # Draw content with scrolling
        content_y = -scrollbar.scroll_position
        for line in pages[current_page].split("\n"):
            font = pygame.font.Font(None, 24)
            text = font.render(line, True, WHITE)
            screen.blit(text, (10, content_y))
            content_y += 30
        scrollbar.draw(screen)
        back_button.draw(screen)

    pygame.display.flip()

pygame.quit()

# This is chenged due to GIT test 
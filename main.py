import flet as ft
import random
import string

def main(page: ft.Page):
    # Set the page title and background color
    page.title = "Puzzle App"
    page.bgcolor = ft.colors.DEEP_PURPLE_900  # Dark purple background
    
    # Set the window size
    page.window_width = 360
    page.window_height = 640
    
    # You can also set the minimum and maximum size if needed
    page.window_min_width = 300
    page.window_min_height = 300
    page.window_max_width = 1200
    page.window_max_height = 900

    # Top Section: App Logo and Name
    logo = ft.Image(
        src="logo.png",  # Replace with your logo URL or local path
        width=150,
        height=150,
        fit=ft.ImageFit.CONTAIN,
        border_radius=ft.border_radius.all(10),
    )
    app_name = ft.Text(
        "Puzzle App",
        size=40,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.YELLOW_500,  # Bright yellow text
        text_align=ft.TextAlign.CENTER,
    )

    # Word Search Button
    word_search_button = ft.ElevatedButton(
        text="Word Search",
        icon=ft.icons.SEARCH,
        width=250,
        height=60,
        bgcolor=ft.colors.AMBER_800,  # Dark amber button
        color=ft.colors.WHITE,
        on_click=lambda e: word_search_page(page),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            overlay_color=ft.colors.TRANSPARENT,
            elevation=5,
            animation_duration=100,
        ),
    )

    # Bottom Section: Additional Options
    settings_button = ft.IconButton(
        icon=ft.icons.SETTINGS,
        icon_size=30,
        on_click=lambda e: settings_page(page),
        style=ft.ButtonStyle(
            shape=ft.CircleBorder(),
            bgcolor=ft.colors.BLUE_GREY_800,  # Dark blue-grey background
            overlay_color=ft.colors.TRANSPARENT,
            elevation=5,
            animation_duration=100,
        ),
        icon_color=ft.colors.LIGHT_BLUE_200,  # Light blue icon color
    )
    
    high_scores_button = ft.IconButton(
        icon=ft.icons.LEADERBOARD,
        icon_size=30,
        on_click=lambda e: high_scores_page(page),
        style=ft.ButtonStyle(
            shape=ft.CircleBorder(),
            bgcolor=ft.colors.GREEN_800,  # Dark green background
            overlay_color=ft.colors.TRANSPARENT,
            elevation=5,
            animation_duration=100,
        ),
        icon_color=ft.colors.LIGHT_GREEN_200,  # Light green icon color
    )
    
    about_button = ft.IconButton(
        icon=ft.icons.INFO,
        icon_size=30,
        on_click=lambda e: about_page(page),
        style=ft.ButtonStyle(
            shape=ft.CircleBorder(),
            bgcolor=ft.colors.ORANGE_800,  # Dark orange background
            overlay_color=ft.colors.TRANSPARENT,
            elevation=5,
            animation_duration=100,
        ),
        icon_color=ft.colors.ORANGE_200,  # Light orange icon color
    )

    footer_text = ft.Text(
        "If you're facing any issues, please report to SE Software and Web Developers",
        size=12,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.GREY_400,
    )

    # Layout
    page.add(
        ft.Column(
            [
                ft.Row(
                    [logo],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                app_name,
                ft.Row(
                    [word_search_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [settings_button, high_scores_button, about_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                footer_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
    )


def settings_page(page):
    page.snack_bar = ft.SnackBar(ft.Text("Settings page is under construction."))
    page.snack_bar.open = True
    page.update()

def high_scores_page(page):
    page.snack_bar = ft.SnackBar(ft.Text("High Scores page is under construction."))
    page.snack_bar.open = True
    page.update()

def about_page(page):
    page.snack_bar = ft.SnackBar(ft.Text("About page is under construction."))
    page.snack_bar.open = True
    page.update()

def place_word_in_grid(grid, word):
    rows, cols = len(grid), len(grid[0])
    direction = random.choice(["H", "V"])  # Horizontal or Vertical
    if direction == "H":
        start_row = random.randint(0, rows - 1)
        start_col = random.randint(0, cols - len(word))
        for i, letter in enumerate(word):
            grid[start_row][start_col + i] = letter
    elif direction == "V":
        start_row = random.randint(0, rows - len(word))
        start_col = random.randint(0, cols - 1)
        for i, letter in enumerate(word):
            grid[start_row + i][start_col] = letter

def generate_random_grid(rows, cols, words_in_grid):
    grid = [["" for _ in range(cols)] for _ in range(rows)]

    for word in words_in_grid:
        place_word_in_grid(grid, word)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "":
                grid[r][c] = random.choice(string.ascii_uppercase)
    
    return grid

def check_word(e, words_in_grid, grid, found_words_display, found_words):
    word = e.control.value.lower()  # Convert the input word to lowercase
    words_in_grid_lower = [w.lower() for w in words_in_grid]  # Convert the words in the grid to lowercase
    
    if word in words_in_grid_lower and word not in found_words:
        found_words.append(word)  # Add the word to the found words list
        result.value = f"'{word}' found!"
        result.color = ft.colors.GREEN_ACCENT_400  # Green for found
        found_words_display.value = ", ".join(found_words)  # Update the found words display
    else:
        result.value = f"'{word}' not found or already found!"
        result.color = ft.colors.RED_ACCENT_400  # Red for not found
    
    e.page.update()

def word_search_page(page: ft.Page):
    page.title = "Word Search Puzzle"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 360
    page.window_height = 640

    # Load the wordlist file
    with open("wordlist.txt", "r") as file:
        wordlist = file.read().splitlines()

    # Select a random subset of words from the wordlist
    words_in_grid = random.sample(wordlist, 5)  # Adjust the number of words as needed

    # Generate random grid of letters with the words in it
    rows, cols = 10, 10# Adjust grid size as needed
    grid = generate_random_grid(rows, cols, words_in_grid)

    # Text box for word input
    word_input = ft.TextField(
        label="Enter a word",
        on_submit=lambda e: check_word(e, words_in_grid, grid, found_words_display, found_words),
        width=250,
        border_radius=ft.border_radius.all(10),
        color=ft.colors.WHITE,
        bgcolor=ft.colors.BLUE_GREY_800,  # Dark blue-grey background for the input
    )

    # Display grid of letters
    grid_controls = []
    for row in grid:
        row_controls = []
        for letter in row:
            row_controls.append(
                ft.ElevatedButton(
                    text=letter,
                    on_click=lambda e, letter=letter: handle_letter_click(e, letter, word_input),
                    width=30,
                    height=30,
                    bgcolor=ft.colors.INDIGO_900,  # Dark indigo for the grid buttons
                    color=ft.colors.WHITE,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=5),
                        overlay_color=ft.colors.TRANSPARENT,
                        elevation=3,
                        animation_duration=100,
                    ),
                )
            )
        grid_controls.append(ft.Row(controls=row_controls, spacing=5))
    
    grid_display = ft.Column(controls=grid_controls, spacing=5)

    # Result display
    global result
    result = ft.Text(value="", size=16, color="white")

    # Score display
    score = ft.Text(value="Score: 0", size=16, color=ft.colors.LIME_400)

    # Display for found words
    found_words = []
    found_words_display = ft.Text(value="Found Words: ", size=16, color=ft.colors.YELLOW_300)

    # Set the page controls directly
    page.controls = [
        ft.Column(
            controls=[
                ft.Text("Word Search Puzzle", size=24, color=ft.colors.PINK_400, weight=ft.FontWeight.BOLD),
                word_input,
                ft.Text("Find the hidden words!", size=18, color=ft.colors.ORANGE_400),
                grid_display,
                result,
                score,
                found_words_display,  # Add found words display
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        )
    ]

    # Update the page
    page.update()

def handle_letter_click(e, letter, word_input):
    word_input.value += letter
    word_input.update()

# Run the app
ft.app(target=main)

import tkinter as tk
import random


def process_data(data):
  """
  Processes a list of lines from a text file and returns a list of dictionaries containing song title and lyrics.

  Args:
      data: A list of strings representing the lines from the text file.

  Returns:
      A list of dictionaries. Each dictionary has two keys:
          title: The title of the song (a string).
          lyrics: A list of strings representing the couplets of the song.
  """
  songs = []
  song_title = []
  lyrics = []
  empty_line_count = 0  # Count empty lines to track song separation
  is_title = True  # Flag to track if we're processing the title
  # Skip the first line (if it exists) to avoid potential hidden characters
  data = data[1:]
  for line in data:
    line = line.strip()
    if not line:
      empty_line_count += 1
      if empty_line_count == 4:  # 4 empty lines signifies end of song
        if song_title:  # Only append title if it has content
          songs.append({"title": "\n".join(song_title), "lyrics": lyrics})
        song_title = []
        lyrics = []
        empty_line_count = 0  # Reset counter
        is_title = True  # Reset title flag
      else:
        # Ignore single or double empty lines
        pass
    else:
      if is_title:
        # Only append the first line to the title
        if not song_title:
          song_title.append(line)
        is_title = False  # Switch to lyrics after first line of title
      else:
        lyrics.append(line)
      empty_line_count = 0  # Reset counter after non-empty line

  # Append the last song (if it exists)
  if song_title:
    songs.append({"title": "\n".join(song_title), "lyrics": lyrics})
  return songs


def show_random_song():
  """
  Selects a random song from the processed data and displays its title and a random couplet in the GUI.
  """
  global songs  # Access the global songs variable

  # Select a random song
  random_song = random.choice(songs)

  # Select a random couplet (ensure there are at least 2)
  if len(random_song["lyrics"]) >= 2:
    random_couplet_index = random.randint(0, len(random_song["lyrics"]) - 2)
    random_couplet = random_song["lyrics"][random_couplet_index]
  else:
    random_couplet = "The song doesn't have enough couplets."

  # Update the text labels in the GUI
  song_title_label.config(text=f"Song: {random_song['title']}")
  couplet_label.config(text=f"{random_couplet}")


# Read the text file (consider UTF-8 encoding)
with open('lyrics.txt', 'r', encoding='utf-8') as f:
  data = f.readlines()

# Process the data
songs = process_data(data)


def show_random_song():
  """Selects a random song and displays question, couplet, and song title."""
  global question_entry, couplet_label, song_title_label

  question = question_entry.get()
  question_entry.delete(0, tk.END)

  random_song = random.choice(songs)
  if len(random_song["lyrics"]) >= 2:
      random_couplet_index = random.randint(0, len(random_song["lyrics"]) - 2)
      random_couplet = random_song["lyrics"][random_couplet_index]
  else:
      random_couplet = "The song doesn't have enough couplets."

  question_entry.insert(0, question)
  couplet_label.config(text=random_couplet, font=("Arial", 16, "bold"))
  song_title_label.config(text=random_song["title"], font=("Arial", 12))


# Initialize the Tkinter GUI
root = tk.Tk()
root.title("TAYLOR IT!")
root.iconbitmap('8ball.ico')

# Set window dimensions (optional)
window_width = 600
window_height = 400
root.geometry(f"{window_width}x{window_height}")

# Load the magic ball image (replace with your image path)
magic_ball_image = tk.PhotoImage(file='taylor.png')  # Replace with your image path

# Create the magic ball image label on the right side
magic_ball_label = tk.Label(root, image=magic_ball_image)
magic_ball_label.place(relx=0.65, rely=0.1, relwidth=0.3, relheight=0.8)  # Adjust position and size

# Create the text field for question entry on the left side
question_entry = tk.Entry(root, font=("Arial", 14))
question_entry.place(relx=0.1, rely=0.3, relwidth=0.5, relheight=0.1)  # Adjust position and size

# Create the label for "Ask a Question..." on the left side
question_label = tk.Label(root, text="Your Question:", font=("Arial", 12), fg="gray")
question_label.place(relx=0.1, rely=0.2)  # Adjust position

# Create the label for displaying the couplet in large font on the left side
couplet_label = tk.Label(root, text="", justify="left", wraplength=int(window_width * 0.4))
couplet_label.place(relx=0.1, rely=0.5, relwidth=0.5, relheight=0.3)  # Adjust position and size

# Create the label for displaying the song title in a smaller font on the left side below couplet
song_title_label = tk.Label(root, text="", font=("Arial", 10),  wraplength=int(window_width * 0.4))
song_title_label.place(relx=0.1, rely=0.8, relwidth=0.5, relheight=0.2)  # Adjust position and size

# Create the button with text positioned below the text field
button = tk.Button(root, text="Ask Taylor", font=("Arial", 14), command=show_random_song)
button.place(relx=0.1, rely=0.4, relwidth=0.5, relheight=0.1)  # Adjust position and size
# **Important:** Start the main event loop to keep the GUI running (place this outside the function)
root.mainloop()
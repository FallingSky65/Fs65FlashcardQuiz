# Fs65FlashcardQuiz

The Fs65FlashcardQuiz allows you to test yourself one custom flashcards in `.csv` format. To use, clone the `main.py` into a directory with your csv file, and run `python main.py <path to your csv file>`. The csv file must have 2 columns (2+ columns will ignore all columns 2<). This python file makes use of the `sys`, `os`, `pandas`, and `random` libraries. If you run this code on Windows, you can fix the clearing terminal problem by changing the `clear` function to use `os.system("cls")`.
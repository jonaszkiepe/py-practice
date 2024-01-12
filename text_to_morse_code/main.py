import time
import numpy as np
import simpleaudio as sa

MORSE_ALPHABET = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": " "
}


def translate_to_morse_code(text: str):
    upper_text = text.upper()
    morse_text = [MORSE_ALPHABET[letter] for letter in upper_text]
    return morse_text


def morse_code_to_sound(morse_code: list):
    def generate_sine_wave(freq, duration, sample_rate=44100):
        # Generate time points
        t = np.linspace(0, duration, int(duration * sample_rate), False)
        # Generate sine wave notes
        note = np.sin(freq * t * 2 * np.pi)
        # Normalize to 16-bit range
        audio = note * (2**15 - 1) / np.max(np.abs(note))
        # Convert to 16-bit data
        audio = audio.astype(np.int16)
        # Start playback
        play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
        # Wait for playback to finish
        play_obj.wait_done()

    for letter in morse_code:
        time.sleep(0.5)
        for char in letter:
            if char == ".":
                generate_sine_wave(500, 0.1)
            if char == "-":
                generate_sine_wave(500, 0.2)
            if char == " ":
                time.sleep(0.5)


morse_code = translate_to_morse_code(input())
morse_code_to_sound(morse_code)

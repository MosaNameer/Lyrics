import time

def print_lirik():
    lirik = [
        ("Ooh ✨", 1.0, 0.03),
        ("I, I just woke up from a dream 💭", 0.8, 0.13),
        ("Where you and I had to say goodbye 👋", 0.8, 0.11),
        ("And I don't know what it all means 😕", 0.9, 0.11),
        ("But since I survived, I realized 💫", 0.9, 0.1),

        ("Wherever you go, that's where I'll follow 👣", 0.7, 0.09),
        ("Nobody's promised tomorrow ⏳", 0.7, 0.09),
        ("", 0.5, 0.0),
        ("", 0.8, 0.09),
        ("So I'ma love you every night ❤️", 1.0, 0.08),
        ("like it's the last night 🌙", 1.0, 0.09),
        ("If the world was ending 🌍", 0.9, 0.09),
        ("I'd wanna be next to you 🫂", 0.7, 0.13),
        ("", 0.5, 0.0),
        ("", 0.8, 0.9),
        ("", 0.5, 0.06),
        ("If the party was over 🎭", 0.8, 0.09),
        ("and our time on Earth was through ⌛", 0.8, 0.13),
        ("", 0.3, 0.9),
        ("", 0.3, 0.9),
        ("", 0.5, 0.06),
        ("I'd wanna hold you just for a while 🤗", 0.7, 0.13),
        ("and die with a smile 😊", 0.7, 0.14),
        ("If the world was ending 🌎", 0.5, 0.13),
        ("I'd wanna be next to you 💝", 0.5, 0.13),
        ("", 0.5, 0.0),
        (" .d88b.  .d88b. ", 0.1, 0.002),
        ("d88P Y88bd88P Y88b", 0.1, 0.002),
        ("888   888888   888", 0.1, 0.002), 
        ("Y88b d88PY88b d88P", 0.1, 0.002),
        (" 'Y88P'   'Y88P' ", 0.1, 0.002),
        ("", 0.2, 0.0),
        ("", 0.2, 0.0),
        ("", 0.2, 0.0),
        
        
        ("  /\\  /\\ ", 0.1, 0.002),
        (" /  \\/  \\", 0.1, 0.002),
        (" \\      /", 0.1, 0.002),
        ("  \\    /", 0.1, 0.002),
        ("   \\  /", 0.1, 0.002),
        ("    \\/", 0.1, 0.002),
 
    ]

    for teks, delay_baris, delay_huruf in lirik:
        for c in teks:
            print(c, end='', flush=True)
            time.sleep(delay_huruf)
        print()
        time.sleep(delay_baris)

if __name__ == "__main__":
    print_lirik()

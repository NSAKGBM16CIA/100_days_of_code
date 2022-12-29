from morse_dict import morse_dict
# import ui

class Encoder():
    def __init__(self):
        self.file = ""
        self.text = ""
        self.split_morse = ""

    def encode_morse(self, text):
        code_message = ""
        for c in text:
            code_message += morse_dict[c.capitalize()].strip()
            self.split_morse += f"{morse_dict[c.capitalize()].strip()}|"
        show_text = code_message.replace("\s", " ")
        return show_text

    def decode_morse(self, text):
        # make values keys and strip to remove trailing white spaces
        reverse_dict = {y.strip(): x for x, y in morse_dict.items()}
        code_message =""
        for word in text.split("|"):
            code_message += reverse_dict[word]
        return code_message.capitalize()

    def read_file(self, file):
        try:
            with open(file, 'r') as f:
                self.text = f.read()
                self.file = file
                # print(self.text, self.file)
                return self.text
        except Exception:
             return "Error: Could not read file!"

    def code(self, text):
        try:
            if text[0].isalpha():
                self.split_morse = ""
                return self.encode_morse(text)
            else:
                return self.decode_morse(self.split_morse)
        except Exception:
            # whatever error that occurs from key error to character format etc
            return "Error: Could not decode file!"

    def save_file(self, text):
        filename = self.file.split('/')[-1]
        # print(filename)
        if text[0].isalpha():
            path = f"encoded_files/{filename}_encxxx.txt"
            if "_decxxx.txt" in path:
                path = path.replace("_decxxx.txt", "")
            # print(path)
        else:
            path = f"encoded_files/{filename}_decxxx.txt"
            if "_encxxx.txt" in path:
                path = path.replace("_encxxx.txt", "")
            # print(path)
        try:
            with open(path, 'w') as file:
                file.write(self.code(text))
                return "En/Decoding Successful. File Saved!"
        except Exception:
            return "Error: Could not save file!"

# encoder = Encoder()
# s = encoder.encode_morse("I love you.")
# print(s)
# s2 = encoder.decode_morse(encoder.split_morse)
# print(s2.capitalize())




from typing import List
from unittest import TestCase

def get_matching_bracket(code: str, position: int) -> int:
    if code[position] == "[":
        bracket, counterbracket, incrementer = "[", "]", 1
    else:
        bracket, counterbracket, incrementer = "]", "[", -1
    brackets_to_found = 1
    while brackets_to_found:
        position += incrementer
        if code[position] == counterbracket:
            brackets_to_found -= 1
        elif code[position] == bracket:
            brackets_to_found += 1
    return position

def correct_data(data):
    if data == -1:
        return 255
    elif data == 256:
        return 0
    return data

def brain_luck(code: str, input: str):
    output: List[str] = []
    input_pointer = 0
    code_pointer = 0
    data_pointer = 0
    data = {}
    while code_pointer < len(code):
        command = code[code_pointer]
        if command == ">":
            data_pointer += 1
        elif command == "<":
            data_pointer -= 1
        elif command == "+":
            data[data_pointer] = correct_data(data.get(data_pointer, 0) + 1)
        elif command == "-":
            data[data_pointer] = correct_data(data.get(data_pointer, 0) - 1)
        elif command == ".":
            output.append(chr(data.get(data_pointer, 0)))
        elif command == ",":
            data[data_pointer] = ord(input[input_pointer])
            input_pointer += 1
        elif command == "[":
            if data.get(data_pointer, 0) == 0:
                code_pointer = get_matching_bracket(code, code_pointer)
        elif command == "]":
            if data.get(data_pointer, 0) != 0:
                code_pointer = get_matching_bracket(code, code_pointer)
        code_pointer += 1
    return "".join(output)


class PowerTest(TestCase):
    def test(self):
        self.assertEqual(brain_luck(',+[-.,+]', 'Codewars' + chr(255)), 'Codewars')
        self.assertEqual(brain_luck(',[.[-],]', 'Codewars' + chr(0)), 'Codewars')
        self.assertEqual(brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)), chr(72))
        self.assertEqual(brain_luck('+[-[<<[+[--->]-[<<<]]]>>>-]>-.---.>..>.<<<<-.<+.>>>>>.>.<<.<-.', ""), "hello world")
        self.assertEqual(get_matching_bracket(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', 4), 29)
        self.assertEqual(get_matching_bracket(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', 29), 4)
        self.assertEqual(get_matching_bracket(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', 6), 14)
        self.assertEqual(get_matching_bracket(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', 14), 6)
        self.assertEqual(get_matching_bracket(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', 17), 24)
        self.assertEqual(get_matching_bracket(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', 24), 17)


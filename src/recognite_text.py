import os
import sys
from typing import List, Any

import easyocr


def recognite_text(file_path: str) -> List[Any]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    try:
        reader = easyocr.Reader(['en', 'ru'], gpu=False)

        return reader.readtext(file_path, detail=False)
    except Exception as e:
        print(e)
        return []


def main(*args, **kwargs):
    text_list = recognite_text(args[0])

    text = ' '.join(text_list)

    print(text)


    sys.stdout.flush()


if __name__ == '__main__':
    main(*sys.argv[1:])

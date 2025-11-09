from typing import Any
from bidi.algorithm import get_display
import jdatetime
import re
import arabic_reshaper
from persian_logger.terminal_supports_rtl import TerminalSupport
class PersianConverter:

    _EN_TO_FA = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
    
    @staticmethod
    def to_persian_numbers(text: str) -> str:
        return str(text).translate(PersianConverter._EN_TO_FA)

    @staticmethod
    def now_persian() -> str:
        now = jdatetime.datetime.now()
        fa_date = PersianConverter.to_persian_numbers(
            now.strftime("%Y/%m/%d")
        )
        fa_time = PersianConverter.to_persian_numbers(
            now.strftime("%H:%M:%S")
        )
        return f"{fa_date} | {fa_time}"

    @staticmethod
    def reshape_farsi(text: str) -> str:
        reshaped = arabic_reshaper.reshape(text)
        return get_display(reshaped)

    @staticmethod
    def full_convert(text: Any) -> str:
        text = str(text)
        text = PersianConverter.to_persian_numbers(text)
        return PersianConverter.reshape_farsi(text)


    @staticmethod
    def smart_fa(func):
        def wrapper(self, text):
            if not TerminalSupport.terminal_supports_rtl():
                return func(self, text)
            else:
                text = PersianConverter.full_convert(text)
                return func(self, text)
        return wrapper
    @staticmethod
    def _is_persian_char(c):
        return '\u0600' <= c <= '\u06FF' or '\uFB50' <= c <= '\uFEFF'

    @staticmethod
    def _is_persian_word(word):
        return any(PersianConverter._is_persian_char(c) for c in word)
    
    @staticmethod
    def _pseudo_rtl(text):
       
        tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)

        if all(PersianConverter._is_persian_word(t) for t in tokens if re.match(r'\w+', t)):
           
            return "".join(tokens)
     
        words = [t for t in tokens if re.match(r'\w+', t)]
        length = len(words)
        ftr_lst = [None] * length
        for i, word in enumerate(words):
            if PersianConverter._is_persian_word(word):
                ftr_lst[length - i - 1] = word
            else:
                ftr_lst[i] = word
        
        ftr_lst = [w if w is not None else "" for w in ftr_lst]

        
        idx = 0
        result_tokens = []
        for t in tokens:
            if re.match(r'\w+', t):
                result_tokens.append(ftr_lst[idx])
                idx += 1
            else:
                result_tokens.append(t)

        return " ".join(result_tokens)

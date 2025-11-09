import os

class TerminalSupport:

    @staticmethod
    def terminal_supports_rtl():

        term_program = os.environ.get("TERM_PROGRAM", "").lower()
        colorterm = os.environ.get("COLORTERM", "").lower()
        term = os.environ.get("TERM", "").lower()

        candidates = [term_program, colorterm, term]

        if any(
            x in candidates for x in [
                "vscode",
                "konsole",
                "terminology",
                "iterm"
            ]
            ):
            return True

        if "gnome" in term or "xterm" in term:
            return False

        return False
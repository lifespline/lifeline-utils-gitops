class LogColour:
    """
    ANSI escape code: \033
    ANSI format: \033[{style};{foreground};{background}m
    https://ozzmaker.com/add-colour-to-text-in-python/
    """
    ansi_code = '\033['
    fg = {
        "black" : '30',
        "red" : '31',
        "green" : '32',
        "yellow" : '33',
        "blue" : '34',
        "purple" : '35',
        "cyan" : '36',
        "white" : '37',
        "none": '0'
    }

    bg = {
        "black" : '40',
        "red" : '41',
        "green" : '42',
        "yellow" : '43',
        "blue" : '44',
        "purple" : '45',
        "cyan" : '46',
        "white" : '47',
        "none": '0'
    }
    style = {
        'none' : 0,
        'bold' : 1,
        'underline' : 2,
        'italics' : 3,
        'underline' : 4,
    }

    def get_code(style='', fg='', bg=''):
        """Get ANSI color code:

        style;foreground;background

        Args:
            style ([type]): [description]
            fg ([type]): [description]
            bg ([type]): [description]

        Returns:
            [type]: [description]
        """
        ansi_code = '\033['
        code = ansi_code

        if style:
            code += str(style)
        if fg:
            code += f";{str(fg)}"
        if bg:
            code += f";{str(bg)}"
        if code == ansi_code:
            code += '0;0;0'

        code +='m'

        return code

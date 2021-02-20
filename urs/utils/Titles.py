"""
Titles
======
Display ASCII art that is used throughout this program.
"""


from colorama import (
    init, 
    Fore, 
    Style
)

### Automate sending reset sequences to turn off color changes at the end of 
### every print.
init(autoreset = True)

class MainTitle():
    """
    Method for printing the main URS title.
    """

    @staticmethod
    def title():
        """
        Print URS title.
        """

        print(Fore.WHITE + Style.BRIGHT + r"""
 __  __  _ __   ____  
/\ \/\ \/\`'__\/',__\ 
\ \ \_\ \ \ \//\__, `\
 \ \____/\ \_\\/\____/
  \/___/  \/_/ \/___/ 
""")

class PRAWTitles():
    """
    Methods for printing PRAW scraper titles.
    """

    @staticmethod
    def r_title():
        """
        Print Subreddit scraper title.
        """

        print(Fore.WHITE + Style.BRIGHT + r"""
 _ __  
/\`'__\
\ \ \/ 
 \ \_\ 
  \/_/ 
""")

    @staticmethod
    def u_title():
        """
        Print Redditor scraper title.
        """

        print(Fore.WHITE + Style.BRIGHT + r"""
 __  __  
/\ \/\ \ 
\ \ \_\ \
 \ \____/
  \/___/ 
""")

    @staticmethod
    def c_title():
        """
        Print comments scraper title.
        """

        print(Fore.WHITE + Style.BRIGHT + r"""
  ___   
 /'___\ 
/\ \__/ 
\ \____\
 \/____/
""")

    @staticmethod
    def b_title():
        """
        Print basic scraper title.
        """

        print(Fore.WHITE + Style.BRIGHT + r"""
 __        
/\ \       
\ \ \____  
 \ \ '__`\ 
  \ \ \L\ \
   \ \_,__/
    \/___/... Only scrapes Subreddits. 
""")

class AnalyticsTitles():
    """
    Methods for printing for analytical tool titles.
    """

    @staticmethod
    def f_title():
        """
        Print frequencies title.
        """

        print(Fore.WHITE + Style.BRIGHT + r"""
   ___  
 /'___\ 📈
/\ \__/ 
\ \ ,__\ 
 \ \ \_/
  \ \_\ 
   \/_/
""")

    @staticmethod
    def wc_title():
        """
        Print wordcloud title.
        """

        print(Fore.WHITE + Style.BRIGHT + r"""
 __  __  __    ___ 🖌️ 
/\ \/\ \/\ \  /'___\ 
\ \ \_/ \_/ \/\ \__/ 
 \ \___x___/'\ \____\
  \/__//__/   \/____/
""")

class Errors():
    """
    Methods for printing error titles.
    """

    @staticmethod
    def e_title():
        """
        Print error title.
        """

        print(Fore.RED + Style.BRIGHT + r"""
   __   
 /'__`\ 
/\  __/ 
\ \____\
 \/____/... Please recheck args or refer to help or usage examples.
""")

    @staticmethod
    def p_title(error):
        """
        Print PRAW error title.

        Parameters
        ----------
        error: PrawException
            PrawException raised when API validation fails

        Returns
        -------
        None
        """

        print(Fore.RED + Style.BRIGHT + r"""
 _____   
/\ '__`\ 
\ \ \L\ \
 \ \ ,__/... Please recheck API credentials or your internet connection.
  \ \ \/ 
   \ \_\ 
    \/_/

Prawcore exception: %s
""" % error)

    @staticmethod
    def l_title(reset_timestamp):
        """
        Print rate limit error title.

        Parameters
        ----------
        reset_timestamp: str
            Reset timestamp provided by PRAW

        Returns
        -------
        None
        """

        print(Fore.RED + Style.BRIGHT + r"""
 __        
/\ \       
\ \ \      
 \ \ \  __ 
  \ \ \L\ \
   \ \____/
    \/___/... You have reached your rate limit.

Please try again when your rate limit is reset: %s
""" % reset_timestamp)

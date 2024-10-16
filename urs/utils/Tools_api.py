"""
Tools
=====
Running all tools that URS has to offer.
"""


import logging
from argparse import ArgumentParser, Namespace
from typing import Tuple

from praw import Reddit

from urs.analytics.Frequencies import GenerateFrequencies
from urs.analytics.Wordcloud import GenerateWordcloud
from urs.praw_scrapers.live_scrapers.Livestream import Livestream
from urs.praw_scrapers.static_scrapers.Basic import RunBasic
from urs.praw_scrapers.static_scrapers.Comments import RunComments
from urs.praw_scrapers.static_scrapers.Redditor import RunRedditor
from urs.praw_scrapers.static_scrapers.Subreddit import RunSubreddit
from urs.praw_scrapers.utils.Validation import Validation
from urs.utils.Cli import CheckCli, Parser
from urs.utils.Titles import MainTitle
from urs.utils.Utilities import DateTree
from argparse import Namespace


class RunApi:
    """
    Methods to call CLI and all tools.
    """

    def __init__(self, namespace: Namespace, reddit: Reddit) -> None:
        """
        Initialize variables used in instance methods:

            self._reddit: Reddit instance
            self._args: argparse Namespace object
            self._parser: argparse ArgumentParser object

        :param Reddit reddit: PRAW `Reddit` object.
        """

        self._args = namespace
        self._reddit = reddit

    def run_urs(self) -> None:
        """
        Switch for running all URS tools.
        """

        if (self._args.subreddit):
            """
            Run PRAW scrapers.
            """

            Validation.validate_user_from_api(self._reddit)

            if self._args.subreddit:
                print("==== self._args", self._args)
                print("==== self._reddit", self._reddit)
                result = RunSubreddit.run_from_api(self._args, self._reddit)
                return result[1]

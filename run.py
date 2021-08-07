#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:54:55 2021

@author: tiffanybiles
"""

"""A youtube terminal simulator."""
from video_player.py import VideoPlayer
from command_parser.py import CommandException
from command_parser.py import CommandParser


if __name__ == "__main__":
    print("""Hello and welcome to YouTube, what would you like to do?
    Enter HELP for list of available commands or EXIT to terminate.""")
    video_player = VideoPlayer()
    parser = CommandParser(video_player)
    while True:
        command = input("YT> ")
        if command.upper() == "EXIT":
            break
        try:
            parser.execute_command(command.split())
        except CommandException as e:
            print(e)
    print("YouTube has now terminated its execution. "
          "Thank you and goodbye!")
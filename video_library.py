#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:56:37 2021

@author: tiffanybiles
"""

"""A video library class."""

from video.py import Video
from pathlib import Path
import csv
import random


# Helper Wrapper around CSV reader to strip whitespace from around
# each item.
def _csv_reader_with_strip(reader):
    yield from ((item.strip() for item in line) for line in reader)


class VideoLibrary:
    """A class used to represent a Video Library."""

    def __init__(self):
        """The VideoLibrary class is initialized."""
        self._videos = {}
        with open(Path(__file__).parent / "videos.txt") as video_file:
            reader = _csv_reader_with_strip(
                csv.reader(video_file, delimiter="|"))
            for video_info in reader:
                title, url, tags = video_info
                self._videos[url] = Video(
                    title,
                    url,
                    [tag.strip() for tag in tags.split(",")] if tags else [],
                )

    def get_all_videos(self):
        """Returns all available video information from the video library."""
        return list(self._videos.values())
    
    def get_allowed_videos(self):
        return [v for v in self.get_all_videos() if not v.is_flagged]
    
    
    def get_video(self, video_id):
        """Returns the video object (title, url, tags) from the video library.
        Args:
            video_id: The video url.
        Returns:
            The Video object for the requested video_id. None if the video
            does not exist.
        """
        return self._videos.get(video_id, None)
    
    def get_random_video_id(self):
        try:
            return random.choice([video.video_id for video in self.get_allowed_videos()])
        except IndexError:
            return None
    
    def search_videos(self, search_term: str):
         search_term = search_term.lower()
         return [v for v in self.get_allowed_videos() if search_term in v.title.lower()]

    def get_videos_with_tag(self, tag: str):
        return [v for v in self.get_allowed_videos() if tag in v.tags]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 15:13:36 2021

@author: tiffanybiles
"""

from video_library.py import VideoLibrary


def test_library_has_all_videos():
    library = VideoLibrary()
    assert len(library.get_all_videos()) == 5


def test_parses_tags_correctly():
    library = VideoLibrary()
    video = library.get_video("amazing_cats_video_id")

    assert video is not None
    assert video.title == "Amazing Cats"
    assert video.video_id == "amazing_cats_video_id"
    assert set(video.tags) == {"#cat", "#animal"}


def test_parses_video_correctly_without_tags():
    library = VideoLibrary()
    video = library.get_video("nothing_video_id")

    assert video is not None
    assert video.title == "Video about nothing"
    assert video.video_id == "nothing_video_id"
    assert video.tags == ()

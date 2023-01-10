#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytube

input_link = input('Enter your https link: ')
yt = pytube.YouTube(input_link)
stream = yt.streams.get_highest_resolution()
stream.download()

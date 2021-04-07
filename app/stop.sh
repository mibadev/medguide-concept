#!/bin/bash

sudo systemctl stop  med-bot.service
sudo systemctl disable med-bot.service
sudo systemctl status med-bot.service
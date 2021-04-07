#!/bin/bash

sudo systemctl enable med-bot.service
sudo systemctl restart med-bot.service
sudo systemctl status med-bot.service
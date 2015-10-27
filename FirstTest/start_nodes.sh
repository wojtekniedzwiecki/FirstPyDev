#!/usr/bin/env bash
java -jar /Applications/Selenium/selenium-server-standalone-2.45.0.jar -role webdriver -nodeConfig /Users/wojtekniedzwiecki/Documents/workspace/FirstPyDev/selenium-node-chrome-mac.cfg.json &&
java -jar /Applications/Selenium/selenium-server-standalone-2.45.0.jar -role webdriver -nodeConfig /Users/wojtekniedzwiecki/Documents/workspace/FirstPyDev/selenium-node-firefox-mac.cfg.json &&
java -jar /Applications/Selenium/selenium-server-standalone-2.45.0.jar -role webdriver -nodeConfig /Users/wojtekniedzwiecki/Documents/workspace/FirstPyDev/selenium-node-safari-mac.cfg.json

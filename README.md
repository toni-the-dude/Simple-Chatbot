# Simple Chatbot
## Overview
This short project was made using the Rasa framework whilst following the Coursera 2-hour guided project <a href="https://www.coursera.org/projects/chatbot-rasa-python">"Create Your First Chatbot with Rasa and Python"</a>. 

<p>The chatbot embodies the simple functionality of telling the time zone of one of several cities.</p>

![telling_time1](https://github.com/toni-the-dude/Simple-Chatbot/blob/main/.misc/showcase1.PNG?raw=true)<br>
![telling_time2](https://github.com/toni-the-dude/Simple-Chatbot/blob/main/.misc/showcase4.PNG?raw=true)

<p>It was made using the default template for a chatbot provided by Rasa, which I then modified accordingly.</p>

## Usage
<ol>
<li>To be able to interact with the chatbot, run the command "rasa shell" in the directory "./Chatbot".</li>
<li>In order to ascertain how the bot is interpreting the converstaion, use "rasa shell nlu" in the same directory.</li> 
<li>Finally, if any adjustments are made to the code, retrain the bot with the updated code using "rasa train".</li> 
</ol>

## Walkthrough

<p>There are 4 main files which have been modified from the basic template.</p>
<ol>
  <li><a href="https://github.com/toni-the-dude/Simple-Chatbot/blob/main/Chatbot/data/nlu.yml">nlu.yml</a></li>
  <li><a href="https://github.com/toni-the-dude/Simple-Chatbot/blob/main/Chatbot/data/stories.yml">stories.yml</a></li>
  <li><a href="https://github.com/toni-the-dude/Simple-Chatbot/blob/main/Chatbot/domain.yml">domain.yml</a></li>
  <li><a href="https://github.com/toni-the-dude/Simple-Chatbot/blob/main/Chatbot/actions/actions.py">actions.py</a></li>
</ol>

entities
slots
rasa run actions

![course](https://github.com/toni-the-dude/Simple-Chatbot/blob/main/.misc/showcase2.PNG?raw=true)

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
  <li>
    <a href="https://github.com/toni-the-dude/Simple-Chatbot/blob/main/Chatbot/data/nlu.yml">nlu.yml</a>
    <p>NLU (Natural Language Understanding) is the part of Rasa that performs intent classification, entity extraction, and response retrieval.</p>
    <p>Below can be seen how the intent of the user can be defined by listing examples that ilustrate said intent. Furthermore, the words wrapped in square brackets are placeholders for what Rasa calls entities. They can be seen following the placeholders, wrapped in round brackets. I describe entities later.</p>

  ![nlu](https://github.com/toni-the-dude/Simple-Chatbot/blob/main/.misc/showcase3.PNG?raw=true)
  </li>
  
  <li>
    <a href="https://github.com/toni-the-dude/Simple-Chatbot/blob/main/Chatbot/data/stories.yml">stories.yml</a>
    <p>Stories are a formatted conversation between the user and the AI chatbot to which the AI will usually adhere to.</p>
    <p>The pattern can be inferred from the example below.</p>
  
  ![nlu](https://github.com/toni-the-dude/Simple-Chatbot/blob/main/.misc/showcase5.PNG?raw=true)
  </li>
  
  <li>
    <a href="https://github.com/toni-the-dude/Simple-Chatbot/blob/main/Chatbot/domain.yml">domain.yml</a>
    <p>A domain encompasses everything the AI should know. It specifies the intents, entities, slots, responses, and actions the bot should know about.</p>
    <p>Entities and slots are tied by their function. If entities are the value to be extracted from a user's prompt, then slots are the location where that value is meant to end up in.</p>

  ![nlu](https://github.com/toni-the-dude/Simple-Chatbot/blob/main/.misc/showcase6.PNG?raw=true)
  </li>
  
  <li>
    <a href="https://github.com/toni-the-dude/Simple-Chatbot/blob/main/Chatbot/actions/actions.py">actions.py</a>
    <p>Actions are functions that can make us of our slots and entities.</p>
    <p>In my case, I have defined a single action that does something based on whether or not the value from a slot is found within my comically large dictionary. Namely, it tells the time.</p>
    <p>To be able to have actions run, a section from the base template within "endpoints.yml" has been uncommented. Additionaly, the command "rasa run actions" must be run.</p>
  
  ![nlu](https://github.com/toni-the-dude/Simple-Chatbot/blob/main/.misc/showcase7.PNG?raw=true)
  </li>
</ol>

## Conclusion

![course](https://github.com/toni-the-dude/Simple-Chatbot/blob/main/.misc/showcase2.PNG?raw=true)

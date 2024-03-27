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
    <p>Below can be seen how the intent of the user can be defined by listing examples that ilustrate said intent. I have added significantly more entries to city_info than what is shown in order to increase the confidence in determining this particular intent. More on this further down.</p> 
    <p>Furthermore, the words wrapped in square brackets are placeholders for what Rasa calls entities. They can be seen following the placeholders, wrapped in round brackets. I describe entities later.</p>

  ![nlu](https://github.com/toni-the-dude/Simple-Chatbot/blob/main/.misc/showcase3.PNG?raw=true)
  </li>
  
  <li>
    <a href="https://github.com/toni-the-dude/Simple-Chatbot/blob/main/Chatbot/data/stories.yml">stories.yml</a>
    <p>Stories are a formatted conversation between the user and the AI chatbot to which the AI will usually adhere to.</p>
    <p>The pattern can be inferred from the example below.</p>
  
  ![stories](https://github.com/toni-the-dude/Simple-Chatbot/blob/main/.misc/showcase5.PNG?raw=true)
  </li>
  
  <li>
    <a href="https://github.com/toni-the-dude/Simple-Chatbot/blob/main/Chatbot/domain.yml">domain.yml</a>
    <p>A domain encompasses everything the AI should know. It specifies the intents, entities, slots, responses, and actions the bot uses.</p>
    <p>Entities and slots are tied by their function. If entities are the value to be extracted from a user's prompt, then slots are the location where that value is meant to end up in.</p>

  ![domain](https://github.com/toni-the-dude/Simple-Chatbot/blob/main/.misc/showcase6.PNG?raw=true)
  </li>
  
  <li>
    <a href="https://github.com/toni-the-dude/Simple-Chatbot/blob/main/Chatbot/actions/actions.py">actions.py</a>
    <p>Actions are functions that can make use of our slots and entities.</p>
    <p>In my case, I have defined a single action that does something based on whether or not the value from a slot is found within my comically large dictionary. Namely, it tells the time.</p>
    <p>To be able to have actions run, a section from the base template within "endpoints.yml" has been uncommented. Additionaly, the command "rasa run actions" must be run.</p>
  
  ![actions](https://github.com/toni-the-dude/Simple-Chatbot/blob/main/.misc/showcase7.PNG?raw=true)
  </li>
</ol>

## Challenges

<p>I have kept certain parts of the template which should have been deleted. This, alongside insufficient data in the NLU, caused the AI to misinterpret.</p>
<p>Using "rasa shell nlu", one can inspect confidence values, entity association, etc., which has proven essential to troubleshooting.</p>

![c1](https://github.com/toni-the-dude/Simple-Chatbot/blob/main/.misc/showcase8.PNG?raw=true)
![c2](https://github.com/toni-the-dude/Simple-Chatbot/blob/main/.misc/showcase9.PNG?raw=true)
![c3](https://github.com/toni-the-dude/Simple-Chatbot/blob/main/.misc/showcase10.PNG?raw=true)
![c4](https://github.com/toni-the-dude/Simple-Chatbot/blob/main/.misc/showcase11.PNG?raw=true)

<p>"city_info" specifically used to have an abismal value for cities which were not in the NLU examples, which I fixed by adding more entries to the "city_info" intent.</p>

## Conclusion

This about sums it up for the project. It gave me surface level insight on machine learning and familiarized me with a cool framework.

![course](https://github.com/toni-the-dude/Simple-Chatbot/blob/main/.misc/showcase2.PNG?raw=true)

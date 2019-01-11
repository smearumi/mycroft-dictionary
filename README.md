# <img src='https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/book.svg' card_color='#000000' width='50' height='50' style='vertical-align:bottom'/> Dictionary
Find out the definition/meaning of a specific word from dictionary.

## About 
You can find out the definition/meaning of a specific word from dictionary using Oxford Dictionaries API.

## Installation
You should be able to install this skill via `mycroft-msm install https://github.com/smearumi/mycroft-dictionary.git` or you can install this skill via Installer Skill from web interface (https://home.mycroft.ai/#/skill).

## Configuration
At first, you must obtain your API credentials from "Oxford Dictionaries".
Please sign up/login into https://developer.oxforddictionaries.com/ and get your API key credentials. (i.e. Application ID, Application Key)

You can configure this skill via web interface (home.mycroft.ai). After a few minutes of having the skill installed, you should see configuration options in the https://home.mycroft.ai/#/skill location.

Fill this out with your appropriate information and hit save.

OR

If you desire total privacy, please edit your config file located at:

        ~/.mycroft/mycroft.conf

If it does not exist, create it. This file must be contain a valid json, add the following to it:

        "DictionarySkill": {
            "base_url": "https://od-api.oxforddictionaries.com:443/api/v1",
            "language": "en",
            "app_id": "YOUR APPLICATION ID",
            "app_key": "YOUR APPLICATION KEY"
        }  

## Examples 
* "define cat"
* "define the cat"

## Credits 
S. M. Estiaque Ahmed (@smearumi)



## Category
Daily
**Information**
Productivity

## Tags
#mycroft
#skill
#dictionary
#home
#voice
#assistant

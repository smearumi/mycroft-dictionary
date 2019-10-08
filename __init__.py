# Copyright 2019 S. M. Estiaque Ahmed
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.skills.core import intent_handler


class DictionarySkill(MycroftSkill):
    def __init__(self):
        super(DictionarySkill, self).__init__(name="DictionarySkill")

    @intent_handler(IntentBuilder("DefineIntent").require("Define")
                    .require("Word"))
    def handle_define_intent(self, message):
        try:
            base_url = "https://od-api.oxforddictionaries.com:443/api/v2"

            config = self.config_core.get("DictionarySkill", {})

            if not config == {}:
                language = str(config.get("language"))
                app_id = str(config.get("app_id"))
                app_key = str(config.get("app_key"))

            else:
                language = str(self.settings.get("language"))
                app_id = str(self.settings.get("app_id"))
                app_key = str(self.settings.get("app_key"))

            if not base_url or not language or not app_id or not app_key:
                raise Exception("None found.")

        except Exception:
            self.speak_dialog("settings.error")
            return

        word = message.data.get("Word")

        if not word:
            return

        api_url = "{0}/entries/{1}/{2}".format(base_url, language, word)

        api_headers = {'Content-Type': 'application/json',
                       'Accept': 'application/json',
                       'app_id': app_id,
                       'app_key': app_key}

        try:
            response = requests.get(api_url, headers=api_headers)

        except Exception:
            self.speak_dialog("connection.error")
            return

        if response.status_code == 200:
            try:
                definition = response.json()['results'][0][
                                                'lexicalEntries'][0][
                                                    'entries'][0]['senses'][0][
                                                        'definitions'][0]

                self.speak_dialog("definition",
                                  {"word": word, "definition": definition})

            except KeyError:
                definition = response.json()['results'][0][
                                                'lexicalEntries'][0][
                                                    'entries'][0]['senses'][0][
                                                        'crossReferenceMarkers'
                                                                           ][0]

                self.speak_dialog("grammer",
                                  {"word": word, "definition": definition})

        elif response.status_code == 404:
            self.speak_dialog("invalid", {"word": word})

    def stop(self):
        pass


def create_skill():
    return DictionarySkill()

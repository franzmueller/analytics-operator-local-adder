#  Copyright 2020 InfAI (CC SES)
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import unittest

from senergy_local_analytics import Input

import main


class TestMainMethods(unittest.TestCase):

    def test_process(self):
        input1 = Input("value1")
        input2 = Input("value2")
        input1.current_value = 1
        input1.name = "test1"
        input2.current_value = 3
        input2.name = "test2"
        output = main.process([input1, input2])
        self.assertTrue(output.send)
        self.assertEqual({'sum', 'message_id', 'timestamp'}, output.values.keys())
        input1.current_value = 7
        input1.name = "test1"
        input2.current_value = 4
        input2.name = "test3"
        output = main.process([input1, input2])
        self.assertEqual(14, output.values["sum"])





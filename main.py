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
from senergy_local_analytics import App, Input

app = App()

input1 = Input("value1")
input2 = Input("value2")

app.config([input1, input2])


def process(inputs: list[Input]):
    val = 0
    for inp in inputs:
        if inp.current_value is not None:
            val += inp.current_value
    app.set_output("sum", val)
    app.send_message()


app.process_message(process)

if __name__ == '__main__':
    print("start operator", flush=True)
    app.main()

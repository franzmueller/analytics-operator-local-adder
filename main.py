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
import typing
import uuid
from datetime import datetime

from senergy_local_analytics import App, Input, Output

values = {}


def process(inputs: typing.List[Input]):
    for inp in inputs:
        if inp.current_value is not None:
            values[inp.current_topic] = inp.current_value
    return Output(True, {"sum": sum(values.values()), "message_id": str(uuid.uuid4()),
                         "timestamp": '{}Z'.format(datetime.utcnow().isoformat())})


if __name__ == '__main__':
    app = App()

    input1 = Input("value1")
    input2 = Input("value2")
    input3 = Input("value3")
    input4 = Input("value4")
    input5 = Input("value5")

    app.config([input1, input2, input3, input4, input5])
    print("start operator", flush=True)
    app.process_message(process)
    app.main()

# -*- coding: UTF-8 -*-
#   Copyright (c) 2021 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
import unittest

sys.path.append("../")
from pycorrector.ernie_csc.ernie_csc_corrector import ErnieCscCorrector


class TestModel(unittest.TestCase):
    def test_case_ernie_csc(self):
        """ Test using ernie csc model"""
        error_sentences = [
            '真麻烦你了。希望你们好好的跳无',
            '少先队员因该为老人让坐',
            '机七学习是人工智能领遇最能体现智能的一个部分',
            '一只小鱼船浮在平净的河面上',
            '我的家乡是有明的渔米之乡',
        ]

        correct_sentences = [
            '真麻烦你了。希望你们好好的跳舞',
            '少先队员应该为老人让座',
            '机器学习是人工智能领域最能体现智能的一个部分',
            '一只小鱼船浮在平净的河面上',
            '我的家乡是有名的渔米之乡'
        ]
        corrector = ErnieCscCorrector()
        for sent, correct in zip(error_sentences, correct_sentences):
            result = corrector.correct(sent)
            assert result['target'] == correct


if __name__ == '__main__':
    unittest.main()

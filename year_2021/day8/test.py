import unittest

from year_2021.day8.main import parse_val_p1, get_output


class MyTestCase(unittest.TestCase):
    input_list = [
        'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
        'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
        'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
        'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
        'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
        'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
        'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
        'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
        'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
        'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'
    ]
    output_val_dict = {
       # 'fdgacbe cefdb cefbgd gcbe': 8394,
        'fcgedb cgb dgebacf gc': 9781,
        'cg cg fdcagb cbg': 1197,
        'efabcd cedba gadfec cb': 9361,
        'gecf egdcabf bgf bfgea': 4873,
        'gebdcfa ecba ca fadegcb': 8418,
        'cefg dcbef fcge gbcadfe': 4548,
        'ed bcgafe cdgba cbgef': 1625,
        'gbdfcae bgc cg cgb': 8717,
        'fgae cfgab fg bagce': 4315
    }

    def testPart1(self):
        self.assertEqual(26, parse_val_p1(self.input_list))

    def testPart2(self):
        for k,v in self.output_val_dict.items():
            list_output = k.split(' ')
            self.assertEqual(v, get_output(list_output))
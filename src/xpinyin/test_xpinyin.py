import pytest

from xpinyin import Pinyin
# add execute command
# pytest --cov=xpinyin/ --cov-report=html --cov-config xpinyin/.coveragerc
p = Pinyin()


class TestGetPinyin:

    @pytest.mark.parametrize("expected,actual", [
        (p.get_pinyin(u"中国"), 'zhong-guo'),
        (p.get_pinyin(u"飞机", tone_marks='marks'), 'fēi-jī'),
        (p.get_pinyin(u"大海", tone_marks='numbers'), 'da4-hai3'),
        (p.get_pinyin(u"爱好", ""), 'aihao'),
        (p.get_pinyin(u"高兴", "|"), 'gao|xing'),
        (p.get_pinyin(u"雾霾", convert="upper"), 'WU-MAI'),
        (p.get_pinyin(u"下雪", convert="capitalize"), 'Xia-Xue'),
        (p.get_pinyin(u"wo爱NI啊", "!"), 'wo!ai!NI!a'),
        (p.get_pinyin(u"上海", tone_marks='marks'), u'sh\xe0ng-h\u01cei'),
    ])
    def test_get_pinyin(self, expected, actual):
        assert expected == actual


class TestGetInitial:

    @pytest.mark.parametrize("expected,actual", [
        (p.get_initial(u"你"), 'N'),
        (p.get_initial(u"好"), 'H'),
        (p.get_initial(u"w"), 'w')
    ])
    def test_get_initial(self, expected, actual):
        assert expected == actual


class TestGetInitials:

    @pytest.mark.parametrize("expected,actual", [
        (p.get_initials(u"你好"), 'N-H'),
        (p.get_initials(u"江河", ""), 'JH'),
        (p.get_initials(u"树木", "|"), 'S|M'),
        (p.get_initials(u"SL", "!"), 'S!L')
    ])
    def test_get_initials(self, expected, actual):
        assert expected == actual

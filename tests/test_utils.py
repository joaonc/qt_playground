import pytest

from src.utils import OsData, OsName


class TestOsName:
    @pytest.mark.parametrize(
        'name, expected',
        [
            ('Windows', OsName.Windows),
            ('Darwin', OsName.MacOS),
            ('Linux', OsName.Linux),
        ],
    )
    def test_from_system_name(self, name, expected):
        assert OsName.from_system_name(name) is expected

    def test_this(self):
        os_name = OsName.this()
        assert type(os_name) is OsName


class TestOsData:
    def test_init(self):
        os_data = OsData('foo')
        assert os_data.data == 'foo'
        assert os_data.os_include == list()
        assert os_data.os_exclude == list()

    def test_overlap(self):
        with pytest.raises(ValueError):
            OsData('foo', os_include=[OsName.Windows, OsName.Linux], os_exclude=[OsName.Linux])

    @pytest.mark.parametrize(
        'os_data, os_name, expected',
        [
            (OsData('foo'), OsName.Linux, True),
            (OsData('foo', os_include=[OsName.MacOS, OsName.Linux]), OsName.Linux, True),
            (OsData('foo', os_include=[OsName.MacOS]), OsName.Linux, False),
            (OsData('foo', os_exclude=[OsName.MacOS, OsName.Linux]), OsName.Linux, False),
        ],
    )
    def test_applies(self, os_data, os_name, expected):
        assert os_data.applies(os_name) is expected

    def test_applies_current_os(self):
        os_data=OsData('foo', os_include=[OsName.this()])
        assert os_data.applies() is True

    def test_does_not_apply_current_os(self):
        os_data=OsData('foo', os_exclude=[OsName.this()])
        assert os_data.applies() is False

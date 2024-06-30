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

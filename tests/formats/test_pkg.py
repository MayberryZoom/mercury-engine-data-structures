from construct import Container, ListContainer
from tests.test_lib import parse_and_build_compare

from mercury_engine_data_structures.formats.pkg import Pkg
from mercury_engine_data_structures.game_check import Game

_EMPTY_DREAD_PKG = (b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')


def test_compare_dread(dread_path):
    parse_and_build_compare(
        Pkg.construct_class(Game.DREAD), Game.DREAD, dread_path.joinpath("packs/system/system.pkg")
    )


def test_build_empty_pkg():
    pkg = Pkg(Container(files=ListContainer()), Game.DREAD)

    assert pkg.build() == _EMPTY_DREAD_PKG


def test_remove_pkg_element():
    single_element_pkg = (b'|\x00\x00\x00\x08\x00\x00\x00\x01\x00\x00\x00\xd2\x04\x00\x00'
                          b'\x00\x00\x00\x00\x80\x00\x00\x00\x86\x00\x00\x00\x00\x00\x00\x00'
                          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                          b'FOOBAR\x00\x00')

    pkg = Pkg.parse(single_element_pkg, Game.DREAD)
    assert pkg.build() == single_element_pkg

    pkg.remove_asset(1234)
    assert pkg.build() == _EMPTY_DREAD_PKG

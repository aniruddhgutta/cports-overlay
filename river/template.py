pkgname = "river"
pkgver = "0.4.1"
pkgrel = 0
hostmakedepends = ["zig-bin", "pkgconf", "scdoc"]
makedepends = [
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.19-devel",
]
depends = ["xwayland"]
pkgdesc = "Non-monolithic Wayland compositor"
license = "0BSD OR CC-BY-SA-4.0 OR GPL-3.0-or-later OR MIT"
url = "https://codeberg.org/river/river"
source = [
    f"{url}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz",
    f"https://codeberg.org/ifreund/zig-pixman/archive/v0.3.0.tar.gz > {pkgname}-pixman-0.3.0.tar.gz",
    f"https://codeberg.org/ifreund/zig-wayland/archive/v0.5.0.tar.gz > {pkgname}-wayland-0.5.0.tar.gz",
    f"https://codeberg.org/ifreund/zig-wlroots/archive/v0.19.4.tar.gz > {pkgname}-wlroots-0.19.4.tar.gz",
    f"https://codeberg.org/ifreund/zig-xkbcommon/archive/v0.4.0.tar.gz > {pkgname}-xkbcommon-0.4.0.tar.gz",
]
source_paths = [
    ".",
    "zig-pixman",
    "zig-wayland",
    "zig-wlroots",
    "zig-xkbcommon",
]
sha256 = [
    "066a4cd282ce47079abc7081da10a8c8df6e73d5c491268bf5dbb75769809ff0",  # river
    "cd7fe3415d4d58685a94fdedd308e9994a37f012828940cfb603461de7f2c6ad",  # pixman
    "fa9705e83613b5555d7117ce5c602f10591d6598e69a73fba2e6039200db4f4b",  # wayland
    "ef3f8ef0c6ae516d244248f536290ef647dd10964ff992aa3160e53c06de85cf",  # wlroots
    "e6df77d511cf9402f6ac08455c8d1fb727b6c3d66191e246671f62e5db083c49",  # xkbcommon
]


def prepare(self):
    for p in source_paths[1:]:
        self.do("zig", "fetch", "--global-cache-dir", "deps", p)


def build(self):
    self.do(
        "zig",
        "build",
        "--system",
        "deps/p",
        "-Dpie",
        "-Doptimize=ReleaseSafe",
        "-Dxwayland",
        "-Dman-pages",
        "--prefix",
        "zig_output",
    )


def install(self):
    self.install_bin("zig_output/bin/river")
    self.install_files("LICENSES", "usr/share/licenses/river")
    self.install_files("zig_output/share/river-protocols", "usr/share")

pkgname = "rill"
pkgver = "0.5.0"
pkgrel = 0
hostmakedepends = ["zig-bin", "pkgconf"]
makedepends = [
    "river",
    "wayland-devel",
    "wayland-protocols",
]
depends = ["xwayland"]
pkgdesc = "River-based scrolling window manager"
license = "MIT"
url = "https://codeberg.org/lzj15/rill"
source = [
    f"{url}/archive/{pkgver}.tar.gz",
    f"https://codeberg.org/ifreund/zig-wayland/archive/v0.5.0.tar.gz > {pkgname}-wayland-0.5.0.tar.gz",
]
source_paths = [
    ".",
    "zig-wayland",
]
sha256 = [
    "e11a26eef4c1254a634edc12414bc541c583784a286b0a0b1e8e3626ab3e7797",  # rill
    "fa9705e83613b5555d7117ce5c602f10591d6598e69a73fba2e6039200db4f4b",  # wayland
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
        "--prefix",
        "zig_output",
    )


def install(self):
    self.install_bin("zig_output/bin/rill")
    self.install_license("LICENSE")

pkgname = "nwg-look"
pkgver = "1.1.0"
pkgrel = 0
build_style = "go"
hostmakedepends = [
    "go",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
]
depends = ["gsettings-desktop-schemas", "xcur2png"]
pkgdesc = "GTK3 settings editor adapted to work in the wlroots environment"
license = "MIT"
url = "https://github.com/nwg-piotr/nwg-look"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fa00b755246f8fcaf0058e54b0ec0013b43db065280de73fdae4b470359d31d9"


def install(self):
    self.install_bin(f"build/{pkgname}")
    self.install_license("LICENSE")
    self.install_file("stuff/main.glade", f"usr/share/{pkgname}")
    self.install_files("langs", f"usr/share/{pkgname}", name="langs")
    self.install_file(f"stuff/{pkgname}.desktop", "usr/share/applications")
    self.install_file(
        f"stuff/{pkgname}.svg",
        "usr/share/icons/hicolor/scalable/apps",
    )

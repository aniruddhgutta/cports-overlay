pkgname = "papirus-folders"
pkgver = "1.14.0"
pkgrel = 0
build_style = "makefile"
depends = [
    "bash",
    "papirus-icon-theme",
]
pkgdesc = "Change the color of folders in Papirus icon theme"
license = "MIT"
url = "https://github.com/PapirusDevelopmentTeam/papirus-folders"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "658723db46638ad988ef91ed7d28e9941b528418f7c83d51fe17cdf4985e6dd2"
# no checks provided
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

pkgname = "zig-bin"
pkgver = "0.15.2"
pkgrel = 0
pkgdesc = "Zig programming language toolchain"
license = "MIT"
url = "https://ziglang.org"
source = f"{url}/download/{pkgver}/zig-x86_64-linux-{pkgver}.tar.xz"
sha256 = "02aa270f183da276e5b5920b1dac44a63f1a49e55050ebde3aecc9eb82f93239"


def install(self):
    self.install_license("LICENSE")
    self.install_files("lib", "usr/lib/zig/")
    self.install_file("zig", "usr/lib/zig/", mode=0o755)
    self.install_dir("usr/bin")
    self.install_link("usr/bin/zig", "../lib/zig/zig")
    self.install_files("doc", "usr/share/doc", name="zig")

# Author: Zengping
class Bining():
    dictBinMethod = {"chi": bin, }

    def __init__(self, var_serial, target_serial):
        self.var_serial = var_serial
        self.target_serial = target_serial

    def bin(self, method="chi"):
        bin_foo = self.dictBinMethod[method]
        return bin_foo(self.var_serial, self.target_serial)

    def chi_bin(self):
        return None

    def best_bin(self):
        return None

    def average_bin(self):
        return None


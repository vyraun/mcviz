from dual import DualLayout
from feynman import FeynmanLayout, PrunedHadronsLayout, CombinedLayout
from phi import PhiLayout

layouts = {}
layouts["dual"] = DualLayout
layouts["feynman"] = FeynmanLayout
layouts["phi"] = PhiLayout
layouts["jetless"] = PrunedHadronsLayout
layouts["combined"] = CombinedLayout
default = "feynman"

def list_layouts():
    return sorted(layouts.keys())

def get_layout(name):
    if name is None:
        return layouts[default]
    return layouts[name]

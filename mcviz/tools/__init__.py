from tools import contract_jets, remove_kinks, gluballs, chainmail, contract_loops, pluck, unsummarize
from tagging import tag

tools = {}
tools["Kinks"] = remove_kinks
tools["Gluballs"] = gluballs
tools["Chainmail"] = chainmail
tools["Jets"] = contract_jets
tools["Loops"] = contract_loops
tools["Pluck"] = pluck
tools["Unsummarize"] = unsummarize

def list_tools():
    return sorted(tools.keys())

def apply_tool(name, graph_view):
    tools[name](graph_view)
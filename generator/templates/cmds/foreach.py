{% extends "base_tmpl.py" %}

{% set args = [
('LoopVar', 'str', 'Loop Variable for the foreach loop', ''),
('LoopItems', 'str', 'Items to loop over', ''),
] %}

{% block Render_Inner %}
        ret = ["{{ CmdName }}(" + self.LoopVar + " "]
        for item in self.LoopItems:
            if isinstance(item, str):
                ret.append(item + " ")
            if isinstance(item, SetList):
                ret.append("${" + item.Name + "} ")
        ret[-1] += ")"
{% endblock %}

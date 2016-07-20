{% extends "cmd_base_tmpl.py" %}

{% set args = [
('LoopVar', 'str', 'Loop Variable to end the foreach loop with', ''),
] %}

{% block Func_Render_Body_Inner %}
        ret = ["{{ CmdName }}(" + self.LoopVar + ")"]
{% endblock %}

{% extends "cmd_base_tmpl.py" %}

{% set args = [
('LoopVar', 'str', '', ''),
] %}

{%- block Func_Render_Body_Inner %}
        ret = ["{{ CmdName }}(" + self.LoopVar + ")"]
{%- endblock %}

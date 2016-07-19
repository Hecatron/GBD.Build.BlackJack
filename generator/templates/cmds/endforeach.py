{% extends "base_tmpl.py" %}

{% set args = [
('LoopVar', 'str', 'Loop Variable to end the foreach loop with', '')
] %}

{% block Render_Inner %}
        ret = ["{{ CmdName }}(" + self.LoopVar + ")"]
{% endblock %}

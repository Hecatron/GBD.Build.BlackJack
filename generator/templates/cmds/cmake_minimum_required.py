{% extends "cmd_base_tmpl.py" %}

{% set args = [
('Version', 'Version', 'Minimum required version of cmake', '')
] %}

{% block Init_Post %}
        if self.Version is None: self.Version = Version(2,8)
{% endblock %}

{% block Render_Inner %}
        ret.append("{{ CmdName }}(" + self.Version.render_string() + ")")
{% endblock %}

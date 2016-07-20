{% extends "cmd_base_tmpl.py" %}

{% set args = [
('Version', 'Version', 'Minimum required version of cmake', ''),
] %}

{% block Func_ClassInit_Post %}
        if self.Version is None: self.Version = Version(2,8)
{% endblock %}

{% block Func_Render_Body_Inner %}
        ret.append("{{ CmdName }}(" + self.Version.render_string() + ")")
{% endblock %}

{% extends "cmd_target_tmpl.py" %}

{% block Render_Inner %}
        ret.append("set(" + self.Name)
        for item in self.Sources:
            if isinstance(item, str):
                ret.append('    "' + item + '" ')
            if isinstance(item, SetList):
                ret.append('    ' + item.Name)
        if self.Options:
            ret.append(self.Options)
        ret[-1] += ")"
{% endblock %}

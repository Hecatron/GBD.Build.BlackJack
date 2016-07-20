{% extends "base_tmpl.py" %}

{% set args = [
('Name', 'str', 'Name of the target / set'),
('Sources', '[]', 'List of Sources to include into the target / set'),
('Options', 'str', 'Options', 'None'),
] %}

{% block Render_Inner %}
        tmpline = "{{ CmdName }}(" + self.Name
        if self.Options:
            tmpline += " " + self.Options
        ret.append(tmpline)
        for item in self.Sources:
            if isinstance(item, str):
                ret.append('    "' + item + '" ')
            if isinstance(item, SetList):
                ret.append('    ' + item.Name)
        ret[-1] += ")"
{% endblock %}

{% block Prop_Name %}
    @property
    def Name(self):
        """Name of the target"""
        return self._Name

    @Name.setter
    def Name(self, value):
        self._Name = value.replace(" ", "_")
{% endblock %}
